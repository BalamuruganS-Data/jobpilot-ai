from pathlib import Path
import shutil

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.repositories.resume_repository import ResumeRepository


UPLOAD_DIR = Path("uploads/resumes")


class ResumeService:

    @staticmethod
    def upload_resume(file: UploadFile, db: Session):

        # Create upload folder if it doesn't exist
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

        file_path = UPLOAD_DIR / file.filename

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        resume = Resume(
            filename=file.filename,
            filepath=str(file_path)
        )

        return ResumeRepository.create(db, resume)