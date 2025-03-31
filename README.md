# Nvidia Q&A Chatbot

A local browser-based chatbot that specifically answers Nvidia-related questions using a lightweight LLM.

## Features

- Local browser-based operation
- FastAPI backend with React frontend
- Lightweight LLM for quick responses
- Nvidia-specific question filtering
- Vector store for efficient information retrieval

## Project Structure

```
nvidia-qa-bot/
├── backend/         # FastAPI backend
├── frontend/       # React frontend
├── models/         # Model files and configurations
├── data/           # Nvidia documentation and training data
└── tests/          # Test suites
```

## Setup

### Prerequisites

- Python 3.9+
- Node.js 16+
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/dhruvildarji1409/nvidia-qa-bot.git
cd nvidia-qa-bot
```

2. Set up backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up frontend:
```bash
cd frontend
npm install
```

## Development

1. Start backend server:
```bash
cd backend
uvicorn app.main:app --reload
```

2. Start frontend development server:
```bash
cd frontend
npm start
```

## License

MIT