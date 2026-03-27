import os

from dotenv import load_dotenv

import requests

from config import HF_API_URL

load_dotenv()

def generate_image(prompt: str) -> bytes:
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        raise ValueError("Missing HUGGINGFACE_API_KEY.")

    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.post(
            HF_API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=120,
        )
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"Hugging Face API error: {exc}") from exc

    if response.status_code != 200:
        try:
            details = response.json()
        except ValueError:
            details = response.text
        raise RuntimeError(f"Hugging Face API error: {details}")

    return response.content
