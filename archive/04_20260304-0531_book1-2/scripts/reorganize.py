import os
import shutil
import re

root = r"C:\Users\reney\OneDrive\Desktop\AwNi\Rene\GrayArea"

# 1. Move discuss-20260301.txt to source/
transcript = os.path.join(root, "discuss-20260301.txt")
if os.path.exists(transcript):
    shutil.move(transcript, os.path.join(root, "source", "discuss-20260301.txt"))
    print("OK: discuss-20260301.txt -> source/")
else:
    print("SKIP: transcript already moved")

# 2. Move all ##-* topic folders to lore/
lore_dir = os.path.join(root, "lore")
moved = 0
for name in os.listdir(root):
    if re.match(r"^\d{2}-", name):
        src = os.path.join(root, name)
        if os.path.isdir(src):
            shutil.move(src, os.path.join(lore_dir, name))
            moved += 1

print(f"OK: {moved} topic folders -> lore/")

# 3. Report final state
print("\n=== ROOT ===")
for name in sorted(os.listdir(root)):
    if not name.startswith("."):
        print(f"  {name}/")

print(f"\n=== lore/ ({len(os.listdir(lore_dir))} items) ===")
print(f"\n=== book1/ ===")
for dirpath, dirnames, filenames in os.walk(os.path.join(root, "book1")):
    level = dirpath.replace(root, "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(dirpath)}/")
    if level < 2:
        subindent = "  " * (level + 1)
        for f in filenames[:3]:
            print(f"{subindent}{f}")
        if len(filenames) > 3:
            print(f"{subindent}... ({len(filenames)} files total)")

print("\nDONE")
