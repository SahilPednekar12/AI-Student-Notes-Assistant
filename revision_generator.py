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


def generate_revision_notes(notes_text):

    prompt = f"""
    You are a study assistant.

    Read the notes below and create structured revision notes.

    Include:
    - Important Concepts
    - Key Definitions
    - Important Points
    - Summary

    Notes:

    {notes_text}
    """

    response = model.generate_content(prompt)

    return response.text