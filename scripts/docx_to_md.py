import sys
import os
from docx import Document

def run(file_in, file_out):
    doc = Document(file_in)
    lines = []
    for p in doc.paragraphs:
        text = ''
        for r in p.runs:
            t = r.text.replace('\n',' ')
            if not t:
                continue
            if r.bold:
                t = f"**{t}**"
            if r.italic:
                t = f"*{t}*"
            text += t
        style_name = p.style.name.lower() if p.style is not None else ''
        if 'heading' in style_name:
            # try to get level
            lvl = 1
            parts = style_name.split()
            for part in parts:
                if part.isdigit():
                    try:
                        lvl = int(part)
                    except:
                        pass
            lines.append('#' * lvl + ' ' + text + '\n')
        elif any(k in style_name for k in ('bullet','list')):
            lines.append('- ' + text + '\n')
        else:
            if text.strip() == '':
                lines.append('\n')
            else:
                lines.append(text + '\n\n')

    with open(file_out, 'w', encoding='utf-8') as f:
        f.writelines(lines)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python docx_to_md.py input.docx [output.md]')
        sys.exit(1)
    inp = sys.argv[1]
    outp = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(inp)[0] + '.md'
    run(inp, outp)
    print('Wrote', outp)
