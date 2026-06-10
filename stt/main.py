import Levenshtein
from groq import Groq
from dotenv import load_dotenv
import os
import re
import sys
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def normalize_arabic(text):
    if not text:
        return ""
    
    tashkeel = re.compile(r'[\u064B-\u0652]')
    text = re.sub(tashkeel, "", text)
    text = re.sub(r'[أإآ]', 'ا', text)
    text = re.sub(r'ى', 'ي', text)
    text = re.sub(r'ة', 'ه', text)
    text = re.sub(r'ذ', 'ز', text) 
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace(" ", "")
    
    return text

def evaluate_speech(audio_file_path, true_text):
    try:
        with open(audio_file_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(audio_file_path, file.read()),
                model="whisper-large-v3",
                language="ar",
                response_format="text"
            )
        
        predicted_text = transcription.strip()

        clean_predicted = normalize_arabic(predicted_text)
        clean_true = normalize_arabic(true_text)

        similarity = Levenshtein.ratio(clean_predicted, clean_true) * 100
        
        status = "PASS" if similarity >= 70 else "FAIL"

        return {
            "true_text": true_text,
            "predicted_text": predicted_text,
            "similarity": round(similarity, 2),
            "status": status
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    if len(sys.argv) > 2:
        audio_path = sys.argv[1]
        target_text = sys.argv[2]
        result = evaluate_speech(audio_path, target_text)
        sys.stdout.write(json.dumps(result, ensure_ascii=False) + '\n')
        sys.stdout.flush()


