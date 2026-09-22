from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    name: str = os.getenv("JARVIS_NAME", "Jarvis")
    wake_word: str = os.getenv("WAKE_WORD", "jarvis").lower()
    voice_enabled: bool = os.getenv("VOICE_ENABLED", "true").lower() == "true"
    listen_timeout: int = int(os.getenv("LISTEN_TIMEOUT", "5"))
    phrase_time_limit: int = int(os.getenv("PHRASE_TIME_LIMIT", "12"))
    stt_language: str = os.getenv("STT_LANGUAGE", "en-IN")
    ai_api_key: str = os.getenv("AI_API_KEY", "")
    ai_base_url: str = os.getenv("AI_BASE_URL", "https://api.openai.com/v1")
    ai_model: str = os.getenv("AI_MODEL", "gpt-4o-mini")

settings = Settings()
