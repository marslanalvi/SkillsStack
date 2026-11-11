"""One-time migration: move skills from collected-skills/ into category plugins.

Reads tools/classification.json (original path -> plugin key), tools/duplicates.json
(which copy of a duplicated skill is primary) and tools/sources.json (where each
source collection came from). Uses `git mv` so history follows each skill.

  plugins/<category>/<plugin>/skills/<skill>/   primary skills
  alternates/<skill>--<collection>/             other copies of duplicated skills
  sources/<collection>/                         collection-level files (licenses, notes)

Every moved skill gets an ATTRIBUTION.md. Relative links that pointed outside a
skill folder to a file that exists are rewritten to the file's new location.

Usage: python tools/restructure.py [--dry-run]
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD = "collected-skills"
TOOLS = os.path.join(ROOT, "tools")

# Folder renames for skills that would otherwise clash inside one plugin.
RENAMES = {
    "ui-ux-pro-max-skill/cli/assets/skills/design-system": "design-system-tokens",
}

LINK_RE = re.compile(r"(?<![\w/.])((?:\.\./)+[^\s)`\"'<>#*]+)")


def load(name):
    with open(os.path.join(TOOLS, name), encoding="utf-8") as f:
        return json.load(f)


def source_for(path, sources):
    best = None
    for s in sources:
        prefix = s["folder"].rstrip("/")
        if path == prefix or path.startswith(prefix + "/"):
            if best is None or len(prefix) > len(best["folder"].rstrip("/")):
                best = s
    return best or {"repo_url": "", "license": "unknown", "confidence": "unknown"}


def plan(classification, duplicates):
    alternates = {}
    for name, info in duplicates.items():
        for alt in info["alternates"]:
            alternates[alt] = info["primary"]
    moves = {}
    for path, plugin in classification.items():
        folder = RENAMES.get(path, path.split("/")[-1])
        collection = path.split("/")[0]
        if path in alternates:
            dest = f"alternates/{folder}--{collection}"
        else:
            cat, sub = plugin.split("/")
            dest = f"plugins/{cat}/{sub}/skills/{folder}"
        moves[path] = dest
    clashes = {}
    for src, dest in moves.items():
        clashes.setdefault(dest, []).append(src)
    bad = {k: v for k, v in clashes.items() if len(v) > 1}
    if bad:
        raise SystemExit(f"Destination clashes: {json.dumps(bad, indent=1)}")
    return moves, alternates


def find_links(moves):
    """Collect ../ links in markdown files that leave the skill folder but resolve."""
    found = []
    for src in moves:
        skill_dir = os.path.join(ROOT, OLD, src)
        for dp, _, files in os.walk(skill_dir):
            for fn in files:
                if not fn.lower().endswith(".md"):
                    continue
                fpath = os.path.join(dp, fn)
                with open(fpath, encoding="utf-8", errors="replace") as f:
                    text = f.read()
                for link in set(LINK_RE.findall(text)):
                    target = os.path.normpath(os.path.join(dp, link.rstrip(".,;:")))
                    inside = os.path.commonpath([target, skill_dir]) == os.path.normpath(skill_dir)
                    if not inside and os.path.isfile(target):
                        found.append((src, os.path.relpath(fpath, skill_dir), link.rstrip(".,;:"), target))
    return found


def new_location(old_abs, moves):
    rel = os.path.relpath(old_abs, os.path.join(ROOT, OLD)).replace(os.sep, "/")
    for src in sorted(moves, key=len, reverse=True):
        if rel == src or rel.startswith(src + "/"):
            return os.path.join(ROOT, moves[src] + rel[len(src):])
    collection, _, rest = rel.partition("/")
    return os.path.join(ROOT, "sources", collection, rest)


def git(*args):
    subprocess.run(["git", *args], cwd=ROOT, check=True)


def attribution(src, source, primary_of=None, own_license=None):
    lines = [
        "---",
        f"source_collection: {src.split('/')[0]}",
        f"source_repo: {source.get('repo_url') or 'unknown'}",
        f"license: {source.get('license') or 'unknown'}",
        f"attribution_confidence: {source.get('confidence', 'unknown')}",
        f"original_path: {OLD}/{src}",
    ]
    if primary_of:
        lines.append(f"alternate_of: {primary_of}")
    lines += [
        "---",
        "",
        "# Attribution",
        "",
    ]
    repo = source.get("repo_url")
    if repo:
        lines.append(f"This skill was collected from [{repo}]({repo}) "
                     f"(license: {source.get('license') or 'unknown'}).")
    else:
        lines.append("The original source repository for this skill has not been confirmed yet.")
    if own_license:
        lines.append(f"This skill ships its own license file, [{own_license}]({own_license}), "
                     "which takes precedence over the collection-level license above.")
    lines += [
        "The original authors keep ownership of this work. Check the upstream license "
        "before reusing, modifying or redistributing it.",
        "",
    ]
    return "\n".join(lines)


def main(dry):
    classification = load("classification.json")
    duplicates = load("duplicates.json")
    sources = load("sources.json")
    moves, alternates = plan(classification, duplicates)
    links = find_links(moves)
    print(f"{len(moves)} skills to move, {len(alternates)} alternates, {len(links)} links to rewrite")
    if dry:
        for l in links[:20]:
            print("  link", l[0], l[2])
        return

    for src, dest in sorted(moves.items()):
        os.makedirs(os.path.dirname(os.path.join(ROOT, dest)), exist_ok=True)
        git("mv", f"{OLD}/{src}", dest)

    # Collection-level leftovers (e.g. ECC/LICENSE) go to sources/<collection>/.
    old_root = os.path.join(ROOT, OLD)
    for dp, _, files in os.walk(old_root):
        for fn in files:
            rel = os.path.relpath(os.path.join(dp, fn), old_root).replace(os.sep, "/")
            dest = f"sources/{rel}"
            os.makedirs(os.path.dirname(os.path.join(ROOT, dest)), exist_ok=True)
            git("mv", f"{OLD}/{rel}", dest)

    # Rewrite links to their targets' new locations.
    for src, frel, link, target in links:
        fpath = os.path.join(ROOT, moves[src], frel)
        new_target = new_location(target, moves)
        new_link = os.path.relpath(new_target, os.path.dirname(fpath)).replace(os.sep, "/")
        with open(fpath, encoding="utf-8", errors="replace", newline="") as f:
            text = f.read()
        text = re.sub(r"(?<![\w/.])" + re.escape(link), new_link, text)
        with open(fpath, "w", encoding="utf-8", newline="") as f:
            f.write(text)

    # Renamed skills: keep the frontmatter name in step with the folder.
    for src, folder in RENAMES.items():
        fpath = os.path.join(ROOT, moves[src], "SKILL.md")
        with open(fpath, encoding="utf-8", newline="") as f:
            text = f.read()
        text = re.sub(r"(?m)^name:.*$", f"name: {folder}", text, count=1)
        with open(fpath, "w", encoding="utf-8", newline="") as f:
            f.write(text)

    for src, dest in moves.items():
        apath = os.path.join(ROOT, dest, "ATTRIBUTION.md")
        if os.path.exists(apath):
            raise SystemExit(f"ATTRIBUTION.md already exists in {dest}")
        primary = alternates.get(src)
        own = next((fn for fn in sorted(os.listdir(os.path.join(ROOT, dest)))
                    if fn.upper().startswith(("LICENSE", "LICENCE"))), None)
        with open(apath, "w", encoding="utf-8") as f:
            f.write(attribution(src, source_for(src, sources),
                                moves[primary] if primary else None, own))

    # Remove now-empty directories under collected-skills/.
    for dp, dirs, files in os.walk(old_root, topdown=False):
        if not os.listdir(dp):
            os.rmdir(dp)
    print("done")


if __name__ == "__main__":
    main("--dry-run" in sys.argv)
