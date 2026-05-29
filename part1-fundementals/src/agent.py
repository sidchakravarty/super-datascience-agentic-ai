from google.genai import Client
from src.config import Config

# Initialize client
google_client = Client(api_key=Config.GOOGLE_API_KEY)

def get_gemini_response(contents):
    """Helper function to get response from Gemini"""
    response = google_client.models.generate_content(
        model=Config.DEFAULT_GEMINI_MODEL,
        contents=contents,
        config={"max_output_tokens": Config.DEFAULT_MAX_TOKENS}
    )
    return response.text