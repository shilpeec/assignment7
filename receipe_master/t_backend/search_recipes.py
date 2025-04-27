from mcp import Tool
import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel

# Define InputSchema for the search query
class InputSchema(BaseModel):
    query: str

@Tool(name="search_recipes", input_schema=InputSchema)
def search_recipes(query: str) -> dict:
    with open('backend/data/recipes.json', 'r', encoding='utf-8') as f:
        recipes = json.load(f)

    embeddings = np.load('backend/data/embeddings/embeddings.npy')
    index = faiss.read_index('backend/data/faiss_index/recipes.index')

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_emb = model.encode([query])

    distances, indices = index.search(query_emb, k=1)

    if indices[0][0] < len(recipes):
        best_recipe = recipes[indices[0][0]]
        return {
            "text": best_recipe['text'],
            "url": best_recipe['url']
        }
    else:
        return {"text": None, "url": None}
