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


def generate_interview_questions(notes_text):

    prompt = f"""
    You are an interview preparation assistant.

    Based on the notes provided below:

    Generate 15 important interview questions.

    Rules:
    - Question should be technical.
    - Include detailed answer.
    - Format properly.
    - Use only information from notes.
    - Make answers easy to understand.

    Notes:

    {notes_text}
    """

    response = model.generate_content(
        prompt
    )

    return response.text