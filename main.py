from fastapi import FastAPI
from app.routes import resume_routes

app = FastAPI(title="Resume Skill Analyzer API")

app.include_router(resume_routes.router)

@app.get("/")
def home():
    return {"message": "🚀 Resume Skill Analyzer API Running Successfully"}