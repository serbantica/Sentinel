# LinkedInPost Repository Setup Guide

This document provides step-by-step instructions for creating the private `serbantica/LinkedInPost` repository on GitHub and migrating the staged files from this directory.

## Prerequisites

- GitHub account with owner access to `serbantica`
- Git and GitHub CLI installed
- SSH keys configured (or HTTPS access)

---

## Step 1: Create the Private GitHub Repository

### Option A: Via GitHub Web Interface

1. Open your browser and go to: https://github.com/new
2. Fill in repository details:
   - **Owner:** `serbantica`
   - **Repository name:** `LinkedInPost`
   - **Description:** `AI-powered LinkedIn post generator`
   - **Visibility:** **Private**
   - **DO NOT** check "Initialize this repository with a README"
3. Click **"Create repository"**

### Option B: Via GitHub CLI (faster)

```bash
gh repo create serbantica/LinkedInPost \
  --private \
  --description "AI-powered LinkedIn post generator"
```

**Checkpoint:** Repository `serbantica/LinkedInPost` should now exist (but be empty).

---

## Step 2: Initialize and Push the Staged Files

The project files are staged in `LinkedInPost/` within this repository. Run the following from the Sentinel root:

```bash
# Copy staged files to a temporary working directory
cp -r LinkedInPost/ /tmp/LinkedInPost-init
cd /tmp/LinkedInPost-init

# Initialize a git repository
git init
git add .
git commit -m "Initial project structure"

# Add the remote and push
git remote add origin git@github.com:serbantica/LinkedInPost.git
git branch -M main
git push -u origin main
```

**Checkpoint:** The new repository should now contain the initial project files.

**Verify on GitHub:** Go to https://github.com/serbantica/LinkedInPost and confirm the files are there.

---

## Step 3: Configure Repository Settings

1. **Go to repository settings:** https://github.com/serbantica/LinkedInPost/settings
2. **Confirm visibility** is set to **Private**
3. **Set up branch protection** (recommended):
   - Go to "Branches" → "Add branch protection rule"
   - Branch name pattern: `main`
   - Enable: "Require a pull request before merging"
4. **Add topics/tags** for discoverability (within your org):
   - Go to repository main page → gear icon next to "About"
   - Add topics: `ai`, `linkedin`, `content-generation`, `openai`, `python`

---

## Step 4: Set Up Local Development

```bash
# Clone the repository
git clone git@github.com:serbantica/LinkedInPost.git
cd LinkedInPost

# Install dependencies
uv sync

# Configure environment
cp config/.env.example config/.env
# Edit config/.env with your OPENAI_API_KEY
```

---

## Verification Checklist

- [ ] Repository `serbantica/LinkedInPost` exists and is **Private**
- [ ] All files from `Sentinel/LinkedInPost/` are in the new repository
- [ ] `README.md` explains the project clearly
- [ ] `pyproject.toml` has all necessary dependencies
- [ ] `.gitignore` is present and appropriate
- [ ] Project structure (`core/`, `api/`, `tests/`) is in place
- [ ] Repository visibility confirmed as **Private**
- [ ] Branch protection configured

---

**Document created:** 2026-03-28  
**Target repository:** https://github.com/serbantica/LinkedInPost (private)  
**Source staging area:** `Sentinel/LinkedInPost/`
