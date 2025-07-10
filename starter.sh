#!/bin/bash

# FastAPI GenAI Project Starter Script
# Usage: 
#   chmod +x starter.sh
#   ./starter.sh
# 
# This script creates a complete FastAPI project structure with:
# - Python files and directories
# - pyproject.toml with dependencies
# - Docker configuration
# - Git repository initialization
# - Virtual environment setup with uv

mkdir -p {api,core,data,models}

# Create Python files
touch api/__init__.py
touch api/routes.py
touch api/agents.py
touch core/{memory.py,embeddings.py,config.py}
touch main.py

# Create environment files
cat > .env <<EOF
OPENAI_API_KEY=your-key-here
EOF

cat > pyproject.toml <<EOF
[project]
name = "sentinel"
version = "0.1.0"
description = "FastAPI-based GenAI MVP app with FAISS and OpenAI"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "fastapi",
    "uvicorn[standard]",
    "openai",
    "faiss-cpu",
    "python-dotenv",
    "pymongo",
]

[tool.uv]
dev-dependencies = []
EOF

# Create README
cat > README.md <<EOF
# Sentinel

FastAPI-based GenAI MVP app with FAISS and OpenAI.
EOF

# Create Dockerfile
cat > Dockerfile <<EOF
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir uv && uv sync
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

# Create docker-compose.yml
cat > docker-compose.yml <<EOF
version: "3.8"
services:
  app:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - .:/app
    restart: unless-stopped
EOF

# Create .gitignore
cat > .gitignore <<EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.venv/
venv/
ENV/
env/

# Environment variables
.env
.env.local
.env.production

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log

# Database
*.db
*.sqlite3

# Cache
.cache/
.pytest_cache/
EOF

echo "✅ Project 'Sentinel' scaffolded successfully in current directory."
echo "🔄 Initializing git repository..."
git init

echo "📦 Installing dependencies with uv..."
uv sync

echo "🎉 Setup complete! Your Sentinel project is ready."
echo "Next steps:"
echo "  - Add your OpenAI API key to .env file"
echo "  - Start coding in main.py"
echo "  - Run: uvicorn main:app --reload"