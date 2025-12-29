
## common file to aggregate all API routers

from fastapi import APIRouter
from app.api.health.v1.health import router as v1_health_router
from app.api.summary.v1.summary import router as v1_summary_router

api_router = APIRouter()


api_router.include_router(v1_health_router, prefix="/health", tags=["health"])
api_router.include_router(v1_summary_router, prefix="/summary", tags=["summary"])