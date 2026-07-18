"""
Hugging Face Inference Provider

This module is responsible for communicating with the Hugging Face
Inference API. It provides a clean interface that can be used by the
AI service layer without exposing implementation details.
"""

from huggingface_hub import InferenceClient
from config import Config


class HuggingFaceProvider:
    """
    Handles communication with the Hugging Face Inference API.
    """

    def __init__(self):
        """
        Initialize the Hugging Face client.
        """
        self.client = InferenceClient(
            api_key=Config.HUGGINGFACE_API_TOKEN,
        )

        self.model = Config.HUGGINGFACE_MODEL

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the configured Hugging Face model.

        Parameters
        ----------
        prompt : str
            User prompt.

        Returns
        -------
        str
            AI generated response.
        """

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful medical assistant. "
                            "Provide educational information only. "
                            "Do not diagnose diseases or replace "
                            "professional medical advice."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                max_tokens=Config.MAX_RESPONSE_TOKENS,
                temperature=Config.TEMPERATURE,
            )

            return {
                "success": True,
                "provider": "huggingface",
                "model": self.model,
                "response": response.choices[0].message.content.strip(),
                "error": None,
            }

        except Exception as ex:
            return {
                "success": False,
                "provider": "huggingface",
                "model": self.model,
                "response": "",
                "error": str(ex),
            }