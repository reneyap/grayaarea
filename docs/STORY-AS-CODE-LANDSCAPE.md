# Story as Code — What Exists in the World

> Research compiled 2026-03-02. Covers tools, practices, and communities
> treating narrative/fiction development with software engineering discipline.
> Updated 2026-03-02: Nx monorepo integration notes added.

---

## 1. Interactive Fiction Languages — Story *is* Code

Narrative scripting languages where prose and logic are the same artifact.
Compiled, tested, version-controlled.

| Tool | License | Primary Use | Link |
|------|---------|-------------|------|
| **Ink** | Open Source (MIT) | Branching narrative for games & web | https://www.inklestudios.com/ink/ |
| **Twine** | Open Source (GPL) | Nonlinear hypertext fiction | https://twinery.org/ |
| **Inform 7** | Open Source (Artistic 2.0, since 2022) | Natural-language interactive fiction | https://ganelson.github.io/inform-website/ |
| **Inform 6** | Open Source (Artistic 2.0) | Lower-level IF programming (C-like) | https://www.inform-fiction.org/ |
| **TADS 3** | Open Source (TADS License) | Text adventure development system | https://www.tads.org/ |
| **ChoiceScript** | Proprietary (Choice of Games) | Choice-based commercial IF | https://www.choiceofgames.com/make-your-own-games/choicescript-ide/ |
| **Yarn Spinner** | Open Source (MIT) | Dialogue scripting for Unity/Godot | https://yarnspinner.dev/ |
| **Ren'Py** | Open Source (MIT + LGPL) | Visual novel engine with Python scripting | https://www.renpy.org/ |
| **Articy:draft** | Proprietary | Professional narrative design (AAA games) | https://www.articy.com/ |
| **ink Unity Integration** | Open Source (MIT) | Bridge Ink ↔ Unity game engine | https://github.com/inkle/ink-unity-integration |

### Notable: Ink's IDE (Inky)
- Play-as-you-write: live preview refreshes as you type
- Error highlighting as-you-type
- Jump-to-definition on story branches (like code navigation)
- Export to JSON (compiled format) and web HTML
- https://github.com/inkle/inky

### Notable: Inform 7's Skein
- Tracks player paths as a **branching tree** — the structural equivalent of git branches for narrative
- "Blessed" transcript responses = passing tests
- Deviations highlighted on replay = regression detection
- https://ganelson.github.io/inform-website/

---

## 2. Version Control for Prose — Git on Fiction

Writers applying source control to long-form writing.

| Resource | Type | Link |
|----------|------|------|
| **Git** | Open Source (GPL-2.0) | https://git-scm.com/ |
| **GitHub** | Proprietary (free tier) — hosts many public novel repos | https://github.com/ |
| **Gwern.net methodology** | Public reference — essays under git, full linting pipeline, writing checklist as QA process | https://gwern.net/about |
| **Dendron** | Open Source (AGPL) — hierarchical Markdown note/doc system, VS Code native | https://www.dendron.so/ |
| **Obsidian** | Proprietary (free for personal) — linked Markdown vault, graph view | https://obsidian.md/ |
| **Logseq** | Open Source (AGPL) — outliner + graph, Markdown-based | https://logseq.com/ |

### Common git-for-writing patterns (community practice, no single tool):
- Branches = alternate plot timelines or POV experiments
- Commits = scene checkpoints
- Tags = draft milestones (v0.1-outline, v1.0-first-draft)
- Pull Requests = co-author review
- Issues = plot holes, continuity errors, TODO scenes
- GitHub Actions / CI = automated word count, linting, PDF build

---

## 3. Prose Linting & Quality Automation

Tools that apply code-review-style automation to writing.

| Tool | License | What It Does | Link |
|------|---------|--------------|------|
| **Vale** | Open Source (MIT) | Style linting for prose — enforce house style, flag weak words | https://vale.sh/ |
| **proselint** | Open Source (BSD) | Flags bad writing habits, anachronisms, redundancy | https://github.com/amperser/proselint |
| **write-good** | Open Source (MIT) | Flags passive voice, weasel words, adverb overuse | https://github.com/btford/write-good |
| **alex** | Open Source (MIT) | Flags insensitive language | https://alexjs.com/ |
| **LanguageTool** | Open Source core (LGPL); cloud tier proprietary | Grammar, style, consistency | https://languagetool.org/ |
| **Grammarly** | Proprietary | Grammar + style AI suggestions | https://www.grammarly.com/ |
| **Hemingway App** | Proprietary (free web version) | Readability scoring | https://hemingwayapp.com/ |

