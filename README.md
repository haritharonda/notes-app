# Notes App (React + FastAPI + PostgreSQL)

## Frontend
- React app with Axios for API calls
- Deployed on Vercel

## Backend
- FastAPI app with PostgreSQL + SQLAlchemy
- Deployed on Render

## Setup
1. Clone repo
2. For frontend: `cd notes-frontend && npm install && npm start`
3. For backend: `cd notes-backend && pip install -r requirements.txt && uvicorn main:app --reload`
4. Set `DATABASE_URL` in Render to your PostgreSQL connection string

## API Routes
- GET `/notes` → fetch all notes
- POST `/notes` → create new note
- DELETE `/notes/{id}` → delete note
- GET `/health` → health check

## Deployment
- Frontend → Vercel
- Backend → Render (with PostgreSQL DB)
