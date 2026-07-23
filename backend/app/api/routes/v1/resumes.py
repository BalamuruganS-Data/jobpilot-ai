from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.resume import ResumeResponse
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)


@router.post("/upload", response_model=ResumeResponse)
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    service = ResumeService()

    return service.upload_resume(file, db)