# Open-Source Story-as-Code Landscape for Writing a Science-Fiction Trilogy

## Executive summary

“Story-as-code” applies software engineering primitives—plain-text source, explicit schemas, deterministic builds, automated quality checks, and collaborative review—to narrative production. The ecosystem is not a single platform so much as an interoperability “stack”: (a) human-friendly authoring formats (most commonly Markdown-family text), (b) structured metadata (YAML/TOML/JSON), (c) version control (git), (d) automation/CI for exports (Pandoc/Quarto/LaTeX/HTML→PDF engines), and (e) people and communities that have already hardened these patterns (Docs-as-Code, interactive fiction, publishing tooling). citeturn21search0turn21search1turn21search10turn22search11turn0file0

Across open-source projects with demonstrated recent activity (roughly March 2024–March 2026), the most robust “novel-ready” center of gravity is **Markdown + Pandoc + git + CI** because it gives you (1) durable, tool-agnostic source files, (2) multi-format export (EPUB/PDF/HTML/DOCX) from one source, and (3) a composable automation story via filters/linting and build pipelines. citeturn5search2turn21search10turn23search3turn0file0

For **science-fiction series work**, the core technical design challenge isn’t drafting—it’s *continuity at scale*: controlled vocabularies (alien terms, starship classes), canonical timelines, and cross-book dependencies. The strongest open-source pattern is therefore a **two-plane architecture**:  
- a **linear manuscript plane** (Book 1 chapters/scenes, edited primarily as text), and  
- a **graph/bible plane** (“source of truth” for lore, characters, factions, tech rules, chronology), ideally queryable and renderable. citeturn0file0turn10search4turn16search5turn16search3

Top recommendations (expanded later) prioritize portability and trilogy-scale maintainability:  
- **Stack A: Git + Markdown (CommonMark/Pandoc Markdown) + Pandoc + CI + Vale/cspell/codespell + optional Calibre** (max portability; best “one source, many outputs”). citeturn21search0turn21search10turn26search21turn18search2turn18search1turn0search1turn0search3  
- **Stack B: novelWriter or Manuskript for scene/structure UX + git-backed plaintext + Pandoc build/export** (writer-centric UI without abandoning “as-code” invariants). citeturn0file0turn13search12turn13search14turn21search10  
- **Stack C: TiddlyWiki or Wiki.js as the world-bible backbone + structured YAML/JSON datasets + static publishing (Hugo/MkDocs/Docusaurus) + manuscript pipeline** (best continuity tooling and “living bible” publishing). citeturn6search0turn10search4turn3search7turn3search3

## Landscape inventory and comparison

This inventory emphasizes open-source projects that (a) are clearly identifiable as open-source (license stated on official site/repo) and (b) show visible signs of recent activity or sustained maintenance in the last two years (recent releases, ongoing issue activity, or explicit maintenance posture). Where a tool is widely used but not actively releasing, it is flagged accordingly. citeturn23search10turn0search2turn6search2turn6search4turn6search0turn0file0

A compact, category-level inventory (non-exhaustive but broad across the “story-as-code” stack):

**Manuscript drafting and fiction-focused IDEs (open-source options)**  
novelWriter; Manuskript; plus general-purpose code editors used for prose-as-code (VS Code, etc.). citeturn0file0turn13search12turn13search14turn26search19

**World-bible / knowledge-base backends (open-source options)**  
TiddlyWiki (single-file wiki, portable); Wiki.js (self-hosted wiki, supports git-backed workflows); Logseq (graph/outliner). citeturn10search4turn6search0turn6search1turn0file0

**Publishing pipelines and book builders (open-source options)**  
Pandoc; Quarto; bookdown; Sphinx; mdBook; Asciidoctor; plus static-site generators that can publish a “series bible” website (Hugo, MkDocs, Docusaurus, Eleventy, Jekyll, HonKit). citeturn5search2turn1search1turn17search13turn3search4turn3search18turn2search0turn3search7turn3search3turn3search1turn3search5turn3search14turn4search3

**Narrative scripting / branching-story engines (open-source options)**  
Ink (+ Inky); Twine (plus specs and the Twee 3 text format); Yarn Spinner; Inform; Ren’Py. Even if you’re writing a linear novel, these are valuable for *prototyping branching scene variants*, interactive “choose-your-lore” reference docs, or dialogue coverage tests. citeturn20search5turn5search0turn5search4turn19search0turn19search3turn5search6turn20search2turn6search3turn0file0

**Automation & QA (prose linting, spelling, link checking, commits-as-checkpoints)**  
Vale; proselint; write-good; alex; textlint; markdownlint-cli2; LanguageTool; codespell; cspell; lychee; pre-commit. citeturn26search21turn9search1turn9search2turn9search3turn10search0turn10search1turn10search3turn10search4turn18search1turn18search2turn18search3turn18search0turn0file0

