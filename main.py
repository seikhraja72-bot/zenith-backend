from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Configuration
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Sahi Model Initialization (Iss line se error theek ho jayegi)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.get("/")
def home():
    return {"status": "Zenith AI is Online"}

@app.get("/chat")
def chat(prompt: str):
    try:
        # Prompt ko model ke paas bhejna
        response = model.generate_content(prompt)
        return {"reply": response.text}
    except Exception as e:
        # Agar koi error aaye to wo yahan dikhega
        return {"error": str(e)}

