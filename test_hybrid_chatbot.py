"""
Test script for the Hybrid Chatbot Service.
"""
from services.hybrid_chatbot_service import HybridChatbotService


def print_result(question: str, result: dict):
    """Pretty print chatbot response."""

    print("=" * 80)
    print(f"Question     : {question}")
    print(f"Success      : {result['success']}")
    print(f"Source       : {result['source']}")
    print(f"Intent       : {result['intent']}")
    print(f"Confidence   : {result['confidence']}")
    print(f"Processing Time (ms): {result['processing_time_ms']}")
    print(f"Response")
    print("-" * 80)
    print(result["response"])

    if not result["success"]:
        print("-" * 80)
        print("Error:")
        print(result["error"])

    print("=" * 80)
    print()


def main():

    chatbot = HybridChatbotService()

    test_questions = [

        # Rule Engine
        "Hello",
        "Tell me about low iron",
        "Can vitamin D deficiency make me tired?",
        "Should I take vitamin supplements?",
        "Goodbye",

        # AI
        "Explain the biochemical pathway of vitamin D metabolism.",
        "Compare Vitamin D2 and Vitamin D3.",
        "How does Vitamin B12 affect the nervous system?",
        "What are the latest scientific discoveries regarding Vitamin D?"
    ]

    for question in test_questions:

        result = chatbot.get_response(question)

        print_result(question, result)


if __name__ == "__main__":
    main()