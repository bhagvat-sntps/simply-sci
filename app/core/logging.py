""""
Logging configuration for the application.
"""

import logging
import sys
from pythonjsonlogger import jsonlogger
from app.core.config import settings
from app.filters.logging_filters import RequestContextFilter


def setup_logging():
    log_level = logging.DEBUG if settings.debug else logging.INFO

    ## sending logs to standard output , cab be read by docker/kubernetes logging systems
    handler = logging.StreamHandler(sys.stdout)

    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s "
        "%(trace_id)s %(path)s",
        json_indent=4
    )


    handler.setFormatter(formatter)
    handler.addFilter(RequestContextFilter())


    ## ovverride the default root logger, avoid duplicate logs
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.handlers = [handler]

    ## apply same json logger for logs added by uvicorn
    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logger = logging.getLogger(logger_name)
        logger.handlers = [handler]
        logger.propagate = False
