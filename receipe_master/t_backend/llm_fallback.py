from mcp import tool
import google.generativeai as genai

@tool
def llm_fallback(query: str) -> str:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Suggest a recipe for: {query}")
    return response.text
