import pdfplumber
import docx
import os
import sys
base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
import re

def preprocess_resume_text(text):
    """
    Cleans and normalizes extracted resume text to match dataset format.
    """
    # Remove extra spaces, line breaks, and bullet points
    text = re.sub(r"\n+", " ", text)  # Replace multiple newlines with a space
    text = re.sub(r"•|\*|▪", "", text)  # Remove bullet points
    text = re.sub(r"\s{2,}", " ", text)  # Replace multiple spaces with a single space

    # Preserve key sections by adding labels (to keep meaning)
    sections = ["Experience", "Education", "Projects", "Skills", "Certifications"]
    for section in sections:
        text = text.replace(section + ":", f"\n{section.upper()}:")  # Highlight sections

    return text.strip()


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return preprocess_resume_text(text.strip())

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file."""
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return preprocess_resume_text(text.strip())

def extract_text(file_path):
    """Detect file type and extract text accordingly."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please use PDF or DOCX.")

# Example Usage:
if __name__ == "__main__":
    file_path = os.path.join(base_dir, "Resume Amit Mahindra.docx")
    text = extract_text(file_path)
    print(text)  # This will print the extracted text
