# perception.py
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_query(query: str) -> list:
    """Convert a text query into an embedding vector."""
    return model.encode([query])
