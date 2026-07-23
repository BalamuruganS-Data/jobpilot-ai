from sqlalchemy.orm import Session

from app.models.resume import Resume


class ResumeRepository:

    @staticmethod
    def create(db: Session, resume: Resume):

        db.add(resume)

        db.commit()

        db.refresh(resume)

        return resume