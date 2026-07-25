<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.0+-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/DeepSeek_V4_Flash-Free-brightgreen?style=for-the-badge&logo=deepseek&logoColor=white" alt="DeepSeek">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensource&logoColor=white" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
  <br>
  <img src="https://img.shields.io/badge/Stars-Welcome-brightgreen?style=flat-square&logo=github" alt="Stars">
  <img src="https://img.shields.io/badge/Contributions-Open-blue?style=flat-square&logo=github" alt="Contributions">
  <img src="https://img.shields.io/badge/Builds-Passing-success?style=flat-square&logo=github" alt="Builds">
</div>

<br>

<div align="center">
  <h1>💬 Conversational AI Chatbot</h1>
  <p><strong>A context-aware AI chatbot that chats naturally, provides information, gives recommendations, and sparks creativity — powered by DeepSeek V4 Flash Free.</strong></p>
  <p>100% free · No credit card required · Conversation memory included</p>
  <br>
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-chat-modes">Chat Modes</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-deployment">Deployment</a> •
  <a href="#-tech-stack">Tech Stack</a>
</div>

<br>

## ✨ Features

| Feature | Description |
|---|---|
| **🧠 Three Chat Modes** | General Chat, Information & Recommendations, Creative Chat |
| **💾 Conversation Memory** | Remembers context across the entire conversation (up to 20 messages) |
| **🎯 Context-Aware Prompts** | Each mode has a carefully crafted system prompt for coherent dialogue |
| **👍 Feedback Loop** | Thumbs up/down on every response — helps improve prompt quality |
| **🔄 New Conversation** | One-click reset to start fresh |
| **🌙 Dark UI** | Modern, responsive chat interface with smooth animations |
| **📱 Mobile Friendly** | Works perfectly on phone, tablet, and desktop |
| **💰 Zero Cost** | Uses free DeepSeek V4 Flash model via OpenCode Zen API |

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- A free API key from [OpenCode Zen](https://opencode.ai/zen)


## 💬 Chat Modes

### 1. General Chat
Casual conversation about anything — daily topics, fun facts, jokes, and natural dialogue. The bot asks follow-up questions to keep the conversation flowing.

### 2. Information & Recommendations
Ask for factual information, explanations, or personalized recommendations. The bot provides well-reasoned answers and asks about your preferences.

### 3. Creative Chat
Storytelling, poems, imaginative ideas, and playful conversation. Perfect for creative inspiration and entertainment.

## 📡 API Reference

### POST `/chat`

Send a message and get a response.

**Request Body:**
```json
{
  "mode": "general",
  "message": "Tell me a fun fact!"
}
```

**Available Modes:** `general`, `info`, `creative`

**Response:**
```json
{
  "response": "Did you know that octopuses have three hearts..."
}
```

### GET `/history`

Retrieve the current conversation history.

### POST `/reset`

Clear the conversation and start fresh.

### POST `/feedback`

Submit feedback on a response.

```json
{
  "mode": "general",
  "message": "Tell me a fun fact!",
  "response": "Did you know...",
  "helpful": true
}
```

## ☁️ Deployment

### Deploy to Render (Free)

1. Push this repository to GitHub
2. Go to [Render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add environment variables:
   - `ZEN_API_KEY` = your OpenCode Zen API key
   - `SECRET_KEY` = a random secret string for Flask sessions
6. Deploy!

> ⏰ Render's free tier spins down after 15 minutes of inactivity. The app automatically wakes up when you visit it again.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.12+** | Core programming language |
| **Flask** | Web framework with session management |
| **OpenAI SDK** | OpenAI-compatible client for OpenCode Zen API |
| **DeepSeek V4 Flash Free** | Free, powerful LLM for generating responses |
| **Gunicorn** | Production-ready WSGI server |
| **HTML / CSS / JS** | Chat-style user interface |
| **Font Awesome** | UI icons |
| **Render** | Hosting platform (recommended) |

## 📂 Project Structure

```
ai-assistant/
├── app.py                 # Flask app with chat logic and session memory
├── templates/
│   └── index.html         # Chat interface
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── feedback.json          # User feedback storage
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

## 🙏 Acknowledgements

- [OpenCode Zen](https://opencode.ai/zen) for the free DeepSeek V4 Flash API
- [DeepSeek](https://deepseek.com) for the powerful LLM
- [Render](https://render.com) for free hosting

---

<div align="center">
  <p>Made with ❤️ for the open-source community</p>
</div>
