"""
Test script for the Rule Engine.
"""

from chatbot.rule_engine import RuleEngine


def print_result(question: str, result: dict):

    print("=" * 70)
    print(f"Question           : {question}")
    print(f"Matched            : {result['matched']}")
    print(f"Intent             : {result['intent']}")
    print(f"Confidence         : {result['confidence']}")
    print(f"Matched Pattern    : {result['matched_pattern']}")
    print(f"Matched Keywords   : {result['matched_keywords']}")
    print(f"Route              : {result['route']}")
    print(f"Response           : {result['response']}")
    print("=" * 70)
    print()

def main():

    chatbot = RuleEngine()

    test_questions = [
        "Hello",
        "Hi there",
        "What are the symptoms of vitamin D deficiency?",
        "Tell me about low iron",
        "Should I take vitamin supplements?",
        "Can vitamin D deficiency make me tired?",
        "Explain the biochemical pathway of vitamin D metabolism.",
        "Compare Vitamin D2 and Vitamin D3.",
        "Why does iron deficiency occur?",
        "How does Vitamin B12 affect the nervous system?",
        "Goodbye"
    ]

    for question in test_questions:

        result = chatbot.get_response(question)

        print_result(question, result)


if __name__ == "__main__":
    main()