**Git infrastructure and collaboration surfaces (open-source, self-hostable options)**  
Gitea; Forgejo; plus specialized git storage helpers (git-annex) and large-file support (Git LFS). citeturn7search0turn8search1turn7search13turn7search2turn7search3

**Visualization, maps, and structured data layers (open-source building blocks)**  
Mermaid; Graphviz; PlantUML; Leaflet/OpenLayers/MapLibre for interactive maps; TimelineJS for interactive timelines; Datasette + SQLite for queryable character/ship/planet databases; GeoJSON for geodata interchange. citeturn15search0turn15search2turn15search3turn16search0turn16search1turn16search2turn16search3turn16search4turn16search5turn16search6turn16search7

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["novelWriter open source novel writing app screenshot","Manuskript open source novel writing tool screenshot","TiddlyWiki single file wiki screenshot","Inky ink editor screenshot"],"num_per_query":1}

### Tooling comparisons table

The table below focuses on projects most directly relevant to a Book 1 novel workflow (drafting + bible + build/export + QA + publishing), plus a few “glue” tools that materially improve reproducibility.

| project | purpose | primary language | data formats | license | maturity/activity | key pros/cons | ideal use-case |
|---|---|---|---|---|---|---|---|
| Pandoc | universal document conversion; build EPUB/PDF/HTML/DOCX from text source | (implementation varies; documented as “universal document converter”) | Pandoc Markdown; metadata blocks; many in/out formats | GPL-2.0 | active (recent releases and documented release process) | **Pros:** broad format coverage; filterable AST. **Cons:** output tuning can require templates/LaTeX/CSS | canonical build engine for trilogy manuscripts | citeturn5search2turn21search10turn23search10turn23search3 |
| Quarto | project system on top of Pandoc; multi-format publishing | (project repo indicates TypeScript) | Markdown + YAML; project configs | MIT | active (recent CLI releases) | **Pros:** batteries-included project scaffolding; multi-output. **Cons:** features optimized for tech publishing; may feel heavy | book-style site + EPUB/PDF builds, especially if you want a project framework | citeturn1search1turn1search9turn0file0 |
| mdBook | build “book websites” from Markdown | Rust toolchain | Markdown | MPL-2.0 | active (recent crate releases) | **Pros:** fast; strong for web book reading UX. **Cons:** EPUB/PDF less central than HTML book | publish series bible or “making-of” web book | citeturn3search18turn0file0 |
| Sphinx | docs-as-code engine; can publish book-like content | Python | reStructuredText/Markdown via extensions; HTML/PDF builds | BSD | active (recent releases) | **Pros:** mature docs platform; cross-references. **Cons:** more “docs” than “novel”; LaTeX pipeline complexity | publishing world bible as structured documentation | citeturn3search4turn0file0 |
| Asciidoctor | AsciiDoc processing; book-scale structured authoring | Ruby ecosystem | AsciiDoc; outputs include HTML/PDF/EPUB (via toolchain) | MIT | mature; extensive docs | **Pros:** includes/partials; strong long-doc ergonomics. **Cons:** AsciiDoc learning curve vs Markdown | authoring heavily structured “bible” or appendix-heavy books | citeturn21search3turn21search23turn0file0 |
| bookdown | R Markdown book publishing | R | R Markdown; PDF/EPUB/HTML | GPL-3.0 | active package; hosted service sunsetting Mar 31, 2026 | **Pros:** book-centric features. **Cons:** integration for pure fiction may be overkill; hosted service deprecating | if you already use RMarkdown/Quarto and want bookdown features | citeturn17search13turn10search5turn0file0 |
| Hugo | static site generator (fast) for lore sites | Go (project is “fast and modern static site generator”) | Markdown + front matter | Apache-2.0 | active (recent releases) | **Pros:** very fast; front matter in YAML/TOML/JSON. **Cons:** theme/config complexity | publish a canonical “Series Bible” website from git | citeturn3search7turn12search2turn0file0 |
| MkDocs | static docs/site generator | Python (project is MkDocs) | Markdown | BSD | active (recent releases) | **Pros:** simple; docs-friendly navigation. **Cons:** less “bookish” by default | low-friction bible site with search/navigation | citeturn3search3turn0file0 |
| Docusaurus | docs site generator with React; good for knowledge bases | JS/TS ecosystem | Markdown/MDX | MIT | active (recent releases) | **Pros:** modern UI, search, versioning. **Cons:** JS build tooling overhead | versioned bible docs (“v1 canon”, “v2 retcons”) | citeturn3search1turn0file0 |
| Eleventy (11ty) | flexible static site generator | JS ecosystem | Markdown + data files | MIT | active (recent releases) | **Pros:** data-driven pages from JSON/YAML; flexible. **Cons:** less opinionated; you build conventions | generate character database pages from YAML/JSON | citeturn4search2turn0file0 |
| Jekyll | Ruby-based static site generator | Ruby | Markdown + front matter | MIT | mature; ongoing maintenance | **Pros:** large ecosystem; GitHub Pages heritage. **Cons:** Ruby toolchain; convention-heavy | simple “bible site” hosted via common workflows | citeturn4search3turn0file0 |
| HonKit | GitBook-like docs/book generator | JS ecosystem | Markdown | MIT | active (recent releases) | **Pros:** familiar “GitBook” style; simple. **Cons:** smaller ecosystem than Hugo/MkDocs | fast, GitBook-like story bible/book web | citeturn4search5turn0file0 |
| novelWriter | fiction-focused IDE for long-form drafting | (project emphasized as “built for long-form fiction”) | plaintext/Markdown-oriented workflow (as described by project) | GPL-3.0 | positioned as active OSS writing IDE | **Pros:** novel-specific UX; scenes/chapters. **Cons:** you still need export/build discipline | drafting Book 1 with scene-level structure while keeping text-based sources | citeturn13search14turn0file0 |
| Manuskript | fiction writing tool (Scrivener-like) | (project positioned as open-source alternative) | project format; exports | GPL-3.0 | active project presence | **Pros:** planning aids; open-source. **Cons:** export/build may still need external tooling | writers wanting a planning+drafting GUI but OSS | citeturn13search12turn0file0 |
| Zettlr | Markdown editor (research + longform) | (project positioned as Markdown editor with Pandoc integrations) | Markdown; citations; export via Pandoc | GPL-3.0 | active releases in ecosystem | **Pros:** writing+citations; export hooks. **Cons:** less fiction-specific structure | SF research + drafting notes with consistent exports | citeturn13search0turn13search1turn0file0 |
| TiddlyWiki | single-file / self-hosted wiki for lore | JavaScript ecosystem | tiddlers (wiki text / JSON); single HTML | BSD | active releases | **Pros:** ultra-portable; offline; extensible. **Cons:** scaling to multi-author needs conventions | personal “series bible in one file” + portable canon | citeturn10search4turn0file0 |
| Wiki.js | server wiki with git-backed workflows | Node.js ecosystem | Markdown; git storage options | AGPL-3.0 | active project presence | **Pros:** multi-user; permissions; git sync. **Cons:** server ops; AGPL implications if modified | collaborative bible for co-authors/editors | citeturn6search0turn0file0 |
| Logseq | outliner + graph knowledge base | ClojureScript/JS ecosystem | Markdown/Org-style blocks | AGPL-3.0 | active repo | **Pros:** graph thinking; daily notes. **Cons:** app-level workflow; exports require planning | research + worldbuilding with backlink graph | citeturn6search1turn0file0 |
| Ink | narrative scripting language; branching story logic | (project emphasizes scripting language + compiler) | .ink source → compiled JSON | MIT | mature ecosystem; active docs | **Pros:** deterministic compilation; great for branching prototypes. **Cons:** not a novel formatter | explore alternate POV/plot branches; dialogue prototyping; “what-if” continuity tests | citeturn20search4turn20search0turn20search20turn0file0 |
| Inky | Ink editor (play-as-you-write) | (editor for Ink) | .ink; exports web/JSON | MIT | active companion tool | **Pros:** tight Ink workflow; preview. **Cons:** niche if you don’t use Ink | author branching scenes for later linearization into manuscript | citeturn20search5turn5search0turn0file0 |
| Twine + Twee 3 | hypertext fiction tooling; can be “story-as-code” via text formats | JS ecosystem | Twine HTML; Twee 3 text spec | GPL (Twine); specs open | active community/spec work | **Pros:** visual graph; text-based source via Twee. **Cons:** conversion to linear novel is non-trivial | mapping branching plot options; interactive appendices/side stories | citeturn5search4turn19search0turn19search3turn19search12turn0file0 |
| Yarn Spinner + ysc | dialogue scripting and compilation | C# ecosystem | .yarn; .yarnproject JSON; .yarnc + CSV outputs | MIT | active docs and tooling | **Pros:** plain-text dialogue; compiler outputs tables/metadata. **Cons:** engine-oriented | manage dialogue-heavy SF scenes; export line tables for review | citeturn20search2turn19search6turn19search2turn0file0 |
| Inform | interactive fiction authoring system | (toolchain; includes testing constructs) | source → IF artifacts | Artistic-2.0 | open-source repo | **Pros:** strong “test transcripts” culture. **Cons:** specialized | if you want mechanically testable IF side projects or lore simulators | citeturn6search3turn0file0 |
| Ren’Py | visual novel engine, Python scripting | Python + engine components | script + assets | MIT + LGPL | active releases | **Pros:** strong for VN prototypes. **Cons:** game pipeline overhead | prototype character/scene interactions; later novelize | citeturn6search4turn0file0 |
| Vale | prose linter; “code review for writing” | (project is CLI; LSP support exists) | rules + config; runs on Markdown/AsciiDoc/etc | MIT | active (recent releases; LSP tooling) | **Pros:** customizable style; CI-friendly. **Cons:** rule curation work | enforce glossary/canon spellings; catch weak prose patterns in CI | citeturn26search21turn26search2turn26search13turn0file0 |
| ChrisChinchilla/vale-vscode | in-editor Vale integration for VS Code | TypeScript | editor integration; uses Vale + vale-ls | MIT | active fork; recent issues/notes | **Pros:** real-time lint feedback; supports vocab workflows. **Cons:** extension/tooling complexity during LSP transitions | “lint as you write” in VS Code while keeping CI as source of truth | citeturn31view0turn29view0turn28search9 |
| pre-commit | hook framework to enforce checks before commits | Python | hook configs (YAML) | MIT | active (recent releases) | **Pros:** standardizes checks across machines. **Cons:** initial setup overhead | ensure every commit passes lint/format/metadata validation | citeturn18search0turn18search4 |
| Calibre + ebook-convert | conversion toolchain between ebook formats | primarily Python + C/C++ components | many ebook formats; CLI conversion | GPL-3.0 | active (frequent releases) | **Pros:** practical format conversion; CLI. **Cons:** heavyweight dependency | convert EPUB to legacy formats (e.g., MOBI/AZW3) when required | citeturn0search5turn0search7turn0search2turn0search3 |

