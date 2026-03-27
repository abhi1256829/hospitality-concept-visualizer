import os

from dotenv import load_dotenv

import google.generativeai as genai

from config import GEMINI_MODEL

load_dotenv()

def generate_text(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY.")

    genai.configure(api_key=api_key)

    try:
        response = genai.generate_text(
    model=GEMINI_MODEL,
    prompt=f"Write a short, vivid hospitality concept description for: {prompt}"
)
    except Exception as exc:
        raise RuntimeError(f"Gemini API error: {exc}") from exc

    text = getattr(response, "text", "")
    if not text or not text.strip():
        raise RuntimeError("Gemini returned an empty response.")

    return text.strip()
