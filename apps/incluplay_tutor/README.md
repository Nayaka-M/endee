# IncluPlayAI Tutor 🎓

AI-powered NCERT tutor for Indian school students using **Endee Vector Database** + **Groq AI LLaMA 3.3 70B**.

## How Endee is Used
- 40+ NCERT knowledge chunks stored as vectors in Endee
- Student question converted to vector
- Endee performs semantic similarity search
- Top matching chunks sent to Groq AI as context (RAG)
- Groq generates clear student-friendly answer

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
# Add your GROQ_API_KEY to .env
uvicorn main:app --reload
```

## API Endpoints
- GET `/` - Health check
- POST `/ask` - AI Tutor with RAG
- POST `/search` - Semantic search via Endee
- POST `/quiz` - Generate AI quiz
- GET `/db-stats` - Endee DB stats

## Full Flutter Project
https://github.com/Nayaka-M/incluplayai