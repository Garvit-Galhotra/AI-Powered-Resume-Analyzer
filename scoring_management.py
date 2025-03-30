import os
import re
from transformers import pipeline
from ats_scoring.extract_text import extract_text
from ats_scoring.ats_scoring import analyze_ats_compliance


# STEP 1: LOAD A TINY LOCAL MODEL (Mistral-7B-Instruct-v0.1)
# This model is small enough to run locally without GPU.


# Use a very small text-generation model
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M", device="cpu")

# AI-POWERED FEEDBACK USING LOCAL MODEL

def clean_ai_text(text):
    """
    Cleans and structures AI-generated text into a readable list format.
    """
    # Remove extra spaces, line breaks, and unnecessary symbols
    text = re.sub(r"\s+", " ", text).strip()

    # Attempt to extract bullet points from AI response
    suggestions = re.split(r"\d+\.\s|\n- ", text)  # Split at numbers like "1." or bullet points "- "

    # Remove empty entries and format as a list
    suggestions = [s.strip() for s in suggestions if s.strip()]

    return suggestions[:5] 

def ai_feedback(resume_text, job_desc):
    """
    Uses a locally running LLM (DistilGPT-2) to generate resume feedback.
    """
    prompt =  f"""
    You are an AI resume expert. Analyze this resume and suggest 3-5 specific improvements.
    
    1. Identify missing skills based on the job description.
    2. Suggest wording enhancements for clarity and impact.
    3. Highlight any formatting issues that could affect ATS ranking.

    Resume: {resume_text}

    Job Description: {job_desc}

    Provide the feedback as a structured numbered list:
    
    1. <Your first suggestion>
    2. <Your second suggestion>
    3. <Your third suggestion>
    4. <Your fourth suggestion>
    5. <Your fifth suggestion>
    
    Do **not** repeat the content of the resume or job description. Do **not** include unnecessary text.
    """

    response = generator(prompt, max_length=1000, do_sample=True, truncation=True)
    
    if "generated_text" in response[0]:
        return clean_ai_text(response[0]["generated_text"][:500])  # Hard truncate response
    else:
        return ["No feedback available."]

# PROCESS RESUME FILE


def score_resume(resume_path, job_desc, required_skills):
    """
    Extracts text and runs ATS + AI scoring.
    """
    # Extract text from resume file
    resume_text = extract_text(resume_path)

    # Run ATS compliance check
    ats_score = analyze_ats_compliance(resume_text, required_skills)

    # Generate AI feedback using DistilGPT-2
    feedback = ai_feedback(resume_text, job_desc)

    return {
        "resume_path": resume_path,
        "ats_compliance": ats_score,
        "final_resume_score": ats_score,  # Using ATS for now, AI feedback is separate
        "ai_feedback": feedback
    }


# testing the function
if __name__ == "__main__":
    resume_file = "Resume Amit Mahindra.docx"
    job_description = "Looking for a Python Developer with expertise in ML and AI."
    required_skills = "Python, Machine Learning, AI, NLP, Data Science"

    results = score_resume(resume_file, job_description, required_skills)

    print("\n🔹 Resume Scoring Results:")
    print(f"📄 Resume: {results['resume_path']}")
    print(f"✅ ATS Compliance Score: {results['ats_compliance']} / 100")
    print(f"🏆 Final Resume Score: {results['final_resume_score']} / 100")
    print(f"💡 AI Feedback:\n{results['ai_feedback']}")
