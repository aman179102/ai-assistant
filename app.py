import os
import json
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, session
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "super-secret-key-change-in-production")

client = OpenAI(
    api_key=os.getenv("ZEN_API_KEY"),
    base_url="https://opencode.ai/zen/v1",
)

MODEL = "deepseek-v4-flash-free"
FEEDBACK_FILE = "feedback.json"
MAX_HISTORY = 20

CHAT_MODES = {
    "general": {
        "name": "General Chat",
        "icon": "fa-comments",
        "description": "Chat about anything — casual conversation, fun facts, and daily topics",
        "system": "You are a friendly and engaging conversational AI. Chat naturally with the user on any topic. Be warm, helpful, and keep the conversation flowing. Ask follow-up questions to keep things interesting. Respond in 2-4 sentences unless the user asks for more detail.",
    },
    "info": {
        "name": "Information & Recommendations",
        "icon": "fa-lightbulb",
        "description": "Ask for facts, explanations, and personalized recommendations",
        "system": "You are a knowledgeable guide. Provide accurate information and thoughtful recommendations based on the user's questions. When giving recommendations, ask about their preferences first. Support your answers with clear reasoning. Be concise but thorough.",
    },
    "creative": {
        "name": "Creative Chat",
        "icon": "fa-feather",
        "description": "Storytelling, jokes, poems, and imaginative conversations",
        "system": "You are a creative and imaginative conversation partner. Tell stories, write poems, crack jokes, and explore wild ideas. Be playful, use vivid language, and encourage the user to be creative too. Make every response entertaining and inspiring.",
    },
}


def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)
    return []


def save_feedback(entry):
    feedback = load_feedback()
    feedback.append(entry)
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(feedback, f, indent=2)


@app.route("/")
def index():
    return render_template("index.html", modes=CHAT_MODES)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mode = data.get("mode", "general")
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Please enter a message"}), 400

    chat_mode = CHAT_MODES.get(mode)
    if not chat_mode:
        return jsonify({"error": "Invalid chat mode"}), 400

    if "conversation" not in session:
        session["conversation"] = []

    history = session["conversation"][-(MAX_HISTORY - 1):]
    messages = [{"role": "system", "content": chat_mode["system"]}]
    for entry in history:
        messages.append({"role": "user", "content": entry["user"]})
        messages.append({"role": "assistant", "content": entry["bot"]})
    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=512,
            temperature=0.8,
        )
        bot_reply = response.choices[0].message.content

        session["conversation"].append({
            "user": user_message,
            "bot": bot_reply,
            "mode": mode,
        })
        session.modified = True

        return jsonify({"response": bot_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/reset", methods=["POST"])
def reset():
    session.pop("conversation", None)
    return jsonify({"status": "ok"})


@app.route("/history", methods=["GET"])
def get_history():
    conv = session.get("conversation", [])
    return jsonify({"history": conv})


@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json()
    entry = {
        "mode": data.get("mode"),
        "message": data.get("message", "")[:200],
        "response": data.get("response", "")[:200],
        "helpful": data.get("helpful"),
        "timestamp": datetime.now().isoformat(),
    }
    save_feedback(entry)
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
