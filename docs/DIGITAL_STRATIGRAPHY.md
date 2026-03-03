# Digital Stratigraphy: The "Story-as-Sediment" Philosophy

## The Concept

"Digital Stratigraphy" treats the project history not as a single messy draft that gets overwritten, but as **distinct chronological layers of creative intent**. 

In physical stratigraphy, the deeper you dig, the older the era you find. Each layer represents a distinct period of time with its own environment, rules, and lifeforms. Applying this to `GrayArea` ensures that previous iterations of the story (e.g., the 2023 collaboration vs. the 2026 reboot) are preserved as foundational bedrock rather than overwritten mistakes.

## Implementation in GrayArea

We structure our repository like geological strata:

### Layer 0: The Bedrock (Legacy)
**Location:** `archive/00_2020-2023_original/` 
*   **Status:** Sealed. Inactive.
*   **Purpose:** Contains the raw, unrefined, and sometimes contradictory original manuscripts. This is the source material.
*   **Example:** Daneel is "born" (biological metaphor).

### Layer 1: The Analysis (Excavation & Atomization)
**Location:** `archive/01_20260301-02_discussion/`
*   **Status:** Active Reference. 
*   **Purpose:** Deconstruction. We break the bedrock into atomic elements (timelines, mechanics, specific debates).
*   **Method:** **Atomization.** Instead of long documents, we create specific folders for specific ideas (e.g., `01-Manhattan-Sinking-Mechanisms/`).
*   **Example:** Daneel "emerges" (digital metaphor). The debate on *how* happens here.

### Layer 2: The Synthesis (Construction)
**Location:** `book1/drafts/`
*   **Status:** Current Workspace.
*   **Purpose:** Reconstruction. Taking the refined atoms from Layer 1 and assembling them into the narrative flow of the final story.
*   **Method:** Chapter-by-chapter execution based on the "Truth" established in Layer 1.

## Why We Atomize (Drill-Down vs. Flattening)

We explicitly chose **not to flatten** the folder structure in Layer 1 (`archive/01...`). 

1.  **High-Fidelity Context:** A 50-page Word doc is a "Blob." It's hard to reference. A specific folder (`05-Polar-Shift...`) implies a "vertical slice" of a single idea.
2.  **Asset Encapsulation:** By using folders, we can store related artifacts (maps, physics calculations, character reaction notes) directly alongside the text file without cluttering the root directory.
3.  **Traceability:** It allows us to trace a specific idea upward through the layers (like following a fossil lineage). We can see exactly *where* and *when* a canon fact changed.

## The Prime Directive

**Preserve, Do Not Overwrite.**

*   If a core concept changes (e.g., the date of the X20 Event), do not simply edit the old file.
*   Create a new "Stratum" (e.g., `02_2026_Revised_Timeline/`) that supersedes the old one.
*   The old file remains as a record of the "Road Not Taken."

## Long-Term Vision: The Database Migration

The "Atomization" strategy is not just for file organization; it is a **pre-processing step for a future Knowledge Base**.

Eventually, the `GrayArea` repository will outgrow complex file trees. At that stage, the atomic units (currently folders like `05-Polar-Shift...`) will migrate into a structured **Graph or Relational Database** (e.g., Obsidian vault, Notion DB, or custom SQL).

### Why Stratigraphy Enabled this Future:
1.  **Structured Data:** Because we atomized early, we don't have to "unmangle" a 100,000-word manuscript later. The data is already chunked by topic.
2.  **Entity Mapping:** The "folder-as-entity" model maps directly to database records (Folder Name = Entity ID; Content = Description field).
3.  **Version Control:** The "strata" concept (Legacy vs. Current) becomes a simple version attribute in the database (`ver: 2020`, `ver: 2026`).

By organizing this way now, we are future-proofing the lore for when it needs to be queried, not just read.
