from fastapi import FastAPI
import uvicorn
from app.core.config import settings
from app.core.lifespan import lifespan
from app.api.router import api_router
from app.core.logging import setup_logging
from app.middlewares.correlation import correlation_middleware


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    # setup logging
    setup_logging()

    app = FastAPI(title="My API",lifespan=lifespan)
    app.middleware("http")(correlation_middleware)
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