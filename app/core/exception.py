import logging
from datetime import datetime
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.context import correlation_id_ctx

logger = logging.getLogger(__name__)


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
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


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception("Unhandled exception")
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal Server Error",
            "traceId": correlation_id_ctx.get(),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "path": request.url.path,
        },
    )
