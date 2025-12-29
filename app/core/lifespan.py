from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    The lifespan protocol is a single async context that runs once at startup (before yield) and once at shutdown (after yield).

    This is used for app startup activities like connecting to databases, and shutdown activities like closing connections.

    Also this triggered on os process signals like SIGTERM and SIGINT, which used to handle graceful shutdowns.

    """
    try:
        logger.info("Application startup")
        yield
        logger.info("Application shutdown" , exc_info= {    
                 
        })
    finally:
        logger.info("App shutting down...Cleaning up resources...")

