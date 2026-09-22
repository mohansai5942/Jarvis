# Jarvis Browser Edition

Run with Node.js 22+: `npm install && npm start`, then open port 3000.

For CodeSandbox/Devbox, expose port 3000. For Render, deploy this repository as a Node web service and set `OPENAI_API_KEY` as a secret environment variable.

The API key stays on the server. Browser microphone input uses the Web Speech API and requires browser permission; HTTPS is recommended for deployed microphone access.
