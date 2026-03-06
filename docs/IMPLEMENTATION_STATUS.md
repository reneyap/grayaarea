# GrayArea — Implementation Status

**Last Updated:** 2026-03-05  
**Phase:** Book 1 Planning → Drafting Transition

---

## Current State: What's Actually Running

### ✅ Fully Implemented

**Git-Based Canon Management**
- Lore organized in `/lore/Codex/` with 11 canonical character profiles
- Timeline consolidated in `Timeline.md`
- Constraints, artifacts, technology organized in subdirectories
- CONSOLIDATION_MAP.md tracking canon decisions
- ISSUES.md generated from AI-assisted consistency audits
- Conventional commits enforced via copilot-instructions.md

**Digital Stratigraphy Archive**
- Layer 0: `archive/00_2020-2023_original/` — sealed bedrock
- Layer 1: `archive/01_*/` — discussion/analysis layers (83 atomized topics)
- Layer 2: `book1/` — current synthesis workspace
- Provenance tracking via folder structure

**Documentation**
- ARCHITECTURE.md (full stack design)
- DIGITAL_STRATIGRAPHY.md (philosophy)
- STORY-AS-CODE-FEEDBACK.md (critical analysis)
- STORY-AS-CODE-LANDSCAPE.md (ecosystem research)
- README.md with project overview

**Book 1 Planning**
- 19-chapter structure finalized (see `docs/METADATA/Book1-Planning/81-*`)
- Word count targets debated and decided
- Act structure outlined
- Chapter stubs created in `book1/chapters/`

**Prose Quality Tooling** (New)
- Vale configuration (`.vale.ini`) with house style rules
- Custom vocabulary for GrayArea canon terms
- Write-good integration for passive voice, weasel words

**AI Workflow**
- Manual lore audits via Claude (Copilot Chat)
- Search-based consistency checking (`grep_search`, `semantic_search`)
- AI-assisted canon consolidation from source material

### 🚧 Partially Implemented

**Chapter Prose**
- Status: Outlines and stubs exist; minimal prose drafted
- Next: Draft Chapters 1-5 (Act 1) to validate workflow
- Template created for front matter consistency

**Workflow Automation**
- Status: Manual git workflow with conventional commits
- Next: Pre-commit hooks for Vale linting, YAML validation
- Future: GitHub Actions CI for automated builds

---

## Planned But Not Implemented

### ⏳ Deferred to Phase 2 (Post Book 1 Draft)

**Supabase Database Layer**
- Schema designed in ARCHITECTURE.md
- Tables: `topics`, `canon`, `characters`, `timeline_events`, `chapters`
- Import script pseudocode exists but untested
- **Decision Point**: Determine if git+Markdown is sufficient for Book 1

**Next.js Web Application**
- Planned features:
  - Chapter editor with Markdown preview
  - Canon dashboard with search
  - Character profile viewer
  - Timeline visualization
  - Word count tracking
- **Status**: Zero implementation; frontend code doesn't exist
- **Rationale**: Prose drafting takes priority over tooling

**Expo Mobile App**
- Planned features:
  - Offline chapter reading
  - Quick canon lookup
  - Note-taking for story ideas
- **Status**: Zero implementation
- **Rationale**: Not needed for solo authoring; defer to publication phase

**MCP Server (Model Context Protocol)**
- Planned functionality:
  - Expose canon, characters, timeline as MCP resources
  - Tools: `check_canon`, `search_topics`, `validate_continuity`
  - Integration with Claude/Cursor for real-time canon checking
- **Status**: Designed but not coded
- **Decision Point**: Implement when real-time canon checks become bottleneck

**AI Embeddings & Semantic Search**
- Planned: OpenAI text-embedding-3-small → pgvector
- Purpose: Semantic similarity search across 83 discussion topics
- **Status**: Not implemented; using manual search instead
- **Rationale**: Topic count manageable for manual search

**CI/CD Pipeline**
- Planned:
  - GitHub Actions on every push to `main`
  - Vale linting (prose quality gates)
  - cspell (typo detection)
  - Word count tracking
  - Automated EPUB/PDF builds via Pandoc
- **Status**: Infrastructure research complete; zero automation
- **Next**: Add pre-commit hooks locally before GitHub Actions

**Canon Visualization**
- Planned:
  - TimelineJS for events
  - Mermaid diagrams for character relationships
  - Leaflet maps for locations
  - Datasette for queryable canon tables
