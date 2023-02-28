from fastapi import APIRouter
from app.api.routes.notes import router as notes_router

router = APIRouter()
router.include_router(notes_router, prefix="/notes", tags=["notes"])
