from .actions import ActionRouter
from .ai import AIClient
from .config import settings
from .speech import SpeechIO

class JarvisAssistant:
    def __init__(self) -> None:
        self.io = SpeechIO()
        self.actions = ActionRouter()
        self.ai = AIClient()
        self.running = True

    def run(self) -> None:
        self.io.speak(
            f"{settings.name} online. Say a command, or type one if microphone input is unavailable."
        )
        while self.running:
            try:
                user_text = self.io.listen()
                if not user_text:
                    continue

                if user_text.lower() in {"exit", "quit", "shutdown", "goodbye"}:
                    self.io.speak("Shutting down. Goodbye.")
                    self.running = False
                    continue

                reply = self.actions.handle(user_text)
                if reply is None:
                    reply = self.ai.chat(user_text)

                self.io.speak(reply)
            except KeyboardInterrupt:
                print("\nJarvis stopped.")
                break
            except Exception as exc:
                self.io.speak(f"An unexpected error occurred: {exc}")
