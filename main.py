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

# Latest API Key configuration
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Latest Model name use kar rahe hain
model = genai.GenerativeModel('gemini-1.5-flash')

@app.get("/")
def home():
    return {"status": "Zenith AI is Online"}

@app.get("/chat")
def chat(prompt: str):
    try:
        # Latest generation method
        response = model.generate_content(prompt)
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}