## Technical architectures and data formats

A “story-as-code” architecture is best understood as a **source graph** and a **build graph**.

**Source graph:** your repository contains (1) manuscript text, (2) structured metadata, (3) world-bible artifacts, and (4) build tooling. The durability of the workflow depends on choosing formats whose tooling is plural (usable by many editors/builders) and whose semantics are explicit (schemas, conventions, tests). citeturn22search11turn21search0turn21search10turn0file0

**Build graph:** deterministic compilation from source → output artifacts (EPUB/PDF/HTML/print). The more your pipeline resembles a software build (pinned versions, stable templates, lint gates), the easier it is to maintain across three books. citeturn23search10turn0search2turn0file0

### Core text formats and where they fit

**Markdown family (most common “prose code”)**  
CommonMark provides a standardized Markdown specification, reducing ambiguity across renderers. citeturn21search0turn21search4  
GitHub Flavored Markdown (GFM) describes the Markdown dialect used for rendering user content on GitHub, adding extensions like tables and task lists. citeturn21search1turn21search5  
Pandoc’s Markdown is a deliberately extended variant that adds book-relevant features (metadata blocks, footnotes, citations, tables, math), and Pandoc can enumerate enabled extensions per format. citeturn21search10turn21search22turn21search6

**Front matter and metadata conventions**  
Static-site and publishing projects often store per-file metadata (title, tags, date, series book number, POV, location, “canon status”) in front matter. Hugo explicitly supports front matter in YAML/TOML/JSON. citeturn12search2turn0file0  
Yarn Spinner uses `.yarnproject` as a JSON project file describing scripts and configuration. citeturn20search2turn19search2

