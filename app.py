from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load Q&A pairs
with open("static/questions.json") as f:
    qa_pairs = json.load(f)

# Add basic greetings
greetings = {
    "hi": "Hello! 👋 Ask me anything about the future of AI.",
    "hello": "Hi there! What would you like to know about AI?",
    "hey": "Hey! Let's chat about what AI could look like in 10 years.",
    "good morning": "Good morning! Ready to explore the future of AI?",
    "good evening": "Good evening! I'm here to answer your AI questions."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.form["question"].strip().lower()
    
    # Check if it's a greeting
    if user_question in greetings:
        answer = greetings[user_question]
    else:
        # Lookup exact match
        answer = qa_pairs.get(user_question.capitalize(), "Sorry, I don't have an answer to that. Try asking something else about AI's future.")
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
