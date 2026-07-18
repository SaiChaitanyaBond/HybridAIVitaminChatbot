"""
Hybrid Chatbot Service

Coordinates the Rule Engine and AI Service.
"""

import logging
import time

from chatbot.rule_engine import RuleEngine
from ai.ai_service import AIService

logger = logging.getLogger(__name__)


class HybridChatbotService:
    """
    Hybrid chatbot that combines a rule-based engine
    with an AI service.
    """

    def __init__(self):
        self.rule_engine = RuleEngine()
        self.ai_service = AIService()

    @staticmethod
    def _processing_time(start_time: float) -> float:
        """
        Calculate elapsed processing time in milliseconds.
        """
        return round((time.perf_counter() - start_time) * 1000, 2)

    def get_response(self, user_input: str) -> dict:
        """
        Generate a chatbot response.

        Parameters
        ----------
        user_input : str
            User message.

        Returns
        -------
        dict
            Standardized chatbot response.
        """

        start_time = time.perf_counter()

        logger.info("Received user input: %s", user_input)

        # -----------------------------
        # Rule Engine
        # -----------------------------
        rule_result = self.rule_engine.get_response(user_input)

        if rule_result["route"] == "rule":

            processing_time = self._processing_time(start_time)

            logger.info(
                "Rule matched | intent=%s | confidence=%.2f | time=%sms",
                rule_result["intent"],
                rule_result["confidence"],
                processing_time
            )

            return {
                "success": True,
                "source": "rule_engine",
                "provider": "internal",
                "model": "rule_engine",
                "intent": rule_result["intent"],
                "confidence": rule_result["confidence"],
                "response": rule_result["response"],
                "processing_time_ms": processing_time
            }

        # -----------------------------
        # AI Routing
        # -----------------------------
        logger.info("Routing request to Hugging Face AI")

        ai_result = self.ai_service.generate_response(user_input)

        processing_time = self._processing_time(start_time)

        if ai_result["success"]:

            logger.info(
                "AI response generated | provider=%s | model=%s | time=%sms",
                ai_result.get("provider"),
                ai_result.get("model"),
                processing_time
            )

            return {
                "success": True,
                "source": "huggingface",
                "provider": ai_result.get("provider"),
                "model": ai_result.get("model"),
                "intent": None,
                "confidence": None,
                "response": ai_result["response"],
                "processing_time_ms": processing_time
            }

        # -----------------------------
        # AI Failure
        # -----------------------------
        logger.error(
            "AI request failed | error=%s | time=%sms",
            ai_result.get("error"),
            processing_time
        )

        return {
            "success": False,
            "source": "huggingface",
            "provider": ai_result.get("provider"),
            "model": ai_result.get("model"),
            "intent": None,
            "confidence": None,
            "response": "",
            "error": ai_result.get("error"),
            "processing_time_ms": processing_time
        }