**Plain-text interactive narrative formats (useful even for linear novels)**  
Ink compiles `.ink` source to an intermediate JSON runtime format; the repository documents the JSON runtime format and explains the `.json` intermediate. citeturn20search0turn20search20turn20search4  
Twine supports plaintext via the Twee 3 specification, described as the text format for marking up the source code of Twine stories (equivalent to Twine HTML story files). citeturn19search0turn19search3turn19search12  
Yarn Spinner’s `ysc compile` compiles `.yarn` files into `.yarnc` plus CSV string tables and metadata. citeturn19search6turn19search2turn20search6

**Org-mode**  
Org mode can publish/export to multiple formats (HTML, LaTeX, ODT, etc.), making it a viable “story as text code” format if you already live in Emacs and want sophisticated outlining. citeturn12search3

**Fountain**  
Fountain is a plain-text markup syntax for screenplays; it’s relevant to sci-fi novel workflows when you want script-like drafting for dialogue-heavy scenes or audio drama side content. citeturn12search0turn12search4

### A practical reference architecture

Below is a minimal architecture that supports (a) Book 1 drafting, (b) trilogy bible continuity, and (c) automated exports. The key pattern is **single-source text + structured data + deterministic builds**.

```mermaid
flowchart LR
  subgraph Repo[Git repo]
    M[manuscript/ (Markdown chapters + YAML metadata)]
    B[bible/ (wiki or markdown docs)]
    D[data/ (characters.yml, timeline.yml, glossary.yml, maps.geojson)]
    T[templates/ filters/ styles/]
  end

  M -->|pandoc| O1[book-1.epub]
  M -->|pandoc + latex engine| O2[book-1.pdf]
  M -->|pandoc/quarto| O3[book-1.html]

  D -->|static site generator| W[bible site (HTML)]
  B -->|static site generator| W

  Repo --> CI[CI pipeline: lint + build + release artifacts]
```

