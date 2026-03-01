from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):
    message: str
    resume_skills: list[str]
    job_required_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]
    match_percentage: float
