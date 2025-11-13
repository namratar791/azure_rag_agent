from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from config import AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_INDEX, AZURE_SEARCH_KEY

search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY)
)

def retrieve_context(query: str, top_k: int = 3):
    """Search top-k results from Azure AI Search"""
    results = search_client.search(
        search_text=query,
        top=top_k,
        query_type="semantic",
        semantic_configuration_name="default",
        select=["content", "source"]
    )
    docs = []
    for r in results:
        docs.append({"content": r["content"], "source": r.get("source", "unknown")})
    return docs
