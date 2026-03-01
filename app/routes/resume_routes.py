from fastapi import APIRouter, UploadFile, File, HTTPException, Form
import os
import shutil

from app.models.resume_response import ResumeAnalysisResponse
from app.utils.text_extractor import extract_text
from app.services.skill_extractor import extract_skills

router = APIRouter()

UPLOAD_FOLDER = "uploads"


@router.post("/analyze-resume", response_model=ResumeAnalysisResponse)
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        if not file.filename.endswith((".pdf", ".docx")):
            raise HTTPException(status_code=400, detail="Only PDF and DOCX files are allowed.")

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        resume_text = extract_text(file_path)
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        matched_skills = list(set(resume_skills) & set(jd_skills))
        missing_skills = list(set(jd_skills) - set(resume_skills))

        match_percentage = (
            round((len(matched_skills) / len(jd_skills)) * 100, 2)
            if jd_skills else 0
        )

        return ResumeAnalysisResponse(
            message="Resume analysis completed",
            resume_skills=resume_skills,
            job_required_skills=jd_skills,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            match_percentage=match_percentage,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
