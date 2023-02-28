from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_notes() -> List[dict]:
    notes = [
        {"id": 1, "note": "Note 1"},
        {"id": 2, "note": "Note 2"},
    ]

    return notes
