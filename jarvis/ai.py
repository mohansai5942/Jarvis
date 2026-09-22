from openai import OpenAI

from .config import settings
from .memory import ConversationMemory

SYSTEM_PROMPT = """You are Jarvis, a capable personal AI assistant.
Be concise, accurate, practical, and professional.
You can discuss programming, study, productivity, technology, general knowledge,
and the user's configured tasks. Never claim to have performed an action unless
the action handler actually performed it.
"""

class AIClient:
    def __init__(self) -> None:
        self.memory = ConversationMemory()
        self.client = None
        if settings.ai_api_key:
            self.client = OpenAI(
                api_key=settings.ai_api_key,
                base_url=settings.ai_base_url,
            )

    def chat(self, user_text: str) -> str:
        self.memory.add("user", user_text)

        if not self.client:
            reply = (
                "AI backend is not configured yet. Add AI_API_KEY to .env. "
                "I can still handle built-in commands such as opening websites, "
                "searching the web, telling the time, and opening applications."
            )
            self.memory.add("assistant", reply)
            return reply

        try:
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            messages.extend(self.memory.recent())
            response = self.client.chat.completions.create(
                model=settings.ai_model,
                messages=messages,
                temperature=0.4,
            )
            reply = response.choices[0].message.content or "I did not get a usable response."
            self.memory.add("assistant", reply)
            return reply
        except Exception as exc:
            return f"I couldn't reach the AI service: {exc}"
