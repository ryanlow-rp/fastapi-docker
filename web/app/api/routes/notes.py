from typing import List
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from app.schemas.note import NoteCreate, Note
from app.db.repositories.note import NotesRepository
from app.api.deps import get_repository

router = APIRouter()


@router.get(
    "/", response_model=List[Note], name="notes:get-notes", status_code=HTTP_200_OK
)
async def get_all_notes(
    repo: NotesRepository = Depends(get_repository(NotesRepository)),
) -> List[Note]:
    notes = await repo.retrieve_all_notes()
    return notes


@router.post(
    "/", response_model=Note, name="notes:create-note", status_code=HTTP_201_CREATED
)
async def create_new_note(
    new_note: NoteCreate = Body(..., embed=True),
    repo: NotesRepository = Depends(get_repository(NotesRepository)),
) -> Note:
    created_note = await repo.create_note(new_note=new_note)
    return created_note
