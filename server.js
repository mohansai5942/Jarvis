const express = require("express");
const path = require("path");
const dotenv = require("dotenv");
const OpenAI = require("openai");

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;
const publicDir = path.join(__dirname, "public");

app.use(express.json({ limit: "1mb" }));
app.use(express.static(publicDir));

const client = process.env.OPENAI_API_KEY
  ? new OpenAI({ apiKey: process.env.OPENAI_API_KEY })
  : null;

const instructions = `You are Jarvis, a polished personal AI assistant.
Be concise but useful. Address the user naturally.
You can help with programming, AI/ML, study, productivity, business, web development,
technology and general knowledge.
Never claim you performed an external action unless the server actually performed it.
If an action is unavailable, clearly say so and suggest the safe alternative.
`;

app.get("/api/health", (_req, res) => {
  res.json({
    ok: true,
    aiConfigured: Boolean(client),
    name: "Jarvis",
  });
});

app.post("/api/chat", async (req, res) => {
  try {
    const { message, history = [] } = req.body || {};

    if (!message || typeof message !== "string") {
      return res.status(400).json({ error: "Message is required." });
    }

    if (!client) {
      return res.status(503).json({
        error: "AI backend is not configured. Add OPENAI_API_KEY to the server environment.",
      });
    }

    const safeHistory = Array.isArray(history)
      ? history
          .filter((item) => item && ["user", "assistant"].includes(item.role))
          .slice(-12)
          .map((item) => ({
            role: item.role,
            content: String(item.content).slice(0, 8000),
          }))
      : [];

    const response = await client.responses.create({
      model: process.env.OPENAI_MODEL || "gpt-5",
      instructions,
      input: [...safeHistory, { role: "user", content: message }],
    });

    res.json({ reply: response.output_text || "I could not generate a response." });
  } catch (error) {
    console.error("AI error:", error);
    res.status(500).json({
      error: "Jarvis could not reach the AI service.",
    });
  }
});

app.get("*splat", (_req, res) => {
  res.sendFile(path.join(publicDir, "index.html"));
});

app.listen(PORT, () => {
  console.log(`Jarvis is running at http://localhost:${PORT}`);
});
