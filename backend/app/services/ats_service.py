from app.schemas.ats import ATSScoreRequest


class ATSService:
    def calculate_score(self, request: ATSScoreRequest) -> int:
        # Temporary dummy score
        return 75