# Separation Next Steps: Creating the AI Nanny Repository

This document provides exact, step-by-step instructions for completing the repository separation and creating the new `serbantica/ai-nanny` repository.

## Prerequisites

✅ Documentation has been copied to `migrated/ai-nanny-docs/`  
✅ `Docs/` folder replaced with pointer README.md  
✅ Root README.md updated with separation notice  
✅ MIGRATION_GUIDE.md includes git subtree commands  

## Current Status

The Sentinel repository is ready for separation. All documentation is staged in `migrated/ai-nanny-docs/` and the Docs folder has been cleaned up.

---

## Step-by-Step Migration Process

### Step 1: Create the New GitHub Repository

#### Option A: Via GitHub Web Interface

1. **Open your browser** and go to: https://github.com/new
2. **Fill in repository details:**
   - Owner: `serbantica`
   - Repository name: `ai-nanny`
   - Description: `AI Companion Orchestration Platform for elderly care with multi-device coordination`
   - Visibility: Choose **Public** or **Private** based on your preference
   - **DO NOT** check "Initialize this repository with a README"
   - **DO NOT** add .gitignore or license yet
3. **Click "Create repository"**
4. **Keep the page open** - you'll need the repository URL for the next steps

#### Option B: Via GitHub CLI (faster)

```bash
gh repo create serbantica/ai-nanny \
  --public \
  --description "AI Companion Orchestration Platform for elderly care with multi-device coordination"
```

**Checkpoint:** Repository `serbantica/ai-nanny` should now exist (but be empty).

---

### Step 2: Extract Docs History Using Git Subtree

This preserves the commit history of the Docs folder.

```bash
# Navigate to your Sentinel repository
cd /path/to/Sentinel

# Ensure you're on the main branch and up to date
git checkout main
git pull origin main

# Create a new branch containing only the Docs folder history
# This may take a minute depending on repository size
git subtree split -P Docs -b ai-nanny-docs

# Verify the branch was created and contains the Docs files
git log ai-nanny-docs --oneline -5
git ls-tree ai-nanny-docs
```

**Expected output:** You should see the Docs files in the root of the `ai-nanny-docs` branch.

**Checkpoint:** Branch `ai-nanny-docs` created with Docs history.

---

### Step 3: Add Remote and Push to New Repository

```bash
# Add the new repository as a remote
# Use SSH if you have SSH keys configured, otherwise use HTTPS
git remote add ai-nanny git@github.com:serbantica/ai-nanny.git

# Verify the remote was added
git remote -v | grep ai-nanny

# Push the ai-nanny-docs branch to the new repository's main branch
git push ai-nanny ai-nanny-docs:main

# Verify the push was successful
git ls-remote ai-nanny
```

**Checkpoint:** The new repository should now contain all the Docs files with their commit history intact.

**Verify on GitHub:** Go to https://github.com/serbantica/ai-nanny and confirm the files are there.

---

### Step 4: Clone and Set Up the New Repository

```bash
# Clone the new repository to work on it
cd /path/to/your/projects
git clone git@github.com:serbantica/ai-nanny.git
cd ai-nanny

# Verify the files are present
ls -la

# The files from Docs/ are now in the root
# You may want to reorganize them into a docs/ subdirectory
mkdir -p docs
mv *.md docs/ 2>/dev/null || true
mv *.txt docs/ 2>/dev/null || true

# Create the project structure
mkdir -p core
mkdir -p dashboard/components
mkdir -p device
mkdir -p personas
mkdir -p tests
mkdir -p config

# Create placeholder Python files
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

### Step 5: Create Essential Repository Files

#### Create README.md

```bash
cat > README.md << 'EOF'
# AI Nanny - AI Companion Orchestration Platform

Cloud-native orchestration engine enabling multi-persona AI companions with multi-device coordination for elderly care and assisted living facilities.

## Overview

