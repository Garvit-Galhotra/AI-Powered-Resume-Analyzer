import json
import numpy as np
import sounddevice as sd
import pyttsx3  # Import pyttsx3 for text-to-speech
from vosk import Model, KaldiRecognizer
import queue

# ===========================
# STEP 1: LOAD MODELS & SETUP AUDIO STREAM
# ===========================

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

# ===========================
# STEP 2: LOAD INTERVIEW QUESTIONS
# ===========================

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

# ===========================
# STEP 3: TEXT-TO-SPEECH FUNCTION
# ===========================

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

# ===========================
# STEP 4: REAL-TIME SPEECH RECOGNITION
# ===========================

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

# ===========================
# STEP 5: RESPONSE ANALYSIS (SCORING SYSTEM)
# ===========================

def analyze_response(response_text):
    """
    Evaluates the interview response based on confidence, clarity, and relevance.
    """
    word_count = len(response_text.split())
    sentence_count = response_text.count(".") + response_text.count("!") + response_text.count("?")
    avg_sentence_length = word_count / max(sentence_count, 1)

    confidence_score = min(100, avg_sentence_length * 10)  # Longer sentences indicate more confidence
    clarity_score = min(100, (100 - abs(15 - avg_sentence_length) * 5))  # Ideal sentence length: ~15 words
    relevance_score = np.random.randint(50, 100)  # Placeholder (can be improved)

    return {
        "confidence": round(confidence_score, 2),
        "clarity": round(clarity_score, 2),
        "relevance": round(relevance_score, 2)
    }

# ===========================
# STEP 6: FINAL INTERVIEW SCORING
# ===========================

def calculate_final_score(scores_list):
    """
    Computes the final interview score based on all responses.
    """
    avg_confidence = np.mean([s["confidence"] for s in scores_list])
    avg_clarity = np.mean([s["clarity"] for s in scores_list])
    avg_relevance = np.mean([s["relevance"] for s in scores_list])

    final_score = (avg_confidence * 0.4) + (avg_clarity * 0.3) + (avg_relevance * 0.3)
    return round(final_score, 2)

# ===========================
# STEP 7: RUN REAL-TIME INTERVIEW
# ===========================

def run_interview(job_role, num_questions):
    """
    Conducts an AI-powered interview session in real-time.
    """
    questions = load_interview_questions(job_role, num_questions)
    scores_list = []

    print(f"\n🔹 Starting AI Interview for {job_role}")

    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        speak_text(question)  # Convert text question to speech

        # Transcribe user's answer in real-time
        transcribed_text = transcribe_audio()
        print(f"📝 Transcription: {transcribed_text}")

        # Analyze the response
        response_scores = analyze_response(transcribed_text)
        scores_list.append(response_scores)

        print(f"📊 Scores: {response_scores}")

    # Calculate final interview score
    final_score = calculate_final_score(scores_list)
    print(f"\n🏆 Final Interview Score: {final_score} / 100")
    speak_text(f"Your final interview score is {final_score} out of 100.")  # Speak the final score

    return final_score

# ===========================
# STEP 8: TEST THE SYSTEM
# ===========================

if __name__ == "__main__":
    job_role = input("🔹 Enter the job role you want to prepare for: ")
    num_questions = int(input("🔹 How many questions do you want to answer? "))

    run_interview(job_role, num_questions)
