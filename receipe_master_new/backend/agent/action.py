# action.py

import os
import google.generativeai as genai

# Initialize Gemini or any LLM (assuming key already set)
#genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
genai.configure(api_key="abcd")

def fallback_to_llm(query: str) -> dict:
    """Use LLM to find a recipe online or generate one."""
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Find or generate a good food recipe for: {query}. Provide title and URL if possible."

    response = model.generate_content(prompt)
    text = response.text.strip()

    return {
        "text": text,
        "url": None  # You can improve later to extract links if needed
    }
