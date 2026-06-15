import google.generativeai as genai
import os
import json

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_quiz(notes_text):

    prompt = f"""
    Based on the notes below generate exactly 10 MCQ questions.

    Return ONLY valid JSON.

    Format:

    [
        {{
            "question":"Question text",
            "options":[
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer":"Correct Option"
        }}
    ]

    Notes:
    {notes_text}
    """

    response = model.generate_content(
        prompt
    )

    text = response.text.strip()

    text = text.replace(
        "```json",
        ""
    )

    text = text.replace(
        "```",
        ""
    )

    return json.loads(text)