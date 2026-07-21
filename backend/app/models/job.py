from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from app.database.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    location = Column(String(255))
    salary = Column(String(100))

    source = Column(String(100))

    job_url = Column(String(1000), unique=True)

    ats_score = Column(Float, default=0)

    status = Column(String(50), default="Found")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )