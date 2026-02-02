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
    OutputFieldMappingEntry,
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

# Create or update an index
def create_or_update_index():

    fields = [
        SearchField(name="id", type="Edm.String", key=True, filterable=True, sortable=True, facetable=True, analyzer_name="keyword"),
        SearchField(name="parent_id", type="Edm.String", key=False, filterable=True, sortable=False, facetable=False),
        SearchField(name="page_chunk", type="Edm.String", filterable=False, sortable=False, facetable=False, searchable=True),
        SearchField(name="page_embeddings", type="Collection(Edm.Single)", stored=True, searchable=True, vector_search_dimensions=1536, vector_search_profile_name="hnsw_text_3_small_profile"),
        SearchField(name="story_title", type="Edm.String", filterable=True, sortable=True, facetable=False, searchable=True),
        SearchField(name="last_modified", type="Edm.DateTimeOffset", filterable=True, sortable=True, facetable=False),
        SearchField(name="source_path", type="Edm.String", filterable=True, sortable=False, facetable=False),
        SearchField(name="source_file", type="Edm.String", filterable=True, sortable=True, facetable=True),
    ]

    vector_search = VectorSearch(
        profiles = [
            VectorSearchProfile(
                name = "hnsw_text_3_small_profile",
                algorithm_configuration_name = "alg",
                vectorizer_name = "kaz_aoai_vectorizer"
                )
        ],
        algorithms=[HnswAlgorithmConfiguration(name="alg")],
        vectorizers=[
            AzureOpenAIVectorizer(
                vectorizer_name = "kaz_aoai_vectorizer",
                parameters = AzureOpenAIVectorizerParameters(
                    resource_url = AOAI_ENDPOINT,
                    deployment_name = AOAI_EMBEDDING_DEPLOYMENT,
                    model_name = AOAI_EMBEDDING_MODEL,
                    api_key = AOAI_API_KEY,
                )
            )
        ]
    )

    semantic_search=SemanticSearch(
        default_configuration_name = SEMANTIC_CONFIGURATION_NAME,
        configurations = [
            SemanticConfiguration(
                name = SEMANTIC_CONFIGURATION_NAME,
                prioritized_fields = SemanticPrioritizedFields(
                    content_fields = [
                        SemanticField(field_name="page_chunk")
                    ]
                )
            )
        ]
    )

    index = SearchIndex(name=INDEX_NAME, fields=fields, vector_search=vector_search, semantic_search=semantic_search)
    index_client.create_or_update_index(index)
    print(f"Index '{INDEX_NAME}' created or updated successfully.")


# Create or update a Data Source
def create_or_update_datasource():
    ds = SearchIndexerDataSourceConnection(
        name = DATA_SOURCE_NAME,
        type = "azureblob",
        connection_string=BLOB_CONNECTION_STRING,
        container = SearchIndexerDataContainer(name=BLOB_CONTAINER_NAME, query=BLOB_FOLDER_NAME)
    )
    indexer_client.create_or_update_data_source_connection(ds)
    print(f"Datasource '{DATA_SOURCE_NAME}' created or updated successfully.")


# Create or update a skill set
def create_or_update_skillset():
    skills = [

        # A lightweight and high-performance text chunking implementation that does not parse or interpret PDF structure.
        # It performs a simple fixed-length character-based split.
        # The function takes pre-extracted plain text as input and returns an array of text chunks.
        {
            "@odata.type": "#Microsoft.Skills.Text.SplitSkill",
            "name": "#splitPages",
            "context": "/document",
            "textSplitMode": "pages",
            "maximumPageLength": 1000,
            "inputs": [{"name": "text", "source": "/document/content"}],
            "outputs": [
                {"name": "textItems", "targetName": "chunks"},
                {"name": "ordinalPositions", "targetName": "chunkOrdinals"},
            ],
        },

        # A full document analysis pipeline that operates on binary PDF or image data.
        # It performs OCR, layout analysis, and physical page detection to produce
        # page-level structured output (text, tables, coordinates, and metadata).
        # This approach supports image-based PDFs but is computationally heavy and costly.
        # {
        #     "@odata.type": "#Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill",
        #     "context": "/document",
        #     "inputs": [
        #         {"name": "file_data", "source": "/document/file_data"}
        #     ],
        #     "outputs": [
        #         {"name": "pages", "targetName": "pages"}
        #     ]
        # }

        # Title extraction (first line) via Web API skill
        {
            "@odata.type": "#Microsoft.Skills.Custom.WebApiSkill",
            "name": "#extractTitle",
            "context": "/document/chunks/*",
            "uri": TITLE_SKILL_API_URI,
            "httpMethod": "POST",
            "timeout": "PT30S",
            "batchSize": 1,
            "degreeOfParallelism": 1,
            "inputs": [
                {"name": "text", "source": "/document/chunks/*"}
            ],
            "outputs": [
                {"name": "title", "targetName": "story_title"}
            ]
        },

        # Azure OpenAI Embedding skill for indexing-time vectorization
        {
            "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
            "name": "#embed",
            "context": "/document/chunks/*",
            "resourceUri": AOAI_ENDPOINT,
            "modelName": AOAI_EMBEDDING_MODEL,
            "deploymentId": AOAI_EMBEDDING_DEPLOYMENT,
            "apiKey": AOAI_API_KEY,
            "inputs": [{"name": "text", "source": "/document/chunks/*"}],
            "outputs": [{"name": "embedding", "targetName": "chunkVector"}],
            "dimensions": 1536,
        },
    ]

    skillset = SearchIndexerSkillset(
        name = SKILLSET_NAME,
        skills = skills,
        description = "Split into page-sized chunks, extract title, and generate embeddings with AOAI."
    )
    
    indexer_client.create_or_update_skillset(skillset)
    print(f"Skillset '{SKILLSET_NAME}' created or updated successfully.")
    

