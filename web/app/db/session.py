import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from app.core.config import DATABASE_URL

DB_URL = f"{DATABASE_URL}_test" if os.environ.get("TESTING") else DATABASE_URL
engine = create_engine(str(DB_URL), pool_pre_ping=True, poolclass=NullPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