Pandoc filters work by reading a JSON serialization of the Pandoc AST, transforming it, and writing it back—this is the primary “programmability hook” for story-as-code transformations (e.g., enforce scene headers, auto-expand glossary tags, normalize em-dash usage). citeturn23search3turn21search10

## Licensing and community health

### License patterns you will encounter

The story-as-code landscape spans permissive and copyleft licenses, and this matters chiefly for **tooling**, not for your **novel text**. Most authors keep the *manuscript* under standard copyright while licensing *build scripts/templates* under an OSS license; mixing them naïvely can confuse downstream users about what is reusable. GitHub’s own documentation stresses that choosing a license is what makes software reuse legally clear. citeturn17search17

Common patterns in the tools researched:

- **Permissive licenses (MIT/BSD/Apache-2.0):** common for libraries, CLIs, and web tooling—e.g., Ink (MIT), Mermaid (MIT), Leaflet (BSD-2-Clause), Docusaurus (MIT), Hugo (Apache-2.0). citeturn20search4turn15search0turn16search0turn3search1turn3search7  
- **Strong copyleft (GPL/AGPL):** common for end-user applications, self-hosted services, and some writer tools—e.g., calibre (GPL-3.0), Logseq (AGPL-3.0), Wiki.js (AGPL-3.0). citeturn0search7turn6search1turn6search0  
- **License transitions as a community health signal:** Forgejo publicly documented a switch to GPLv3+ and a release scheduling approach (“time-based” releases every two months), illustrating that governance decisions can change over time. citeturn7search13turn8search1turn8search3

### How to assess community health for novel production risk

For a trilogy, “health” is less about stars and more about: predictable releases, responsive issue triage, stable docs, and the existence of escape hatches (interchange formats).

Pragmatic signals visible in the researched sources:

- **Release cadence and recency:** calibre shows frequent releases (e.g., Feb 2026 releases visible on the repo’s release page), suggesting active maintenance. citeturn0search2turn0search1  
- **Explicit documentation and tooling depth:** Pandoc maintains a structured manual and a public release process; its extensibility via filters is documented. citeturn21search10turn23search10turn23search3  
- **Active issue traffic in relevant subcomponents:** ChrisChinchilla’s Vale VS Code extension shows late-2025 issue activity and documents a substantial architectural change (switch to Vale Language Server), a typical sign of active engineering—and also a reminder to pin versions in CI if you need stability. citeturn31view0turn29view0  
- **Maintenance posture (including “maintenance-only”):** Dendron publicly frames itself as “maintenance mode” and directs users toward alternatives; this is valuable for risk management because it tells you not to bet your trilogy on new feature development there. citeturn6search2  
- **Hosted-service deprecations that might affect your pipeline:** the bookdown hosted site indicates a sunset date (March 31, 2026). Even if the package continues, relying on the hosted surface is a fragile dependency. citeturn10search5turn17search13

## Recommended workflows for Book 1 in a trilogy

This section is intentionally concrete: it maps story craft needs (planning, canon, revision, collaboration, export) onto reproducible tooling.

### Planning and structured drafting

A series-friendly “story-as-code” repo benefits from three layers of structure:

1. **Outline layer**: high-level arc and chapter intent (Markdown).  
2. **Scene layer**: one file per scene (or short chapter segment) with metadata.  
3. **Canon layer**: world bible and constraints (tech rules, timeline, glossary). citeturn0file0turn12search2turn21search10

A proven community pattern is to treat git primitives as narrative primitives: branches for alternate plotlines, commits as scene checkpoints, tags for milestone drafts, issues for plot holes/continuity, pull requests for review. fileciteturn0file0L55-L62

For Book 1 with Book 2–3 planned, consider a branching strategy like:

- `main`: canonical state of Book 1 (and evolving bible).  
- `bible`: optional protected branch for canon-only changes (glossary, tech rules, timeline).  
- `experiments/*`: alternative scene sequences, POV swaps, or “hard-SF plausibility” variants.  
- tags: `b1-outline-v0.1`, `b1-draft1-v1.0`, `b1-draft2-v2.0`, `b1-copyedit-v3.0`. fileciteturn0file0L55-L61

