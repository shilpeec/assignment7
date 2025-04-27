import numpy as np
import faiss

def search_faiss(query_embedding, top_k=5):
    index = faiss.read_index("data/faiss_index/recipes.index")
    
    # Ensure query_embedding is a numpy array
    query_embedding = np.array(query_embedding).astype('float32')
    
    # Ensure it is 2D (batch_size, dimension)
    if query_embedding.ndim == 1:
        query_embedding = np.expand_dims(query_embedding, axis=0)
    
    # Now it’s safe to search
    distances, indices = index.search(query_embedding, top_k)
    return distances, indices
