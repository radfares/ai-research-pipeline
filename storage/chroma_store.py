"""ChromaDB vector store wrapper."""
import chromadb
from chromadb.config import Settings
import os
from dotenv import load_dotenv

load_dotenv()

class ChromaStore:
    def __init__(self, host=None, port=None, collection_name=None):
        self.client = chromadb.HttpClient(
            host=host or os.getenv("CHROMADB_HOST", "localhost"),
            port=int(port or os.getenv("CHROMADB_PORT", "8000")),
            settings=Settings(allow_reset=True)
        )
        self.collection = self.client.get_or_create_collection(
            collection_name or os.getenv("CHROMADB_COLLECTION", "ai_research")
        )

    def add(self, ids, documents, metadatas):
        self.collection.add(ids=ids, documents=documents, metadatas=metadatas)

    def query(self, q, n_results=5, filters=None):
        return self.collection.query(query_texts=[q], n_results=n_results, where=filters)
