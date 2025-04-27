from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import json
import os

# Load recipes
with open('backend/data/recipes.json', 'r', encoding='utf-8') as f:
    recipes = json.load(f)

# Extract recipe texts
texts = [recipe['text'] for recipe in recipes]

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings
embeddings = model.encode(texts, show_progress_bar=True)

# Save embeddings
os.makedirs('backend/data/embeddings', exist_ok=True)
np.save('backend/data/embeddings/embeddings.npy', embeddings)

# Create and save FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
os.makedirs('backend/data/faiss_index', exist_ok=True)
faiss.write_index(index, 'backend/data/faiss_index/recipes.index')

print("✅ Embeddings and FAISS index created successfully!")
