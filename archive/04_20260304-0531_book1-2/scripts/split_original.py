import re
import os

def slugify(s):
    s = s.strip()
    s = re.sub(r"[^0-9a-zA-Z]+", "_", s)
    s = re.sub(r"_+", "_", s)
    s = s.strip('_') or 'section'
    # limit length to avoid filesystem/path-length problems
    if len(s) > 60:
        s = s[:60].rstrip('_')
    return s

def main():
    infile = 'ORIGINAL.md'
    if not os.path.exists(infile):
        print('ERROR: ORIGINAL.md not found in current directory')
        return 1
    with open(infile, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    sections = []
    current = {'title': 'preface', 'lines': []}

    for line in lines:
        if re.match(r'^\s{0,}#{1,2}\s+', line):
            # new heading starts a new section
            # push current
            sections.append(current)
            title = line.lstrip('#').strip()
            current = {'title': title, 'lines': [line]}
        else:
            current['lines'].append(line)

    sections.append(current)

    created = []
    for i, sec in enumerate(sections):
        idx = f"{i:02d}"
        title = sec.get('title') or f'section_{idx}'
        slug = slugify(title)
        fname = f'ORIGINAL_{idx}_{slug}.md'
        with open(fname, 'w', encoding='utf-8') as out:
            out.writelines(sec['lines'])
        created.append(fname)

    print('Created', len(created), 'files:')
    for p in created:
        print(' -', p)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
