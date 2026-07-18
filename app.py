"""
Hybrid AI Vitamin Chatbot

Main Flask application.
"""

import os

from flask import Flask, jsonify, render_template, request

# Initialize application logging
import logging_config

from services.hybrid_chatbot_service import HybridChatbotService

app = Flask(__name__)

chatbot = HybridChatbotService()


@app.route("/")
def home():
    """
    Render the chatbot user interface.
    """
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """
    Chatbot REST API endpoint.
    """

    data = request.get_json()

    if not data:
        return jsonify(
            {
                "success": False,
                "error": "No JSON payload received."
            }
        ), 400

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify(
            {
                "success": False,
                "error": "Message cannot be empty."
            }
        ), 400

    result = chatbot.get_response(user_message)

    return jsonify(result)


@app.route("/health")
def health():
    """
    Simple health check endpoint.
    """

    return jsonify(
        {
            "status": "UP",
            "application": "Hybrid AI Vitamin Chatbot"
        }
    )


if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG", "False").lower() == "true",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5001))
    )