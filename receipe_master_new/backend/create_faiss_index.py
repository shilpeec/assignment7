from mcp import tool
import faiss
import numpy as np
import os

@tool
def create_faiss_index() -> str:
    embeddings = np.load('data/embeddings/embeddings.npy')
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs('backend/data/faiss_index', exist_ok=True)
    faiss.write_index(index, 'backend/data/faiss_index/recipes.index')

    return "FAISS index created."
