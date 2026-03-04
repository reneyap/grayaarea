from pathlib import Path
p = Path('archive/original/md')
if not p.exists():
    print('Directory not found:', p)
    raise SystemExit(1)
renamed = 0
skipped = 0
for f in sorted(p.iterdir()):
    if f.is_file() and f.name.startswith('ORIGINAL_'):
        new_name = f.name.replace('ORIGINAL_','',1)
        new_path = f.with_name(new_name)
        if new_path.exists():
            print('SKIP (exists):', f.name, '->', new_name)
            skipped += 1
        else:
            f.rename(new_path)
            print('RENAMED:', f.name, '->', new_name)
            renamed += 1

print('\nDone. Renamed:', renamed, 'Skipped:', skipped)
