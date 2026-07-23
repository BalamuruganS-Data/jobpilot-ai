from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job import JobCreate


class JobRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, job: JobCreate) -> Job:
        db_job = Job(
            company=job.company,
            title=job.title,
            location=job.location,
            salary=job.salary,
            source=job.source,
            job_url=job.job_url,
        )

        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)

        return db_job

    def get_all(self):
        return self.db.query(Job).all()

    def get_by_id(self, job_id: int):
        return (
            self.db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

    def delete(self, job: Job):
        self.db.delete(job)
        self.db.commit()