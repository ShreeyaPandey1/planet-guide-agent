from flask import Flask
from agent import Agent  # adjust if needed

app = Flask(__name__)

@app.route("/")
def home():
    return "Planet Guide Agent is running 🚀"

@app.route("/run")
def run_agent():
    agent = Agent()
    result = agent.run()  # change if your function name is different
    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)      