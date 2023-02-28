from sqlalchemy import Column, Integer, String
from app.db.base_class import Base


class Note(Base):
    id = Column(Integer, primary_key=True, index=True)
    note = Column(String(256), nullable=False)
