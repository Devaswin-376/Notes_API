from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel):
    title: str
    content: str
    
class NoteUpdate(BaseModel):
    title: str
    content: str
    
class NoteVersionOut(BaseModel):
    id: int
    title: str
    content: str
    editor_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
        
class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    
    class Config:
        from_attributes = True