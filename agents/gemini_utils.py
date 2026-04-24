import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Try modern models first, then older aliases for compatibility.
MODEL_CANDIDATES = [
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-1.5-flash-latest",
    "gemini-1.5-flash",
]


def _discover_model_candidates() -> list[str]:
    """Return available Gemini models that support content generation."""
    discovered: list[str] = []
    try:
        for model in genai.list_models():
            methods = getattr(model, "supported_generation_methods", []) or []
            name = getattr(model, "name", "")
            if "generateContent" in methods and name.startswith("models/gemini"):
                discovered.append(name.replace("models/", "", 1))
    except Exception:
        # Ignore discovery errors and rely on static fallbacks.
        return []
    return discovered


def generate_text(prompt: str) -> str:
    """Generate text with automatic Gemini model fallback."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY. Add it to your .env file.")

    genai.configure(api_key=api_key)

    dynamic_candidates = _discover_model_candidates()
    model_candidates = MODEL_CANDIDATES + [
        candidate for candidate in dynamic_candidates if candidate not in MODEL_CANDIDATES
    ]

    last_error = None
    for model_name in model_candidates:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return (response.text or "").strip()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            continue

    raise RuntimeError(f"No compatible Gemini model available. Last error: {last_error}")
