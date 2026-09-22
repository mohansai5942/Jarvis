from __future__ import annotations

import datetime as dt
import os
import platform
import subprocess
import webbrowser
from urllib.parse import quote_plus

class ActionRouter:
    def handle(self, text: str) -> str | None:
        command = text.strip().lower()
        if not command:
            return "Please give me a command."

        if command in {"hello", "hi", "hey"}:
            return "Hello. Systems are ready."

        if "who are you" in command or "what are you" in command:
            return "I am Jarvis, your personal desktop AI assistant."

        if command in {"help", "what can you do"}:
            return (
                "I can open websites and common apps, search the web, tell the time, "
                "and answer questions through the configured AI backend."
            )

        if "time" in command:
            return dt.datetime.now().strftime("The time is %I:%M %p.")

        if "date" in command:
            return dt.datetime.now().strftime("Today is %A, %d %B %Y.")

        if command.startswith("search the web for "):
            query = text[len("search the web for "):].strip()
            return self._search(query)

        if command.startswith("search for "):
            query = text[len("search for "):].strip()
            return self._search(query)

        sites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "github": "https://github.com",
            "gmail": "https://mail.google.com",
            "chatgpt": "https://chatgpt.com",
            "brandique": "https://brandique.in",
        }
        for name, url in sites.items():
            if command in {f"open {name}", name}:
                webbrowser.open(url)
                return f"Opening {name}."

        if command.startswith("open "):
            target = command[5:].strip()
            if target.startswith("http://") or target.startswith("https://"):
                webbrowser.open(target)
                return "Opening the requested website."

        apps = {
            "calculator": self._open_calculator,
            "notepad": self._open_notepad,
        }
        if command.startswith("open "):
            target = command[5:].strip()
            if target in apps:
                try:
                    apps[target]()
                    return f"Opening {target}."
                except Exception as exc:
                    return f"I couldn't open {target}: {exc}"

        if "system info" in command or "system information" in command:
            return f"OS: {platform.system()} {platform.release()} | Machine: {platform.machine()}"

        return None

    @staticmethod
    def _search(query: str) -> str:
        if not query:
            return "Tell me what you want me to search for."
        webbrowser.open(f"https://www.google.com/search?q={quote_plus(query)}")
        return f"Searching the web for {query}."

    @staticmethod
    def _open_calculator() -> None:
        system = platform.system()
        if system == "Windows":
            subprocess.Popen(["calc.exe"])
        elif system == "Darwin":
            subprocess.Popen(["open", "-a", "Calculator"])
        else:
            subprocess.Popen(["gnome-calculator"])

    @staticmethod
    def _open_notepad() -> None:
        system = platform.system()
        if system == "Windows":
            subprocess.Popen(["notepad.exe"])
        elif system == "Darwin":
            subprocess.Popen(["open", "-a", "TextEdit"])
        else:
            subprocess.Popen(["gedit"])
