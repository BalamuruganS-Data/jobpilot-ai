from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import setup_logger
from app.database.init_db import init_db
from app.api.routes.v1 import router as api_v1_router

logger = setup_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("JobPilot AI backend starting...")
    init_db()
    yield
    logger.info("JobPilot AI backend shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)
app.include_router(
    api_v1_router,
    prefix="/api/v1",
)


@app.get("/")
async def root():
    logger.info("Root endpoint called")

    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }


@app.get("/health")
async def health():
    logger.info("Health endpoint called")

    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "version": settings.APP_VERSION,
    }