- **Status**: Static Markdown only
- **Next**: Generate simple timeline diagram from Timeline.md

---

## Technology Stack: Designed vs. Active

| Component | Planned | Status | Notes |
|-----------|---------|--------|-------|
| **Source Control** | Git | ✅ Active | Conventional commits enforced |
| **Lore Format** | Markdown | ✅ Active | 11 profiles, atomized topics |
| **Database** | Supabase | ❌ Not deployed | Schema designed |
| **Web Frontend** | Next.js | ❌ Not started | Deferred to Phase 2 |
| **Mobile** | Expo | ❌ Not started | Deferred to Phase 2 |
| **AI Integration** | MCP Server | ❌ Not started | Manual workflow sufficient |
| **Prose Linting** | Vale | 🚧 Config added | Need to install + run |
| **Build System** | Pandoc | ⏳ Planned | CI integration future |
| **Monorepo** | Nx | ⏳ Scaffolded? | Unclear if functional |

---

## Decision Framework

### When to Implement Deferred Features

**Implement Supabase/Next.js if:**
- Chapter count exceeds 50 and git-grep becomes unwieldy
- Co-authoring requires collaborative editing
- Need to share interactive canon bible with beta readers

**Implement MCP Server if:**
- Drafting reveals frequent canon lookup during writing
- Cross-book continuity checks become bottleneck (Book 2+)
- Real-time validation needed in editor (Cursor integration)

**Implement CI/CD if:**
- Working with co-authors/editors (consistency enforcement)
- Preparing for publication (automated EPUB/PDF builds)
- Managing multiple draft versions across branches

**Implement Mobile App if:**
- Publishing Book 1 and want reader companion
- Need field notes capture away from desk

---

## Current Bottlenecks

1. **Prose drafting**: Architecture is ready; writing is the constraint
2. **Vale not installed**: Config exists but tool not in use yet
3. **Chapter templates**: Need to validate front matter schema against real prose
4. **Canon queries**: Manual search works but could be faster with database

---

## Next Actions (Immediate)

1. ✅ Tag baseline state (`b1-planning-v1.0`)
2. ✅ Create `.vale.ini` and custom vocabulary
3. ✅ Document implementation status (this file)
4. ✅ Create chapter template
5. ⏳ Install Vale locally (see Vale Installation section below)
6. ⏳ Test Vale on existing chapters: `vale book1/chapters/`
7. ⏳ Draft Chapters 1-3 to validate workflow
8. ⏳ Add pre-commit hooks (Vale + YAML validation)

---

## Vale Installation (Platform-Specific)

### macOS
```bash
brew install vale
vale --version
```

### Windows (Git Bash)

**Option A: Using Scoop (Recommended)**
```bash
# Install Scoop (requires PowerShell admin)
powershell -Command "iwr -useb get.scoop.sh | iex"

# Then install Vale
scoop install vale

# Verify
vale --version
```

**Option B: Using Chocolatey**
```bash
# Install Chocolatey first if needed (requires admin PowerShell)
# See https://chocolatey.org/install

choco install vale

# Verify
vale --version
```

**Option C: Direct Download (No Package Manager)**
1. Visit: https://github.com/errata-ai/vale/releases
2. Download latest `vale_*_Windows_x86_64.zip`
3. Extract to a folder in your PATH (e.g., `C:\Program Files\vale\`)
4. Add folder to PATH environment variable
5. Restart git bash terminal
6. Verify: `vale --version`

**Troubleshooting**: 
- If git bash can't find `vale` after installation, restart the terminal
- Scoop/Chocolatey require admin rights; ensure you run PowerShell as Administrator
- On Windows, you may need to add the installation folder to your Windows PATH environment variable

---

## Success Criteria for Phase 1 (Book 1 Draft)

- [ ] Chapters 1-19 drafted (first pass, ~70k words)
- [ ] All chapters pass Vale linting
- [ ] Canon consistency validated (no ISSUES.md blockers)
- [ ] Chapter front matter schema stable
- [ ] Git workflow proven for full draft cycle

**After Phase 1 completes**, reassess whether Supabase/Next.js infrastructure is needed for Book 2 or if git+Markdown scales adequately.

---

**Philosophy**: Optimize for writing velocity now; infrastructure payoff increases with corpus size and collaboration needs.
