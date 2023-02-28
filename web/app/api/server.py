from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.core import config
from app.api.routes import router as api_router


def get_application():
    app = FastAPI(
        title=config.PROJECT_NAME, version=config.VERSION, root_path=config.API_PREFIX
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    return app


app = get_application()
