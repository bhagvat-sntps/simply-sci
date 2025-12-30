import logging
from datetime import datetime
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.context import correlation_id_ctx

logger = logging.getLogger(__name__)



class ExternalServiceError(Exception):
    """
    Custom exception to represent errors from external services.
    """
    def __init__(
        self,
        message: str,
        status_code: int = 502,
        details: str | None = None,
    ):
        self.message = message
        self.status_code = status_code
        self.details = details




async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    """
    validation exception handler to log validation errors and return a structured JSON response.
    422 Unprocessable Entity status code is used for validation errors.
    """
    logger.warning(
        "Validation error",
        extra={"errors": exc.errors()},
    )
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):
    """
    HTTP exception handler to log HTTP exceptions and return a structured JSON response.
    """
    logger.info(
        "HTTP exception",
        extra={
            "status": exc.status_code,
            "detail": exc.detail,
        },
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


async def external_service_exception_handler(
    request: Request,
    exc: ExternalServiceError,
):
    """
    External service exception handler to log external service errors and return a structured JSON response.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "details": exc.details,
        },
    )

async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
):
    """
    Unhandled exception handler to log unexpected errors and return a generic structured JSON response.
    500 Internal Server Error status code is used for unhandled exceptions.
    """
    logger.exception("Unhandled exception")
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal Server Error , {}".format(str(exc)),
            "traceId": correlation_id_ctx.get(),
            "timestamp": datetime.now().isoformat() + "Z",
            "path": request.url.path,
        },
    )
