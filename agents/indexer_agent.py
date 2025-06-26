from chromadb import PersistentClient
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

class IndexerAgent:
    def __init__(self, persist_directory="data/chroma_db"):
        self.persist_directory = persist_directory
        self.client = PersistentClient(path=persist_directory, settings=Settings(anonymized_telemetry=False))
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
    
    def index_documents(self, kb, collection_name="email_kb"):
        existing_collections = [col.name for col in self.client.list_collections()]
        
        if collection_name in existing_collections:
            print(f"Collection '{collection_name}' already exists. Skipping indexing.")
            return self.client.get_collection(collection_name), self.embedder
        
        collection = self.client.create_collection(collection_name)

        documents = [f"Category: {item['category']}, Intent: {item['intent']}, Answer: {item['response']}" for item in kb]
        ids = [f"doc_{i}" for i in range(len(documents))]
        
        for i in range(0, len(documents), 5461):
            batch = documents[i:i+5461]
            embeddings = self.embedder.encode(batch).tolist()
            collection.add(documents=batch, ids=ids[i:i+5461], embeddings=embeddings)
        
        return collection, self.embedder
