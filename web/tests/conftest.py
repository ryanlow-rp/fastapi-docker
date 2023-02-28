import warnings
import os

import pytest_asyncio
from asgi_lifespan import LifespanManager

from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.orm import Session

import alembic
from alembic.config import Config

# Apply migrations at beginning and end of testing session


@pytest_asyncio.fixture(scope="session")
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    os.environ["TESTING"] = "1"
    config = Config("alembic.ini")

    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")

# Create a new application for testing


@pytest_asyncio.fixture
def app(apply_migrations: None) -> FastAPI:
    from app.api.server import get_application

    return get_application()

# Grab a reference to our database when needed


@pytest_asyncio.fixture
def session(app: FastAPI) -> Session:
    from app.api.deps import get_session

    return get_session()

# Make requests in our tests


@pytest_asyncio.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="https://testserver",
            headers={"Content-Type": "application/json"}
        ) as client:
            yield client
