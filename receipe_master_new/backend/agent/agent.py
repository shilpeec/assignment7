from agent.perception import embed_query  # Updated to use embed_query
from agent.memory import search_faiss
from agent.action import fallback_to_llm
from sentence_transformers import SentenceTransformer


model = SentenceTransformer('all-MiniLM-L6-v2')


def run_agent(user_query: str):
    trace = []

    # Step 1: Perception (embedding)
    query_embedding = embed_query(user_query)
    trace.append("Perception: Query converted to embedding.")
    print(f"Query Embedding: {query_embedding}")  # Log the embedding to verify

    # Step 2: Memory (search FAISS index)
    distances, indices = search_faiss(query_embedding)
    trace.append("Memory: Searched FAISS index for similar content.")
    
    # Log distances and indices returned by FAISS
    print(f"FAISS Distances: {distances}")
    print(f"FAISS Indices: {indices}")

    # Step 3: Decision (based on distance threshold)
    if distances[0][0] < 0.4:
        trace.append(f"Memory: Found relevant match with distance {distances[0][0]:.4f}.")
        memory_content = "Answer found from memory (embeddings)."
        return {"text": memory_content}, trace
    else:
        trace.append("Memory: No good match found. Will query LLM.")
        # Step 4: Action (query LLM)
        llm_answer = fallback_to_llm(user_query)
        trace.append("Action: Queried LLM and got fresh answer.")
        return {"text": llm_answer}, trace
