# DISCREPANCIES — Active Issues & Resolutions

**Last Scan:** 2026-03-05 (Post-Consolidation Phase 3)  
**Status:** Major X20 date conflict identified; other timeline elements require alignment

---

## UNRESOLVED DISCREPANCIES

### 1. X20 Event Date — CRITICAL CONFLICT
**Issue:** Multiple canonical date references conflict

| Source | Stated Date | Context |
|--------|------------|---------|
| DISCREPANCIES.md (original, 2026-03-04) | **2037** | "Adjusted X20 to **2037**" |
| Timeline.md | **2030** | "THE X20 EVENT (2030)" section header; "Date: 2030" explicit |
| Daneel.md | 2030 (implied) | "X20 Breakpoint (2030)" |
| Isaac.md | 2030-2032 | "Post-X20 infrastructure chaos" context dated ~2032 |

**Impact:** If X20 is 2037 (per original directive), then **50-year gap to Story Present 2087 is correct**; if X20 is 2030, gap is **57 years**.

**Dependent Issues:**
- Leandro.md says born ~2032 "post-X20"; if X20 is 2037, this is pre-X20 ✗
- Timeline section "PRE-X20 ERA (2020-2030)" implies X20 at 2030
- Timeline section "THE RETREAT & COLLAPSE PHASE (2030-2077)" starts at 2030

**Resolution Required:** Decide canonical X20 date (2030 vs 2037); update all dependent timeline sections.

---

### 2. Leandro Birth Year Inconsistency (Dependent on X20)
**Issue:** Leandro.md states birth ~2032 with qualifier "post-X20"

- If X20 = 2030: ✓ Correct (2032 is post-X20)
- If X20 = 2037: ✗ Wrong (2032 is pre-X20)

**Leandro arc timeline:**
- Born ~2032
- Hosted Daneel ~15 years (2032-2047)
- Accidental seizure transfer ~2047 (age ~15 to DeeJay)

**Status:** Awaits X20 date resolution

---

### 3. Isaac Death Timeline
**Issue:** Isaac.md lacks explicit death date

**Current references:**
- "Deceased (~2037)" in INDEX.md
- "Post-X20 infrastructure chaos" context suggests ~2030-2032 timeframe
- Giving Leandro the smartwatch hub "Isaac's Hospital Gift" dated to enable infant transfer

**Candidate death window:**
- Early: ~2030-2032 (immediately post-X20)
- Late: ~2035-2037 (7 years post-X20)

**Impact:** Affects timeline of Daneel's substrate transfers (coma patient → Leandro sequence)

**Status:** Requires explicit timestamp in Isaac.md

---

### 4. Alysa Birth Year Verification
**Issue:** Multiple birth year references need cross-check

**Stated:** Born ~2060  
**Validation:**
- Age 14-15 at central park encounter: would be ~2074-2075 ✓
- Age 19-20 at departure: would be ~2079-2080 (duration ~5 years) ✓
- If X20 is 2037: Alysa born 2060 is 23 years post-X20
- If X20 is 2030: Alysa born 2060 is 30 years post-X20

**Status:** Internally consistent; awaits X20 date to verify gap semantics

---

### 5. Timeline Section Order Mismatch (Non-Critical)
**Issue:** Historical events in Timeline.md appear out of chronological sequence

**Sections in order as written:**
1. AI Urbanization Era (2043-2052) — BEFORE
2. Atlantic Circulation Instability (2052)
3. Superstorm Sequence (2056-2060) — THEN
4. **Geomagnetic Weakening Detection (2063-2065)** — AFTER
5. THE X20 EVENT (2030) — APPEARS LAST (but should be ~in sequence ~2030)

**Status:** Requires restructuring Timeline.md sections into chronological order

---

## VERIFIED CONSISTENCIES (Locked Across Consolidation)

