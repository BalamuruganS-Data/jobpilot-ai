from fastapi import APIRouter

from app.schemas.ats import ATSScoreRequest, ATSScoreResponse
from app.services.ats_service import ATSService

router = APIRouter(
    prefix="/ats",
    tags=["ATS"],
)


@router.post("/score", response_model=ATSScoreResponse)
def score_resume(request: ATSScoreRequest):
    service = ATSService()

    result = service.calculate_score(request)

    return ATSScoreResponse(**result)