"""
Common file to place Context variables for request-scoped data.
"""

from contextvars import ContextVar

correlation_id_ctx: ContextVar[str | None] = ContextVar(
    "correlation_id", default=None
)

path_ctx: ContextVar[str | None] = ContextVar(
    "path", default=None
)
