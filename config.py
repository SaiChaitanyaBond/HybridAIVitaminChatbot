"""
Application configuration for the Hybrid AI Vitamin Chatbot.
"""

import os
from dotenv import load_dotenv

# Load variables from .env when running locally
load_dotenv()


class Config:
    """Application configuration."""

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")

    # AI Provider
    AI_PROVIDER = os.getenv("AI_PROVIDER", "huggingface").lower()

    # Hugging Face
    HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN", "")

    # Default model
    HUGGINGFACE_MODEL = os.getenv(
        "HUGGINGFACE_MODEL",
        "meta-llama/Llama-3.1-8B-Instruct"
    )

    # Rule Engine
    CONFIDENCE_THRESHOLD = float(
        os.getenv("CONFIDENCE_THRESHOLD", "0.80")
    )

    # Chat Settings
    MAX_RESPONSE_TOKENS = int(
        os.getenv("MAX_RESPONSE_TOKENS", "512")
    )

    TEMPERATURE = float(
        os.getenv("TEMPERATURE", "0.7")
    )