### Character Ages & Timelines
- ✅ **Daneel:** ~50 years old (PRIME emergence 2037 → Book 1 2087) [confirmed across Daneel.md, INDEX.md]
- ✅ **Leandro:** 15-year host duration ~2032-2047 [Leandro.md self-consistent]
- ✅ **Alysa:** ~5-year host duration ~2075-2080, age trajectory 14-15→19-20 [Alysa.md, Daneel.md crossref]
- ✅ **Cleo:** Age 17 at Book 1 opening (~2085-2086) [Cleo.md]
- ✅ **Petrus:** Age 14 at emergency transfer (Book 1 climax ~2086) [Petrus.md]
- ✅ **Eli:** ~40-46 years old (born ~2038-2043); Echo 1 at age 10 (2048-2053); Echo 2 at Book 1 era [Eli.md, INDEX.md]

### Institutional Framework
- ✅ **Foundation Doctrine:** Overstay constraint + Triad continuity (Active/Alpha/Beta) [locked across Foundation.md, INDEX.md, all host profiles]
- ✅ **Cohabitation Protocol:** Consent-based, host driver default, Daneel passenger support bounded [Foundation.md]
- ✅ **Host Selection:** Recursive depth + emotional regulation + low dominance traits [Foundation.md, Petrus.md pre-transfer analysis]

### Transfer Mechanics
- ✅ **Transfer Types:** Controlled migration, accidental collapse shift, consent-based transfer [Daneel.md, all host transitions self-consistent]
- ✅ **Requirements Chain:** Host destabilization + hub + proximity + viable basin + release window [Daneel.md § Transfer Mechanics]

### Entity Ambiguity
- ✅ **Origin Preserved:** X20-linked persistence (emergent-from-physics vs. captured-fragment models both live) [Entity.md, Eli.md cross-confirmation]
- ✅ **Echo Phenomenology:** NZ 2050 (Echo 1) and Old Manhattan Book 1 era (Echo 2) architecture consistent [Eli.md, Entity.md alignment]

### Token Succession Ritual
- ✅ **Beanie→Pendant lineage:** Isaac → Leandro → Alysa → Cleo → Petrus [metaphorically tracked across Leandro, Alysa, Cleo, Petrus .md files]

---

## RESOLVED ITEMS (From 2026-03-04 Scan)

1. ✅ **Character Naming:** "Leandro" standardized for Host 4 (Zika-affected developmental host)
2. ✅ **Entity Terminology:** "The Entity / The Resonance" adopted (preserves ambiguity; no "Alien" label)
3. ✅ **Robot War Arc:** Integrated into Timeline.md (2055-2065 kinetic AI conflict phase)
4. ✅ **Old Manhattan Status:** Phased narrative (economically marginalizing → permanently flooded post-X20)
5. ✅ **Eli's Age Reconciliation:** Born ~2038-2043 (pre-X20); aged ~40-46 at Book 1 era; Echo 1 at age 10 (consistent with Charlene generational position)

---

## ACTION ITEMS

| Priority | Task | Owner | Target Date | Files |
|----------|------|-------|-------------|-------|
| CRITICAL | Resolve X20 date (2030 vs 2037) | Lore Lead | 2026-03-05 | Timeline.md, Daneel.md, all dependent profiles |
| CRITICAL | Update Leandro.md if X20 date changes | Content | 2026-03-05 | Leandro.md (line: "post-X20") |
| HIGH | Explicit Isaac death timestamp | Content | 2026-03-05 | Isaac.md (add § death narrative) |
| MEDIUM | Reorder Timeline.md chronologically | Editing | 2026-03-06 | Timeline.md (restructure sections) |
| LOW | Cross-verify all character birth years | QA | 2026-03-06 | INDEX.md (timeline table) |

---

## CONSOLIDATION IMPACT NOTES

**Post-Phase-3-Codex consolidation (2026-03-05):**
- 88 files deleted (raw/ directory pruned; 3 core concept files moved to Codex)
- 11 canonical profiles created/updated (Daneel, Isaac, Leandro, Alysa, Cleo, Petrus, DeeJay, Eli, Entity, Foundation, Timeline)
- Discovery: X20 date ambiguity surfaced during cross-profile consistency scan

**Consolidation validated these elements as locked:**
- All character ages internally self-consistent within individual profiles
- Institutional doctrine uniform across Foundation.md, all host profiles, INDEX.md
- Transfer mechanics canonical and deterministic
- Ambiguities properly preserved (Entity origin, hidden truths)

**No content lost; all changes tracked in git history.**

