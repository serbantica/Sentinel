# Migration Guide: Separating AI Nanny from Sentinel

## Overview

This guide provides step-by-step instructions for creating a new repository for the AI Companion Orchestration Platform (AI Nanny) and migrating documentation from the Sentinel repository while preserving git history.

**Target Repository:** `serbantica/ai-nanny`

## Prerequisites

- GitHub account with repository creation access
- Git command line tools
- Understanding of both project proposals (see DOCS_ANALYSIS.md)
- Familiarity with `git subtree` or `git filter-repo`

---

## Quick Migration Using Git Subtree (Recommended)

The `git subtree` approach is the easiest way to extract the Docs folder while preserving its commit history.

### Step 1: Extract Docs History

```bash
# In the Sentinel repository
cd /path/to/Sentinel

# Create a new branch containing only the Docs folder history
git subtree split -P Docs -b ai-nanny-docs

# Verify the branch was created
git log ai-nanny-docs --oneline
```

### Step 2: Create the New Repository

#### Option A: Via GitHub Web Interface

1. Go to https://github.com/new
2. **Repository name:** `ai-nanny`
3. **Owner:** `serbantica`
4. **Description:** "AI Companion Orchestration Platform for elderly care with multi-device coordination"
5. **Visibility:** Choose Public or Private
6. **Initialize:** Do NOT initialize with README, .gitignore, or license (we'll push these)
7. Click "Create repository"

#### Option B: Via GitHub CLI

```bash
gh repo create serbantica/ai-nanny --public --description "AI Companion Orchestration Platform for elderly care with multi-device coordination"
```

### Step 3: Push to New Repository

```bash
# Add the new repository as a remote
git remote add ai-nanny git@github.com:serbantica/ai-nanny.git

# Push the ai-nanny-docs branch to the new repository's main branch
git push ai-nanny ai-nanny-docs:main

# Verify the push
git ls-remote ai-nanny
```

### Step 4: Clean Up (Optional)

```bash
# Remove the temporary branch (optional)
git branch -D ai-nanny-docs

# Remove the remote (optional, if you don't need it anymore)
git remote remove ai-nanny
```

---

## Alternative: Using git filter-repo (Advanced)

For more complex history manipulation or if you need to filter specific files/commits, use `git filter-repo`.

⚠️ **Warning:** This is a destructive operation. Always work on a fresh clone.

### Installation

```bash
# Install git-filter-repo
pip install git-filter-repo
```

### Usage

```bash
# Clone a fresh copy of Sentinel
git clone https://github.com/serbantica/Sentinel.git sentinel-temp
cd sentinel-temp

# Extract only the Docs folder
git filter-repo --path Docs/ --force

# Create the new repo and push
git remote add origin git@github.com:serbantica/ai-nanny.git
git push -u origin main

# Clean up
cd ..
rm -rf sentinel-temp
```

**Reference:** https://github.com/newren/git-filter-repo

---

## Alternative: Using git filter-branch (Legacy)

⚠️ **Warning:** `git filter-branch` is deprecated. Use `git subtree` or `git filter-repo` instead.

```bash
# For reference only - not recommended
git filter-branch --subdirectory-filter Docs -- --all
```

---

## Step 1 (Detailed): Create the New Repository

### Option A: Via GitHub Web Interface

1. Go to https://github.com/new
2. **Repository name:** `ai-nanny`
3. **Owner:** `serbantica`
4. **Description:** "AI Companion Orchestration Platform for elderly care with multi-device coordination"
5. **Visibility:** Choose Public or Private
6. **Initialize:** Do NOT initialize with README, .gitignore, or license (we'll add these)
7. Click "Create repository"

### Option B: Via GitHub CLI

```bash
gh repo create serbantica/ai-nanny --public --description "AI Companion Orchestration Platform for elderly care with multi-device coordination"
```

---

## Step 2: Set Up the New Repository Structure

After creating the repository and pushing the Docs history, you can set up the new repository structure.

```bash
# Clone the new repository
git clone git@github.com:serbantica/ai-nanny.git
cd ai-nanny

# The repository now contains the documentation from Sentinel's Docs folder
# You can reorganize or add additional structure as needed

# Create directory structure for implementation
mkdir -p core
mkdir -p dashboard/components
mkdir -p device
mkdir -p personas
mkdir -p tests
mkdir -p config

# The docs from Docs/ are now in the root
# You may want to move them to a docs/ subdirectory:
mkdir -p docs
mv *.md docs/ 2>/dev/null || true
mv *.txt docs/ 2>/dev/null || true

# Create placeholder files for implementation
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

## Step 3: Create README for New Repository

Create or update `README.md` in the ai-nanny repository:

```markdown
# AI Nanny - AI Companion Orchestration Platform

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
ai-nanny/
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

## Step 4: Create pyproject.toml for New Repository

Create `pyproject.toml`:

```toml
[project]
name = "ai-nanny"
version = "0.1.0"
description = "AI Companion Orchestration Platform for elderly care with multi-device coordination"
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

## Step 5: Create .gitignore

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

## Step 6: Initial Commit and Push

```bash
# In the ai-nanny directory
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

## Step 7: Verify Migration in Sentinel Repository

The Sentinel repository has already been updated:
- Documentation moved to `migrated/ai-nanny-docs/` staging area
- `Docs/` folder now contains only a pointer README.md
- Root README.md updated with repository separation notice

No additional cleanup needed in Sentinel - the migration is complete!

---

## Step 8: Cross-Reference Both Projects

### In Sentinel README

Already updated with repository separation section linking to `serbantica/ai-nanny`.

### In AI Nanny README

Add a reference back to Sentinel:
```markdown
## Related Projects

- [Sentinel](https://github.com/serbantica/Sentinel) - Mental health companion system (separate project)
```

---

## Step 9: Update Documentation References

In the new repository, update any references that mention "Sentinel":

```bash
# Search for Sentinel references
cd ai-nanny
grep -r "Sentinel" docs/

# Update as needed to clarify separation
```

---

## Verification Checklist

After migration, verify:

- [ ] New repository created at `serbantica/ai-nanny` and accessible
- [ ] Git history from Docs folder preserved in new repo
- [ ] All documentation from Sentinel/Docs pushed to new repo
- [ ] New repo has proper README explaining the project
- [ ] New repo has pyproject.toml with correct dependencies
- [ ] New repo has .gitignore
- [ ] New repo has initial directory structure
- [ ] Sentinel repo has migrated/ai-nanny-docs/ staging area
- [ ] Sentinel repo Docs/ folder replaced with pointer README.md
- [ ] Sentinel README updated with repository separation notice
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
4. Consult SEPARATION_NEXT_STEPS.md for detailed step-by-step instructions

---

## Next Steps After Migration

### For AI Nanny
1. Review docs/AI-Companion-Software-Dev.md for implementation plan
2. Set up development environment
3. Begin Week 1 implementation (Core Engine)

### For Sentinel
1. Continue with Sentinel_Roadmap_v2.md
2. Focus on mental health features
3. Implement security and compliance foundations

---

**Last Updated:** 2026-01-18
