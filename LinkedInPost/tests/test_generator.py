from unittest.mock import MagicMock, patch

import pytest

from core.generator import PostGenerator


@pytest.fixture()
def generator():
    with patch("core.generator.OpenAI"):
        gen = PostGenerator()
        return gen


def _mock_response(text: str) -> MagicMock:
    response = MagicMock()
    response.choices[0].message.content = text
    return response


def test_create_returns_string(generator):
    generator.client.chat.completions.create.return_value = _mock_response(
        "Great post! #AI #Tech"
    )
    result = generator.create(topic="AI trends")
    assert isinstance(result, str)
    assert len(result) > 0


def test_create_handles_none_content(generator):
    generator.client.chat.completions.create.return_value = _mock_response(None)
    result = generator.create(topic="AI trends")
    assert result == ""


def test_create_includes_topic_in_prompt(generator):
    generator.client.chat.completions.create.return_value = _mock_response("Post text")
    generator.create(topic="machine learning")
    call_args = generator.client.chat.completions.create.call_args
    messages = call_args.kwargs["messages"]
    assert any("machine learning" in m["content"] for m in messages)


def test_create_length_medium_by_default(generator):
    generator.client.chat.completions.create.return_value = _mock_response("Post")
    generator.create(topic="Python")
    call_args = generator.client.chat.completions.create.call_args
    messages = call_args.kwargs["messages"]
    assert any("250 words" in m["content"] for m in messages)


def test_create_length_short(generator):
    generator.client.chat.completions.create.return_value = _mock_response("Short post")
    generator.create(topic="Python", length="short")
    call_args = generator.client.chat.completions.create.call_args
    messages = call_args.kwargs["messages"]
    assert any("150 words" in m["content"] for m in messages)


def test_create_length_long(generator):
    generator.client.chat.completions.create.return_value = _mock_response("Long post")
    generator.create(topic="Python", length="long")
    call_args = generator.client.chat.completions.create.call_args
    messages = call_args.kwargs["messages"]
    assert any("400 words" in m["content"] for m in messages)
