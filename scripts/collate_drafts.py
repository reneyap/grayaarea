#!/usr/bin/env python3
"""
Collate all ## Draft sections from book1/draft1a/chapters into a single markdown file
for easy reading as a short story or novella.
"""

import os
import re

SOURCE_DIR = r"book1/draft1a/chapters"
OUTPUT_FILE = r"book1/draft1a/GRAY_AREA_SHORT_STORY.md"
OMITTED_MARKER = "<!-- Begin prose draft below this line -->"

def collate_chapters():
    if not os.path.exists(SOURCE_DIR):
        print(f"Directory not found: {SOURCE_DIR}")
        return

    files = sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith(".md")])
    full_text = []
    
    # Add a main title
    full_text.append("# GRAY AREA: The Foundation Protocols\n\n> A compiled draft based on chapter vignettes and context.\n\n---\n")

    for filename in files:
        filepath = os.path.join(SOURCE_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # extract the title (first line usually)
        title_match = re.search(r"^# (.*)", content, re.MULTILINE)
        chapter_title = title_match.group(1).strip() if title_match else filename

        # extract text between ## Draft and ## Vignette (or end of file)
        # Regex explanation:
        # ## Draft\s+               -> Match the header and newline
        # (?:<!--.*?-->\s*)?        -> Non-capturing group for the optional HTML comment
        # (.*?)                     -> Capture the prose content (non-greedy)
        # (?=\n## Vignette|\Z)      -> Lookahead for the next section or end of string
        draft_match = re.search(r"## Draft\s+(?:<!--.*?-->\s*)?(.*?)(?=\n## Vignette|\Z)", content, re.DOTALL)
        
        if draft_match:
            prose = draft_match.group(1).strip()
            # If prose is empty, maybe add a placeholder?
            if not prose:
                prose = "*[Draft pending]*"
            
            # Format: 
            # ## Chapter Title
            # 
            # Prose...
            full_text.append(f"## {chapter_title}\n\n{prose}\n\n")
            print(f"Processed: {chapter_title}")
        else:
            print(f"Skipping {filename}: Could not find '## Draft' section.")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("\n".join(full_text))

    print(f"\nSuccessfully collated {len(files)} chapters into:\n{OUTPUT_FILE}")

if __name__ == "__main__":
    collate_chapters()
