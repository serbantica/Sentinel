# LinkedInPost

AI-powered LinkedIn post generator that creates professional, engaging content from topics, articles, and project updates.

## Overview

LinkedInPost helps professionals and developers craft compelling LinkedIn posts by leveraging AI to:
- Generate post drafts from topic prompts or article summaries
- Adapt tone and style for professional audiences
- Suggest relevant hashtags and engagement hooks
- Optimize post length and formatting for LinkedIn's algorithm

## Project Structure

```
LinkedInPost/
├── core/                    # Core generation engine
│   ├── __init__.py
│   ├── generator.py         # Post generation logic
│   ├── templates.py         # Post templates and styles
│   └── optimizer.py         # Hashtag and engagement optimization
├── api/                     # FastAPI REST API
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── tests/                   # Test suite
│   └── __init__.py
├── config/                  # Configuration
│   └── .env.example
├── README.md
├── pyproject.toml
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.11+
- OpenAI API key (or compatible LLM provider)

### Installation

```bash
git clone git@github.com:serbantica/LinkedInPost.git
cd LinkedInPost
uv sync
cp config/.env.example config/.env
# Edit config/.env with your API keys
```

### Usage

```python
from core.generator import PostGenerator

generator = PostGenerator()
post = generator.create(
    topic="Launching our new AI mental health platform",
    tone="professional",
    length="medium"
)
print(post)
```

## Related Projects

- [Sentinel](https://github.com/serbantica/Sentinel) - Human-AI Mental Health Companion System

## Current Status

**Phase:** Initial Setup  
**Visibility:** Private

---

**Repository created:** 2026-03-28
