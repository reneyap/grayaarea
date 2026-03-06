import os
import re

root_dir = 'lore/Codex'

def update_content(content):
    # Replace Alejandro -> Leandro
    content = re.sub(r'\bAlejandro\b', 'Leandro', content)
    content = re.sub(r'\bALEJANDRO\b', 'LEANDRO', content)
    content = re.sub(r'\balejandro\b', 'leandro', content)

    # Replace Alien -> Entity
    content = re.sub(r'\bAlien\b', 'Entity', content)
    content = re.sub(r'\bALIEN\b', 'ENTITY', content)
    content = re.sub(r'\balien\b', 'entity', content)

    # Replace 2025 -> 2037
    content = content.replace('2025', '2037')

    # Replace "Toxic/Submerged Manhattan" -> "Retired (Civic Vote) Manhattan"
    content = re.sub(r'(?i)toxic\s+manhattan', 'Retired (Civic Vote) Manhattan', content)
    content = re.sub(r'(?i)submerged\s+manhattan', 'Retired (Civic Vote) Manhattan', content)

    return content

# Read and update all text files
for root, dirs, files in os.walk(root_dir):
    for f in files:
        if not f.endswith(('.txt', '.md')): continue
        filepath = os.path.join(root, f)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            try:
                content = file.read()
            except UnicodeDecodeError:
                continue
                
        new_content = update_content(content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)

# Rename directories bottom-up
for root, dirs, files in os.walk(root_dir, topdown=False):
    for d in dirs:
        new_d = d.replace('Alejandro', 'Leandro').replace('Alien', 'Entity').replace('2025', '2037')
        if new_d != d:
            os.rename(os.path.join(root, d), os.path.join(root, new_d))

print("Lore Codex updated.")
