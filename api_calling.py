from google import genai
from dotenv import load_dotenv
import os

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

