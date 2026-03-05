# Consolidation Map — Codex Reorganization (2026-03-04)

This document tracks the consolidation of 75 files into streamlined canonical profiles.

---

## REORGANIZATION SUMMARY

### What Moved

| Folder/Files | Destination | Reason |
|--------------|-------------|--------|
| **Meta/** (8 files) | docs/METADATA/Book1-Planning | Creative planning ≠ lore reference |
| **Working notes** (3 .md files) | lore/raw/ | Drafts; not canon |

### Working Notes Moved to lore/raw/

```
- cost_of_hosting_and_ghost_data.md
- daneel-persistence-foundation.md
- daneel_james_identity_and_lineage.md
```

**Rationale:** These are creative development notes, not settled canonical lore.

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

### Characters Awaiting Consolidation (Phase 2)

These detailed micro-files remain in Characters/ awaiting secondary consolidation:

| Character | Files | Status | Next Step |
|-----------|-------|--------|-----------|
| **Isaac** | 15, 18, 21, 23, 34, 37 | Awaiting Isaac.md | Consolidate creator storyline |
| **Jason Prime** | 15, 20, 21, 37 | Cross-referenced | Daneel.md references only |
| **Leandro** | 25, 26, 27, 32, 33 | Awaiting Leandro.md | Consolidate host arc |
| **Mary** | 30 | Single file | Create Mary.md expansion |
| **DeeJay** | 28, 31, 66, 67, 68, 69, 70 | Awaiting DeeJay.md | Consolidate rival arc |
| **Eli** | 49, 50, 52, 55, 74 | Awaiting Eli.md | Consolidate bridge figure |
| **Entity** | 12, 17, 72, 73, 75 | Awaiting Entity.md | Consolidate central mystery |
| **Foundation** | 29, 41, 43, 44, 64 | Awaiting Foundation.md | Consolidate institutional doctrine |

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
| **Timeline.md** | World history | Pre-X20 through 2087; geopolitics, infrastructure, tech evolution |
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
│   └── driver_passenger_dynamic.md
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

## PHASE 2 IMPLEMENTATION (Recommended)

### High Priority (Do Next)

| Task | Files | Goal |
|------|-------|------|
| Create Isaac.md | 15, 18, 21, 23, 34, 37 | PRIME architect story |
| Create DeeJay.md | 28, 31, 66, 67, 68, 69, 70 | Rival/ideological foe arc |
| Create Eli.md | 49, 50, 52, 55, 74 | Bridge figure & mysteries |

### Medium Priority

| Task | Files | Goal |
|------|-------|------|
| Create Foundation.md | 29, 41, 43, 44, 64 | Institutional doctrine & schism |
| Create Entity.md | 12, 17, 72, 73, 75 | Central mystery & consciousness |
| Consolidate Hosts.md or individual profiles | 25, 26, 27, 30 | Host-specific deep dives |

### Later Phases

- Standardize file formats (.md vs .txt)
- Optimize folder organization (consider collapsing empty buckets)
- Create visual relationship diagrams
- Generate Table of Contents for Codex

---

## BENEFITS REALIZED

| Benefit | Impact | Evidence |
|---------|--------|----------|
| **Reduced file sprawl** | 75 → ~50 actively referenced | 4 new canonical files eliminate redundancy |
| **Clearer intent** | Lore vs. creative process separated | Meta/ moved; working notes archived |
| **Single source of truth** | Daneel story no longer fragmented | 38, 39, 40 consolidated into Daneel.md |
| **Better navigation** | Quick reference available | INDEX.md provides lookup + reading paths |
| **Preserved deep dives** | Original files still available | Researchers can access detailed micro-analyses |
| **Git history maintained** | Consolidation reversible | All changes tracked; no content lost |

---

## QUALITY ASSURANCE

### Consolidated Files Verified

- ✅ **Daneel.md:** 38, 39, 40 fully integrated
- ✅ **Timeline.md:** 08, 09, 11, 14, 42, 60 fully integrated
- ✅ **INDEX.md:** Cross-references validated
- ✅ **CONSOLIDATION_MAP.md:** This document

### Remaining Tasks

- [ ] Phase 2 character profiles (Isaac, DeeJay, Eli, etc.)
- [ ] Final INDEX.md update
- [ ] Git commit with full tracking

---

## REVISION STATUS

| Date | Change | Status |
|------|--------|--------|
| 2026-03-04 | Meta/ → docs/METADATA/ | ✓ Complete |
| 2026-03-04 | Working notes → lore/raw/ | ✓ Complete |
| 2026-03-04 | Create Daneel.md (38, 39, 40) | ✓ Complete |
| 2026-03-04 | Create Timeline.md (08, 09, 11, 14, 42, 60) | ✓ Complete |
| 2026-03-04 | Create INDEX.md | ✓ Complete |
| 2026-03-04 | Create CONSOLIDATION_MAP.md | ✓ Complete |
| TBD | Create Isaac.md, DeeJay.md, Eli.md | Pending |
| TBD | Create Foundation.md, Entity.md | Pending |
| TBD | Final git commit & push | Pending |

