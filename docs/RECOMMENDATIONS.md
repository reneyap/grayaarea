# GrayArea — Next Steps Recommendations

**Date:** 2026-03-05  
**Status:** Post-merge (`feat/immediate-recommendations` merged to main)  
**Prepared for:** Book 1 Drafting Phase

---

## Executive Summary

The `feat/immediate-recommendations` branch successfully merged, establishing foundational tooling and documentation. The infrastructure is ready for prose drafting. **Three priority actions** unlock the next phase without speculation.

---

## 🥇 Priority 1: Validate the Prose Workflow (This Week)

**Goal**: Draft Chapters 1–5 (Act 1) to pressure-test your setup  
**Rationale**: Infrastructure exists; prose drafting reveals blind spots documentation can't show

### What to Do

1. Open [book1/chapters/01_Old_Grand_Central.md](book1/chapters/01_Old_Grand_Central.md)
   - This is your anchor chapter (Eli POV, Grand Central scene, story opens here)
   - Use [lore/Codex/Eli.md](lore/Codex/Eli.md) and [lore/Codex/Timeline.md](lore/Codex/Timeline.md) for consistency

2. Fill the YAML front matter using the template from [book1/chapters/_TEMPLATE.md](book1/chapters/_TEMPLATE.md)
   ```yaml
   title: "Old Grand Central"
   book: 1
   chapter: 1
   pov: "Elijah Williams"
   location: "Grand Central Terminal, Manhattan"
   date_story: "2254-09-17"
   word_count_target: 3500
   status: "draft"
   ```

3. Draft the prose (aim for ~1000 words minimum to test Vale linting)

4. Validate with Vale linting (see Priority 2)

5. Repeat for Chapters 2–5

### Why Now

- All lore is consolidated; you won't get mid-draft canon surprises
- Chapter template prevents rework cycle on metadata
- Word counts become **real** (not targets); informs Books 2–3 pacing
- First draft cycle tests whether the front matter schema fits your actual workflow

### Success Criteria

- ✅ Chapters 1–5 have prose drafts (word count within 20% of target)
- ✅ Zero Vale warnings on finalized prose
- ✅ No new canon additions needed (or all added to lore/ + git-tracked)
- ✅ Template confirms scalable to remaining 14 chapters

---

## 🥈 Priority 2: Install Vale & Test Linting (Today)

**Goal**: Confirm the prose tooling works before heavy drafting  
**Effort**: 5 minutes  
**Blocker**: If Vale doesn't work on Windows Git Bash, fix the config before writing heavily

### What to Do

1. Install Vale:
   ```bash
   # Windows (PowerShell/Admin or Chocolatey CLI)
   choco install vale
   
   # macOS
   brew install vale
   ```

2. Test on an existing chapter:
   ```bash
   cd /c/Users/reney/OneDrive/Desktop/AwNi/Rene/GrayArea
   vale book1/chapters/01_Old_Grand_Central.md
   ```

3. Review output
   - Expected: Warnings on passive voice, weasel words, repetition
   - Adjust `.vale.ini` if rules are too strict/loose
   - Confirm custom vocabulary (`accept.txt`, `reject.txt`) works

### Why Now

- The branch merged `.vale.ini` + custom vocab; **verify it actually runs**
- Windows Git Bash can have CLI issues; better to discover now
- Prose drafting cycle (Priority 1) depends on linting feedback

### Success Criteria

- ✅ `vale --version` runs without error
- ✅ `vale book1/chapters/` scans all chapters without crashes
- ✅ Custom GrayArea terms (Daneel, Attractor, X20) don't trigger false positives
- ✅ `.vale.ini` rules catch real issues (test with intentionally weak prose)

---

## 🥉 Priority 3: Decide on Phase 2 Architecture (This Sprint)

**Goal**: Resolve the design/execution gap for post-Book-1 work  
**Scope**: Supabase + Next.js + MCP vs. optimized git-only approach  
**Timeline**: Decision by end of sprint; implementation stays deferred until prose drafting stabilizes

### The Decision

**ARCHITECTURE.md proposes a full tech stack:**
- Supabase (PostgreSQL + pgvector)
- Next.js editor + dashboard
- MCP server for real-time canon checks
- Timeline visualization (TimelineJS, Leaflet maps)

