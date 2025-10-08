from flask import Flask, render_template, request, jsonify
import json
import difflib

app = Flask(__name__)

with open("static/qna.json", "r", encoding="utf-8") as f:
    qna = json.load(f)

greetings = {
    "hi": "Hello there 👋! I’m your Financial Literacy Assistant. Ask me about money, saving, investing, or taxes!",
    "hello": "Hi! Ready to learn smart money moves?",
    "hey": "Hey! Let’s talk about financial growth 💹",
    "good morning": "Good morning ☀️! A great day to learn something about finance!",
    "good evening": "Good evening 🌙! Let’s discuss wealth building strategies!",
    "thanks": "You’re welcome 💰. Stay financially smart!"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question", "").lower().strip()

    # Greeting responses
    for key, reply in greetings.items():
        if user_question.startswith(key):
            return jsonify({"answer": reply})

    # Fuzzy matching
    questions = [qa["question"].lower() for qa in qna]
    match = difflib.get_close_matches(user_question, questions, n=1, cutoff=0.4)

    if match:
        for qa in qna:
            if qa["question"].lower() == match[0]:
                return jsonify({"answer": qa["answer"]})

    return jsonify({"answer": "Hmm 🤔 I don’t have that info yet. Try asking about budgeting, investing, or taxes!"})

if __name__ == "__main__":
    app.run(debug=True)
