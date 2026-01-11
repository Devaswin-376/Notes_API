from fastapi import Depends, APIRouter, status,HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.note import Note
from app.models.note_version import NoteVersion
from app.schemas.note import NoteCreate, NoteUpdate, NoteVersionOut,NoteOut
from app.core.dependencies import get_current_user
from app.models.user import User



router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/", response_model=NoteOut,status_code=status.HTTP_201_CREATED)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    print("CREATE NOTE WITH VERSION LOGIC ACTIVE")
    new_note = Note(
        title=note.title,
        content=note.content,
        owner_id=current_user.id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    
    version = NoteVersion(
        note_id=new_note.id,
        version_number=1,
        title=new_note.title,
        content=new_note.content,
        editor_id=current_user.id,
    )
    db.add(version)
    db.commit()
    
    return new_note


@router.put("/{note_id}")
def update_note(
    note_id: int,
    data: NoteUpdate,
    db: Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    note = db.query(Note).filter(Note.id == note_id).first()
    
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    if note.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to update")
    
    last_version = (
        db.query(NoteVersion)
        .filter(NoteVersion.note_id == note.id)
        .order_by(NoteVersion.version_number.desc())
        .first()
    )

    next_version = 1 if not last_version else last_version.version_number + 1
    
    # Update the note
    note.title = data.title
    note.content = data.content
    
    # Create a new version entry
    new_version = NoteVersion(
        note_id=note.id,
        version_number=next_version,
        title = note.title,
        content = note.content,
        editor_id = current_user.id
    )
    db.add(new_version)
    db.commit()
    db.refresh(new_version)
    
    return new_version

@router.get("/{note_id}/versions", response_model=list[NoteVersionOut])
def list_versions(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note or note.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Note not found")

    return (
        db.query(NoteVersion)
        .filter(NoteVersion.note_id == note_id)
        .order_by(NoteVersion.created_at.desc())
        .all()
    )


@router.post("/{note_id}/versions/{version_id}/restore")
def restore_version(
    note_id: int,
    version_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note or note.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Note not found")

    version = (
        db.query(NoteVersion)
        .filter(
            NoteVersion.id == version_id,
            NoteVersion.note_id == note_id,
        )
        .first()
    )

    if not version:
        raise HTTPException(status_code=404, detail="Version not found")

    last_version = (
        db.query(NoteVersion)
        .filter(NoteVersion.note_id == note.id)
        .order_by(NoteVersion.version_number.desc())
        .first()
    )

    next_version = 1 if not last_version else last_version.version_number + 1
    # 🔹 Save current state before restoring
    backup = NoteVersion(
        note_id=note.id,
        version_number=next_version,
        title=note.title,
        content=note.content,
        editor_id=current_user.id,
    )
    db.add(backup)

    # 🔹 Restore
    note.title = version.title
    note.content = version.content

    db.commit()
    return {"message": "Version restored successfully"}


@router.get(
    "/{note_id}/versions/{version_id}",
    response_model=NoteVersionOut
)
def get_version(
    note_id: int,
    version_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note or note.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Note not found")

    version = (
        db.query(NoteVersion)
        .filter(
            NoteVersion.id == version_id,
            NoteVersion.note_id == note_id
        )
        .first()
    )

    if not version:
        raise HTTPException(status_code=404, detail="Version not found")

    return version



@router.delete("/{note_id}", status_code=200)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    if note.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(note)
    db.commit()

    return {"message": "Note deleted successfully"}
