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

TITLE_SKILL_API_URI = "https://<PUT_YOUR_SKILL_API_SERVER>/extractTitle"
TITLE_SKILL_API_KEY = None

# Set up credentials (API key-based authentication)
SEARCH_CREDENTIAL = AzureKeyCredential(SEARCH_API_KEY)
AOAI_CREDENTIAL = AzureKeyCredential(AOAI_API_KEY)

# Clients
index_client = SearchIndexClient(endpoint=SEARCH_ENDPOINT, credential=SEARCH_CREDENTIAL)
indexer_client = SearchIndexerClient(endpoint=SEARCH_ENDPOINT, credential=SEARCH_CREDENTIAL)

# Run Indexer
def run_indexer():
    indexer_client.run_indexer(INDEXER_NAME)
    print(f"Indexer '{INDEXER_NAME}' started.")


# Confirm running status of Indexer
def get_indexer_status() -> dict:
    status = indexer_client.get_indexer_status(INDEXER_NAME)
    last = status.last_result

    # indexer has not run yet
    if last is None:
        return {
            "status": "notRun",
            "items_processed": 0,
            "items_failed": 0,
            "errors": [],
            "warnings": [],
        }

    # after run at least one time
    result = {
        "status": last.status,  # notStarted / inProgress / success / failed / transientFailure
        "items_processed": last.item_count,
        "items_failed": last.failed_item_count,
        "start_time": last.start_time.isoformat() if last.start_time else None,
        "end_time": last.end_time.isoformat() if last.end_time else None,
        "errors": [],
        "warnings": [],
    }

    if last.errors:
        result["errors"] = [
            {
                "key": e.key,
                "message": str(e),
                "error_details": str(getattr(e, 'error_details', None)),
            }
            for e in last.errors
        ]

    if last.warnings:
        result["warnings"] = [
            {
                "key": w.key,
                "message": str(w),
            }
            for w in last.warnings
        ]

    return result


# Wait for Indexer
def wait_for_indexer(interval: int = 5, timeout: int = 300):
    start = time.time()

    while True:
        result = get_indexer_status()

        status = result["status"]

        if status in ("success", "failed", "transientFailure"):
            print("Indexer process end.")
            return result

        if time.time() - start > timeout:
            raise TimeoutError("Indexer did not finish within timeout")

        print("Waiting Indexer processing.....")
        print(f"Status:{result["status"]}")
        print(f"Items processed:{result["items_processed"]}")
        print(f"Items failed:{result["items_failed"]}")

        time.sleep(interval)

# Main Entry Point
def main():
    run_indexer()
    result = wait_for_indexer()
    print("\n*** Result of Indexer Execution:\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()