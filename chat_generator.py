
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_notes_question(notes_text, user_question):

    prompt = f"""
    You are an AI Study Assistant.

    Answer ONLY using the uploaded notes.

    If the answer is not available in the notes,
    reply exactly:

    This information is not available in the uploaded notes.

    Notes:
    {notes_text}

    Question:
    {user_question}
    """

    response = model.generate_content(
        prompt
    )

    return response.text

