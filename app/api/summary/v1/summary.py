from http.client import HTTPException
from fastapi import APIRouter, HTTPException
import logging


router: any = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/", tags=["Summary"])
async def health_check() -> dict:
    """
    Returns a summary status to verify that the Summary API is running.
    """
    logger.info("summary endpoint called......")
    return {"status": "ok"} 