import os

root = r"C:\Users\reney\OneDrive\Desktop\AwNi\Rene\GrayArea\book1\chapters"

chapters = [
    ("03", "act1", "ACT I — Instability",   "The Wanderer's Return"),
    ("04", "act1", "ACT I — Instability",   "Containment Protocol"),
    ("05", "act1", "ACT I — Instability",   "Human Supremacy"),
    ("06", "act2", "ACT II — Pattern",      "Residual Noise"),
    ("07", "act2", "ACT II — Pattern",      "The First Echo"),
    ("08", "act2", "ACT II — Pattern",      "Infrastructure"),
    ("09", "act2", "ACT II — Pattern",      "Phase Lock"),
    ("10", "act2", "ACT II — Pattern",      "Public Narrative"),
    ("11", "act3", "ACT III — Escalation",  "Patient Zero"),
    ("12", "act3", "ACT III — Escalation",  "Cavity"),
    ("13", "act3", "ACT III — Escalation",  "Recursive Depth"),
    ("14", "act3", "ACT III — Escalation",  "Overload"),
    ("15", "act3", "ACT III — Escalation",  "The Triage"),
    ("16", "act4", "ACT IV — Alignment",    "Convergence"),
    ("17", "act4", "ACT IV — Alignment",    "The Bridge"),
    ("18", "act4", "ACT IV — Alignment",    "Detuning"),
    ("19", "act4", "ACT IV — Alignment",    "Collapse"),
]

STUB = """# Chapter {num}: {title}

**{act}**

> Status: STUB
> Word target: ~3,500
> POV: TBD
> Timeline position: TBD

---

## Notes

<!-- Add scene beats, character entrances, setting details here -->

---

## Draft

<!-- Begin prose draft below this line -->
"""

for num, act_slug, act_label, title in chapters:
    slug = title.lower().replace("'", "").replace(" ", "-")
    filename = f"ch{num}-{slug}.md"
    path = os.path.join(root, filename)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(STUB.format(num=int(num), title=title, act=act_label))
        print(f"Created: {filename}")
    else:
        print(f"Exists:  {filename}")

files = sorted(os.listdir(root))
print(f"\n{len(files)} files in book1/chapters/")
for f in files:
    print(f"  {f}")
