import speech_recognition as sr
import pyttsx3

from .config import settings

class SpeechIO:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.engine = None
        if settings.voice_enabled:
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty("rate", 175)
                self.engine.setProperty("volume", 1.0)
            except Exception:
                self.engine = None

    def speak(self, text: str) -> None:
        print(f"Jarvis: {text}")
        if not self.engine:
            return
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception:
            pass

    def listen(self) -> str:
        if not settings.voice_enabled:
            return input("You: ").strip()

        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.4)
                audio = self.recognizer.listen(
                    source,
                    timeout=settings.listen_timeout,
                    phrase_time_limit=settings.phrase_time_limit,
                )
            text = self.recognizer.recognize_google(audio, language=settings.stt_language)
            print(f"You: {text}")
            return text.strip()
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError, OSError):
            return input("Type command: ").strip()
