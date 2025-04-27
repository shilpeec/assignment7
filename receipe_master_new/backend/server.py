from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from agent.agent import run_agent

app = FastAPI()

# Allow CORS for the Chrome extension domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://ekjhmhcancipnphmkmgbhfeokmeimmph"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_recipe(query: dict):
    try:
        user_query = query.get("query", "")
        if not user_query:
            return JSONResponse(content={"error": "No query provided"}, status_code=400)

        answer, trace = run_agent(user_query)

        return {"answer": answer, "trace": trace}
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
