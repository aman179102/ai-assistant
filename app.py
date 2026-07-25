import os
import json
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("ZEN_API_KEY"),
    base_url="https://opencode.ai/zen/v1",
)

MODEL = "deepseek-v4-flash-free"
FEEDBACK_FILE = "feedback.json"

PROMPTS = {
    "qa": {
        "name": "Answer Questions",
        "icon": "fa-question-circle",
        "description": "Ask factual questions and get informative answers",
        "prompts": [
            {
                "id": "qa_short",
                "label": "Short & Direct",
                "system": "You are a helpful assistant. Answer the user's question concisely in 2-3 sentences. Be accurate and factual.",
            },
            {
                "id": "qa_detailed",
                "label": "Detailed Explanation",
                "system": "You are a knowledgeable tutor. Provide a comprehensive, well-structured answer with examples and explanations. Write 3-4 paragraphs.",
            },
            {
                "id": "qa_creative",
                "label": "Creative & Fun",
                "system": "You are a creative and witty explainer. Answer the question in an engaging, fun, and memorable way. Use analogies and humor where appropriate.",
            },
        ],
    },
    "summarize": {
        "name": "Summarize Text",
        "icon": "fa-compress-alt",
        "description": "Paste any text and get a concise summary",
        "prompts": [
            {
                "id": "sum_short",
                "label": "One-Line Summary",
                "system": "You are a text summarizer. Summarize the following text in ONE single sentence. Be precise and capture the main idea only.",
            },
            {
                "id": "sum_bullet",
                "label": "Bullet Points",
                "system": "You are a text analyst. Summarize the following text using 3-5 bullet points. Each bullet should capture one key takeaway. Be clear and concise.",
            },
            {
                "id": "sum_detailed",
                "label": "Detailed Summary",
                "system": "You are a professional editor. Provide a thorough summary covering the main arguments, supporting details, and conclusions. Write 2-3 paragraphs maintaining the original tone.",
            },
        ],
    },
    "creative": {
        "name": "Creative Writing",
        "icon": "fa-feather-alt",
        "description": "Generate stories, poems, essays, and more",
        "prompts": [
            {
                "id": "cr_story",
                "label": "Short Story",
                "system": "You are a creative writer. Write a short story based on the user's prompt. Include interesting characters, vivid descriptions, and a satisfying narrative arc. Keep it 300-500 words.",
            },
            {
                "id": "cr_poem",
                "label": "Poem",
                "system": "You are a poet. Write a poem based on the user's theme. Use rhythmic language, imagery, and emotional depth. Can be rhyming or free verse.",
            },
            {
                "id": "cr_essay",
                "label": "Essay / Article",
                "system": "You are a skilled essay writer. Write a well-structured short essay or article on the given topic. Include an introduction, body with key points, and a conclusion. Write 400-600 words.",
            },
        ],
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
    return render_template("index.html", functions=PROMPTS)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    function_key = data.get("function")
    prompt_key = data.get("prompt")
    user_input = data.get("input", "").strip()

    if not function_key or not prompt_key or not user_input:
        return jsonify({"error": "Missing required fields"}), 400

    func = PROMPTS.get(function_key)
    if not func:
        return jsonify({"error": "Invalid function"}), 400

    prompt_config = next((p for p in func["prompts"] if p["id"] == prompt_key), None)
    if not prompt_config:
        return jsonify({"error": "Invalid prompt style"}), 400

    system_msg = prompt_config["system"]

    if function_key == "summarize":
        user_msg = f"{system_msg}\n\nText to summarize:\n{user_input}"
        messages = [{"role": "user", "content": user_msg}]
    else:
        messages = [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_input},
        ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=1024,
            temperature=0.7,
        )
        reply = response.choices[0].message.content
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json()
    entry = {
        "function": data.get("function"),
        "prompt": data.get("prompt"),
        "user_input": data.get("input", "")[:200],
        "response": data.get("response", "")[:200],
        "helpful": data.get("helpful"),
        "timestamp": datetime.now().isoformat(),
    }
    save_feedback(entry)
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
