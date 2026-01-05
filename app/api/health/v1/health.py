from fastapi import APIRouter

router: any = APIRouter()


@router.get("/")
async def health_check() -> dict:
    """
    Health check endpoint to verify that the API is running.
    """
    return {"status": "ok"}
