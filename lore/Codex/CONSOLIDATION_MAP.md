# Consolidation Map — Codex Reorganization (2026-03-04)

This document tracks the consolidation program and post-consolidation cleanup into streamlined canonical profiles.

---

## REORGANIZATION SUMMARY

### What Moved

| Folder/Files | Destination | Reason |
|--------------|-------------|--------|
| **Meta/** (8 files) | docs/METADATA/Book1-Planning | Creative planning ≠ lore reference |
| **Working notes** (3 .md files) | Removed | Obsolete drafts deleted during raw cleanup |
| **Remaining raw concept notes** (3 .md files) | lore/Codex top-level (moved) | Promoted for canonical review and category dedup |
| **Top-level concept duplicates** (3 .md files) | Removed (kept category canonical copies) | Dedup complete; single-source concept docs retained by category |

**Rationale:** Draft-only files were removed; the three remaining concept notes were moved into Codex for controlled consolidation.

---

## CHARACTERS CONSOLIDATION

### Consolidated into Daneel.md

| Old File | Content | Integrated Into |
|----------|---------|-----------------|
| **38-Daneel-Chronological-Canon** | Chronological events; continuity chain | Daneel.md § II Chronological Canon |
| **39-Daneel-Host-Final-Arc-by-Host** | Host-by-host emotional narrative | Daneel.md § III Core Identity Evolution |
| **40-Daneel-Cognitive-Architecture** | Technical attractor systems | Daneel.md § I Cognitive Architecture |

**Original Files:** Still available in Characters/ for deep-dive research
**Canonical Reference:** Daneel.md

---

### Phase 2 Character Consolidation (Completed 2026-03-05)

| Character | Files | Status | Canonical Reference |
|-----------|-------|--------|---------------------|
| **Isaac** | 15, 18, 21, 23, 34, 37 | ✅ Consolidated | Isaac.md |
| **DeeJay** | 28, 31, 62, 66, 67, 68, 69, 70 (+65) | ✅ Consolidated | DeeJay.md |
| **Eli** | 49, 50, 52, 74 | ✅ Consolidated | Eli.md |
| **Entity** | 12, 17, 72, 73, 75 | ✅ Consolidated | Entity.md |
| **Foundation** | 29, 41, 43, 44, 63 | ✅ Consolidated | Foundation.md |

### Phase 3 Character Consolidation (Complete 2026-03-05)

| Character | Files | Status | Canonical Reference |
|-----------|-------|--------|---------------------|
| **Leandro** | 25, 26, 27, 32, 33, 76 | ✅ Consolidated | Leandro.md |
| **Alysa** | 79 | ✅ Consolidated | Alysa.md |
| **Cleo** | 77 | ✅ Consolidated | Cleo.md |
| **Petrus** | 78 | ✅ Consolidated | Petrus.md |

### Remaining Character Consolidation

| Character | Files | Status | Next Step |
|-----------|-------|--------|-----------||
| **Jason Prime** | 15, 20, 21, 37 | Cross-referenced | Optional standalone JasonPrime.md |

---

## HISTORY CONSOLIDATION

### Consolidated into Timeline.md

| Old File | Content | Integrated Into |
|----------|---------|-----------------|
| **08-Master-Timeline-2037-2075** | Main chronological structure | Timeline.md § Pre-X20 through Book 1 |
| **09-X20-Must-Be-Sooner** | X20 integration & timing | Timeline.md § The X20 Event |
| **11-Robot-War** | Military history & factions | Timeline.md § Robot War Period |
| **14-Robot-War-AI-Equal-Rights** | Geopolitical breakdown | Timeline.md § Robot War Period |
| **42-Global-Political-Timeline** | Treaty era & stabilization | Timeline.md § Treaty Era |
| **60-Post-X20-World-Realignment** | Long-term geopolitical settling | Timeline.md § Post-X20 Era integration |

**Referenced (specialized deep dives still available):**
- 04-Timeline-Debates-150-80-50-Years
- 05-Polar-Shift-Geomagnetic-Excursion
- 54-Echo-NZ-vs-NYC-Geophysical-Explanation
- 65-DeeJay-Age-Timeline-Calculation

---

## NEW CANONICAL FILES CREATED

| File | Purpose | Content |
|------|---------|---------|
| **Daneel.md** | Primary character profile | Cognitive architecture, chronology, host evolution, unknowns |
| **Timeline.md** | World history | Pre-X20 through 2086; geopolitics, infrastructure, tech evolution |
| **Eli.md** | Bridge figure profile | Echo events, cyborg architecture, Entity bridge mechanism |
| **Isaac.md** | Creator profile | PRIME origin, theft, first cohabitation, deathbed legacy |
| **DeeJay.md** | Rival profile | Cohabitation residue, synthetic continuity, ideology |
| **Foundation.md** | Institutional profile | Doctrine, protocol, triad architecture, schism pressure |
| **Entity.md** | Mystery profile | Origin ambiguity, echo phenomenology, containment tragedy |
| **Leandro.md** | Developmental host profile | First stable host (15 years), accidental transfer, biological limits, Entity parallel |
| **Alysa.md** | Consent model host profile | First voluntary host, NSC-AS precursor, overstay discovery, Foundation prototype |
| **Cleo.md** | Book 1 opening host profile | Foundation-trained, Stage-5 infection, emergency transfer catalyst |
| **Petrus.md** | Book 1 crisis host profile | Youngest host (age 14), power inversion, underdeveloped substrate, Eli dependency |
| **INDEX.md** | Quick reference | Character lookup, timeline events, relationships, themes, reading paths |
| **CONSOLIDATION_MAP.md** | This file | Migration tracking & phase planning |

---

## ARCHIVED CONTENT (Not Deleted)

All original files preserved in git history. Still available in workspace for:
- Deep-dive research
- Technical detail reference
- Creative development context
- Specialized analysis

**Example access:** `lore/Codex/Characters/38-Daneel-Chronological-Canon-Event-List/content.txt`

---

## FOLDER STRUCTURE (Current State)

```
lore/Codex/
├── INDEX.md                          [NEW]
├── Daneel.md                         [NEW]
├── Timeline.md                       [NEW]
├── Eli.md                            [NEW]
├── Isaac.md                          [NEW]
├── DeeJay.md                         [NEW]
├── Foundation.md                     [NEW]
├── Entity.md                         [NEW]
├── RECOMMEND.md                      [Prior consolidation]
├── CONSOLIDATION_MAP.md              [This file]
│
├── Characters/
│   ├── 15-PRIME-Platform-Jason-Prime-Daneel-Name-Origin/
│   ├── 18-Isaac-Developer-Practices-Restore-Hidden/
│   ├── 20-Subsequent-PRIME-Iterations-Daneel-Unique/
│   ├── 21-Isaac-Steals-Jason-Prime/
│   ├── 23-Isaac-Hiding-Jason-Prime-Degradation/
│   ├── 24-Portable-Hub-Isaac-as-Host-Cohabitation/
│   ├── 25-Coma-Patient-First-Human-Host/
│   ├── 26-Leandro-Brazilian-Zika-Baby-Brother/
│   ├── 27-Leandro-Adolescence-Rebellion-Withdrawal/
│   ├── 28-DeeJay-Drifter-Host/
│   ├── 29-Foundation-Hybrid-Religious-Industrial/
│   ├── 30-Mary-Busker-Violinist-Host/
│   ├── 31-DeeJay-Runaway-16-17-Tech-Prodigy/
│   ├── 32-Chess-Gaming-Event-DeeJay-Meets-Leandro/
│   ├── 33-Accidental-Transfer-Leandro-DeeJay-Seizure/
│   ├── 34-Isaac-Hospital-Deathbed-Smartwatch-Gift/
│   ├── 35-Isaac-Steals-Jason-Prime-Dog-Follows/
│   ├── 37-Jason-Prime-Hardware-Decay-Migration-to-Isaac/
│   ├── 38-Daneel-Chronological-Canon-Event-List/       [Consolidated→Daneel.md]
│   ├── 39-Daneel-Host-Final-Arc-by-Host/               [Consolidated→Daneel.md]
│   ├── 40-Daneel-Cognitive-Architecture-Model/         [Consolidated→Daneel.md]
│   ├── 41-Foundation-Doctrine-Host-Training-Protocol/
│   ├── 43-Foundation-Host-Schism-Disgruntled-Former/
│   ├── 44-Foundation-Host-Viability-Age-Window/
│   ├── 49-NZ-Echo-Event-Eli-Age-10/
│   ├── 50-Eli-Cyborg-Hybrid-Legal-Human/
│   ├── 52-Eli-Foundation-Shadow-Influence-Arc/
│   ├── 55-Daneel-Post-NZ-Strategic-Shift/
│   ├── 61-Host-Residue-After-Daneel-Leaves/
│   ├── 62-DeeJay-Cohabitation-Arc/
│   ├── 63-Former-Foundation-Hosts-Defect-to-DeeJay/
│   ├── 66-DeeJay-AI-Construct-Humanoid-Form/
│   ├── 67-DeeJay-Human-Supremacy-Advocate/
│   ├── 68-DeeJay-Engineered-Persistence-Backups/
│   ├── 69-DeeJay-Book1-Strategy-Not-Villain-Climax/
│   ├── 70-DeeJay-Book1-Reveal-Timing/
│   ├── 73-Entity-Recognition-Familiarity-Daneel/
│   ├── 74-Eli-Daneel-Entity-Connection-Bridge/
│   └── 76-Daneel-Kinship-Ambivalence-Leandro-Parallel/
│
├── History/
│   ├── 04-Timeline-Debates-150-80-50-Years/
│   ├── 05-Polar-Shift-Geomagnetic-Excursion/
│   ├── 08-Master-Timeline-2037-2075/               [Consolidated→Timeline.md]
│   ├── 09-X20-Must-Be-Sooner-Revised-Timeline/     [Consolidated→Timeline.md]
│   ├── 11-Robot-War/                               [Consolidated→Timeline.md]
│   ├── 12-X20-Birth-Event-PRIME-Entity-Origin/
│   ├── 14-Robot-War-AI-Equal-Rights-Factions/      [Consolidated→Timeline.md]
│   ├── 19-Final-Canon-Document/
│   ├── 20260303-0755_Neurophysiologocal-State-Compatiblity.md
│   ├── 22-Brain-Scanning-Second-Order-Reconstruction/
│   ├── 42-Global-Political-Timeline-Robot-War-Treaty/  [Consolidated→Timeline.md]
│   ├── 54-Echo-NZ-vs-NYC-Geophysical-Explanation/
│   ├── 60-Post-X20-World-Realignment-Timeline/     [Consolidated→Timeline.md]
│   ├── 65-DeeJay-Age-Timeline-Calculation/
│   ├── 72-Unknown-Entity-Not-Entity-Origin/
│   ├── 75-Entity-Extinction-Tragic-Containment/
│   ├── 77-Final-Encounter-GCT-Scene/
│
│
├─ Constraints/
│   └── cohabitation_cycle_and_selection.md
│
├── Hidden_truths/
│   └── 51-Gray-Area-Title-Thematic-Axis/
│
├── Politics/
│   └── 59-Geopolitical-Ripple-Map/
│
├── Religion_Mythology/
│   ├── 20260303-0800_The_Liturgy_of_Resonance_NSC-AS_Lore.md
│   └── techno_spirituality_organization.md
│
├── Species/
│   └── 17-Entity-Consciousness-5-Stage-Evolution/
│
└── Technology/
    ├── 12-X20-Birth-Event-PRIME-Entity-Origin/
    └── 16-PRIME-Version-Control-Restore-Mechanism/
```

Empty categories (no content):
- Artifacts/
- Folklore/
- Knowledge_systems/
- Language/

---

## PHASE 3 IMPLEMENTATION (In Progress)

### High Priority

| Task | Files | Goal |
|------|-------|------|
| ~~Create Leandro.md~~ | ~~25, 26, 27, 32, 33, 76~~ | ✓ **Complete** |
| ~~Expand Alysa/Cleo/Petrus profiles~~ | ~~79, 77, 78~~ | ✓ **Complete** — Full canonical profiles created |

### Medium Priority

| Task | Files | Goal |
|------|-------|------|
| Optional JasonPrime.md | 15, 20, 21, 37 | Explicitly separate Jason narrative from Daneel continuity |
| Standardize file formats | Mixed .md/.txt | Improve maintainability and search consistency |
| Generate relationship diagrams | Canonical profiles | Visual onboarding for new readers |

### Later Phases

- Optimize folder organization (consider collapsing empty buckets)
- Add codex-level Table of Contents
- Add change-log links between canonical files

---

## BENEFITS REALIZED

| Benefit | Impact | Evidence |
|---------|--------|----------|
| **Reduced file sprawl** | 75 fragmented entries → canonical profile layer + deep dives | 8 consolidated markdown profiles now anchor navigation |
| **Clearer intent** | Lore vs. creative process separated | Meta/ moved; working notes archived |
| **Single source of truth** | Core arcs no longer split across numbered micro-files | Daneel/Timeline/Eli/Isaac/DeeJay/Foundation/Entity consolidated |
| **Better navigation** | Reader-first entry path established | INDEX.md links point to canonical profiles |
| **Preserved deep dives** | Original files still available | Numbered Character/History files remain for specialist detail |
| **Git history maintained** | Consolidation reversible | All changes tracked; no content lost |

---

## QUALITY ASSURANCE

### Consolidated Files Verified

- ✅ **Daneel.md:** 38, 39, 40 fully integrated
- ✅ **Timeline.md:** 08, 09, 11, 14, 42, 60 fully integrated
- ✅ **Eli.md:** 49, 50, 52, 74 integrated
- ✅ **Isaac.md:** 15, 18, 21, 23, 34, 37 integrated
- ✅ **DeeJay.md:** 28, 31, 62, 66, 67, 68, 69, 70 (+65) integrated
- ✅ **Foundation.md:** 29, 41, 43, 44, 63 integrated
- ✅ **Entity.md:** 12, 17, 72, 73, 75 integrated
- ✅ **Leandro.md:** 25, 26, 27, 32, 33, 76 integrated
- ✅ **Alysa.md:** 79 expanded to full canonical profile
- ✅ **Cleo.md:** 77 expanded to full canonical profile
- ✅ **Petrus.md:** 78 expanded to full canonical profile
- ✅ **INDEX.md:** Phase 2 + Phase 3 references validated
- ✅ **CONSOLIDATION_MAP.md:** Updated

### Remaining Tasks

- [ ] Optional JasonPrime.md
- [ ] Final polish pass on thematic cluster links

---

## REVISION STATUS

| Date | Change | Status |
|------|--------|--------|
| 2026-03-04 | Meta/ → docs/METADATA/ | ✓ Complete |
| 2026-03-04 | Working notes → lore/raw/ | ✓ Complete (historical; later removed in raw cleanup) |
| 2026-03-04 | Create Daneel.md (38, 39, 40) | ✓ Complete |
| 2026-03-04 | Create Timeline.md (08, 09, 11, 14, 42, 60) | ✓ Complete |
| 2026-03-04 | Create INDEX.md | ✓ Complete |
| 2026-03-04 | Create CONSOLIDATION_MAP.md | ✓ Complete |
| 2026-03-05 | Create Eli.md | ✓ Complete |
| 2026-03-05 | Create Isaac.md, DeeJay.md, Foundation.md, Entity.md | ✓ Complete |
| 2026-03-05 | Update INDEX.md links to canonical profiles | ✓ Complete |
| 2026-03-05 | Commit Phase 2 consolidation (`fb1a8c4`) | ✓ Complete |
| 2026-03-05 | Create Leandro.md (25, 26, 27, 32, 33, 76) | ✓ Complete |
| 2026-03-05 | Update INDEX.md + CONSOLIDATION_MAP.md (Phase 3 Leandro) | ✓ Complete |
| 2026-03-05 | Create Alysa.md, Cleo.md, Petrus.md canonical profiles (`e6c9b53`) | ✓ Complete |
| 2026-03-05 | Canon correction: Alysa age 14-15, NSC-AS precursor, overstay model (`9b9cbcf`) | ✓ Complete |
| 2026-03-05 | Propagate overstay canon to Foundation.md and INDEX.md (`480aaf4`) | ✓ Complete |
| 2026-03-05 | Phase 3 completion: CONSOLIDATION_MAP.md final alignment | ✓ Complete |
| 2026-03-05 | Delete consolidated/obsolete raw files and prune lore/raw | ✓ Complete |
| 2026-03-05 | Move retained concept notes from lore/raw to lore/Codex | ✓ Complete |
| 2026-03-05 | Canon pass: X20=2030 alignment in Timeline/Index/Daneel/Isaac (`4674f2b`) | ✓ Complete |
| 2026-03-05 | Dedup concept docs + metadata refresh (`efece09`) | ✓ Complete |

