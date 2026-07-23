from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.database.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    version = Column(String, default="1.0")

    file_path = Column(String, nullable=False)

    skills = Column(String)

    experience = Column(String)

    is_default = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)