"""Scan a folder tree for SKILL.md files and write an inventory JSON.

Usage: python tools/inventory.py <root> <out.json>
"""
import json
import os
import sys

import yaml


def read_frontmatter(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end]
    try:
        meta = yaml.safe_load(raw) or {}
        if not isinstance(meta, dict):
            meta = {}
    except yaml.YAMLError:
        # Fall back to a line parser for frontmatter that isn't strict YAML.
        meta = {}
        for line in raw.splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip("\"'")
    return meta, text[end + 4:]


def main(root, out):
    items = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        if "SKILL.md" not in filenames:
            continue
        rel = os.path.relpath(dirpath, root).replace(os.sep, "/")
        meta, body = read_frontmatter(os.path.join(dirpath, "SKILL.md"))
        nfiles = sum(len(f) for _, _, f in os.walk(dirpath))
        items.append({
            "path": rel,
            "collection": rel.split("/")[0],
            "folder": rel.split("/")[-1],
            "name": str(meta.get("name") or rel.split("/")[-1]).strip(),
            "description": " ".join(str(meta.get("description", "")).split()),
            "files": nfiles,
            "body_chars": len(body),
        })
    items.sort(key=lambda x: x["path"])
    for i, it in enumerate(items):
        it["id"] = i
    with open(out, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=1, ensure_ascii=False)
    print(f"{len(items)} skills -> {out}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
