import os
import io
import json
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Gemini API key is missing")

genai.configure(api_key=API_KEY)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Resume ATS Analyzer API is running"}

@app.post("/result")
async def analyze_resume(file: UploadFile):
    file_bytes = await file.read()
    model = genai.GenerativeModel("gemini-flash-latest")

    resume_text = ""

    # -------- Extract resume text --------
    if file.content_type.startswith("image/"):
        img = Image.open(io.BytesIO(file_bytes))
        response = model.generate_content(
            ["Extract all readable text from this resume image.", img]
        )
        resume_text = response.text

    elif file.content_type == "text/plain":
        resume_text = file_bytes.decode(errors="ignore")

    elif file.content_type == "application/pdf":
        response = model.generate_content([
            "Extract all text from this resume PDF.",
            {"mime_type": "application/pdf", "data": file_bytes}
        ])
        resume_text = response.text

    else:
        return {"error": "Unsupported file type"}

    # -------- ATS Prompt (JSON ONLY) --------
    prompt = f"""
You are an ATS (Applicant Tracking System).

Analyze the resume text below and RETURN ONLY VALID JSON.
DO NOT add explanations, markdown, or extra text.

Resume:
{resume_text}

Required JSON format:
{{
  "score": number,
  "strengths": [string],
  "weaknesses": [string],
  "job_roles": [string],
  "improvements": [string]
}}
"""

    ats_response = model.generate_content(prompt)

    # -------- Safe JSON parsing --------
    try:
        result_json = json.loads(ats_response.text)
    except Exception:
        return {
            "error": "Failed to parse AI response",
            "raw_response": ats_response.text
        }

    return result_json
