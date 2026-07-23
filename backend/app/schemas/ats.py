from pydantic import BaseModel


class ATSScoreRequest(BaseModel):
    resume_id: int
    job_id: int


class ATSScoreResponse(BaseModel):
    ats_score: int