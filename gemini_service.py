import os

from dotenv import load_dotenv

from google import genai

from config import GEMINI_MODEL

load_dotenv()

def generate_text(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY.")

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=f"Write a short, vivid hospitality concept description for: {prompt}",
        )
    except Exception as exc:
        raise RuntimeError(f"Gemini API error: {exc}") from exc

    text = getattr(response, "text", "")
    if not text or not text.strip():
        raise RuntimeError("Gemini returned an empty response.")

    return text.strip()