This platform enables:
- **Runtime persona switching** (<2 seconds)
- **Multi-device coordination** (synchronous, handoff, group activities)
- **Edge-cloud hybrid architecture** (Raspberry Pi + cloud control plane)
- **B2B licensing model** for device manufacturers and care facilities

## Documentation

See the `docs/` directory for detailed documentation migrated from the Sentinel repository:
- Architecture and design documents
- Implementation guides
- Business model and use cases

## Project Structure

```
ai-nanny/
├── core/                    # Core orchestration engine
├── dashboard/               # Streamlit demo dashboard
├── device/                  # Raspberry Pi runtime
├── personas/                # Persona definition files
├── tests/                   # Test suite
├── config/                  # Configuration files
└── docs/                    # Documentation
```

## Related Projects

- [Sentinel](https://github.com/serbantica/Sentinel) - Mental health companion system (separate project)

## Current Status

**Phase:** Planning & Architecture  
**Next Steps:** Core engine implementation

## Getting Started

(To be added as implementation progresses)

---

**Repository separated from Sentinel on:** 2026-01-18
EOF
```

#### Create pyproject.toml

```bash
cat > pyproject.toml << 'EOF'
[project]
name = "ai-nanny"
version = "0.1.0"
description = "AI Companion Orchestration Platform for elderly care"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "fastapi",
    "uvicorn[standard]",
    "anthropic",
    "openai",
    "pydantic",
    "python-dotenv",
    "redis",
    "pyyaml",
    "streamlit",
    "paho-mqtt",
]

[project.optional-dependencies]
device = [
    "RPi.GPIO",
    "pyaudio",
    "speech_recognition",
    "elevenlabs",
]

[tool.uv]
dev-dependencies = [
    "pytest",
    "black",
    "ruff",
]
EOF
```

#### Create .gitignore

```bash
cat > .gitignore << 'EOF'
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
EOF
```

---

### Step 6: Commit and Push Initial Structure

```bash
# Stage all new files
git add .

# Create a comprehensive commit
git commit -m "Set up initial project structure" \
           -m "- Reorganized documentation into docs/ subdirectory" \
           -m "- Added core module structure" \
           -m "- Added dashboard and device runtime placeholders" \
           -m "- Created README with project overview" \
           -m "- Added pyproject.toml with dependencies" \
           -m "- Added .gitignore" \
           -m "" \
           -m "Documentation migrated from Sentinel repository with history preserved."

# Push to the main branch
git push origin main
```

**Checkpoint:** The new repository is now fully set up with structure and documentation.

---

### Step 7: Configure Repository Settings

1. **Go to repository settings:** https://github.com/serbantica/ai-nanny/settings
2. **Set up branch protection** (recommended):
   - Go to "Branches" → "Add branch protection rule"
   - Branch name pattern: `main`
   - Enable: "Require a pull request before merging"
3. **Add topics/tags** for discoverability:
   - Go to repository main page
   - Click the gear icon next to "About"
   - Add topics: `ai`, `elderly-care`, `orchestration`, `multi-device`, `persona`, `iot`
4. **Add a description** if not already set:
   - "AI Companion Orchestration Platform for elderly care with multi-device coordination"

---

### Step 8: Clean Up Sentinel Repository (Local)

```bash
# Go back to Sentinel repository
cd /path/to/Sentinel

# Remove the temporary branch (optional)
git branch -D ai-nanny-docs

# Remove the ai-nanny remote (optional)
git remote remove ai-nanny

# Verify Sentinel is clean
git status
```

**Checkpoint:** Sentinel repository is clean and the ai-nanny repository is fully set up.

---

### Step 9: Optional - Transfer Issues

If there are any issues in Sentinel that relate to the AI Nanny project:

1. **Identify relevant issues** in Sentinel repository
2. **Create new issues** in ai-nanny repository
3. **Reference the original issue** in the new issue description
4. **Close original issues** in Sentinel with a note pointing to the new repository
5. **Example close message:**
   ```
   Closing as this relates to the AI Nanny project which has been 
   separated into its own repository: https://github.com/serbantica/ai-nanny
   
   Tracking issue created at: serbantica/ai-nanny#X
   ```

---

### Step 10: Optional - Archive Documentation in Sentinel

If you want to remove the `migrated/ai-nanny-docs/` folder from Sentinel after confirming the migration:

```bash
cd /path/to/Sentinel

