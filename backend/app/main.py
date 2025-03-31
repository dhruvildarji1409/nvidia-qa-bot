from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI(
    title="Nvidia Q&A Chatbot",
    description="A local chatbot for Nvidia-specific questions",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

def is_nvidia_related(question: str) -> bool:
    # Simple keyword-based check (can be improved with better NLP)
    nvidia_keywords = [
        'nvidia', 'gpu', 'cuda', 'geforce', 'rtx', 'gtx', 'quadro',
        'tesla', 'dgx', 'graphics card', 'graphics driver'
    ]
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in nvidia_keywords)

@app.get("/")
async def read_root():
    return {"status": "ok", "message": "Nvidia Q&A Chatbot API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat")
async def chat(question: Question):
    if not is_nvidia_related(question.question):
        return {
            "answer": "I can only answer questions related to Nvidia products and technologies. "
                     "Please rephrase your question to be about Nvidia."
        }
    
    # For now, return a placeholder response
    # TODO: Implement actual LLM integration
    return {
        "answer": f"This is a placeholder response. In the future, I will provide detailed "
                 f"information about your Nvidia-related question: '{question.question}'"
    }