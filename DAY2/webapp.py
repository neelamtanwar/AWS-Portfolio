from flask import Flask, request, jsonify
import statistics

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Python Analytics API is Live!"

@app.route("/health")
def health():
    return {"status": "running"}

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    numbers = data.get("numbers", [])

    if not numbers:
        return jsonify({"error": "No numbers provided"}), 400

    try:
        result = {
            "mean": statistics.mean(numbers),
            "median": statistics.median(numbers),
            "mode": statistics.multimode(numbers),  # FIXED
            "count": len(numbers)
        }
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)