# Only do this after verifying ai-nanny repository is complete
git rm -r migrated/ai-nanny-docs/

git commit -m "Remove migrated ai-nanny docs staging area" \
           -m "Documentation has been successfully migrated to serbantica/ai-nanny"

git push origin main
```

**Note:** Keep this folder for now as a backup until you're confident the migration is complete.

---

## Verification Checklist

After completing all steps, verify:

- [ ] Repository `serbantica/ai-nanny` exists and is accessible
- [ ] All files from `Sentinel/Docs/` are in `ai-nanny/docs/`
- [ ] Git history is preserved (check with `git log docs/`)
- [ ] README.md explains the project clearly
- [ ] pyproject.toml has all necessary dependencies
- [ ] .gitignore is present and appropriate
- [ ] Project structure (core/, dashboard/, device/) is created
- [ ] Repository settings configured (description, topics, branch protection)
- [ ] Both repositories cross-reference each other
- [ ] Sentinel repository Docs/ folder contains pointer README.md
- [ ] Sentinel README.md updated with separation notice
- [ ] DOCS_ANALYSIS.md remains in Sentinel for context

---

## Troubleshooting

### Issue: "git subtree split" is slow or hanging

**Solution:** This is normal for large repositories. Wait for it to complete. For very large repositories (>10k commits), consider using `git filter-repo` instead (see MIGRATION_GUIDE.md).

### Issue: "Permission denied" when pushing

**Solution:** 
1. Verify you have write access to serbantica/ai-nanny
2. Check your SSH keys are configured: `ssh -T git@github.com`
3. Try HTTPS instead: `git remote set-url ai-nanny https://github.com/serbantica/ai-nanny.git`

### Issue: Files not showing in new repository

**Solution:**
1. Verify the push was successful: `git ls-remote ai-nanny`
2. Check you pushed to the correct branch: `git push ai-nanny ai-nanny-docs:main`
3. Refresh the GitHub page (hard refresh with Ctrl+Shift+R)

### Issue: Lost commit history

**Solution:**
1. Verify history in the branch: `git log ai-nanny-docs`
2. If history is missing, re-run `git subtree split -P Docs -b ai-nanny-docs-v2`
3. Push the new branch: `git push ai-nanny ai-nanny-docs-v2:main --force`

---

## Timeline

- **Step 1-3:** 5-10 minutes (repository creation and push)
- **Step 4-6:** 15-20 minutes (setup and initial commit)
- **Step 7:** 5 minutes (settings)
- **Step 8-10:** 10-15 minutes (cleanup and verification)

**Total:** ~45-60 minutes

---

## Next Steps After Completion

### For AI Nanny Repository
1. Review documentation in `docs/` directory
2. Begin implementing core orchestration engine
3. Set up CI/CD pipeline
4. Create initial milestones and project board

### For Sentinel Repository
1. Focus on mental health features per Sentinel_Roadmap_v2.md
2. Continue development without AI Nanny distractions
3. Reference ai-nanny repository in related discussions

---

## Support

If you encounter issues not covered in troubleshooting:
1. Check MIGRATION_GUIDE.md for additional context
2. Review DOCS_ANALYSIS.md for background on the separation decision
3. Consult git documentation for subtree: https://git-scm.com/docs/git-subtree

---

**Document Created:** 2026-01-18  
**Target Repository:** https://github.com/serbantica/ai-nanny  
**Source Repository:** https://github.com/serbantica/Sentinel
