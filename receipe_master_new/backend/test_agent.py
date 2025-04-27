from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize the embedder
embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Sample recipes (you would replace this with your actual recipes)
recipes = [
    "How to make Chana Masala"
]

# Generate embeddings for the recipes
recipe_embeddings = embedder.encode(recipes)  # Embedding all recipes

# Convert embeddings to float32 for FAISS
recipe_embeddings = np.array(recipe_embeddings, dtype=np.float32)

# Create FAISS index
faiss_index = faiss.IndexFlatL2(recipe_embeddings.shape[1])  # Using L2 distance (Euclidean)
faiss_index.add(recipe_embeddings)  # Add embeddings to the index

# Save the FAISS index to disk (for later use)
faiss.write_index(faiss_index, "recipe_faiss_index.index")

print("FAISS index created and saved.")
