<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.0+-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/DeepSeek_V4_Flash-Free-brightgreen?style=for-the-badge&logo=deepseek&logoColor=white" alt="DeepSeek">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensource&logoColor=white" alt="License">
  <img src="https://img.shields.io/badge/Deploy-Ready-6366F1?style=for-the-badge&logo=render&logoColor=white" alt="Render">
  <br>
  <img src="https://img.shields.io/github/stars/aman179102/ai-assistant?style=flat-square&logo=github" alt="Stars">
  <img src="https://img.shields.io/github/forks/aman179102/ai-assistant?style=flat-square&logo=github" alt="Forks">
  <img src="https://img.shields.io/github/issues/aman179102/ai-assistant?style=flat-square&logo=github" alt="Issues">
  <img src="https://img.shields.io/github/last-commit/aman179102/ai-assistant?style=flat-square&logo=git" alt="Last Commit">
</div>

<br>

<div align="center">
  <h1>🤖 AI Assistant</h1>
  <p><strong>A powerful, web-based AI assistant powered by DeepSeek V4 Flash Free — 100% free, no credit card required.</strong></p>
  <p>Ask questions, summarize text, and generate creative content with just a few clicks.</p>
  <br>
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-deployment">Deployment</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-contributing">Contributing</a>
</div>

<br>

## ✨ Features

| Feature | Description |
|---|---|
| **📝 Answer Questions** | Ask factual questions and get concise, detailed, or creative answers |
| **📋 Summarize Text** | Paste lengthy articles — get one-line summaries, bullet points, or detailed breakdowns |
| **🎨 Creative Writing** | Generate stories, poems, essays, and articles from simple prompts |
| **🎯 3 Prompt Styles Per Function** | Short & direct, detailed explanation, or creative & fun — you choose the tone |
| **💬 Feedback Loop** | Rate responses as helpful or not — your feedback refines the experience |
| **🌙 Beautiful Dark UI** | Modern, responsive design that works on desktop and mobile |
| **🔗 Ctrl+Enter Shortcut** | Quick keyboard shortcut for faster interactions |
| **📦 Zero Cost** | Uses free DeepSeek V4 Flash model via OpenCode Zen API |

## 🖥️ Demo

> _Live demo coming soon. Deploy your own instance in under 5 minutes!_

<div align="center">
  <img src="https://via.placeholder.com/800x450/1a1a2e/a855f7?text=AI+Assistant+Dashboard" alt="AI Assistant Screenshot" width="80%" style="border-radius: 12px; border: 1px solid rgba(168,85,247,0.3);">
  <br>
  <em>AI Assistant — Three function tabs with distinct prompt styles</em>
</div>

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- A free API key from [OpenCode Zen](https://opencode.ai/zen)

### Installation

```bash
# Clone the repository
git clone https://github.com/aman179102/ai-assistant.git
cd ai-assistant

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Configure your API key
cp .env.example .env
# Edit .env and add your OpenCode Zen API key
```

### Run Locally

```bash
python app.py
```

Open your browser and navigate to **http://localhost:5000**

### Usage

1. Select a function tab: **Answer Questions**, **Summarize Text**, or **Creative Writing**
2. Choose a prompt style (e.g., Short & Direct, Detailed Explanation)
3. Type your question or paste your text
4. Click **Generate Response** or press `Ctrl + Enter`
5. Rate the response with 👍 or 👎

## 📡 API Reference

### POST `/chat`

Generate a response from the AI assistant.

**Request Body:**

```json
{
  "function": "qa",
  "prompt": "qa_short",
  "input": "What is the capital of France?"
}
```

**Available Functions:**

| Function Key | Description | Prompt Options |
|---|---|---|
| `qa` | Answer questions | `qa_short`, `qa_detailed`, `qa_creative` |
| `summarize` | Summarize text | `sum_short`, `sum_bullet`, `sum_detailed` |
| `creative` | Creative writing | `cr_story`, `cr_poem`, `cr_essay` |

**Response:**

```json
{
  "response": "The capital of France is Paris..."
}
```

### POST `/feedback`

Submit feedback on a response.

```json
{
  "function": "qa",
  "prompt": "qa_short",
  "input": "What is the capital of France?",
  "response": "The capital of France is Paris...",
  "helpful": true
}
```

## ☁️ Deployment

### Deploy to Render (Free)

[![Deploy to Render](https://img.shields.io/badge/Deploy%20to-Render-6366F1?style=for-the-badge&logo=render&logoColor=white)](https://render.com/deploy)

1. Push this repository to GitHub
2. Go to [Render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add environment variable:
   - `ZEN_API_KEY` = your OpenCode Zen API key
6. Deploy!

> **Note:** On Render's free tier, services spin down after 15 minutes of inactivity. Use [cron-job.org](https://cron-job.org) to ping your app every 5 minutes to keep it awake.

### Deploy to Vercel

<details>
<summary>Click to expand</summary>

Vercel supports Python via serverless functions. Add a `vercel.json`:

```json
{
  "builds": [{
    "src": "app.py",
    "use": "@vercel/python"
  }],
  "routes": [{
    "src": "/(.*)",
    "dest": "app.py"
  }]
}
```

Set the `ZEN_API_KEY` environment variable in your Vercel dashboard.
</details>

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.12+** | Core programming language |
| **Flask** | Web framework for the backend |
| **OpenAI SDK** | OpenAI-compatible client for OpenCode Zen API |
| **DeepSeek V4 Flash Free** | Free, powerful LLM for generating responses |
| **Gunicorn** | Production-ready WSGI server |
| **HTML / CSS / JS** | Frontend user interface |
| **Font Awesome** | Icons for the UI |
| **Render** | Hosting platform (recommended) |

## 📂 Project Structure

```
ai-assistant/
├── app.py                 # Flask application with API routes
├── templates/
│   └── index.html         # Web user interface
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── feedback.json          # User feedback storage
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

## 🤝 Contributing

Contributions are what make the open-source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

## 🙏 Acknowledgements

- [OpenCode Zen](https://opencode.ai/zen) for the free DeepSeek V4 Flash API
- [DeepSeek](https://deepseek.com) for the powerful LLM
- [Render](https://render.com) for free hosting

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/aman179102">aman179102</a></p>
  <p>
    <a href="https://github.com/aman179102/ai-assistant/issues">Report Bug</a> •
    <a href="https://github.com/aman179102/ai-assistant/issues">Request Feature</a>
  </p>
</div>
