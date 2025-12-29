import time
import uuid
import logging
from fastapi import Request
from app.core.context import correlation_id_ctx, path_ctx

logger = logging.getLogger(__name__)

async def correlation_middleware(request: Request, call_next):
    start = time.perf_counter()

    correlation_id = (
        request.headers.get("x-correlation-id")
        or str(uuid.uuid4())
    )

    # Set context vars
    correlation_id_ctx.set(correlation_id)
    path_ctx.set(request.url.path)

    # pass controller to the route handler . which executes the actual request and returns response

    response = await call_next(request)

    duration = round((time.perf_counter() - start) * 1000, 2)

    ## after response is generated , final log is added with request/response details
    logger.info(
        "Request completed",
        extra={
            "method": request.method,
            "status_code": response.status_code,
            "duration_ms": duration,
        },
    )

    response.headers["x-correlation-id"] = correlation_id
    return response
