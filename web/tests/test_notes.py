import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
from app.schemas.note import NoteCreate

# decorate all tests with @pytest.mark.asyncio
pytestmark = pytest.mark.asyncio


@pytest.fixture
def new_note():
    return NoteCreate(
        note="test note"
    )


class TestNoteRoutes:
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("notes:create-note"), json={})
        assert res.status_code != HTTP_404_NOT_FOUND

    async def test_invalid_input_raises_error(
        self, app: FastAPI, client: AsyncClient
    ) -> None:
        res = await client.post(app.url_path_for("notes:create-note"), json={})
        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY


class TestCreateNote:
    async def test_valid_input_creates_note(
        self, app: FastAPI, client: AsyncClient, new_note: NoteCreate
    ) -> None:
        res = await client.post(
            app.url_path_for("notes:create-note"), json={"new_note": new_note.dict()}
        )
        assert res.status_code == HTTP_201_CREATED
        created_note = NoteCreate(**res.json())
        assert created_note == new_note
