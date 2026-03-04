"""Manage the top `> **<Tag> Note:** <instruction>` header in chapter markdown files.

Usage:
  python scripts/header_manager.py list [--path DIR]
  python scripts/header_manager.py add --tag "Lore Directive" --body "..." [--path DIR] [--force]
  python scripts/header_manager.py edit --tag "Old" --new-tag "New" --body "..." [--path DIR]
  python scripts/header_manager.py delete [--tag TAG] [--path DIR]

Actions operate on files under the given `--path` (default: book1/draft1a/chapters).
The header format is assumed to be a single blockquote line before the `# Chapter` title, e.g.:
  > **Lore Directive Note:** <instruction text>

This script supports dry-run output for safe inspection.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import shutil
import sys
from typing import List, Tuple

HEADER_RE = re.compile(r"^> \*\*(?P<tag>.+?) Note:\*\* (?P<body>.*)$")


def find_md_files(path: str) -> List[str]:
    p = os.path.join(path, "*.md")
    return sorted(glob.glob(p))


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file_atomic(path: str, content: str) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
    shutil.move(tmp, path)


def detect_header(text: str) -> Tuple[int, str, str]:
    """Return (line_index, tag, body) for header if found as the first non-empty line; else (-1, '', '')."""
    lines = text.splitlines()
    for i, line in enumerate(lines[:10]):  # only check top 10 lines
        m = HEADER_RE.match(line.strip())
        if m:
            return i, m.group("tag"), m.group("body")
    return -1, "", ""


def insert_header(text: str, tag: str, body: str) -> str:
    lines = text.splitlines()
    header_line = f"> **{tag} Note:** {body}"
    # find insertion point: before first line starting with '# Chapter'
    for i, line in enumerate(lines):
        if line.strip().startswith("# Chapter"):
            new_lines = lines[:i]
            new_lines.append(header_line)
            new_lines.extend(lines[i:])
            return "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
    # fallback: prepend
    return header_line + "\n\n" + text


def remove_header(text: str, tag: str | None = None) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines[:10]):
        m = HEADER_RE.match(line.strip())
        if m and (tag is None or m.group("tag") == tag):
            del lines[i]
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    return text


def replace_header(text: str, tag: str | None, new_tag: str, new_body: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines[:10]):
        m = HEADER_RE.match(line.strip())
        if m and (tag is None or m.group("tag") == tag):
            lines[i] = f"> **{new_tag} Note:** {new_body}"
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    # if no header found, insert
    return insert_header(text, new_tag, new_body)


def action_list(path: str) -> int:
    files = find_md_files(path)
    missing = []
    present = []
    for f in files:
        txt = read_file(f)
        idx, tag, body = detect_header(txt)
        if idx == -1:
            missing.append(f)
        else:
            present.append((f, tag, body))

    print("Found files:", len(files))
    print("With header:", len(present))
    for p in present:
        print(f"H: {os.path.basename(p[0])} -> tag='{p[1]}' body='{p[2]}'")
    print("Missing header:", len(missing))
    for m in missing:
        print(f"M: {os.path.basename(m)}")
    return 0


def action_add(path: str, tag: str, body: str, force: bool, dry: bool) -> int:
    files = find_md_files(path)
    for f in files:
        txt = read_file(f)
        idx, existing_tag, existing_body = detect_header(txt)
        if idx != -1:
            if not force:
                print(f"Skip (exists): {os.path.basename(f)} -> {existing_tag}")
                continue
            txt = remove_header(txt)
        new_txt = insert_header(txt, tag, body)
        if dry:
            print(f"[dry] Would add header to {os.path.basename(f)}")
        else:
            write_file_atomic(f, new_txt)
            print(f"Added header to {os.path.basename(f)}")
    return 0


def action_edit(path: str, tag: str | None, new_tag: str, new_body: str, dry: bool) -> int:
    files = find_md_files(path)
    for f in files:
        txt = read_file(f)
        idx, existing_tag, existing_body = detect_header(txt)
        if idx == -1:
            print(f"No header in {os.path.basename(f)}; inserting new")
            new_txt = insert_header(txt, new_tag, new_body)
        else:
            new_txt = replace_header(txt, tag, new_tag, new_body)

        if dry:
            print(f"[dry] Would edit header in {os.path.basename(f)}")
        else:
            write_file_atomic(f, new_txt)
            print(f"Edited header in {os.path.basename(f)}")
    return 0


def action_delete(path: str, tag: str | None, dry: bool) -> int:
    files = find_md_files(path)
    for f in files:
        txt = read_file(f)
        idx, existing_tag, existing_body = detect_header(txt)
        if idx == -1:
            print(f"No header in {os.path.basename(f)}; skip")
            continue
        if tag is not None and existing_tag != tag:
            print(f"Tag mismatch in {os.path.basename(f)} (found '{existing_tag}'); skip")
            continue
        new_txt = remove_header(txt, tag)
        if dry:
            print(f"[dry] Would remove header from {os.path.basename(f)}")
        else:
            write_file_atomic(f, new_txt)
            print(f"Removed header from {os.path.basename(f)}")
    return 0


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Manage top header-instruction in chapter markdown files")
    sub = parser.add_subparsers(dest="cmd")

    p_list = sub.add_parser("list")
    p_list.add_argument("--path", default="book1/draft1a/chapters")

    p_add = sub.add_parser("add")
    p_add.add_argument("--tag", required=True)
    p_add.add_argument("--body", required=True)
    p_add.add_argument("--path", default="book1/draft1a/chapters")
    p_add.add_argument("--force", action="store_true")
    p_add.add_argument("--dry", action="store_true")

    p_edit = sub.add_parser("edit")
    p_edit.add_argument("--tag", required=False, help="Only edit headers matching this tag (optional)")
    p_edit.add_argument("--new-tag", required=True)
    p_edit.add_argument("--body", required=True, dest="new_body")
    p_edit.add_argument("--path", default="book1/draft1a/chapters")
    p_edit.add_argument("--dry", action="store_true")

    p_del = sub.add_parser("delete")
    p_del.add_argument("--tag", required=False, help="Only delete headers matching this tag (optional)")
    p_del.add_argument("--path", default="book1/draft1a/chapters")
    p_del.add_argument("--dry", action="store_true")

    args = parser.parse_args(argv)

    if args.cmd == "list":
        return action_list(args.path)
    if args.cmd == "add":
        return action_add(args.path, args.tag, args.body, args.force, args.dry)
    if args.cmd == "edit":
        return action_edit(args.path, args.tag, args.new_tag, args.new_body, args.dry)
    if args.cmd == "delete":
        return action_delete(args.path, args.tag, args.dry)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