**IMPLEMENTATION_STATUS.md shows what's real:**
- ✅ Git-based canon (Markdown lore, 11 profiles, CONSOLIDATION_MAP.md)
- ✅ Digital stratigraphy archive (immutable layers)
- 🚧 Chapter prose (outlines exist; drafting in progress)
- ⏳ All infrastructure (deferred to Phase 2)

### Two Paths Forward

#### **Path A: Git-Only Optimization** (Lower effort, sufficient through Book 1)
**When to choose**: You prioritize speed, work solo, and git/grep searches serve canon checks adequately

**Actions**:
- Add pre-commit hooks for Vale linting + YAML validation
- Create `scripts/canon_check.sh` to automate consistency audits
- Extend CONSOLIDATION_MAP.md with decision diffs per commit
- Tag milestones (e.g., `b1-draft1-v1.0`, `b1-draft2-v2.0`)

**Scaling limit**: Sufficient until ~50 chapters. By Book 2, grep returns 200+ matches; context becomes harder to parse.

#### **Path B: Full Stack** (Higher effort, enables collaboration + scale)
**When to choose**: You want queryable canon, collaborative co-authoring tools, or plan Book 2+ early visualization

**Actions**:
- Implement Supabase schema (tables: `characters`, `timeline_events`, `canon_facts`, `chapters`, `consistency_rules`)
- Build Next.js editor with character/timeline sidebars
- Implement MCP server exposing canon as resources + tools
- Add GitHub Actions CI/CD for Vale linting + import validation

**Scaling benefit**: By Book 3, canonical search ("all mentions of X") returns results <1s with ranked relevance, not grep output.

### Decision Framework

| Factor | Path A (Git-Only) | Path B (Full Stack) |
|--------|-------------------|-------------------|
| **Book 1 Completion Time** | Faster (no infra work) | Slower (build phase) |
| **Real-time Canon Checks** | Manual (grep-based) | Automated (MCP tools) |
| **Co-authoring** | Difficult (merge conflicts) | Native (database) |
| **Book 2/3 Feasibility** | Grinds at 50+ chapters | Scales cleanly |
| **Phase 2 Effort** | ~40 hours (scripts + API) | ~200 hours (full stack) |

### Recommendation

**Start with Path A (git-only optimization):**
- Complete Book 1 prose drafting and first revision cycle without infrastructure distractions
- Use scripted canon checks to validate consistency as you write
- Re-evaluate at `b1-draft1-v1.0` milestone (post-first-draft)
- Build Path B infrastructure if Book 2 timeline demands it

**Why**: You've proven that the git + Markdown approach works (11 profiles consolidated, 83 lore topics atomized, ISSUES.md generated). Adding database complexity before prose stabilizes is premature.

### Success Criteria

- ✅ Decision documented in a **decision log** (`docs/DECISION_LOG.md`)
- ✅ Path A: Pre-commit hooks installed; `scripts/canon_check.sh` written and tested
- ✅ Path B: Supabase schema finalized; Next.js scaffold created (no prose editor yet)

---

## Implementation Order

1. **This week** ⏱ Priority 2 (Vale validation) + Priority 1 start (draft Ch. 1–2)
2. **Next 2 weeks** 🎯 Complete Priority 1 (Ch. 1–5 drafted)
3. **Feature branch** 🔄 Create `feat/phase2-architecture` to prototype Path A or Path B
4. **Sprint end** 📋 Priority 3 decision committed to `docs/DECISION_LOG.md`

---

## References

- [docs/IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md) — what's actually implemented vs. planned
- [docs/STORY-AS-CODE-FEEDBACK.md](STORY-AS-CODE-FEEDBACK.md) — strengths/gaps analysis
- [book1/chapters/_TEMPLATE.md](../book1/chapters/_TEMPLATE.md) — chapter structure
- [lore/Codex/INDEX.md](../lore/Codex/INDEX.md) — canon reference index

---

## Questions?

- **Does Vale work on your machine?** (Priority 2 blocker)
- **Path A or Path B?** (Priority 3 decision)
- **Chapter order for drafting?** (Currently targeting Ch. 1 first; confirm if you prefer a different order)
