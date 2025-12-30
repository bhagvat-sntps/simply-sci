from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
import uvicorn
from app.core.config import settings
from app.core.lifespan import lifespan
from app.api.router import api_router
from app.core.logging import setup_logging
from app.middlewares.correlation import correlation_middleware
from app.core.exception import (
    validation_exception_handler,
    http_exception_handler,
    unhandled_exception_handler,
    external_service_exception_handler,
    ExternalServiceError
)


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    # setup logging
    setup_logging()

    
    app = FastAPI(title="My API",lifespan=lifespan)


    # Register exception handlers only after app creation
    # maintain the below order of exception handlers 
    app.add_exception_handler(
        RequestValidationError,
        validation_exception_handler,
    )
    app.add_exception_handler(
        HTTPException,
        http_exception_handler,
    )
    app.add_exception_handler(
        ExternalServiceError,
        external_service_exception_handler,
    )
    app.add_exception_handler(
        Exception,
        unhandled_exception_handler,
    )

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