# Story-as-Code — Consolidated Landscape

Research compiled 2026-03. This file consolidates the detailed deep-research notes and the shorter landscape document into a single, de-duplicated reference for the GrayArea project.

Executive summary
-----------------
Story-as-code applies software engineering primitives (plain-text source, schemas, version control, deterministic builds, automated QA) to long-form fiction. For trilogy-scale work the core challenge is continuity at scale: a linear manuscript plane (chapters/scenes) plus a graph/bible plane (canon, timelines, glossary) is the most practical architecture.

Top recommended stacks
----------------------
- Stack A (portability): Git + Markdown (Pandoc dialect) + Pandoc + CI + Vale/cspell + pre-commit.
- Stack B (writer UX): novelWriter/Manuskript + git + Pandoc export pipeline.
- Stack C (bible): TiddlyWiki or Wiki.js + structured YAML/JSON + static site (Hugo/MkDocs) for publishing the canon.

Key concepts
------------
- Manuscript plane: one file per chapter/scene (Markdown).
- Canon plane: YAML/JSON fronted datasets (characters.yml, timeline.yml, glossary.yml).
- CI & QA: enforce linting, link checks, and deterministic exports on each commit.

High-level inventory (condensed)
--------------------------------
- Narrative scripting & branching: Ink (MIT), Twine (GPL), Yarn Spinner (MIT). Useful for branching prototypes and dialogue tooling.
- Publishing/build: Pandoc (GPL-2.0), Quarto (MIT), mdBook, Sphinx, Asciidoctor.
- Linting & QA: Vale (MIT), proselint, write-good, LanguageTool, pre-commit hooks.
- Worldbuilding/bible: TiddlyWiki (BSD), Wiki.js (AGPL), Obsidian (local vault), World Anvil (proprietary).
- Editors/IDEs: VS Code, novelWriter, Manuskript, Scrivener (proprietary).
- Visualization & data: Mermaid, Graphviz, TimelineJS, Leaflet + GeoJSON for maps; Datasette for queryable datasets.

Practical recommendations for GrayArea
------------------------------------
- Keep canonical sources in plain text under `book1/`, `lore/`, and `docs/`.
- Use Pandoc Markdown as the primary dialect and run the same engine locally and in CI to avoid dialect drift.
- Store canonical data in `lore/glossary.yml`, `lore/timeline.yml`, `lore/characters.yml` and render views with a static site.
- Use Vale + cspell in CI via `pre-commit` to catch style and spelling issues before merge.

Minimal repo layout (recommended)
---------------------------------
GrayArea/
  README.md
  book1/            ← chapters and scenes (one file per scene)
  lore/             ← YAML/JSON canonical data (glossary, timeline, characters)
  docs/             ← architecture, research, templates
  tools/            ← import scripts, build scripts
  archive/          ← prior drafts and bulk imports

CI and build pattern
--------------------
- Pre-commit hooks: runs Vale, cspell, and lightweight checks.
- CI pipeline: `lint -> build -> artifact` (Pandoc/Quarto to EPUB/PDF/HTML). Use pinned tool versions.
- Artefacts: store PDF/EPUB builds and canonical JSON exports for the bible.

Migration and interoperability notes
-----------------------------------
- Prefer plain-text formats; avoid binary project formats that lock content.
- Standardize on front matter (YAML) and validate it in CI.
- Use Pandoc filters (AST) as the primary migration/normalization mechanism.

Licensing and community health
------------------------------
- Tooling licenses vary; manuscript text remains your copyright. License scripts and templates permissively when possible (MIT/BSD) to ease reuse.
- Check project maintenance (release cadence, docs, issue activity) before depending on a tool in CI.

Nx monorepo notes (how this fits GrayArea)
-----------------------------------------
- Nx maps naturally to the monorepo approach: apps (web, mobile, mcp), libs (db, ai, story-types), tools (import, build).
- Wrap Vale, Pandoc, and build steps as `nx` exec targets for cacheable CI runs.

Next steps
----------
- Decide on the primary Markdown dialect (recommend Pandoc Markdown) and add a `docs/STYLE.md` describing front matter and file conventions.
- Add `pre-commit` with Vale and cspell configs.
- Build a simple `nx` target or GitHub Action that produces an EPUB from `book1/` to validate the pipeline.

Sources & further reading
-------------------------
This consolidation draws from the deeper research file `docs/deep-research/story-as-code-landscape.md` and other community sources (Pandoc, Vale, Ink, Nx docs). The deep-research file is kept as an archive for reference.
