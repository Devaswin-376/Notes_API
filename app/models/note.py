from sqlalchemy import Column, Integer,String, ForeignKey, Text
from app.db.base import Base
from sqlalchemy.orm import relationship

class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    owner = relationship("User")
    
    versions = relationship("NoteVersion", back_populates="note", cascade="all, delete-orphan")