### Worldbuilding and canon management patterns

If you want open-source, offline-first portability, TiddlyWiki is structurally compelling: it can live as a self-contained artifact, but can also be self-hosted, and its licensing and release cadence are explicit. citeturn10search4turn10search0  
If you want multi-user collaboration, permissions, and “wiki as a service,” Wiki.js is a common OSS target; it’s explicitly framed as self-hosted and supports git-oriented backends. citeturn6search0turn0file0

For sci-fi specifics, encode “hard constraints” as data:

- `glossary.yml`: canonical spelling, pronunciation notes, and “first appearance” references.  
- `timeline.yml`: absolute dates/events (with book/scene references).  
- `characters.yml`: factions, rank progression, relationship edges.  
- `maps.geojson`: locations (even fictional coordinate systems) to drive map renderers. citeturn16search5turn16search7turn12search2

Then render these into human-friendly views: static pages (Hugo/MkDocs) or interactive views (TimelineJS, Leaflet-based maps). citeturn3search7turn3search3turn16search0turn16search3turn16search7

### Export targets and print-ready builds

**EPUB and PDF remain the core targets** for ebook and print workflows in open pipelines. Pandoc is the dominant conversion engine for Markdown→EPUB/PDF, while LaTeX engines (e.g., Tectonic) can make PDF builds more reproducible across machines. citeturn21search10turn17search14turn23search0

For template-driven PDF styling, the Eisvogel template is a well-known Pandoc LaTeX template (BSD-3-Clause) and tracks Pandoc compatibility changes in its releases. citeturn23search0turn23search4turn23search8

For CSS-driven “paged media” (HTML→print/PDF), WeasyPrint and Paged.js are open-source options worth evaluating when you want fine typographic control without deep LaTeX work. citeturn11search5turn11search6

**MOBI note (important for 2026 reality):** Kindle Direct Publishing states that MOBI is not supported for reflowable ebooks (since 2021) and that fixed-layout MOBI is also not supported (since 2025). Practically, prioritize EPUB for Kindle workflows; keep MOBI only for legacy/testing. citeturn11search9

When conversion to older/alternate ebook formats is required, calibre’s CLI `ebook-convert` provides deterministic “input → output” conversions and calibre is explicitly GPLv3. citeturn0search7turn0search3turn0search5

### Minimal reproducible repository structure

A minimal (but trilogy-scalable) repo layout that stays editor/tool agnostic:

```text
series-novel/
  README.md
  LICENSES/
    LICENSE.build-scripts.txt
    LICENSE.templates.txt
  manuscript/
    book-1/
      meta.yml
      chapters/
        00-frontmatter.md
        01-prologue.md
        02-ch01.md
        ...
  bible/
    index.md
    factions.md
    technology.md
    planets.md
  data/
    characters.yml
    timeline.yml
    glossary.yml
    maps.geojson
  assets/
    images/
    maps/
  build/
    pandoc/
      defaults.yml
      epub.css
      latex-template.tex   # or vendor Eisvogel
    scripts/
      build.sh
      wordcount.sh
  qa/
    vale/
      .vale.ini
    cspell.json
    .markdownlint.json
  .github/
    workflows/
      build.yml
```

The repo-level workflow concept—*build the manuscript like software* with CI that runs on each commit—is a documented community pattern in story-as-code discussions. fileciteturn0file0L96-L99

### Example CI pipeline for automated builds/exports

Below is a minimal Git-based CI pipeline conceptually aligned with the community patterns noted above (lint + build + artifacts). fileciteturn0file0L96-L99

```yaml
name: build-book

on:
  push:
    branches: [ "main" ]
  pull_request:

jobs:
  qa-and-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # QA: prose and repo hygiene
      - name: Install tools
        run: |
          python -m pip install --upgrade pip
          pip install codespell
          npm install -g cspell markdownlint-cli2

      - name: Spellcheck (codespell)
        run: codespell manuscript bible data

      - name: Spellcheck (cspell)
        run: cspell "manuscript/**/*.md" "bible/**/*.md" "data/**/*.yml"

      - name: Markdown lint
        run: markdownlint-cli2 "manuscript/**/*.md" "bible/**/*.md"

      # Build: Pandoc outputs
      - name: Build EPUB + PDF
        run: |
          ./build/scripts/build.sh

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: book-1-artifacts
          path: |
            dist/book-1.epub
            dist/book-1.pdf
            dist/book-1.html
```

To enforce checks *before* commits hit CI, pre-commit is a well-established framework with recent releases. Lychee is a practical “docs-as-code” style link-checker for Markdown/HTML and can be integrated into CI to keep your bible and manuscript links clean. citeturn18search0turn18search4turn18search3turn18search11

