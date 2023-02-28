from typing import Callable, Type
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.repositories.base import BaseRepository
from app.db.session import SessionLocal
from typing import Generator


def get_session() -> Generator:
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()


def get_repository(Repo_type: Type[BaseRepository]) -> Callable:
    def get_repo(session: Session = Depends(get_session)) -> Type[BaseRepository]:
        return Repo_type(session)

    return get_repo
