import google.generativeai as genai

genai.configure(api_key="abcd")  # Put your Gemini API key here

model = genai.GenerativeModel('gemini-1.5-flash')

def query_llm(prompt: str):
    response = model.generate_content(prompt)
    return response.text
