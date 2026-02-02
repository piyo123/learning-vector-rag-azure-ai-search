import os
import json
from pathlib import Path
from openai import OpenAI
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# =====================
# Settings
# =====================
load_dotenv()
OPENAI_ENDPOINT = os.getenv("OPENAI_ENDPOINT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"

SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
INDEX_NAME = "kazuma-rag-index1" # The index was created via the Azure portal (refer to kazuma-rag-index1-semantic.json).

# =====================
# Clients
# =====================
openai_client = OpenAI(
    base_url=OPENAI_ENDPOINT,
    api_key=OPENAI_API_KEY,
)

search_client = SearchClient(
    endpoint=SEARCH_ENDPOINT,
    index_name=INDEX_NAME,
    credential=AzureKeyCredential(SEARCH_API_KEY)
)

# =====================
# Helper Functions
# =====================

# Embedding (Vectorize)
def embed(text: str) -> list[float]:
    response = openai_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding

# Read 'documents.txt' as a datasource
def load_documents(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# Build the documents JSON payload to upload to an Azure AI Search index
def build_documents(lines: list[str]) -> list[dict]:
    docs = []
    for i, text in enumerate(lines):
        docs.append({
            "id": str(i),
            "content": text,
            "contentVector": embed(text)
        })
    return docs

# Upoad data into Azure AI Search index and build the index
# In this example, the chunking unit is one line from documents.txt.
def upload_documents(file_path: str):
    lines = load_documents(file_path)
    docs = build_documents(lines)

    result = search_client.upload_documents(documents=docs)
    print(f"Uploaded {len(result)} documents")

# Remove all documents from the Azure AI Search index
def clear_index():
    # retrieve all documents
    results = search_client.search(
        search_text="*",
        select=["id"]
    )
    # make 'id' field list
    ids_to_delete = [{"id": r["id"]} for r in results]
    if ids_to_delete:
        # delete
        result = search_client.delete_documents(documents=ids_to_delete)
        print(f"Deleted {len(result)} documents")
    else:
        print("No documents to delete")

# =====================
# Search Execution
# =====================
def search(query: str, k_nearest_neighbors: int = 50) -> list[str]:
    vector_query = VectorizedQuery(
        kind="vector",
        vector=embed(query),
        k=k_nearest_neighbors,
        fields="contentVector",
        exhaustive=True,
    )

    # Semantic config is part of the index and was created in the Azure Portal. (refer to kazuma-rag-index1-semantic.json)
    results = search_client.search(
        search_text=str, # Specify search keywords for hybrid (keyword + vector) search
        vector_queries=[vector_query],
        include_total_count=True,
        select=["id", "content"],
        semantic_configuration_name="kazuma-semantic-config1", 
        query_type="semantic" # Possible values include: 'simple', 'full', "semantic". Default Value: None.
    )

    # The search() method returns a generator.
    # Since it is consumed after iteration, copy it to a list if reuse is required.
    results_list = list(results)

    # for logging
    results_for_stdout = json.dumps(
        results_list[:5], # Show only the top 5 results.
        indent=2,
        ensure_ascii=False
    )
    print(f"total count of search results={results.get_count()}\n")
    print("search results(output only top 5):\n", results_for_stdout)

    return [r["content"] for r in results_list]


# =====================
# Ask LLM
# =====================
def ask_llm(question: str, contexts: list[str]) -> str:
    context_text = "\n\n".join(contexts)

    messages = [
        {
            "role": "system",
            "content": (
                "あなたは与えられたコンテキストのみに基づいて回答するAIです。"
                "コンテキストに答えが無い場合は『分かりません』と答えてください。"
            )
        },
        {
            "role": "user",
            "content": f"""
                        質問:
                        {question}

                        コンテキスト:
                        {context_text}
                        """
        }
    ]

    response = openai_client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages
    )

    return response.choices[0].message.content

# =====================
# Main Entry Point
# =====================
def main():

    clear_index()
    BASE_DIR = BASE_DIR = Path(__file__).resolve().parents[2]
    upload_documents(str(BASE_DIR / "00-assets" / "documents.txt"))

    print("検索クエリを入力してください（終了するには空行でEnter）")

    while True:
        query = input("> ").strip()
        if not query:
            print("終了します。")
            break

        contexts = search(query)
        answer = ask_llm(query, contexts)
        print("\n=== Answer ===")
        print(answer)


if __name__ == "__main__":
    main()

