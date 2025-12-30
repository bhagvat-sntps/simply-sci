from fastapi import APIRouter, Depends
import logging

from app.core.config import settings
from app.services.summary_service import SummaryService
from app.schemas.summary import SummaryRequest, SummaryResponse


router: any = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", response_model=SummaryResponse , tags=["Summary"])
async def summarize(
    payload: SummaryRequest,
    service: SummaryService = Depends(SummaryService),
):
    """
    Summarize the given research paper abstract content.
    """
    summary = await service.summarize_abstract(payload.content)
    return {"summary": summary}