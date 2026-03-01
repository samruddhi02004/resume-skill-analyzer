import spacy
from spacy.matcher import PhraseMatcher

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Improved skill list
SKILL_SET = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "data analysis",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch",
    "flask",
    "fastapi",
    "django",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "git",
    "docker",
    "kubernetes",
    "aws",
    "mongodb",
    "postgresql",
    "linux",
    "excel"
]

# Create PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

patterns = [nlp.make_doc(skill) for skill in SKILL_SET]
matcher.add("SKILLS", patterns)


def extract_skills(text: str):
    doc = nlp(text)

    matches = matcher(doc)

    found_skills = set()

    for match_id, start, end in matches:
        span = doc[start:end]
        found_skills.add(span.text.lower())

    return sorted(list(found_skills))