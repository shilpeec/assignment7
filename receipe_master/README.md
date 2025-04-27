Recipe Search
This project allows you to search for recipes using a combination of FastAPI for the backend and a Chrome Extension for the front end. The recipes are indexed with embeddings generated using Sentence-Transformers and stored in a FAISS index. The Chrome extension queries the FastAPI backend to fetch relevant recipes based on user input.

Features
FastAPI Backend: Provides a recipe search API built with FastAPI.

FAISS Indexing: Uses FAISS for efficient similarity search on precomputed recipe embeddings.

Chrome Extension: Queries the FastAPI API from a Chrome extension to return relevant recipes.

Recipe Embeddings: Recipes are embedded using a transformer model, and the embeddings are stored for quick search.

Memory and Fallback: If a match isn't found in the recipe index, the backend queries a fallback method.

Requirements
Before running the project, ensure you have the following dependencies installed:

Backend Dependencies
Python 3.7+

FastAPI

Pydantic

FAISS (or faiss-cpu for CPU support)

Sentence-Transformers

NumPy

Uvicorn (for serving FastAPI app)