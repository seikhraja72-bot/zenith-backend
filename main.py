from fastapi import FastAPI
import google.generativeai as genai
import os

app = FastAPI()

# Cloud Environment se API Key uthayega
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.get("/")
def home():
    return {"status": "Zenith AI Cloud is Active", "owner": "Shaikh Raja"}

@app.get("/chat")
def chat(prompt: str):
    try:
        response = model.generate_content(prompt)
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}
