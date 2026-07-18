"""
Test script for the Hugging Face AI provider.
"""

from ai.ai_service import AIService


def main():
    """
    Test the configured AI provider.
    """

    print("=" * 60)
    print("Testing Hugging Face AI Provider")
    print("=" * 60)

    ai_service = AIService()

    prompt = "What are the symptoms of Vitamin D deficiency?"

    print(f"\nPrompt:\n{prompt}\n")

    result = ai_service.generate_response(prompt)

    if result["success"]:
        print("=" * 60)
        print("Provider :", result["provider"])
        print("Model    :", result["model"])
        print("=" * 60)
        print(result["response"])
    else:
        print("=" * 60)
        print("Error")
        print("=" * 60)
        print(result["error"])


if __name__ == "__main__":
    main()