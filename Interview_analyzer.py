import json
import numpy as np
import sounddevice as sd
import pyttsx3  # Import pyttsx3 for text-to-speech
from vosk import Model, KaldiRecognizer
import queue


# STEP 1: LOAD MODELS & SETUP AUDIO STREAM


# Load Vosk speech recognition model (Make sure the model is in your project folder)
vosk_model_path = "vosk-model-small-en-us-0.15"
vosk_model = Model(vosk_model_path)

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)  # Adjust speech rate (speed)

# Audio recording queue
audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    """
    Callback function for real-time audio streaming.
    """
    if status:
        print(f"⚠️ Audio error: {status}")
    audio_queue.put(bytes(indata))  # Store raw audio data


# STEP 2: LOAD INTERVIEW QUESTIONS


def load_interview_questions(job_role, num_questions):
    """
    Loads predefined interview questions from a JSON file.
    """
    with open("interview_questions.json", "r") as file:
        questions_data = json.load(file)

    if job_role in questions_data:
        return questions_data[job_role][:num_questions]
    else:
        return ["No questions available for this job role."]


# STEP 3: TEXT-TO-SPEECH FUNCTION


def speak_text(text):
    """
    Converts text into speech using pyttsx3 with a female voice.
    """
    tts_engine = pyttsx3.init()
    voices = tts_engine.getProperty("voices")
    tts_engine.setProperty("voice", voices[1].id)  # Change index based on your system
    tts_engine.setProperty("rate", 150)  # Adjust speed
    print(f"🔊 Speaking: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

# STEP 4: REAL-TIME SPEECH RECOGNITION


def transcribe_audio():
    """
    Captures microphone input and transcribes speech in real-time using Vosk.
    """
    recognizer = KaldiRecognizer(vosk_model, 16000)
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16", channels=1, callback=audio_callback):
        print("🎤 Recording... Speak now!")

        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                return result["text"]


# STEP 5: RESPONSE ANALYSIS (SCORING SYSTEM)


def analyze_response(response_text):
    """
    Analyzes the response and returns a score for confidence, clarity, relevance, and tone.
    """
    if not response_text.strip():
        return {"confidence": 0, "clarity": 0, "relevance": 0, "tone": 0}  # Ensure 'tone' key exists

    # Dummy logic for scoring (Replace with real NLP analysis)
    confidence_score = min(100, max(50, len(response_text) * 2))  # Fake confidence scoring
    clarity_score = min(100, max(50, len(response_text.split()) * 5))  # Fake clarity scoring
    relevance_score = min(100, max(50, len(set(response_text.lower().split())) * 3))  # Fake relevance scoring

    # 🔹 **New: Ensure tone score is included**
    tone_score = min(100, max(50, len(response_text) % 100))  # Fake tone scoring

    return {
        "confidence": confidence_score,
        "clarity": clarity_score,
        "relevance": relevance_score,
        "tone": tone_score  # 🔹 Ensure this key is always present
    }




# STEP 6: FINAL INTERVIEW SCORING

import numpy as np

def calculate_final_score(scores_list):
    """
    Computes the final interview score based on all responses.
    """
    if not scores_list:
        return 0, 0, 0, 0, 0  # If no answers were recorded, return zeros

    avg_confidence = np.mean([s["confidence"] for s in scores_list])
    avg_clarity = np.mean([s["clarity"] for s in scores_list])
    avg_relevance = np.mean([s["relevance"] for s in scores_list])
    avg_tone = np.mean([s["tone"] for s in scores_list])  # New: Average Tone Score

    # Final Interview Score (Weighted Average)
    final_score = (avg_confidence * 0.3) + (avg_clarity * 0.25) + (avg_relevance * 0.25) + (avg_tone * 0.2)

    return round(final_score, 2), round(avg_confidence, 2), round(avg_clarity, 2), round(avg_relevance, 2), round(avg_tone, 2)



# STEP 7: RUN REAL-TIME INTERVIEW

def suggest_job(final_score):
    """
    Suggests a job based on the final interview score.
    """
    if final_score >= 90:
        return "🔥 You are highly skilled! Consider roles like **AI Engineer, ML Engineer, or Data Engineer**."
    elif 75 <= final_score < 90:
        return "✅ Great job! You are suitable for **Software Developer, Python Developer, or Cloud Support Engineer**."
    elif 60 <= final_score < 75:
        return "📈 You have potential! Consider **Web Developer, System Administrator, or Database Engineer**."
    else:
        return "📚 Keep improving! Consider upskilling with courses on **communication, problem-solving, and technical skills.**"


def run_interview(job_role, num_questions):
    """
    Conducts an AI-powered interview session in real-time.
    """
    questions = load_interview_questions(job_role, num_questions)
    scores_list = []

    print(f"\n🔹 Starting AI Interview for {job_role}")

    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        speak_text(question)  # Speak the question

        # Transcribe user's answer in real-time
        transcribed_text = transcribe_audio()
        print(f"📝 Transcription: {transcribed_text}")

        # Analyze the response
        response_scores = analyze_response(transcribed_text)
        scores_list.append(response_scores)

        print(f"📊 Scores for Question {i}: {response_scores}")
        print(f"🎭 Detected Tone: {'Positive' if response_scores['tone'] >= 90 else 'Neutral' if response_scores['tone'] >= 70 else 'Negative'}")

    # Calculate final average scores
    final_score, avg_confidence, avg_clarity, avg_relevance, avg_tone = calculate_final_score(scores_list)

    # Display full final report
    print("\n🏆 Final Interview Report:")
    print(f"⭐ Final Interview Score: {final_score} / 100")
    print(f"💡 Average Confidence: {avg_confidence} / 100")
    print(f"🔍 Average Clarity: {avg_clarity} / 100")
    print(f"🎯 Average Relevance: {avg_relevance} / 100")
    print(f"🎭 Average Tone Score: {avg_tone} / 100")
    
    # Speak the final score
    speak_text(f"Your final interview score is {final_score} out of 100. Your confidence score was {avg_confidence}, clarity was {avg_clarity}, and relevance was {avg_relevance}.")
    # AI suggested Jobs
    speak_text(suggest_job(final_score))
    print(suggest_job(final_score))
    return final_score



# STEP 8: TEST THE SYSTEM

if __name__ == "__main__":
    job_role = input("🔹 Enter the job role you want to prepare for: ")
    num_questions = int(input("🔹 How many questions do you want to answer? "))

    run_interview(job_role, num_questions)