---

## 4. Docs-as-Code / Writing-as-Code Publishing Pipelines

Treating prose manuscripts like software deliverables — built, versioned, published.

| Tool | License | Link |
|------|---------|------|
| **Pandoc** | Open Source (GPL-2.0) | Universal document converter — Markdown → PDF, EPUB, DOCX, HTML | https://pandoc.org/ |
| **Quarto** | Open Source (MIT) | Scientific/narrative publishing system built on Pandoc | https://quarto.org/ |
| **Bookdown** | Open Source (GPL-3.0) | R Markdown → book (PDF, EPUB, HTML) | https://bookdown.org/ |
| **Sphinx** | Open Source (BSD) | Docs-as-code engine, used for books too | https://www.sphinx-doc.org/ |
| **mdBook** | Open Source (MPL-2.0) | Markdown → book website (Rust toolchain) | https://rust-lang.github.io/mdBook/ |
| **Asciidoctor** | Open Source (MIT) | Rich markup language for books + technical docs | https://asciidoctor.org/ |
| **O'Reilly Atlas** | Proprietary | Professional book publishing on git-backed Asciidoc/Markdown | https://atlas.oreilly.com/ |
| **Leanpub** | Proprietary (free tier) | Markdown → self-published book with live preview | https://leanpub.com/ |

### CI/CD for writing (community patterns):
- GitHub Actions with Pandoc to auto-build PDF/EPUB on every commit
- Word count tracking per commit (narrative velocity)
- Automated chapter structure validation

---

## 5. Narrative Design Tools (Professional Game Studios)

How AAA and indie studios manage story as engineering.

| Tool | License | Link |
|------|---------|------|
| **Articy:draft 3** | Proprietary | Full narrative editor: flowcharts, dialogue, variables, exported to game engine | https://www.articy.com/ |
| **Twine** (also used by studios) | Open Source (GPL) | https://twinery.org/ |
| **Dialogic (Godot plugin)** | Open Source (MIT) | Visual dialogue system for Godot | https://github.com/dialogic-godot/dialogic |
| **Ink + Unity** | Open Source (MIT) | Industry-standard branching narrative in Unity games | https://github.com/inkle/ink-unity-integration |
| **ChatMapper** | Proprietary | NPC dialogue tree design tool | https://www.chatmapper.com/ |
| **Machinations** | Proprietary (free tier) | Game system design (not narrative-specific, but used for pacing/economy modeling) | https://machinations.io/ |

---

## 6. World-Building & Story Bible Management

Organizing lore, canon, and continuity — the "source of truth" problem.

| Tool | License | Link |
|------|---------|------|
| **World Anvil** | Proprietary (free tier) | World-building wiki with timeline, genealogy, maps | https://www.worldanvil.com/ |
| **Campfire** | Proprietary (free tier) | Characters, timelines, maps for fiction writers | https://www.campfirewriting.com/ |
| **Notion** | Proprietary (free tier) | General-purpose wiki used by many writers as story bibles | https://www.notion.so/ |
| **Obsidian** | Proprietary (free for personal) | Local Markdown vault — no vendor lock-in | https://obsidian.md/ |
| **TiddlyWiki** | Open Source (BSD) | Self-contained single-file wiki, highly portable | https://tiddlywiki.com/ |
| **WikiJS** | Open Source (AGPL) | Self-hosted wiki with git backend | https://js.wiki/ |

---

## 7. Fiction-Specific Writing Environments

IDEs built specifically for long-form prose.

