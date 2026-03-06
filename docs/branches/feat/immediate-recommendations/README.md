# feat/immediate-recommendations Branch

**Branch**: `feat/immediate-recommendations`  
**Based on**: `baseline` (tagged as `b1-planning-v1.0`)  
**Created**: 2026-03-05  
**Status**: Ready for review (not pushed)

---

## Overview

Implementation of immediate recommendations from `docs/STORY-AS-CODE-FEEDBACK.md`. This branch establishes foundational tooling and documentation for the Book 1 drafting phase, addressing the gap between design documentation (ARCHITECTURE.md) and actual workflow.

## Scope

**What's Included:**
- Workspace-wide instructions (Copilot integration, conventional commits, canon-first principles)
- Prose linting configuration (Vale + custom vocabulary)
- Implementation status tracking (actual vs. planned features)
- Chapter template with front matter schema

**What's NOT Included:**
- Vale installation or testing
- Pre-commit hooks
- GitHub Actions CI/CD
- Supabase/Next.js/MCP infrastructure

These remain in medium-term and long-term phases per STORY-AS-CODE-FEEDBACK.md.

---

## Commits

### 1. `feat(docs): add copilot-instructions.md with project conventions`
**Hash**: `d675d1e`  
**Files**: `.github/copilot-instructions.md` (new)

Workspace-wide instructions ensuring all Copilot interactions follow project conventions:
- Conventional commit standards (types: feat, fix, docs, chore, etc. / scopes: lore, book1, docs, etc.)
- Canon-first architecture (two-plane structure: canon plane + manuscript plane)
- Digital stratigraphy rules (layered archive preservation)
- Git workflow (branching strategy, tagging milestones)
- Chapter front matter schema (YAML metadata for chapters)
- Lore file organization (Markdown + provenance tracking)
- AI assistant guidelines (always check canon, respect locked facts, link not duplicate)

**Why**: Ensures consistent guidance across all future Copilot sessions without repeating instructions.

---

### 2. `fix(docs): enforce explicit file staging in git workflow`
**Hash**: `49ae1ac`  
**Files**: `.github/copilot-instructions.md` (modified)

Added strict rules against lazy git staging:
- **Forbid**: `git add -A` and `git add .`
- **Require**: Explicit file paths (e.g., `git add lore/Codex/Daneel.md docs/ISSUES.md`)
- **Enforce**: Review with `git diff --staged` before committing
- **Rationale**: Never assume exclusive repo access; prevents accidental staging of unrelated changes

**Why**: Discovered this gap when attempting `git add -A` earlier. Multi-contributor repos need explicit staging discipline.

---

### 3. `feat(tools): add Vale prose linting configuration`
**Hash**: `5c14a6d`  
**Files**: 
- `.vale.ini` (new)
- `.vale/styles/Vocab/GrayArea/accept.txt` (new)
- `.vale/styles/Vocab/GrayArea/reject.txt` (new)

Vale linting configuration for prose quality:
- **`.vale.ini`**: Global config + per-directory rules
  - Chapters: write-good style (passive voice, weasel words, repetition)
  - Lore: Vale spelling + repetition checks
  - Archive: disabled (no linting for bedrock layers)
- **`accept.txt`**: GrayArea-specific vocabulary (character names: Daneel, Elijah, Cleo; canon terms: Attractor, X20, neurophysiological; locations: Manhattan, Grand Central)
- **`reject.txt`**: Deprecated/non-standard spellings (discourage "utilize" over "use")

**Next Step**: Install Vale locally (`brew install vale` on Mac, `choco install vale` on Windows), then test: `vale book1/chapters/`

**Why**: Prose linting catches weak patterns early. Custom vocabulary prevents false positives on sci-fi terms.

---

### 4. `docs: add IMPLEMENTATION_STATUS tracking actual vs planned state`
**Hash**: `e600a93`  
**Files**: `docs/IMPLEMENTATION_STATUS.md` (new)

Honest accounting of what's implemented vs. designed:

**✅ Fully Implemented:**
- Git-based canon (Markdown lore, CONSOLIDATION_MAP.md, ISSUES.md)
- Digital stratigraphy archive (layers 0-2)
- Book 1 planning (19 chapters, outlines)
- Prose quality tooling (Vale config, this commit)

**🚧 Partially Implemented:**
- Chapter prose (outlines exist, minimal drafting)
- Workflow automation (manual git, no CI/CD yet)

**⏳ Deferred to Phase 2:**
- Supabase database + schema
- Next.js web app (editor, dashboard, viewer)
- Expo mobile app
- MCP server (canon resources + tools)
- AI embeddings + pgvector
- GitHub Actions CI/CD
- Canon visualization (TimelineJS, Mermaid, Leaflet)

**Decision Framework**: When to implement deferred features (based on actual bottlenecks, not speculation).

**Why**: ARCHITECTURE.md reads like completed work; this document clarifies reality. Prevents confusion for future contributors or co-authors.

