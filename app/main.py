from fastapi import FastAPI
import uvicorn
from app.core.config import settings
from app.core.lifespan import lifespan
from app.api.router import api_router


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    app = FastAPI(title="My API",lifespan=lifespan)
    app.include_router(api_router)
    return app


app = create_app()


# Development server entry point.
def dev():
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        log_level="debug"
)