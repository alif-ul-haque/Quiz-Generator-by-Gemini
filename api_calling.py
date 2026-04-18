from google import genai
from dotenv import load_dotenv
import os,io
from gtts import gTTS

#loading the environment variable
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

#initializing the client
client = genai.Client(api_key=api_key)


#note generator
def note_generator(images):
    prompt = """Summarize the content of the images in note format at max 100 words, make sure to include all the important markdown to differentiate different sections."""
    response = client.models.generate_content( 
        model = "gemini-3-flash-preview",
        contents = [*images, prompt],
    )

    return response.text if getattr(response, "text", None) else "No summary generated."

 #audio transcript generator
def audio_transcription(note):
    note = note.replace("#", "").replace("*", "").replace("_", "").replace("`", "").replace("$", "")
    speech = gTTS(text=note, lang='en',slow=False)
    audio_file = io.BytesIO()
    speech.write_to_fp(audio_file)
    return audio_file

def quiz_generator(images,difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differentiate the options. Add correct answer too,after the quiz"
    response = client.models.generate_content( 
        model = "gemini-3-flash-preview",
        contents = [*images, prompt],
    )

    return response.text if getattr(response, "text", None) else "No quiz generated."

