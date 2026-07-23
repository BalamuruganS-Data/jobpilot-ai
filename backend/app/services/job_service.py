from sqlalchemy.orm import Session

from app.repositories.job_repository import JobRepository
from app.schemas.job import JobCreate


class JobService:
    def __init__(self, db: Session):
        self.repository = JobRepository(db)

    def create_job(self, job: JobCreate):
        """
        Future business logic goes here.

        Examples:
        - Duplicate detection
        - ATS scoring
        - Notification
        - Resume matching
        """

        return self.repository.create(job)

    def get_jobs(self):
        return self.repository.get_all()

    def get_job(self, job_id: int):
        return self.repository.get_by_id(job_id)

    def delete_job(self, job_id: int):
        job = self.repository.get_by_id(job_id)

        if job:
            self.repository.delete(job)

        return job