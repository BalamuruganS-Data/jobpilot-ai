from pydantic import BaseModel


class ATSScoreRequest(BaseModel):
    resume_text: str
    job_description: str


class ATSScoreResponse(BaseModel):
    ats_score: int
    matched_skills: list[str]
    missing_skills: list[str]
    suggestions: list[str]