## Migration and interoperability concerns

Interoperability is where “story-as-code” succeeds or fails. The safest stance for a trilogy is: **keep your authoritative sources in plain text + openly documented schemas**, and treat everything else as a rendered artifact.

### Common failure modes and mitigations

**Markdown dialect drift**  
GFM and CommonMark differ, and Pandoc adds its own extensions. If you mix renderers (GitHub preview, local preview extensions, CI builds), you can get subtle output differences. Mitigation: choose a primary dialect (e.g., Pandoc Markdown), and lint/preview against *the same build engine you use for releases*. citeturn21search0turn21search1turn21search10turn21search22

**Front matter schema mismatch**  
Static site generators and book builders parse front matter differently; Hugo supports YAML/TOML/JSON front matter explicitly, but other engines may have different defaults. Mitigation: standardize on one front matter format (often YAML) and validate with a schema check in CI. citeturn12search2

**Binary project formats**  
Tools that store state in opaque binaries create lock-in. Even in open-source tools, check whether “project state” is diff-friendly. Mitigation: prefer tools that keep content in plaintext files or cleanly export to plaintext builds (Pandoc pipelines; wiki exports; data files). citeturn21search10turn0file0

**Branching narrative formats → linear novels**  
Ink/Twine/Yarn are “story as code,” but they produce interactive branching artifacts. Converting them into a linear novel is a *creative choice*, not a pure technical transform. Still, they can be used safely if you keep source scripts and compile outputs as separate artifacts. Ink’s compilation to JSON and Twine’s text-based Twee 3 spec make them tractable for tooling and diff workflows. citeturn20search20turn20search0turn19search0turn19search3turn19search6

### Conversion tools and “escape hatches”

**Pandoc as the universal escape hatch**  
Pandoc’s extensibility via JSON AST filters (and helper libraries like pandocfilters) enables controlled migrations: you can write a filter once to normalize headings, metadata blocks, or custom scene markers before converting to another format. citeturn23search3turn21search10

**Cross-references and numbering**  
If you maintain appendices (ship registries, technology specs) that need consistent numbering and cross-references, pandoc-crossref is explicitly a Pandoc filter for numbering and cross-references and tracks compatibility with recent Pandoc versions. citeturn23search6turn23search2turn23search14

**Ebook conversions**  
Calibre’s documented CLI (`ebook-convert`) is the pragmatic conversion layer when you need to move between ebook formats outside Pandoc’s sweet spot, and calibre’s licensing is explicitly GPLv3. citeturn0search7turn0search3turn0search5

## Plugins, extensions, templates, and community resources

### High-leverage extensions and templates

For a science-fiction trilogy, the most valuable “extensions” are those that enforce consistency and allow you to *compile your bible into navigable views*.

- **Mermaid** (MIT) gives you diagrams-as-code for relationship graphs, fleet hierarchies, and plot dependency flowcharts; it is actively released. citeturn15search0turn15search1  
- **VS Code Markdown Mermaid support** adds Mermaid rendering to Markdown preview (MIT) and states current Mermaid version support. citeturn24search2  
- **TimelineJS** enables interactive timelines (useful for multi-planet chronologies and relativistic travel timelines). citeturn16search7  
- **Leaflet / OpenLayers / MapLibre + GeoJSON** provide an open mapping stack for interactive star maps or planet maps, with explicit permissive licensing and GeoJSON standardization. citeturn16search0turn16search1turn16search2turn16search5  
- **Eisvogel Pandoc template** provides a maintained LaTeX template, with explicit license and release notes tracking Pandoc changes. citeturn23search0turn23search4turn23search8  
- **Pandoc book templates** (e.g., pandoc-markdown-book-template; pandoc-book-template) provide starter repo scaffolding for EPUB builds; use them as references even if you later customize. citeturn23search13turn23search1

For prose quality automation:

- Vale (MIT) is explicitly a command-line tool bringing code-like linting to prose; it has LSP support, useful across multiple editors. citeturn26search21turn26search2turn26search4  
- codespell (GPL-2.0) catches common misspellings; cspell (MIT) is a configurable spell checker with active releases and CLI tooling. citeturn18search1turn18search14turn18search2  
- lychee (dual MIT/Apache-2.0) is a fast link checker for Markdown/HTML. citeturn18search3turn18search7

A practical caution: editor extension marketplaces can be supply-chain risk surfaces; treat extensions like dependencies and prefer pinned versions and reputable sources when your manuscript repo matters. citeturn24news38

### Communities and learning resources

