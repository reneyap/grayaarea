# GrayArea

> **Book 1 of a sci-fi novel series** — developed as a software project.
>
> A story about consciousness, survival, and the gray area between human and machine.

---

## Repository Structure

- `book1/`   — chapter and scene files (Markdown)
- `lore/`    — canonical data (glossary, timeline, characters)
- `docs/`    — architecture, research, templates
- `tools/`   — import and build scripts
- `archive/` — prior drafts and bulk imports (kept for reference)

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Web app | Next.js 15 |
| Mobile app | Expo 52 |
| Database | Supabase (Postgres + pgvector) |
| Language | TypeScript |
| AI | OpenAI API (GPT-4o + text-embedding-3-small) |
| AI client integration | MCP (`@modelcontextprotocol/sdk`) |
| Monorepo | Nx (`@nx/next` · `@nx/expo` · `@nx/node`) |
| Scripts | bash · Python · Node.js · ts-node |

> Cross-platform: Windows / Mac / Linux. No PowerShell dependencies.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the full design including Supabase schema, TypeScript interfaces, import scripts, and MCP server spec.

See [`docs/DIGITAL_STRATIGRAPHY.md`](docs/DIGITAL_STRATIGRAPHY.md) for the Digital Stratigraphy concept and repository organization philosophy.

---

## Development Approach

This project treats a literary novel as a software project:

- **Lore as data** — 83 canon topic files importable into Supabase
- **Chapters as files** — version-controlled Markdown, one file per chapter
- **Canon as a locked key-value store** — queryable, diffable, AI-checkable
- **Consistency via AI** — GPT-4o structured output validates character voice and timeline integrity
- **Semantic search** — pgvector embeddings on all topic files
- **MCP server** — exposes story bible to AI assistants (Claude, Cursor)

See [`docs/STORY-AS-CODE-LANDSCAPE.md`](docs/STORY-AS-CODE-LANDSCAPE.md) for a survey of story-as-code tooling and how this stack compares.

---

## Conventional Commits

This repo uses [Conventional Commits](https://www.conventionalcommits.org/).

```
feat(book1):     new chapter content or story additions
fix(lore):       canon corrections
docs(tools):     architecture / research documents
chore(tools):    scripts, tooling, config
refactor(book1): restructuring chapters or outline (no content change)
style(book1):    prose edits, formatting
```

---

## Status

- [ ] lore topic files extracted and organized
- [ ] chapter stubs created (Book 1 TOC)
- [ ] Architecture designed (web + mobile + AI + MCP)
- [ ] Nx monorepo scaffold
- [ ] Supabase schema + import pipeline
- [ ] Next.js web app
- [ ] MCP server
- [ ] Expo mobile app
