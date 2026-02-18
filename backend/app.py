from flask import Flask, jsonify
from flask_cors import CORS
import random
from match_data import MATCH_OVERS

app = Flask(__name__)
CORS(app)  # Allow browser extension access

current_over_index = 0


# ===============================
# AI FEATURE EXTRACTION
# ===============================
def extract_features(over):
    balls = over["balls"]

    runs = sum(b for b in balls if isinstance(b, int))
    dot_balls = balls.count(0)
    boundaries = balls.count(4) + balls.count(6)
    wicket = over["wicket"]
    rr_change = over["rr_after"] - over["rr_before"]

    return {
        "runs": runs,
        "dot_balls": dot_balls,
        "boundaries": boundaries,
        "wicket": wicket,
        "rr_change": rr_change
    }


# ===============================
# AI CLASSIFICATION LOGIC
# ===============================
def classify_over(features):
    if features["wicket"] and features["runs"] <= 6:
        return "breakthrough"

    if features["dot_balls"] >= 4 and features["boundaries"] == 0:
        return "pressure"

    if features["boundaries"] >= 2:
        return "dominance"

    if features["rr_change"] > 0.4:
        return "momentum"

    return "neutral"


# ===============================
# NATURAL LANGUAGE GENERATION
# ===============================
def generate_summary(category):
    templates = {
        "pressure": [
            "Dot-ball pressure built steadily with no release shots.",
            "A tight over kept the batter under sustained pressure."
        ],
        "breakthrough": [
            "Sustained pressure resulted in a crucial breakthrough.",
            "A disciplined over ended with a key wicket."
        ],
        "dominance": [
            "Batters controlled the over with confident stroke play.",
            "Aggressive shot-making swung momentum this over."
        ],
        "momentum": [
            "Momentum shifted as the run rate climbed.",
            "The batting side gained control in this phase."
        ],
        "neutral": [
            "A steady over with neither side gaining clear control."
        ]
    }

    return random.choice(templates[category])


# ===============================
# MAIN AI PIPELINE
# ===============================
def analyze_over(over):
    features = extract_features(over)
    category = classify_over(features)
    summary = generate_summary(category)
    return summary


# ===============================
# API ENDPOINT
# ===============================
@app.route("/summary", methods=["GET"])
def get_summary():
    global current_over_index

    over = MATCH_OVERS[current_over_index]
    summary_text = analyze_over(over)

    response = {
        "over": over["over"],
        "summary": summary_text
    }

    # Move to next over (loop for demo)
    current_over_index = (current_over_index + 1) % len(MATCH_OVERS)

    return jsonify(response)


# ===============================
# HEALTH CHECK
# ===============================
@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "AI backend running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context="adhoc")
