# Jarvis AI Assistant

A practical Python desktop AI assistant inspired by the classic Jarvis concept.

## Features
- Voice input with a typed-input fallback
- Text-to-speech responses
- AI chat through an OpenAI-compatible API endpoint
- Web search via the system browser
- Open common desktop applications
- Open websites and run safe system actions
- Conversation memory for the current session
- Configurable wake-word mode
- Safe command allowlist; no arbitrary shell execution by default

## Quick start

### 1. Install Python
Use Python 3.11+.

### 2. Create and activate a virtual environment
Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```powershell
pip install -r requirements.txt
```

### 4. Configure environment
Copy `.env.example` to `.env` and add an AI API key if you want cloud AI replies.

```powershell
copy .env.example .env
```

### 5. Run
```powershell
python main.py
```

## Example commands
- "Open YouTube"
- "Open Google"
- "Search the web for latest Python news"
- "Open calculator"
- "What time is it?"
- "Who are you?"
- "Help"

## Architecture
```
User speech/text
      |
      v
 Input layer -> Intent router -> Action / AI
      |             |             |
      |             |             +--> AI provider
      |             +----------------> Browser / OS actions
      +------------------------------> Conversation
                         |
                         v
                    TTS response
```

## Important
This project intentionally avoids unrestricted shell/PowerShell execution. Add capabilities through explicit handlers in `jarvis/actions.py`.