| Tool | License | Link |
|------|---------|------|
| **Scrivener** | Proprietary | Industry-standard for novelists: cork board, outliner, compile to manuscript | https://www.literatureandlatte.com/scrivener |
| **Ulysses** | Proprietary (subscription, macOS/iOS only) | Markdown-first, distraction-free, library management | https://ulysses.app/ |
| **iA Writer** | Proprietary (one-time purchase) | Minimal Markdown editor, focus mode | https://ia.net/writer |
| **VS Code** | Open Source (MIT) | General code editor used by developers writing prose in Markdown | https://code.visualstudio.com/ |
| **Manuskript** | Open Source (GPL-3.0) | Open-source Scrivener alternative | https://www.theologeek.ch/manuskript/ |
| **novelWriter** | Open Source (GPL-3.0) | Markdown-based, built for long-form fiction, minimal | https://novelwriter.io/ |

---

## Summary: Open Source vs Proprietary

| Category | Best Open Source Option | Best Proprietary Option |
|---|---|---|
| Narrative scripting | Ink (MIT) | ChoiceScript |
| Version control | Git + GitHub | — |
| Prose linting | Vale (MIT) | Grammarly |
| Publishing pipeline | Pandoc + Quarto | O'Reilly Atlas |
| World-building | TiddlyWiki / Obsidian | World Anvil |
| Writing IDE | novelWriter / Manuskript | Scrivener |
| Narrative design | Yarn Spinner | Articy:draft |

---

## 8. Nx Monorepo — Integration Map

**Nx** (Open Source, MIT) — https://nx.dev

Nx manages a monorepo of apps and libraries with cacheable task pipelines.
First-class plugins exist for Next.js and Expo; any CLI tool can be wrapped as an `exec` target.

### Monorepo layout

```
GrayArea/
  apps/
    web/          ← Next.js 15            @nx/next
    mobile/       ← Expo 52              @nx/expo
    mcp/          ← MCP stdio server     @nx/node
  libs/
    db/           ← Supabase client + generated types
    ai/           ← OpenAI helpers (embed, consistency)
    story-types/  ← shared TypeScript interfaces
  tools/
    import/       ← import-topics.ts, embed-topics.ts
    scripts/      ← one-off data scripts
  .vale/          ← Vale config + style rules
```

### Tools from Section 1–7 that slot directly into Nx targets

| Tool | Nx target | Command | Notes |
|------|-----------|---------|-------|
| **Vale** | `nx run web:lint-prose` | `vale apps/web/content/**/*.md` | Add `.vale.ini` at root; runs in CI with `nx affected` |
| **write-good** | `nx run web:writegood` | `npx write-good apps/web/content/**/*.md` | npm package — zero extra install friction |
| **proselint** | `nx run web:proselint` | `proselint apps/web/content/**/*.md` | Python dep; run in Docker CI step if not locally installed |
| **Pandoc** | `nx run web:build-manuscript` | `pandoc 0301/*.md -o dist/manuscript.pdf` | wraps as shell exec target; cacheable by Nx |
| **Quarto** | `nx run web:build-quarto` | `quarto render` | replaces Pandoc if richer output needed |
| **mdBook** | `nx run docs:build` | `mdbook build` | optional: publish story bible as static site |

### Nx plugins to install

```bash
npx nx init                         # adds Nx to existing workspace
npx nx add @nx/next                 # Next.js plugin
npx nx add @nx/expo                 # Expo plugin
npx nx add @nx/node                 # Node apps (MCP server)
```

### Nx + GitHub Actions (CI)

```yaml
# .github/workflows/ci.yml
- name: Nx affected
  run: npx nx affected -t lint lint-prose build test --parallel=3
```

`nx affected` only runs tasks on code that changed since the last commit — identical to how code CI works, now applied to prose and story logic together.

### What does NOT fit Nx (and why)

| Tool | Reason |
|------|--------|
| **Scrivener / Ulysses** | Closed binary editors — no CLI, no scriptable output |
| **World Anvil / Campfire** | Cloud-only, no local files to target |
| **Articy:draft** | No headless mode; export-only workflow |
| **Inform 7** | Possible via headless compile CLI, but adds Inform toolchain to CI — not worth it for this project |

---

*Sources: direct tool documentation, gwern.net methodology writeup, inklestudios.com, twinery.org, Wikipedia (Inform), ifdb.org community, nx.dev documentation.*
