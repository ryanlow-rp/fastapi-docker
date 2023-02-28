from typing import Optional
from app.schemas.core import IDModelMixin, CoreModel

# Shared properties


class NoteBase(CoreModel):
    """
    All common characteristics of our Note resource
    """

    note: Optional[str]

# Properties to receive on item creation


class NoteCreate(NoteBase):
    note: str

# Properties to receive on item update


class NoteUpdate(NoteBase):
    note: str

# Properties shared by models stored in DB


class NoteInDBBase(IDModelMixin, NoteBase):
    id: int
    note: str

    class Config:
        orm_mode = True

# Properties to return to client


class Note(NoteInDBBase):
    pass

# Properties stored in DB


class NoteInDB(NoteInDBBase):
    pass
