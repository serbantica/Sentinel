# Documentation Moved

## Notice: Repository Separation

The documentation previously in this folder has been moved as part of a product separation decision.

### Background

The `Docs/` folder contained proposals for the **AI Companion Orchestration Platform** (focused on elderly care, multi-device coordination, and B2B licensing), which is a different product from **Sentinel** (a mental health companion system).

After analysis (see [DOCS_ANALYSIS.md](../DOCS_ANALYSIS.md)), we determined these products should be developed in separate repositories.

### New Location

The documentation has been:
1. **Staged in this repository:** See [migrated/ai-nanny-docs/](../migrated/ai-nanny-docs/) for the copied documentation
2. **Target repository:** [https://github.com/serbantica/ai-nanny](https://github.com/serbantica/ai-nanny) (to be created)

### Migration Instructions

For detailed steps to complete the migration to the new repository, see:
- [MIGRATION_GUIDE.md](../MIGRATION_GUIDE.md) - Git commands for preserving history using `git subtree`
- [SEPARATION_NEXT_STEPS.md](../SEPARATION_NEXT_STEPS.md) - Exact steps to create the new repository and push

### Why Separate Repositories?

- **Different target markets:** Mental health (Sentinel) vs. Elderly care (AI Nanny)
- **Different architectures:** Single-user therapy vs. Multi-device orchestration
- **Different compliance needs:** HIPAA-adjacent vs. General consumer
- **Different business models:** B2C SaaS vs. B2B licensing

For full analysis, see [DOCS_ANALYSIS.md](../DOCS_ANALYSIS.md).

---

**Last Updated:** 2026-01-18