**Interactive fiction and narrative tooling communities**  
The Interactive Fiction Community Forum is an active place focused on authoring and IF tools (useful for Ink/Twine/Yarn techniques even when writing linear novels). The Interactive Fiction Technology Foundation documents its stewardship of the forum. citeturn22search2turn22search10turn22search6

**Docs-as-code communities (high relevance to “story-as-code”)**  
entity["organization","Write the Docs","documentation community"] is a global community with learning resources, events, and discussion spaces that overlap strongly with the workflows you’ll use (linting, CI publishing, information architecture). citeturn22search1turn22search13

**Git-based collaborative writing patterns**  
Manubot is explicitly designed for writing manuscripts in Markdown stored in a git repository, enabling collaborative workflows and automated evaluation; while scholarly-focused, its rootstock template demonstrates a mature “text + CI” pattern transferable to long-form fiction. citeturn22search11turn22search0turn22search7

### Quick link bundle for core open-source building blocks

(Links are in a code block to keep them explicit and copyable.)

```text
Pandoc: https://pandoc.org/ | https://github.com/jgm/pandoc
Quarto: https://quarto.org/ | https://github.com/quarto-dev/quarto-cli
Calibre: https://calibre-ebook.com/ | https://github.com/kovidgoyal/calibre
TiddlyWiki: https://tiddlywiki.com/ | https://github.com/Jermolene/TiddlyWiki5
Wiki.js: https://js.wiki/ | https://github.com/requarks/wiki
Ink: https://www.inklestudios.com/ink/ | https://github.com/inkle/ink
Twine specs / Twee 3: https://github.com/iftechfoundation/twine-specs
Yarn Spinner: https://yarnspinner.dev/ | https://github.com/YarnSpinnerTool
Mermaid: https://github.com/mermaid-js/mermaid
Leaflet: https://github.com/Leaflet/Leaflet
Datasette: https://github.com/simonw/datasette
Eisvogel template: https://github.com/Wandmalfarbe/pandoc-latex-template
```

## Prioritized recommendations

The “best” stack depends on whether Book 1 is primarily: (a) prose-first with heavy worldbuilding, (b) structurally complex with many alternative scene variants, or (c) co-authored with frequent review and tooling standardization needs. The three stacks below intentionally share an invariant: **plain-text sources stored in git + deterministic builds**.

### Stack A: Manuscript-first Markdown pipeline

**Components**  
- Markdown source (CommonMark/Pandoc Markdown conventions) citeturn21search0turn21search10  
- Pandoc build to EPUB/PDF/HTML citeturn21search10turn23search10  
- Git hosting and review workflow on entity["company","GitHub","code hosting platform"] or entity["company","GitLab","devops platform"] citeturn22search11turn0file0  
- CI enforcing writing QA (Vale, codespell, cspell, lychee) citeturn26search21turn18search1turn18search14turn18search3  
- Optional Calibre for legacy ebook conversions (when required) citeturn0search7turn0search3  

**Why it’s top-ranked for a trilogy**  
It maximizes interoperability and minimizes lock-in: every asset is inspectable and diffable, and you can migrate formats later (Pandoc + filters). It scales cleanly to three books because branching/tagging/review patterns map directly to long-running projects. citeturn23search3turn22search11turn0file0

### Stack B: Fiction IDE + build pipeline hybrid

**Components**  
- Write and organize Book 1 in novelWriter or Manuskript (scene/chapter UX) fileciteturn0file0L133-L145  
- Treat exports/plaintext as the “source of truth” committed to git  
- Build outputs via Pandoc/Quarto, with CI gates (same as Stack A) citeturn21search10turn1search1turn26search21  

**Why it’s strong**  
You get fiction-specific ergonomics without abandoning reproducibility. This is often the best “writer happiness / engineering discipline” compromise, especially for Book 1 where you need momentum and structure while still laying trilogy foundations. citeturn0file0turn21search10

### Stack C: Canon-first world bible with published reference site

**Components**  
- World bible as TiddlyWiki (single-file) or Wiki.js (collaborative server) citeturn10search4turn6search0turn0file0  
- Structured datasets (YAML/JSON + GeoJSON) feeding timeline/map/character views (TimelineJS, Leaflet, Datasette) citeturn16search7turn16search0turn16search6turn16search5  
- Publish bible as a static site (Hugo/MkDocs/Docusaurus) citeturn3search7turn3search3turn3search1  
- Manuscript still built with Pandoc (Stack A engine) citeturn21search10turn23search10  

**Why it’s trilogy-optimal when continuity risk is high**  
Sci-fi series often fail on internal consistency. This stack makes canon *queryable and publishable*, enabling you to catch continuity errors early (e.g., “this ship class doesn’t exist until year X,” “this officer cannot be on two planets simultaneously”). The cost is additional structure and tooling, but it pays off over three books. citeturn0file0turn16search7turn3search7