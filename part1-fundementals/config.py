import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    DEFAULT_ANTHROPIC_MODEL = "claude-haiku-4-5"
    DEFAULT_OPENAI_MODEL = "gpt-4.1-nano"
    DEFAULT_GEMINI_MODEL = "gemini-3.1-flash-lite"

    DEFAULT_MAX_TOKENS = 1024