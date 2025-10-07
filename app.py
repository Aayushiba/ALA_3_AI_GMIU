from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("static/questions.json") as f:
    qa_pairs = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.form["question"].strip()
    answer = qa_pairs.get(user_question, "Sorry, I don't have an answer to that. Try asking something else about AI's future.")
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
