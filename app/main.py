# app/main.py
from fastapi import FastAPI
from app.api.health import router as health_router


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    app = FastAPI(title="My API")
    app.include_router(health_router, prefix="/health", tags=["health"])
    return app


#Initialize the FastAPI application.
app = create_app()


#Event handlers for startup and shutdown.
@app.on_event("startup")
async def startup():
    print("App starting...")

@app.on_event("shutdown")
async def shutdown():
    print("App shutting down...")