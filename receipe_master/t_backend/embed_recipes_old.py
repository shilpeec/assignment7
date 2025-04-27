from mcp import Tool  # Assuming you have the Tool defined as above
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import json
import os
import numpy as np

# Define an input schema, even if it's empty for your case
class InputSchema(BaseModel):
    pass

input_schema = InputSchema()

@Tool(name="embed_recipes", input_schema=input_schema)
def embed_recipes() -> str:
    model = SentenceTransformer('all-MiniLM-L6-v2')

    with open('backend/data/recipes.json', 'r', encoding='utf-8') as f:
        recipes = json.load(f)

    texts = [r['text'] for r in recipes]
    embeddings = model.encode(texts)

    os.makedirs('backend/data/embeddings', exist_ok=True)
    np.save('backend/data/embeddings/embeddings.npy', embeddings)

    return f"Embedded {len(texts)} recipes."
