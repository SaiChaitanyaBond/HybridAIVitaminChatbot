"""
Rule Engine

This module implements the traditional rule-based chatbot.
It loads a knowledge base, matches user input against known
patterns, and returns the best matching response.
"""

import json
import re
from pathlib import Path
from typing import Dict

MIN_CONFIDENCE = 0.60
ROUTE_RULE = "rule"
ROUTE_AI = "ai"

class RuleEngine:
    """
    Traditional rule-based chatbot engine.
    """

    def __init__(self):
        """
        Load the chatbot knowledge base.
        """

        knowledge_file = (
            Path(__file__).parent / "knowledge_base.json"
        )

        with open(knowledge_file, "r", encoding="utf-8") as file:
            self.knowledge_base = json.load(file)

        # Load complexity keywords
        self.complexity_keywords = {
            keyword.lower()
            for keyword in self.knowledge_base.get(
                "complexity_keywords",
                []
            )
        }

    @staticmethod
    def normalize_text(text: str) -> str:
        """
        Normalize text for matching.

        Parameters
        ----------
        text : str
            Input text.

        Returns
        -------
        str
            Normalized text.
        """

        text = text.lower()

        text = re.sub(r"[^\w\s]", "", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()
    
    def is_complex_query(self, user_input: str) -> bool:
        """
        Determine whether the query should be handled by AI.
        """

        normalized = self.normalize_text(user_input)

        words = set(normalized.split())

        for keyword in self.complexity_keywords:

            keyword_words = set(keyword.split())

            if keyword_words.issubset(words):
                return True

        return False

    def get_response(self, user_input: str) -> Dict:
        """
        Return the best matching response using weighted keyword matching.
        """

        if self.is_complex_query(user_input):
            return {
                "matched": False,
                "intent": None,
                "confidence": 0.0,
                "matched_pattern": "",
                "matched_keywords": [],
                "response": "",
                "route": ROUTE_AI
            }

        normalized_input = self.normalize_text(user_input)
        input_words = set(normalized_input.split())

        best_match: Dict | None = None
        best_confidence = 0.0
        best_pattern = ""
        matched_keywords = []

        for intent in self.knowledge_base["intents"]:

            for pattern in intent["patterns"]:

                normalized_pattern = self.normalize_text(pattern)
                pattern_words = set(normalized_pattern.split())

                overlap = input_words.intersection(pattern_words)

                if not overlap:
                    continue

                # Percentage of pattern words matched
                pattern_score = len(overlap) / len(pattern_words)

                # Penalize long questions that only happen to mention the topic
                input_score = len(overlap) / len(input_words)

                # Weighted confidence
                confidence = (0.7 * pattern_score) + (0.3 * input_score)

                if confidence > best_confidence:
                    best_confidence = confidence
                    best_match = intent
                    best_pattern = pattern
                    matched_keywords = sorted(list(overlap))

        if best_match and best_confidence >= MIN_CONFIDENCE:

            return {
                "matched": True,
                "intent": best_match["intent"],
                "confidence": round(best_confidence, 2),
                "matched_pattern": best_pattern,
                "matched_keywords": matched_keywords,
                "response": best_match["responses"][0],
                "route": ROUTE_RULE,
            }

        return {
            "matched": False,
            "intent": None,
            "confidence": round(best_confidence, 2),
            "matched_pattern": best_pattern,
            "matched_keywords": matched_keywords,
            "response": "",
            "route": ROUTE_AI,
        }