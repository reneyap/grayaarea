import os
import re

directory = "book1/draft0/chapters"
files = sorted([f for f in os.listdir(directory) if f.endswith(".md")])

current_chapter_file = None
files_to_remove = []
merged_content_map = {} # Map filename to content

# First pass: Determine which file belongs to which chapter
# and accumulate content in memory (or just record the list of files to merge)

chapter_groups = []
current_group = []

# Special handling for potentially non-chapter starts (like 01, 02 if 00 didn't exist)
# But we know 00_preface exists.

for f in files:
    is_chapter = "_Chapter_" in f or "preface" in f.lower()
    
    if is_chapter:
        if current_group:
            chapter_groups.append(current_group)
        current_group = [f]
    else:
        if not current_group:
            # If we have files before the first chapter, create a dummy group or attach to first
             current_group = [f] # This handles the case if 00 is not a chapter, but 00 is preface so it is.
        else:
            current_group.append(f)

if current_group:
    chapter_groups.append(current_group)

# Now process the groups
for group in chapter_groups:
    base_file = group[0]
    print(f"Processing chapter group based on: {base_file}")
    
    full_content = ""
    
    # Read base file
    with open(os.path.join(directory, base_file), "r", encoding="utf-8") as bf:
        full_content += bf.read()
    
    # Read and append others
    for sub_file in group[1:]:
        print(f"  Appending {sub_file}")
        with open(os.path.join(directory, sub_file), "r", encoding="utf-8") as sf:
            content = sf.read()
            # Add some spacing and a marker to indicate origin, but keep it clean
            full_content += f"\n\n<!-- merged from {sub_file} -->\n\n"
            full_content += content
        files_to_remove.append(sub_file)
        
    # Write back to base file
    with open(os.path.join(directory, base_file), "w", encoding="utf-8") as bf:
        bf.write(full_content)

# Remove the consolidated files
for f in files_to_remove:
    try:
        os.remove(os.path.join(directory, f))
        print(f"Removed {f}")
    except OSError as e:
        print(f"Error removing {f}: {e}")