---

### 5. `feat(book1): add chapter template with front matter schema`
**Hash**: `4412203`  
**Files**: `book1/chapters/_TEMPLATE.md` (new)

Chapter template ensuring consistent structure and metadata:

**Front Matter (YAML)**:
```yaml
title: "Chapter Title"
book: 1
chapter: 0
pov: "Character Name"
location: "Setting"
date_story: "YYYY-MM-DD"
word_count_target: 3500
status: "outline" | "draft" | "revised" | "final"
tags: []
canon_refs: [list of lore files]
notes: ""
```

**Checklists**:
- Canon Consistency: character voices, dates, tech details, locked facts
- Prose Quality: Vale linting, passive voice, POV maintenance

**Structure Suggestions**:
- Opening hook (250 words)
- Scene development (2000 words)
- Rising tension (700 words)
- Chapter climax/cliffhanger (550 words)

**End Notes**:
- Canon additions (new facts for lore/)
- Continuity questions (uncertainties)
- Revision priorities

**Why**: Standardized template accelerates drafting, ensures metadata consistency, and embeds editorial reminders directly in chapters.

---

## Files Created/Modified

| File | Type | Purpose |
|------|------|---------|
| `.github/copilot-instructions.md` | New | Workspace-wide Copilot instructions |
| `.vale.ini` | New | Vale prose linting config |
| `.vale/styles/Vocab/GrayArea/accept.txt` | New | Custom vocabulary (accepted spellings) |
| `.vale/styles/Vocab/GrayArea/reject.txt` | New | Deprecated spellings |
| `docs/IMPLEMENTATION_STATUS.md` | New | Reality check on implemented vs. planned features |
| `book1/chapters/_TEMPLATE.md` | New | Chapter front matter + structure template |

**Total Changes**: 6 new files, ~460 lines of code/docs

---

## Testing & Validation

### What's Been Done
- ✅ Files created and committed with conventional commit messages
- ✅ Explicit file staging (no `git add -A`)
- ✅ All commits follow the project's conventional commit format

### What Needs Testing
- ⏳ Vale linting (need to install Vale, then run: `vale book1/chapters/`)
- ⏳ Chapter template (use it for Chapter 01 draft to validate front matter schema)
- ⏳ Copilot-instructions behavior (verify Copilot applies rules in all future sessions)

### Success Criteria (for full merge)
- [ ] Vale successfully lints existing chapters with no errors on custom vocabulary
- [ ] Chapter 01 draft created using template passes Vale linting
- [ ] Front matter schema validated against first real chapter
- [ ] Copilot applies conventional commits in next coding session

---

## Next Steps

### Immediate (This Week)
1. Install Vale locally: `brew install vale` (Mac) or `choco install vale` (Windows)
2. Test Vale on existing chapters: `vale book1/chapters/`
3. Adjust `.vale.ini` if needed (e.g., word count limits per chapter)
4. Review IMPLEMENTATION_STATUS.md and confirm accuracy

### Medium-term (Weeks 2-4)
1. Draft Chapters 1-3 using template
2. Run Vale on drafts and iterate on vocabulary/rules
3. Add pre-commit hooks to enforce Vale + YAML validation
4. Validate chapter front matter schema in CI

### Long-term (Post Book 1 Draft)
1. Evaluate whether git+Markdown is sufficient or if Supabase is needed
2. Decide on GitHub Actions CI/CD (depends on co-authoring needs)
3. Plan MCP server only if real-time canon checking becomes bottleneck

---

## Decision Points Embedded in PR

**For the Reviewer:**

1. **Vale Scope**: Current config is conservative (write-good rules as suggestions, not errors). Should we be more aggressive (passive voice as errors)? Or keep permissive for creative freedom?

2. **Vocabulary Expansion**: Should GrayArea vocabulary be expanded before merging? (Currently ~25 terms; may need more as writing progresses.)

3. **Chapter Template Word Counts**: Suggested structure totals ~3500 words. Should this vary by chapter? (Act 1 may be shorter, Act 3 longer.)

4. **Deferred Features**: Does IMPLEMENTATION_STATUS.md accurately reflect priorities? Any features that should move from "Phase 2" to "immediate"?

---

## Merge Checklist

- [ ] Vale configuration reviewed (word count targets, rule severity)
- [ ] GrayArea vocabulary approved (character names, tech terms)
- [ ] IMPLEMENTATION_STATUS.md aligns with project priorities
- [ ] Chapter template front matter validated against TOC
- [ ] Copilot-instructions understood and agreed upon
- [ ] Ready to push to `main` or `baseline`

---

**Author Notes**:
This branch implements the "immediate" recommendations from STORY-AS-CODE-FEEDBACK.md Section "SHORT-TERM (Next 2-4 Weeks)". All commits follow conventional commit discipline. No `git add -A` was used; files were staged explicitly by path. Ready for code review before pushing.
