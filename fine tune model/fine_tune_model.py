import os
import sys
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader

# ===========================
# STEP 1: LOAD EXCEL DATA
# ===========================

# Move to the script's base directory
base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(base_dir)

# Load dataset from Excel
dataset_path = os.path.join(base_dir, "resume_similarity_dataset.xlsx")
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"❌ Dataset not found! Check the path: {dataset_path}")

df = pd.read_excel(dataset_path)

# Ensure required columns exist
required_columns = ["resume_text", "job_description", "ideal_resume_text", "similarity_score"]
if not all(col in df.columns for col in required_columns):
    raise ValueError("❌ Dataset is missing required columns!")

# Prepare training data (resume vs ideal resume + job description)
train_examples = [
    InputExample(
        texts=[row["resume_text"], row["ideal_resume_text"], row["job_description"]],
        label=float(row["similarity_score"])  # Normalize score (0-1)
    )
    for _, row in df.iterrows()
]

print(f"✅ Loaded {len(train_examples)} training examples from Excel.")

# ===========================
# STEP 2: LOAD MODEL & SET UP TRAINING
# ===========================

# Load a small pre-trained model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(model_name)

# Convert training examples into a DataLoader
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=8)

# Define loss function
loss_function = losses.CosineSimilarityLoss(model)

print("✅ Model and training setup ready.")

# ===========================
# STEP 3: FINE-TUNE & SAVE MODEL
# ===========================

# Fine-tune the model
print("🚀 Starting fine-tuning...")
model.fit(train_objectives=[(train_dataloader, loss_function)], epochs=3, warmup_steps=100)

# Save the model in "../resume_fine_tuned_model/"
parent_dir = os.path.dirname(base_dir)  # Move one folder up
model_save_path = os.path.join(parent_dir, "resume_fine_tuned_model")

# Create the directory if it doesn't exist
os.makedirs(model_save_path, exist_ok=True)

# Save the fine-tuned model
model.save(model_save_path)

print(f"✅ Fine-tuning complete! Model saved at: {model_save_path}")
