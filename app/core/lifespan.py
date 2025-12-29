from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    The lifespan protocol is a single async context that runs once at startup (before yield) and once at shutdown (after yield).

    This is used for app startup activities like connecting to databases, and shutdown activities like closing connections.

    Also this triggered on os process signals like SIGTERM and SIGINT, which used to handle graceful shutdowns.

    """
    # Startup activities
    print("App starting...Preparing resources...")
    try:
        yield
    finally:
        # Shutdown activities
        print("App shutting down...releasing resources...")

