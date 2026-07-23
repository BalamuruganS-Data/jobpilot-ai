from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class JobBase(BaseModel):
    company: str
    title: str
    location: Optional[str] = None
    salary: Optional[str] = None
    source: Optional[str] = None
    job_url: Optional[str] = None


class JobCreate(JobBase):
    pass


class JobUpdate(BaseModel):
    company: Optional[str] = None
    title: Optional[str] = None
    location: Optional[str] = None
    salary: Optional[str] = None
    source: Optional[str] = None
    ats_score: Optional[float] = None
    status: Optional[str] = None


class JobResponse(JobBase):
    id: int
    ats_score: float
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)