class RetrieverAgent:
    def __init__(self, embedder):
        self.embedder = embedder

    def retrieve_answer(self, collection, query):
        embedding = self.embedder.encode([query])[0]
        results = collection.query(query_embeddings=[embedding], n_results=1)
        return results['documents'][0][0]
