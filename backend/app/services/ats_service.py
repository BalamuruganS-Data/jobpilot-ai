from app.core.skills import TECH_SKILLS
from app.schemas.ats import ATSScoreRequest


class ATSService:
    def calculate_score(self, request: ATSScoreRequest) -> dict:
        resume_text = request.resume_text.lower()
        jd_text = request.job_description.lower()

        matched_skills = []
        missing_skills = []

        for skill in TECH_SKILLS:
            if skill in jd_text:
                if skill in resume_text:
                    matched_skills.append(skill)
                else:
                    missing_skills.append(skill)

        total_required = len(matched_skills) + len(missing_skills)

        if total_required == 0:
            score = 100
        else:
            score = int((len(matched_skills) / total_required) * 100)

        suggestions = [
            f"Add experience with {skill}"
            for skill in missing_skills
        ]

        return {
            "ats_score": score,
            "matched_skills": sorted(matched_skills),
            "missing_skills": sorted(missing_skills),
            "suggestions": suggestions,
        }