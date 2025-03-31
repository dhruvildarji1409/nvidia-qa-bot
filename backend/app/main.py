from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/")
async def read_root():
    return {"status": "ok", "message": "Nvidia Q&A Chatbot API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}