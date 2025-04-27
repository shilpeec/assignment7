# assignment7
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

FAISS 

Sentence-Transformers

NumPy

Uvicorn (for serving FastAPI app)

1. Create Recipe Embeddings
You will first need to generate embeddings for all the recipes using Sentence-Transformer.

There are two different projects -
 1. receipe_master
   Here we are Just trying to search for the embedded receipes only
2. receipe_master_new
   Here we are trying to find any receipe, If it is unable to find the querried receipe from the embeddings then the LLM is called.

Chrome Extension
The Chrome extension is built to interact with the FastAPI backend. It sends a query to the API and displays the response in the extension popup.

Running the Chrome Extension
Load the extension into Chrome:

Go to chrome://extensions/

Enable Developer Mode

Click on "Load unpacked"

Select the chrome_extension folder

Once the extension is loaded, you can click the extension icon to open the popup, enter a query, and receive a relevant recipe.
