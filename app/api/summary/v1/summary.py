from http.client import HTTPException
from fastapi import APIRouter, Depends
import logging
from fastapi.params import Header

from app.core.config import settings
from app.services.summary_service import SummaryService
from app.schemas.summary import AbstractSummaryResponse, SummaryRequest


router: any = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", response_model=AbstractSummaryResponse, tags=["Summary"])
async def summarize(
    payload: SummaryRequest,
    service: SummaryService = Depends(SummaryService),
    authorization: str = Header(...),
) -> AbstractSummaryResponse:
    """
    Summarize the given research paper abstract content.
    """

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")

    return await service.summarize_abstract(payload.content, authorization)
