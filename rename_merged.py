#!/usr/bin/env python3
from pathlib import Path

raw_dir = Path('lore/raw')

# All consolidated files/dirs to rename
items_to_rename = [
    # Isaac.md
    '21-Isaac-Steals-Jason-Prime',
    '23-Isaac-Hiding-Jason-Prime-Degradation',
    '34-Isaac-Hospital-Deathbed-Smartwatch-Gift',
    '37-Jason-Prime-Hardware-Decay-Migration-to-Isaac',
    # Leandro.md
    '25-Coma-Patient-First-Human-Host',
    '26-Alejandro-Brazilian-Zika-Baby-Brother',
    '27-Alejandro-Adolescence-Rebellion-Withdrawal',
    '32-Chess-Gaming-Event-DeeJay-Meets-Alejandro',
    '33-Accidental-Transfer-Alejandro-DeeJay-Seizure',
    '76-Daneel-Kinship-Ambivalence-Alejandro-Parallel',
    # DeeJay.md
    '28-DeeJay-Drifter-Host',
    '31-DeeJay-Runaway-16-17-Tech-Prodigy',
    '62-DeeJay-Cohabitation-Arc',
    '65-DeeJay-Age-Timeline-Calculation',
    '66-DeeJay-AI-Construct-Humanoid-Form',
    '67-DeeJay-Human-Supremacy-Advocate',
    '68-DeeJay-Engineered-Persistence-Backups',
    '69-DeeJay-Book1-Strategy-Not-Villain-Climax',
    '70-DeeJay-Book1-Reveal-Timing',
    # Foundation.md
    '29-Foundation-Hybrid-Religious-Industrial',
    '41-Foundation-Doctrine-Host-Training-Protocol',
    '43-Foundation-Host-Schism-Disgruntled-Former-Hosts',
    '44-Foundation-Host-Viability-Age-Window',
    '63-Former-Foundation-Hosts-Defect-to-DeeJay',
    # Daneel.md
    '38-Daneel-Chronological-Canon-Event-List',
    '39-Daneel-Host-Final-Arc-by-Host',
    '40-Daneel-Cognitive-Architecture-Model',
    # Eli.md
    '49-NZ-Echo-Event-Eli-Age-10',
    '50-Eli-Cyborg-Hybrid-Legal-Human',
    '52-Eli-Foundation-Shadow-Influence-Arc',
    '74-Eli-Daneel-Entity-Connection-Bridge',
    # Entity.md
    '72-Unknown-Entity-Not-Alien-Origin',
    '73-Entity-Recognition-Familiarity-Daneel',
    '75-Entity-Extinction-Tragic-Containment',
    # Timeline.md
    '42-Global-Political-Timeline-Robot-War-Treaty',
    '60-Post-X20-World-Realignment-Timeline',
    # Characters
    '77-Final-Encounter-GCT-Scene',
    # .md file
    'driver_passenger_dynamic.md'
]

count = 0
for name in items_to_rename:
    old_path = raw_dir / name
    if old_path.exists():
        new_path = raw_dir / f'merge-{name}'
        old_path.rename(new_path)
        count += 1
        print(f'✓ {count}. {name}')

print(f'\n✅ Done! Renamed {count} items.')
