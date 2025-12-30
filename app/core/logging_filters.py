"""
below file defines a logging filter to add request context information such as trace ID and request path to each log records.
"""


import logging
from app.core.context import correlation_id_ctx, path_ctx

class RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.trace_id = correlation_id_ctx.get()
        record.path = path_ctx.get()
        return True
