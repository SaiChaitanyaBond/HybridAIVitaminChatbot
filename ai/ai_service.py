"""
AI Service

Provides a high-level interface for generating AI responses.
The service delegates requests to the configured AI provider.
"""

from typing import Dict

from ai.factory import AIProviderFactory


class AIService:
    """
    High-level service for interacting with AI providers.
    """

    def __init__(self):
        """
        Initialize the configured AI provider.
        """
        self.provider = AIProviderFactory.get_provider()

    def generate_response(self, prompt: str) -> Dict:
        """
        Generate an AI response.

        Parameters
        ----------
        prompt : str
            User's input prompt.

        Returns
        -------
        Dict
            Standardized response returned by the AI provider.
        """

        if not prompt or not prompt.strip():
            return {
                "success": False,
                "provider": None,
                "model": None,
                "response": "",
                "error": "Prompt cannot be empty."
            }

        return self.provider.generate_response(prompt)