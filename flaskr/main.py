from flask import Flask, request, jsonify, render_template
from Chatbot import Chatbot
from config import APIKEY

app = Flask(__name__)
chatbot = Chatbot(apiKey=APIKEY)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("userInput")
    response = chatbot.chat(user_input)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
