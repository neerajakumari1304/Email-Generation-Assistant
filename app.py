import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, render_template, request
from models.email_generator import generate_email_strategy_a, generate_email_strategy_b
from evaluation.evaluator import evaluate_email

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    intent = request.form.get("intent", "").strip()
    facts_raw = request.form.get("facts", "").strip()
    tone = request.form.get("tone", "formal").strip()
    strategy = request.form.get("strategy", "A").strip()

    facts = [f.strip() for f in facts_raw.split(",") if f.strip()]

    if not intent or not facts:
        return render_template("index.html", error="Intent and Facts are required.")

    if strategy == "A":
        email = generate_email_strategy_a(intent, facts, tone)
    else:
        email = generate_email_strategy_b(intent, facts, tone)

    scores = evaluate_email(email, facts, tone)

    return render_template("index.html",
        email=email,
        scores=scores,
        intent=intent,
        facts_raw=facts_raw,
        tone=tone,
        strategy=strategy
    )

if __name__ == "__main__":
    app.run(debug=True)
