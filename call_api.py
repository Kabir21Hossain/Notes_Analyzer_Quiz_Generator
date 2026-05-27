from google import genai
from dotenv import load_dotenv
import os,io
from gtts import gTTS

load_dotenv()

key=os.environ.get('GEMINI_API_KEY')
client =genai.Client(api_key=key)


def note_generator(images):
    prompt = """Summarize the picture as note format at max 100 words,
        ensure to add markdown to differentiate relevancy"""

    response = client.models.generate_content(
        model='gemini-2.0-flash',   # ✅ changed
        contents=[images, prompt]
    )
    return response.text


def quiz_generator(images, level):
    prompt = f"""Generate 3 quizzes based on the {level}.
            Make sure to add necessary markdown"""

    response = client.models.generate_content(
        model='gemini-2.0-flash',   # ✅ changed
        contents=[images, prompt]
    )
    return response.text


def audio_transcript(text):
    speech=gTTS(text,lang='en',slow=False)
    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


