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

TITLE_SKILL_API_URI = "https://unsilicified-earnest-untheistically.ngrok-free.dev/extractTitle"
TITLE_SKILL_API_KEY = None

# Set up credentials (API key-based authentication)
SEARCH_CREDENTIAL = AzureKeyCredential(SEARCH_API_KEY)
AOAI_CREDENTIAL = AzureKeyCredential(AOAI_API_KEY)

# Clients
index_client = SearchIndexClient(endpoint=SEARCH_ENDPOINT, credential=SEARCH_CREDENTIAL)
indexer_client = SearchIndexerClient(endpoint=SEARCH_ENDPOINT, credential=SEARCH_CREDENTIAL)

# Clean up resources
def clean_up():
    indexer_client.delete_data_source_connection(DATA_SOURCE_NAME)
    print(f"Datasource '{DATA_SOURCE_NAME}' deleted successfully.")

    indexer_client.delete_skillset(SKILLSET_NAME)
    print(f"Skillset '{SKILLSET_NAME}' deleted successfully.")

    indexer_client.delete_indexer(INDEXER_NAME)
    print(f"Indexer '{INDEXER_NAME}' deleted successfully.")

    index_client.delete_knowledge_base(KNOWLEDGE_BASE_NAME)
    print(f"Knowledge base '{KNOWLEDGE_BASE_NAME}' deleted successfully.")

    index_client.delete_knowledge_source(knowledge_source=KNOWLEDGE_SOURCE_NAME)
    print(f"Knowledge source '{KNOWLEDGE_SOURCE_NAME}' deleted successfully.")

    index_client.delete_index(INDEX_NAME)
    print(f"Index '{INDEX_NAME}' deleted successfully.")


# =====================
# Main Entry Point
# =====================
def main():
    clean_up()


if __name__ == "__main__":
    main()