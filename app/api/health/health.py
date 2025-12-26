from fastapi import APIRouter

router: any = APIRouter()


@router.get("/", tags=["Health"])
async def health_check() -> dict:
    """
    Health check endpoint to verify that the API is running.
    """
    return {"status": "ok"} 