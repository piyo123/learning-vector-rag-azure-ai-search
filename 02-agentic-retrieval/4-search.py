import requests
import json
import os
import time
from azure.search.documents.indexes.models import (
    AzureOpenAIVectorizer, 
    AzureOpenAIVectorizerParameters, 
    FieldMapping,
    HnswAlgorithmConfiguration, 
    KnowledgeBase, 
    KnowledgeBaseAzureOpenAIModel, 
    KnowledgeSourceReference, 
    KnowledgeRetrievalOutputMode, 
    KnowledgeRetrievalLowReasoningEffort,
    SemanticSearch, 
    SemanticConfiguration, 
    SemanticPrioritizedFields, 
    SemanticField, 
    SearchIndex, 
    SearchField, 
    SearchIndexer,
    SearchIndexerDataSourceConnection,
    SearchIndexerDataContainer,
    SearchIndexerSkillset,
    SearchIndexKnowledgeSource, 
    SearchIndexKnowledgeSourceParameters, 
    SearchIndexFieldReference,
    VectorSearch, 
    VectorSearchProfile, 
)
from azure.search.documents.indexes import SearchIndexClient, SearchIndexerClient
from azure.search.documents import SearchIndexingBufferedSender
from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
from azure.search.documents.knowledgebases.models import (
    KnowledgeBaseRetrievalRequest, 
    KnowledgeBaseMessage, 
    KnowledgeBaseMessageTextContent, 
    SearchIndexKnowledgeSourceParams
)
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# Define variables
SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AOAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AOAI_EMBEDDING_MODEL = "text-embedding-3-small"   
AOAI_EMBEDDING_DEPLOYMENT = "text-embedding-3-small"
AOAI_MODEL_NAME = "gpt-4o-mini"
AOAI_MODEL_DEPLOYMENT = "gpt-4o-mini"
INDEX_NAME = "stories-index"
INDEXER_NAME = f"{INDEX_NAME}-indexer"
SKILLSET_NAME = f"{INDEX_NAME}-skillset"
DATA_SOURCE_NAME = f"{INDEX_NAME}-datasource"
KNOWLEDGE_SOURCE_NAME = f"{INDEX_NAME}-knowledge-source"
KNOWLEDGE_BASE_NAME = f"{INDEX_NAME}-knowledge-base"
SEMANTIC_CONFIGURATION_NAME = f"{INDEX_NAME}-semantic-config"

BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")
BLOB_FOLDER_NAME = os.getenv("BLOB_FOLDER_NAME")

TITLE_SKILL_API_URI = "https://<PUT_YOUR_SKILL_SERVER_NAME>/extractTitle"
TITLE_SKILL_API_KEY = None

# Set up credentials (API key-based authentication)
SEARCH_CREDENTIAL = AzureKeyCredential(SEARCH_API_KEY)
AOAI_CREDENTIAL = AzureKeyCredential(AOAI_API_KEY)

# Clients
index_client = SearchIndexClient(endpoint=SEARCH_ENDPOINT, credential=SEARCH_CREDENTIAL)
indexer_client = SearchIndexerClient(endpoint=SEARCH_ENDPOINT, credential=SEARCH_CREDENTIAL)

# Execute search
def search(query: str) -> str:

    # Set up messages
    instructions = """
    A Q&A agent that can answer questions about classic folktales.
    Answwer in Japanese even if the question is asked in English.
    If you don't have the answer, respond with "I don't know".
    """

    messages = [
        {
            "role": "system",
            "content": instructions
        }
    ]

    # Run agentic retrieval
    agent_client = KnowledgeBaseRetrievalClient(endpoint=SEARCH_ENDPOINT, knowledge_base_name=KNOWLEDGE_BASE_NAME, credential=SEARCH_CREDENTIAL)
    
    messages.append({
        "role": "user",
        "content": query
    })

    req = KnowledgeBaseRetrievalRequest(
        messages=[
            KnowledgeBaseMessage(
                role = m["role"],
                content = [KnowledgeBaseMessageTextContent(text=m["content"])]
            ) for m in messages if m["role"] != "system"
        ],
        knowledge_source_params = [
            SearchIndexKnowledgeSourceParams(
                knowledge_source_name = KNOWLEDGE_SOURCE_NAME,
                include_references = True,
                include_reference_source_data = True,
                always_query_source = True
            )
        ],
        include_activity = True,
        retrieval_reasoning_effort = KnowledgeRetrievalLowReasoningEffort
    )

    result = agent_client.retrieve(retrieval_request=req)
    print(f"Retrieved content from '{KNOWLEDGE_BASE_NAME}' successfully.")

    # Display the response, activity, and references
    response_contents = []
    activity_contents = []
    references_contents = []

    # responses
    response_parts = []
    for resp in result.response:
        for content in resp.content:
            response_parts.append(content.text)

    response_content = "\n\n".join(response_parts) if response_parts else "No response found on 'result'"
    response_contents.append(response_content)
    print(f"\n*** response_content:\n{response_content}\n")

    messages.append({
        "role": "assistant",
        "content": response_content
    })

    # activities
    if result.activity:
        activity_content = json.dumps([a.as_dict() for a in result.activity], indent=2, ensure_ascii=False)
    else:
        activity_content = "No activity found on 'result'"

    activity_contents.append(activity_content)
    print(f"\n*** activity_content:\n{activity_content}\n")

    if result.references:
        # Show only the top 5 results.
        references_content = json.dumps([r.as_dict() for r in result.references][:5], indent=2, ensure_ascii=False)
    else:
        references_content = "No references found on 'result'"

    references_contents.append(references_content)
    print(f"\n*** references_content:\n{references_content}\n")

# Main Entry Point
def main():
    
    print("検索クエリを入力してください（終了するには空行でEnter）")

    while True:
        query = input("> ").strip()
        if not query:
            print("終了します。")
            break

        search(query)


if __name__ == "__main__":
    main()