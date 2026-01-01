from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from app.gateways.openai_gateway import OpenAIGateway

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    The lifespan protocol is a single async context that runs once at startup (before yield) and once at shutdown (after yield).

    This is used for app startup activities like connecting to databases, and shutdown activities like closing connections.

    Also this triggered on os process signals like SIGTERM and SIGINT, which used to handle graceful shutdowns.

    """
    try:
        # Create shared gateway and store on app.state
        app.state.openai_gateway = OpenAIGateway()
        logger.info("Application startup")
        yield
        logger.info("Application shutdown", exc_info={})
    finally:
        # Close if it exists
        gateway = getattr(app.state, "openai_gateway", None)
        if gateway is not None:
            await gateway.aclose()
        await app.state.openai_gateway.aclose()
        logger.info("App shutting down...Cleaning up resources...")
