import re
import docx
import pdfplumber
import spacy
from .extract_text import extract_text
import os
import sys
base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Load spaCy NLP model for keyword extraction
nlp = spacy.load("en_core_web_sm")

def check_ats_friendly_format(text):
    """
    Checks if the resume is ATS-friendly by detecting common formatting issues.
    Returns a penalty score (0-10), where 10 is highly ATS-unfriendly.
    """
    penalty = 0

    # Check for tables (ATS struggles with tables in DOCX)
    if "table" in text.lower():
        penalty += 3  # Penalize if tables are mentioned

    # Check for images (ATS can't read images)
    if "image" in text.lower():
        penalty += 3  

    # Check if resume has bullet points (good for ATS readability)
    if not re.search(r"•|-", text):
        penalty += 2  # Penalize if no bullet points found

    return penalty

def check_keyword_relevance(text, required_skills):
    """
    Checks if the resume contains required job skills.
    Returns a keyword match percentage (0-100%).
    """
    extracted_words = {token.lemma_.lower() for token in nlp(text) if token.is_alpha}
    required_words = {skill.lower() for skill in required_skills.split(",")}

    matched_keywords = extracted_words.intersection(required_words)
    match_score = (len(matched_keywords) / len(required_words)) * 100

    return round(match_score, 2)

def check_resume_structure(text):
    """
    Checks if key resume sections (Experience, Education, Skills) are present.
    Returns a structure completeness score (0-10).
    """
    required_sections = ["Experience", "Education", "Skills"]
    found_sections = sum(1 for section in required_sections if section.lower() in text.lower())

    return (found_sections / len(required_sections)) * 10  # Convert to a 10-point scale

def analyze_ats_compliance(text, required_skills):
    """
    Runs all ATS compliance checks and returns a final ATS compliance score (0-100).
    """
    ats_penalty = check_ats_friendly_format(text)  # Formatting penalty (0-10)
    keyword_match = check_keyword_relevance(text, required_skills)  # Keyword match %
    structure_score = check_resume_structure(text)  # Structure completeness (0-10)

    # Normalize each component
    ats_score = max(0, 100 - ats_penalty)  # Ensure no negative score
    keyword_contribution = (keyword_match / 100) * 50  # Normalize keyword relevance (0-50)
    structure_contribution = (structure_score / 10) * 50  # Normalize structure (0-50)

    # Final ATS score (0-100)
    final_ats_score = min(100, ats_score * 0.4 + keyword_contribution * 0.3 + structure_contribution * 0.3)

    return round(final_ats_score, 2)


# Example Usage
if __name__ == "__main__":
    file_path = os.path.join(base_dir, "Resume Amit Mahindra.docx")
    sample_resume_text = extract_text(file_path)  # Replace with your resume path
    
    required_skills = "Python, Java, AWS, Machine Learning, NLP"
    
    ats_score = analyze_ats_compliance(sample_resume_text, required_skills)
    print(f"ATS Compliance Score: {ats_score}/100")
