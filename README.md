# JARVIS — Browser AI Assistant

Jarvis is a browser-based personal AI assistant with a futuristic chat UI, microphone input, browser text-to-speech, and a secure server-side AI backend.

## Run locally

Requirements: Node.js 22+

```bash
npm install
```

Create `.env` from `.env.example` and set your server-side AI key:

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-5
PORT=3000
```

Then:

```bash
npm start
```

Open http://localhost:3000.

## Online preview

### CodeSandbox / Devbox
Import this GitHub repository into a Node.js environment, run `npm install` and `npm start`, then expose port 3000 in the preview.

### Render
This repository includes `render.yaml`. Create a Render Web Service from this repository, keep the build command `npm install`, start command `npm start`, and add `OPENAI_API_KEY` as a secret environment variable. Render will provide an HTTPS URL.

## Features

- Futuristic responsive Jarvis interface
- Chat UI
- Microphone speech-to-text
- Browser text-to-speech
- AI backend via OpenAI Responses API
- Session conversation history
- Backend health indicator
- Quick prompts
- Server-side API key protection

Never put an API key in frontend JavaScript or commit it to GitHub.
