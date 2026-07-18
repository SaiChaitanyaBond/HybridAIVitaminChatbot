"""
AI Provider Factory

Creates and returns the configured AI provider.
"""

from config import Config
from ai.providers.huggingface_provider import HuggingFaceProvider


class AIProviderFactory:
    """
    Factory responsible for returning the configured AI provider.
    """

    @staticmethod
    def get_provider():
        """
        Return the configured AI provider.

        Returns
        -------
        object
            AI provider instance.
        """

        provider = Config.AI_PROVIDER.lower()

        if provider == "huggingface":
            return HuggingFaceProvider()

        raise ValueError(
            f"Unsupported AI provider: {Config.AI_PROVIDER}"
        )