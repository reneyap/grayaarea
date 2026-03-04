import os
import re

directory = "book1/draft0/chapters"
files = sorted([f for f in os.listdir(directory) if f.endswith(".md")])

for i, f in enumerate(files):
    # Strip leading number and underscore
    # e.g. 03_Chapter_1 -> Chapter_1...
    # e.g. 00_preface -> preface...
    
    match = re.match(r"^\d+_(.+)$", f)
    if match:
        base_name = match.group(1)
    else:
        base_name = f # Should not happen based on file list
        
    new_name = f"{i:02d}_{base_name}"
    
    # If the file names are already correct (e.g. 00_preface is 00_preface), this is fine.
    # 03_Chapter_1 becomes 01_Chapter_1.
    
    old_path = os.path.join(directory, f)
    new_path = os.path.join(directory, new_name)
    
    if old_path != new_path:
        os.rename(old_path, new_path)
        print(f"Renamed {f} -> {new_name}")
