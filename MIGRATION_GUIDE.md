# Migration Guide: Separating AI Companion Orchestrator from Sentinel

## Overview

This guide provides step-by-step instructions for creating a new repository for the AI Companion Orchestration Platform and removing it from the Sentinel repository.

## Prerequisites

- GitHub account with repository creation access
- Git command line tools
- Understanding of both project proposals (see DOCS_ANALYSIS.md)

---

## Step 1: Create the New Repository

### Option A: Via GitHub Web Interface

1. Go to https://github.com/new
2. **Repository name:** `ai-companion-orchestrator` (or your preferred name)
3. **Description:** "Cloud-native orchestration engine for multi-persona AI companions with multi-device coordination"
4. **Visibility:** Choose Public or Private
5. **Initialize:** Do NOT initialize with README, .gitignore, or license (we'll add these)
6. Click "Create repository"

### Option B: Via GitHub CLI

```bash
gh repo create ai-companion-orchestrator --public --description "Cloud-native orchestration engine for multi-persona AI companions"
```

---

## Step 2: Set Up the New Repository Structure

Clone the new repository and create the initial structure:

```bash
# Clone the new repository
git clone https://github.com/YOUR_USERNAME/ai-companion-orchestrator.git
cd ai-companion-orchestrator

# Create directory structure
mkdir -p core
mkdir -p dashboard/components
mkdir -p device
mkdir -p personas
mkdir -p tests
mkdir -p config
mkdir -p docs

# Create placeholder files
touch core/__init__.py
touch core/persona_manager.py
touch core/conversation_engine.py
touch core/state_manager.py
touch core/audio_pipeline.py
touch core/event_bus.py
touch dashboard/app.py
touch device/main.py
touch device/hardware_interface.py
touch tests/__init__.py
touch config/config.yaml
touch config/.env.example
```

---

## Step 3: Copy Documentation from Sentinel

```bash
# Assuming you're in the ai-companion-orchestrator directory
# and the Sentinel repo is cloned at ../Sentinel

# Copy the Docs folder contents
cp ../Sentinel/Docs/AI\ Nanny\ Platform\ –\ Persona\ Customization.md docs/
cp ../Sentinel/Docs/AI-Companion-Orchestration-Platform.1.txt docs/
cp ../Sentinel/Docs/AI-Companion-Software-Dev.md docs/

# Optional: Clean up Test.txt if not needed
```

---

## Step 4: Create README for New Repository

Create `README.md` in the ai-companion-orchestrator repository:

```markdown
# AI Companion Orchestration Platform

Cloud-native orchestration engine enabling multi-persona AI companions with multi-device coordination for elderly care and assisted living facilities.

## Overview

This platform enables:
- **Runtime persona switching** (<2 seconds)
- **Multi-device coordination** (synchronous, handoff, group activities)
- **Edge-cloud hybrid architecture** (Raspberry Pi + cloud control plane)
- **B2B licensing model** for device manufacturers and care facilities

## Architecture

```
┌─────────────────────────────────────────┐
│   Orchestration Control Plane (Cloud)   │
├─────────────────────────────────────────┤
│ • Persona Registry & Hot-Swap Engine    │
│ • Multi-Device Session Manager          │
│ • Event Bus (device ↔ device comms)     │
│ • Analytics & Telemetry                 │
└─────────────────────────────────────────┘
              ↓ ↓ ↓
    ┌─────────┴─┴─┴─────────┐
    │   Device Agent (Edge)  │
    ├────────────────────────┤
    │ • Lightweight runtime  │
    │ • Audio I/O handler    │
    │ • Persona cache        │
    │ • Offline fallback     │
    └────────────────────────┘
```

## Project Structure

```
ai-companion-orchestrator/
├── core/                    # Core orchestration engine
│   ├── persona_manager.py
│   ├── conversation_engine.py
│   ├── state_manager.py
│   ├── audio_pipeline.py
│   └── event_bus.py
├── dashboard/               # Streamlit demo dashboard
│   ├── app.py
│   └── components/
├── device/                  # Raspberry Pi runtime
│   ├── main.py
│   └── hardware_interface.py
├── personas/                # Persona definition files
│   ├── storyteller.yaml
│   ├── nurse.yaml
│   └── companion.yaml
├── tests/                   # Test suite
├── config/                  # Configuration files
└── docs/                    # Detailed documentation
```

## Documentation

- [AI Nanny Platform Architecture](docs/AI%20Nanny%20Platform%20–%20Persona%20Customization.md) - Persona customization system design
- [Orchestration Platform Overview](docs/AI-Companion-Orchestration-Platform.1.txt) - Product vision and business model
- [Software Build Guide](docs/AI-Companion-Software-Dev.md) - Week-by-week implementation plan

## Target Market

### Primary Customers
- Nursing homes and assisted living facilities
- Device manufacturers (Amazon, Google, ElliQ)
- Senior care technology platforms

### Business Model
- **SaaS:** $0.50-2.00 per device/month
- **White Label:** $50k-200k/year licensing
- **Professional Services:** Custom persona development

## Current Status

**Phase:** Planning & Architecture  
**Next Steps:** Core engine implementation (Week 1-2)

## Related Projects

- [Sentinel](https://github.com/serbantica/Sentinel) - Mental health companion system (separate project)

## Getting Started

(To be added as implementation progresses)

## License

(Choose your license)

## Contact

(Your contact information)
```

---

## Step 5: Create pyproject.toml for New Repository

Create `pyproject.toml`:

```toml
[project]
name = "ai-companion-orchestrator"
version = "0.1.0"
description = "Cloud-native orchestration engine for multi-persona AI companions"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "fastapi",
    "uvicorn[standard]",
    "anthropic",  # for Claude API
    "openai",     # alternative LLM
    "pydantic",
    "python-dotenv",
    "redis",
    "asyncio",
    "pyyaml",
    "streamlit",  # for dashboard
    "paho-mqtt",  # for device messaging
]

[project.optional-dependencies]
device = [
    "RPi.GPIO",        # Raspberry Pi GPIO
    "pyaudio",         # Audio handling
    "speech_recognition",
    "elevenlabs",      # Text-to-speech
]

[tool.uv]
dev-dependencies = [
    "pytest",
    "black",
    "ruff",
]
```

---

## Step 6: Create .gitignore

Create `.gitignore`:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
ENV/
build/
dist/
*.egg-info/

# Environment
.env
.env.local
config/secrets.yaml

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Testing
.pytest_cache/
.coverage
htmlcov/

# Device-specific
device/logs/
```

---

## Step 7: Initial Commit and Push

```bash
# In the ai-companion-orchestrator directory
git add .

# Create a multi-line commit message
git commit -m "Initial repository structure and documentation" \
           -m "- Added core module structure" \
           -m "- Added dashboard and device runtime placeholders" \
           -m "- Imported documentation from Sentinel repo" \
           -m "- Created README with project overview"

git push origin main
```

---

## Step 8: Clean Up Sentinel Repository

### Remove Docs Folder from Sentinel

```bash
# In the Sentinel repository directory
cd /path/to/Sentinel

# Remove the Docs folder
git rm -r Docs/

# Commit the removal with multi-line message
git commit -m "Move AI Companion Orchestration docs to separate repository" \
           -m "The Docs folder contained proposals for a different product" \
           -m "(AI Companion Orchestrator) which has been moved to its own" \
           -m "repository at: https://github.com/{username}/ai-companion-orchestrator" \
           -m "" \
           -m "See DOCS_ANALYSIS.md for details on why these projects are separate."

git push origin main
```

### Update Sentinel's README

The README has already been updated to clarify the project focus and reference the DOCS_ANALYSIS.md file.

---

## Step 9: Cross-Reference Both Projects

### In Sentinel README

Add (already done):
```markdown
## Related Projects

- [AI Companion Orchestrator](https://github.com/{username}/ai-companion-orchestrator) - Multi-device companion platform for elderly care (separate project)
```

### In Orchestrator README

Add (already in template above):
```markdown
## Related Projects

- [Sentinel](https://github.com/serbantica/Sentinel) - Mental health companion system (separate project)
```

---

## Step 10: Optional - Create Organization

If you want both projects under one umbrella:

1. Create GitHub organization (e.g., "YourCompany-AI")
2. Transfer both repositories to the organization
3. Create organization README explaining both projects

---

## Step 11: Update Documentation References

In the new repository, update any references that mention "Sentinel":

```bash
# Search for Sentinel references
cd ai-companion-orchestrator
grep -r "Sentinel" docs/

# Update as needed to clarify separation
```

---

## Verification Checklist

After migration, verify:

- [ ] New repository created and accessible
- [ ] All documentation copied from Sentinel/Docs to new repo
- [ ] New repo has proper README explaining the project
- [ ] New repo has pyproject.toml with correct dependencies
- [ ] New repo has .gitignore
- [ ] New repo has initial directory structure
- [ ] Sentinel repo has Docs folder removed
- [ ] Sentinel README updated with clarification
- [ ] Both repositories cross-reference each other
- [ ] DOCS_ANALYSIS.md remains in Sentinel for historical context

---

## Timeline

This migration can be completed in **30-60 minutes**.

---

## Questions or Issues?

If you encounter issues during migration:

1. Check that you have correct permissions on both repositories
2. Verify Git remote URLs are correct
3. Review DOCS_ANALYSIS.md for context on why separation is needed

---

## Next Steps After Migration

### For AI Companion Orchestrator
1. Review docs/AI-Companion-Software-Dev.md for implementation plan
2. Set up development environment
3. Begin Week 1 implementation (Core Engine)

### For Sentinel
1. Continue with Sentinel_Roadmap_v2.md
2. Focus on mental health features
3. Implement security and compliance foundations

---

**Last Updated:** 2026-01-18
