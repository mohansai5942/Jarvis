const express = require("express");
const path = require("path");
const dotenv = require("dotenv");
const { GoogleGenAI } = require("@google/genai");

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;
const publicDir = path.join(__dirname, "public");

app.use(express.json({ limit: "1mb" }));
app.use(express.static(publicDir));

const ai = process.env.GEMINI_API_KEY
  ? new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY })
  : null;

const SYSTEM_INSTRUCTION = `You are Jarvis, a polished personal AI assistant.
Be concise but useful. Address the user naturally.
You can help with programming, AI/ML, study, productivity, business, web development,
technology and general knowledge.
Never claim you performed an external action unless the server actually performed it.
If an action is unavailable, clearly say so and suggest a safe alternative.
`;

app.get("/api/health", (_req, res) => {
  res.json({
    ok: true,
    aiConfigured: Boolean(ai),
    name: "Jarvis",
    provider: "Gemini"
  });
});

app.post("/api/chat", async (req, res) => {
  try {
    const { message, history = [] } = req.body || {};

    if (!message || typeof message !== "string") {
      return res.status(400).json({ error: "Message is required." });
    }

    if (!ai) {
      return res.status(503).json({
        error: "Gemini AI is not configured. Add GEMINI_API_KEY to the Railway service variables."
      });
    }

    const safeHistory = Array.isArray(history)
      ? history
          .filter((item) => item && ["user", "assistant"].includes(item.role))
          .slice(-12)
          .map((item) => ({
            role: item.role === "assistant" ? "model" : "user",
            parts: [{ text: String(item.content).slice(0, 8000) }]
          }))
      : [];

    const response = await ai.models.generateContent({
      model: process.env.GEMINI_MODEL || "gemini-3.5-flash",
      contents: [
        ...safeHistory,
        { role: "user", parts: [{ text: message }] }
      ],
      config: {
        systemInstruction: SYSTEM_INSTRUCTION,
        temperature: 0.4,
        maxOutputTokens: 1200
      }
    });

    res.json({ reply: response.text || "I could not generate a response." });
  } catch (error) {
    console.error("Gemini error:", error);
    const status = error?.status || error?.code || 500;
    const providerMessage = error?.error?.message || error?.message || "Unknown Gemini error";
    res.status(500).json({
      error: `Gemini request failed (${status}): ${providerMessage}`
    });
  }
});

app.get("*splat", (_req, res) => {
  res.sendFile(path.join(publicDir, "index.html"));
});

app.listen(PORT, () => {
  console.log(`Jarvis is running at http://localhost:${PORT}`);
});
