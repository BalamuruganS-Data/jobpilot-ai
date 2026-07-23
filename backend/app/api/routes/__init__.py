from fastapi import APIRouter

from app.api.routes.v1 import jobs
from app.api.routes.v1 import resumes
from app.api.routes.v1.ats import router as ats_router

router = APIRouter()

router.include_router(jobs.router)
router.include_router(resumes.router)
router.include_router(ats_router)