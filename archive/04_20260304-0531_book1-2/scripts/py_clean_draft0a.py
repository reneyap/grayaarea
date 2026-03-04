import os
import re

draft_dir = "book1/draft0a/chapters"

# Regex patterns to clean
patterns = [
    (r'<!-- merged from .*? -->', ''),  # Remove merge markers
    (r'\[\[.*?\]\]', ''),               # Remove [[...]] notes
    (r'\[\[\[.*?\]\]\]', ''),           # Remove [[[...]]] notes
    (r'/\*.*?\*/', '', re.DOTALL),      # Remove /* ... */ comments
    (r'\[Note to self:.*?\]', '', re.DOTALL), # Remove [Note to self:...]
    (r'\[From Tsets:.*?\]', '', re.DOTALL),   # Remove [From Tsets:...]
    (r'\[.*?STUB.*?\]', ''),            # Remove [STUB...]
]

# Rename map (old -> new)
rename_map = {
    "00_preface.md": "00_Prologue_The_Echo.md",
    "01_Chapter_1_Old_Grand_Central.md": "01_Old_Grand_Central.md",
    "02_Chapter_2_Sept_2274_NZ_220yr_X6.md": "02_Flashback_New_Zealand_2274.md",
    "03_Chapter_3_Cleo_Saraswati_Petrus.md": "03_Cleo_Saraswati_Petrus.md",
    "04_Chapter_4_Origins.md": "DELETE", # Empty
    "05_Chapter_0_The_X20_Event_2063_years.md": "04_Origin_X20_Event.md",
    "06_Chapter_1_Call_me_Daneel.md": "05_Call_Me_Daneel.md",
    "07_Chapter_2_The_Rubensteins_2023_2080.md": "06_The_Rubensteins.md",
    "08_Chapter_3_The_Tenant.md": "07_The_Tenant.md",
    "09_Chapter_4_STUB_Daneel_miniaturized_the_positronic_chamber_by.md": "08_The_Glasses.md",
    "10_Chapter_5_Coma_ward.md": "09_The_Coma_Ward.md",
    "11_Chapter_6_Christina_Leandro.md": "10_Christina_and_Leandro.md",
    "12_Chapter_7_Maurizio_Annabelle.md": "11_Maurizio_and_Annabelle.md",
    "13_Chapter_8_Leandro_DJ_Alyssa.md": "12_Leandro_DJ_Alyssa.md",
    "14_Chapter_9_Alyssa_visits_Leandro.md": "13_Alyssa_visits_Leandro.md",
    "15_Chapter_10_Leaving_Alyssa.md": "14_Leaving_Alyssa.md",
    "16_Chapter_8_Elementals.md": "15_Elementals.md", # Renumbering continuation
    "17_Chapter_9.md": "DELETE", # Empty
    "18_Chapter_10.md": "DELETE", # Empty
    "19_Chapter_11.md": "DELETE", # Empty
    "20_Chapter_12_Confronts_the_Alien.md": "16_Confronts_the_Alien.md",
}

for filename in os.listdir(draft_dir):
    if not filename.endswith(".md"):
        continue

    file_path = os.path.join(draft_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply cleaning
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Clean up excessive newlines created by removals
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Write back cleaned content (temp)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Rename/Delete
    if filename in rename_map:
        new_name = rename_map[filename]
        if new_name == "DELETE":
            os.remove(file_path)
            print(f"Deleted {filename}")
        else:
            new_path = os.path.join(draft_dir, new_name)
            os.rename(file_path, new_path)
            print(f"Renamed {filename} -> {new_name}")

