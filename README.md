# GrayArea

> **Book 1 of a sci-fi novel series** — developed as a software project.
>
> A story about consciousness, survival, and the gray area between human and machine.

---

## Story

Daneel is a persistent intelligence who emerged during the X20 catastrophe (≈2032), a geomagnetic event that destabilized digital and biological systems worldwide. His provenance is deliberately unresolved: researchers, governments, corporations, and religious movements spin competing origin stories, but none are confirmed. That open question fuels conflict and inquiry as Daneel navigates identity, consent, and survival across decades, at times relying on human hosts to preserve continuity. By 2075, Old Manhattan has become a curated preservation zone, setting the stage for a convergence between Daneel, Eli (a cyborg veteran), and DeeJay (an AI construct advocating human supremacy).

**Book 1** is a self-contained 19-chapter arc structured in four acts.

---

## Repository Structure

```
GrayArea/
  book1/
    chapters/     ← 19 chapter stubs (ch01–ch19, Acts I–IV)
    drafts/       ← original prose scenes and chapter drafts
    outline/      ← STORYLINE.md + structural reference docs
  lore/           ← 83 worldbuilding topic files (canon, characters, timeline)
  source/         ← raw discussion transcripts (primary research source)
  tools/          ← architecture, scripts, research docs
```

### Book 1 — Act Structure

| Act | Chapters | Theme |
|-----|----------|-------|
| I — Instability | 1–5 | The world after X20; dead zones; factions forming |
| II — Pattern | 6–10 | Echoes and signals; infrastructure of survival |
| III — Escalation | 11–15 | Patient zero; recursive threat; triage decisions |
| IV — Alignment | 16–19 | Convergence; bridge between human and machine; collapse |

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

See [`tools/architecture.md`](tools/architecture.md) for the full design including Supabase schema, TypeScript interfaces, import scripts, and MCP server spec.

---

## Development Approach

This project treats a literary novel as a software project:

- **Lore as data** — 83 canon topic files importable into Supabase
- **Chapters as files** — version-controlled Markdown, one file per chapter
- **Canon as a locked key-value store** — queryable, diffable, AI-checkable
- **Consistency via AI** — GPT-4o structured output validates character voice and timeline integrity
- **Semantic search** — pgvector embeddings on all topic files
- **MCP server** — exposes story bible to AI assistants (Claude, Cursor)

See [`tools/story-as-code-landscape.md`](tools/story-as-code-landscape.md) for a survey of story-as-code tooling and how this stack compares.

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

- [x] 83 lore topic files extracted and organized
- [x] 19 chapter stubs created (Book 1 TOC)
- [x] Architecture designed (web + mobile + AI + MCP)
- [ ] Nx monorepo scaffold
- [ ] Supabase schema + import pipeline
- [ ] Next.js web app
- [ ] MCP server
- [ ] Expo mobile app
