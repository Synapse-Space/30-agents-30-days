from sentence_transformers import SentenceTransformer 
from shared_core.knowledge import Embedder 

class LocalEmbedder(Embedder):
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def embed(self, text):
        return self.model.encode(text, normalize_embeddings=True).tolist()
