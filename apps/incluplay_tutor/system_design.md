# IncluPlayAI System Design

## Architecture
Student Question → Flutter App → FastAPI → Endee Vector DB → Groq AI → Answer

## Endee Vector DB Flow
1. NCERT chunks converted to 128-dim vectors
2. Vectors stored in Endee with metadata
3. Query converted to vector
4. Endee.search() finds top-k similar chunks
5. Chunks sent to Groq AI as RAG context
6. Groq generates student-friendly answer

## Components
- Frontend: Flutter Web + Mobile
- Backend: FastAPI Python
- Vector DB: Endee
- AI Model: Groq LLaMA 3.3 70B
- Gamification: Points + Streaks + Score History