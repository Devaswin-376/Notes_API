from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.api.auth import router as auth_router
from app.api.notes import router as notes_router
from app.db.deps import get_db
from app.schemas.note import NoteCreate
from app.models.note import Note
from app.db.base import Base
from app.db.session import engine

#Base.metadata.create_all(bind=engine)


app = FastAPI(title="Notes API with Version History")
app.include_router(auth_router)
app.include_router(notes_router)

@app.post("/notes")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = Note(
        title = note.title,
        content = note.content,
        owner_id = 1 # temporary
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    
    return {
        "id" : new_note.id,
        "title" : new_note.title,
        "content" : new_note.content
    }
    
    