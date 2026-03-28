import os
from openai import OpenAI


class PostGenerator:
    """Generates LinkedIn posts using an LLM."""

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def create(self, topic: str, tone: str = "professional", length: str = "medium") -> str:
        """Generate a LinkedIn post for the given topic.

        Args:
            topic: The subject or idea to write about.
            tone: The tone of the post (professional, conversational, inspirational).
            length: The desired length (short, medium, long).

        Returns:
            A formatted LinkedIn post string.
        """
        length_map = {"short": "150 words", "medium": "250 words", "long": "400 words"}
        word_count = length_map.get(length, "250 words")

        prompt = (
            f"Write a LinkedIn post about: {topic}\n"
            f"Tone: {tone}\n"
            f"Length: approximately {word_count}\n"
            f"Include 3-5 relevant hashtags at the end."
        )

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
