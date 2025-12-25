from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os

app = FastAPI()

# CORS bypass for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Latest Advance Model Configuration
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash') # Sabse stable version

@app.get("/")
def home():
    return {"status": "Zenith AI is Online"}

@app.get("/chat")
def chat(prompt: str):
    try:
        # Latest method for content generation
        response = model.generate_content(prompt)
        return {"reply": response.text}
    except Exception as e:
        return {"error": "API Key issue or Model busy. Please check Render Environment Variables."}

