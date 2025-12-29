from fastapi import APIRouter

router: any = APIRouter()

@router.get("/", tags=["Summary"])
async def health_check() -> dict:
    """
    Returns a summary status to verify that the Summary API is running.
    """
    return {"status": "ok"} 