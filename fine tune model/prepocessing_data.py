import pandas as pd
from sentence_transformers import InputExample
import os
import sys

# Get the absolute path of the script's directory
base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(base_dir)
# Load dataset (update the path to your actual dataset file)
dataset_path = os.path.join(base_dir, "resume_similarity_dataset.xlsx")  # Change if using CSV
df = pd.read_excel(dataset_path)  # Use pd.read_csv() for CSV files

# Ensure dataset has required columns
required_columns = ["resume_text", "job_description", "ideal_resume_text", "similarity_score", "required_skills"]
if not all(col in df.columns for col in required_columns):
    raise ValueError("Dataset is missing required columns!")

# Convert dataset into training format for sentence-transformers
train_data = []
for index, row in df.iterrows():
    resume_text = row["resume_text"]
    job_desc = row["job_description"]
    ideal_resume = row["ideal_resume_text"]
    score = float(row["similarity_score"])   # already normalize in the dataset ( 0.0 to 1.0)

    # Create input pair: (Resume vs Ideal Resume) + Job Description as context
    train_data.append(InputExample(texts=[resume_text, ideal_resume, job_desc], label=score))

print(f"✅ Loaded and processed {len(train_data)} resume samples for fine-tuning.")
