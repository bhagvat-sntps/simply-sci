from fastapi import APIRouter, Depends
import logging

from app.core.config import settings
from app.services.summary_service import SummaryService
from app.schemas.summary import AbstractSummaryResponse, SummaryRequest


router: any = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", response_model=AbstractSummaryResponse , tags=["Summary"])
async def summarize(
    payload: SummaryRequest,
    service: SummaryService = Depends(SummaryService),
)-> AbstractSummaryResponse :
    """
    Summarize the given research paper abstract content.
    """
    return await service.summarize_abstract(payload.content)
    