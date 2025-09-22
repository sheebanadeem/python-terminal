from flask import Flask, render_template, request, jsonify
import os
from pyterminal.engine import run_command
from pyterminal.nlp import parse_nlp

app = Flask(__name__)

# Start in current working directory
current_dir = os.getcwd()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run():
    global current_dir
    data = request.json
    user_input = data.get("command", "")

    # Pass through NLP
    parsed_command = parse_nlp(user_input)
    output, current_dir = run_command(parsed_command, current_dir)

    if output == "exit":
        return jsonify({"output": "Session ended. Please close the tab."})

    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True)
