GrayArea — novel-as-code baseline

GrayArea is Book 1 of a sci-fi novel series treated as a software project:
manuscript content in Markdown, a queryable world-bible, and reproducible
builds (EPUB/PDF/HTML) driven by CI.

Quick links
- Architecture & integration: docs/ARCHITECTURE.md
- Story-as-code landscape: docs/STORY-AS-CODE-LANDSCAPE.md
- Repository organization: docs/DIGITAL_STRATIGRAPHY.md

Layout
- `book1/`   — chapter and scene files (Markdown)
- `lore/`    — canonical data (glossary, timeline, characters)
- `docs/`    — architecture, research, templates
- `tools/`   — import and build scripts
- `archive/` — prior drafts and bulk imports (kept for reference)

Next steps
- Run `pre-commit` setup (Vale, cspell) and install Pandoc locally.
- Build a test EPUB from `book1/` to validate the pipeline.

See `docs/` for full guidance.

