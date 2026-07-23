from fastapi import APIRouter

from app.api.routes.v1 import jobs
from app.api.routes.v1 import resumes

api_router = APIRouter()

api_router.include_router(jobs.router)
api_router.include_router(resumes.router)