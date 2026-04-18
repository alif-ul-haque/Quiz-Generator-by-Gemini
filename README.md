# Quiz Generator by Gemini

A Streamlit app that turns uploaded images into three learning outputs: a concise note summary, an audio narration of that summary, and a quiz generated from the image content.

## Live Demo

Deployed app: [https://pro-quiz-generator.streamlit.app/](https://pro-quiz-generator.streamlit.app/)

## Features

- Upload up to 3 images in JPG, JPEG, or PNG format.
- Generate a short note-style summary from the uploaded images.
- Convert the summary into an audio transcript using text-to-speech.
- Create a quiz from the image content.
- Choose quiz difficulty from Easy, Medium, or Hard.
- Built with Streamlit and Google Gemini.

## How It Works

1. Upload one to three images from the sidebar.
2. Select a quiz difficulty.
3. Click Generate Summary and Quiz.
4. The app sends the images to Gemini to generate:
   - a summary in markdown-friendly note format,
   - an audio version of the summary,
   - a quiz with answers.

## Tech Stack

- Python
- Streamlit
- Google Gemini API via `google-genai`
- Pillow for image handling
- gTTS for audio generation
- python-dotenv for environment variable loading

## Project Structure

- `app.py` - Streamlit user interface and workflow
- `api_calling.py` - Gemini integration, summary generation, quiz generation, and audio creation
- `requirements.txt` - Python dependencies

## Local Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

5. Run the app:

```bash
streamlit run app.py
```

## Notes

- The app currently limits uploads to a maximum of 3 images.
- The generated summary is kept short and formatted for readability.
- Quiz generation depends on the selected difficulty level.

## License

No license has been specified for this project.
