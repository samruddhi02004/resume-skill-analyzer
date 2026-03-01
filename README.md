🚀 Resume Skill Analyzer API

AI-powered FastAPI backend that extracts skills from resumes (PDF/DOCX) and compares them against job descriptions to identify skill gaps.

🎯 Features

Resume Upload (PDF/DOCX)

Text Extraction

NLP-based Skill Extraction (spaCy)

Skill Gap Analysis

Match Percentage Scoring

Structured API Responses

Robust Validation & Error Handling

Auto-generated Swagger Documentation

🛠 Tech Stack

Python 3.11

FastAPI

spaCy NLP

pdfplumber

python-docx

Pydantic

Uvicorn

📂 Project Structure
resume-skill-analyzer/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── models/
│
├── uploads/
├── main.py
├── requirements.txt
└── README.md
🚀 How to Run Locally

Clone repo:

git clone https://github.com/YOUR_USERNAME/resume-skill-analyzer.git
cd resume-skill-analyzer

Create virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Download spaCy model:

python -m spacy download en_core_web_sm

Run server:

uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs
📊 Example Output
{
  "resume_skills": ["python", "fastapi", "sql"],
  "job_required_skills": ["python", "docker", "sql"],
  "matched_skills": ["python", "sql"],
  "missing_skills": ["docker"],
  "match_percentage": 66.67
}
👩‍💻 Author

Built as part of backend + AI project portfolio.