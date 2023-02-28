from app.db.repositories.base import BaseRepository
from app.models.note import Note as NoteModel
from app.schemas.note import NoteCreate, NoteInDB
from typing import List


class NotesRepository(BaseRepository):
    """ "
    All database actions associated with the Note resource
    """
    async def create_note(self, *, new_note: NoteCreate) -> NoteInDB:
        note = NoteModel(note=new_note.note)
        self.session.add(note)
        self.session.commit()
        return note

    async def retrieve_all_notes(self) -> List[NoteModel]:
        return self.session.query(NoteModel).all()