# Create or update an Indexer
def create_or_update_indexer():
    indexer = SearchIndexer(
        name=INDEXER_NAME,
        data_source_name = DATA_SOURCE_NAME,
        target_index_name = INDEX_NAME,
        skillset_name = SKILLSET_NAME,
        field_mappings=[
            FieldMapping(source_field_name="metadata_storage_name", target_field_name="source_file"),
            FieldMapping(source_field_name="metadata_storage_path", target_field_name="source_path"),
            FieldMapping(source_field_name="metadata_storage_last_modified", target_field_name="last_modified"),
        ],
        # Use output_field_mappings to map enrichments to index fields  
        # output_field_mappings=[
        #     OutputFieldMappingEntry(name="/document/chunks/*", target_name="page_chunk"),
        #     OutputFieldMappingEntry(name="/document/chunkVector", target_name="page_embedding_text_3_large"),
        #     OutputFieldMappingEntry(name="/document/chunkOrdinals/*", target_name="page_number"),
        #     OutputFieldMappingEntry(name="/document/Title", target_name="story_title"),
        # ],
        output_field_mappings=[],
        parameters={
            "configuration": {
                "dataToExtract": "contentAndMetadata",
                "parsingMode": "default",
            }
        },
    )

    indexer_client.create_or_update_indexer(indexer)
    print(f"Indexer '{INDEXER_NAME}' created or updated successfully.")


# Create or update a knowledge source
def create_or_update_knowledge_source():
    ks = SearchIndexKnowledgeSource(
        name=KNOWLEDGE_SOURCE_NAME,
        description="Knowledge source for classic folktales.",
        search_index_parameters=SearchIndexKnowledgeSourceParameters( # Fields used by the Knowledge Base to provide search results to the LLM
            search_index_name=INDEX_NAME,
            source_data_fields=[
                SearchIndexFieldReference(name="id"), 
                SearchIndexFieldReference(name="page_chunk"),
                SearchIndexFieldReference(name="story_title"),
                SearchIndexFieldReference(name="source_file")
            ]
        ),
    )
    index_client.create_or_update_knowledge_source(knowledge_source=ks)
    print(f"Knowledge source '{KNOWLEDGE_SOURCE_NAME}' created or updated successfully.")


# Create or update a knowledge base
def create_or_update_knowledge_base():
    aoai_params = AzureOpenAIVectorizerParameters(
        resource_url = AOAI_ENDPOINT,
        deployment_name = AOAI_MODEL_DEPLOYMENT,
        model_name = AOAI_MODEL_NAME,
        api_key = AOAI_API_KEY
    )

    knowledge_base = KnowledgeBase(
        name = KNOWLEDGE_BASE_NAME,
        models = [KnowledgeBaseAzureOpenAIModel(azure_open_ai_parameters=aoai_params)],
        knowledge_sources=[
            KnowledgeSourceReference(
                name = KNOWLEDGE_SOURCE_NAME
            )
        ],
        output_mode=KnowledgeRetrievalOutputMode.ANSWER_SYNTHESIS,
        answer_instructions="Provide a two sentence concise and informative answer based on the retrieved documents."
    )

    index_client.create_or_update_knowledge_base(knowledge_base)
    print(f"Knowledge base '{KNOWLEDGE_BASE_NAME}' created or updated successfully.")


# Main Entry Point
def main():
    create_or_update_index()
    create_or_update_datasource()
    create_or_update_skillset()
    create_or_update_indexer()
    create_or_update_knowledge_source()
    create_or_update_knowledge_base()

if __name__ == "__main__":
    main()