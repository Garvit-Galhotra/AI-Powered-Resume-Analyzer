import os
import json
import random
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from scoring_management import score_resume
from Interview_analyzer import (
    load_interview_questions,
    analyze_response,
    calculate_final_score
)
from textblob import TextBlob

# Set up base directories for templates and static files
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "Frontend"))
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "templates"),
)

# Configure the upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed file types
ALLOWED_EXTENSIONS = {"pdf", "docx"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# ==========================
# 1️⃣ Serve Interview Questions API
# ==========================
@app.route("/api/get_questions", methods=["GET"])
def get_interview_questions():
    job_role = request.args.get("job_role", "default")
    num_questions = int(request.args.get("num_questions", 5))

    questions = load_interview_questions(job_role, num_questions)
    return jsonify({"questions": questions})

# ==========================
# 2️⃣ Process Interview Response API (Using Interview Analyzer)
# ==========================
interview_scores = []  # Stores scores for the session

@app.route("/api/process_response", methods=["POST"])
def process_response():
    global interview_scores
    data = request.get_json()

    if "response_text" not in data:
        return jsonify({"error": "No response text provided"}), 400

    response_text = data["response_text"]
    scores = analyze_response(response_text)  # 🔥 Using `Interview_analyzer`
    interview_scores.append(scores)

    return jsonify({"scores": scores})

# ==========================
# 3️⃣ Get Final Interview Score API
# ==========================
@app.route("/api/final_score", methods=["GET"])
def get_final_score():
    global interview_scores

    if not interview_scores:
        return jsonify({"error": "No responses recorded"}), 400

    final_score = calculate_final_score(interview_scores)
    interview_scores = []  # Reset after scoring

    return jsonify({"final_score": final_score})

# ==========================
# 4️⃣ Evaluate Answer API (Using NLP & Dummy Scores)
# ==========================
@app.route("/api/evaluate_answer", methods=["POST"])
def evaluate_answer():
    data = request.get_json()
    user_answer = data.get("answer", "")

    # ✅ Use Interview Analyzer to process the answer
    response_analysis = analyze_response(user_answer)

    return jsonify(response_analysis)

# ==========================
# 5️⃣ Define Routes for Pages
# ==========================
@app.route("/")
def home():
    return render_template("Home_page.html")

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/interview")
def interview():
    return render_template("interview.html")

# ==========================
# 6️⃣ Resume Scoring API
# ==========================
@app.route("/score_resume", methods=["POST"])
def score_resume_api():
    if "resume" not in request.files:
        return jsonify({"success": False, "error": "No file uploaded"}), 400

    file = request.files["resume"]
    job_desc = request.form.get("job_desc", "")
    required_skills = request.form.get("required_skills", "")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # Process resume scoring
        results = score_resume(file_path, job_desc, required_skills)

        return jsonify({
            "success": True,
            "final_resume_score": results["ats_compliance"],
            "ai_feedback": results["ai_feedback"]
        })
    
    return jsonify({"success": False, "error": "Invalid file format"}), 400

# ==========================
# 7️⃣ Run Flask App
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
