from flask import Flask, request, jsonify
from agent import root_agent

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Planet Guide Agent is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("prompt", "")

    try:
        try:
            response = root_agent.run(user_input)
        except:
            response = root_agent.invoke(user_input)
            return jsonify({"response": str(response)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)