from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # Tiny and fast model

def embed(text: str):
    embedding = model.encode(text)
    return embedding

import numpy as np

def load_embeddings():
    embeddings = np.load('data/embeddings.npy')  # Loading precomputed embeddings
    return embeddings
