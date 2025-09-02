from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/notesdb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class NoteDB(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class NoteCreate(BaseModel):
    content: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/notes")
def get_notes():
    db = SessionLocal()
    notes = db.query(NoteDB).all()
    db.close()
    return notes

@app.post("/notes")
def create_note(note: NoteCreate):
    db = SessionLocal()
    new_note = NoteDB(content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    db.close()
    return new_note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    db = SessionLocal()
    note = db.query(NoteDB).filter(NoteDB.id == note_id).first()
    if not note:
        db.close()
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    db.close()
    return {"message": "Note deleted successfully"}
