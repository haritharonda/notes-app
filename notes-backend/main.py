
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get DB URL from environment (for Vercel/Neon setup)
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

# Database Model
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(Text)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Model
class NoteCreate(BaseModel):
    title: str
    content: str

# ✅ Root endpoint
@app.get("/")
def root():
    return {"message": "Notes API is running 🚀"}

# ✅ Get all notes
@app.get("/notes")
def get_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    db.close()
    return notes

# ✅ Create a note
@app.post("/notes")
def create_note(note: NoteCreate):
    db = SessionLocal()
    db_note = Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    db.close()
    return db_note


