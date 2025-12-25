from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os

app = FastAPI()

# --- CORS SETTINGS (YE ZAROORI HAI) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Isse aapka frontend baat kar payega
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

@app.get("/")
def home():
    return {"status": "Zenith AI Cloud is Active"}

@app.get("/chat")
def chat(prompt: str):
    try:
        response = model.generate_content(prompt)
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}

