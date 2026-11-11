"""Generate plugin manifests, the marketplace file, the catalog and source list.

Scans plugins/<category>/<plugin>/skills/*/SKILL.md (plus alternates/) and writes:
  plugins/<category>/<plugin>/.claude-plugin/plugin.json
  plugins/<category>/<plugin>/README.md
  .claude-plugin/marketplace.json
  catalog.json
  CATALOG.md
  CREDITS.md

Run it after adding, moving or editing skills:  python tools/build_catalog.py
Exits non-zero if a skill is missing a name/description or two skills clash.
"""
import collections
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARKETPLACE = "skills-stack"
REPO = "marslanalvi/SkillsStack"
VERSION = "1.0.0"


def frontmatter(path):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    raw = text[3:end] if end != -1 else ""
    try:
        meta = yaml.safe_load(raw)
        return meta if isinstance(meta, dict) else {}
    except yaml.YAMLError:
        meta = {}
        for line in raw.splitlines():
            if ":" in line and not line.startswith((" ", "\t")):
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip("\"'")
        return meta


def one_line(s, limit=None):
    s = " ".join(str(s or "").split())
    if limit and len(s) > limit:
        s = s[: limit - 1].rstrip() + "…"
    return s


def md_cell(s):
    return s.replace("|", "\\|")


def skill_record(skill_dir, rel):
    meta = frontmatter(os.path.join(skill_dir, "SKILL.md"))
    attr = frontmatter(os.path.join(skill_dir, "ATTRIBUTION.md"))
    original = str(attr.get("original_path", ""))
    return {
        "name": one_line(meta.get("name")) or os.path.basename(skill_dir),
        "folder": os.path.basename(skill_dir),
        "description": one_line(meta.get("description")),
        "path": rel,
        "credit": attr.get("credit", "unknown"),
        "original_author": attr.get("original_author"),
        "original_repo": attr.get("original_repo"),
        "source_collection": original.split("/")[1] if original.count("/") > 1 else "unknown",
        "source_repo": attr.get("collected_from", "unknown"),
        "license": attr.get("license", "unknown"),
        "modified": attr.get("modified", False),
        "alternate_of": attr.get("alternate_of"),
    }


def credit_line(s):
    """Short credit for tables: the skill's own author if known, else the upstream holder."""
    who = s["original_author"] or s["credit"]
    return one_line(who, 60)


def main():
    with open(os.path.join(ROOT, "tools", "taxonomy.json"), encoding="utf-8") as f:
        taxonomy = json.load(f)
    errors = []
    plugins = []
    for key, pdesc in taxonomy["plugins"].items():
        cat, sub = key.split("/")
        pdir = os.path.join(ROOT, "plugins", cat, sub)
        sdir = os.path.join(pdir, "skills")
        if not os.path.isdir(sdir):
            errors.append(f"{key}: no skills/ folder")
            continue
        skills = []
        for folder in sorted(os.listdir(sdir)):
            d = os.path.join(sdir, folder)
            if not os.path.isfile(os.path.join(d, "SKILL.md")):
                continue
            rec = skill_record(d, f"plugins/{cat}/{sub}/skills/{folder}")
            if not rec["description"]:
                errors.append(f"{rec['path']}: missing description")
            skills.append(rec)
        names = collections.Counter(s["name"] for s in skills)
        errors += [f"{key}: duplicate skill name '{n}'" for n, c in names.items() if c > 1]
        plugin_name = f"{cat}-{sub}"
        plugins.append({"key": key, "name": plugin_name, "category": cat,
                        "description": pdesc, "path": f"plugins/{cat}/{sub}", "skills": skills})

        os.makedirs(os.path.join(pdir, ".claude-plugin"), exist_ok=True)
        manifest = {
            "name": plugin_name,
            "version": VERSION,
            "description": f"{pdesc}. {len(skills)} open-source skills compiled by Skills Stack; "
                           "each skill's ATTRIBUTION.md credits its original authors.",
            "author": {"name": "Skills Stack (compiler); skills by their original authors"},
            "homepage": f"https://github.com/{REPO}/tree/main/plugins/{cat}/{sub}",
            "repository": f"https://github.com/{REPO}",
            "keywords": [cat, sub, "skills"],
        }
        with open(os.path.join(pdir, ".claude-plugin", "plugin.json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            f.write("\n")

        lines = [f"# {plugin_name}", "", pdesc + ".", "",
                 "## Install", "", "```bash",
                 f"/plugin marketplace add {REPO}",
                 f"/plugin install {plugin_name}@{MARKETPLACE}", "```", "",
                 f"## Skills ({len(skills)})", "",
                 "| Skill | What it does | Created by | License |", "|---|---|---|---|"]
        for s in skills:
            lines.append(f"| [{s['name']}](skills/{s['folder']}/SKILL.md) | "
                         f"{md_cell(one_line(s['description'], 200))} | {md_cell(credit_line(s))} | "
                         f"{md_cell(one_line(s['license'], 40))} |")
        lines += ["", "## Credit and licenses", "",
                  "Every skill in this plugin was created by the people named above and collected into "
                  "Skills Stack, which compiles open-source skills in one place. The authors keep all rights "
                  "to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and "
                  "any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).", ""]
        with open(os.path.join(pdir, "README.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    alternates = []
    adir = os.path.join(ROOT, "alternates")
    if os.path.isdir(adir):
        for folder in sorted(os.listdir(adir)):
            d = os.path.join(adir, folder)
            if os.path.isfile(os.path.join(d, "SKILL.md")):
                alternates.append(skill_record(d, f"alternates/{folder}"))

    marketplace = {
        "name": MARKETPLACE,
        "owner": {"name": "marslanalvi"},
        "metadata": {
            "description": "A categorized compilation of open-source AI agent skills. All credit to the original "
                           "authors, who keep all rights to their work; see CREDITS.md.",
            "version": VERSION,
        },
        "plugins": [{
            "name": p["name"],
            "source": "./" + p["path"],
            "description": p["description"],
            "version": VERSION,
            "category": p["category"],
            "keywords": [p["category"], p["key"].split("/")[1]],
        } for p in plugins],
    }
    os.makedirs(os.path.join(ROOT, ".claude-plugin"), exist_ok=True)
    with open(os.path.join(ROOT, ".claude-plugin", "marketplace.json"), "w", encoding="utf-8") as f:
        json.dump(marketplace, f, indent=2, ensure_ascii=False)
        f.write("\n")

    catalog = {"categories": taxonomy["categories"], "plugins": plugins, "alternates": alternates}
    with open(os.path.join(ROOT, "catalog.json"), "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=1, ensure_ascii=False)
        f.write("\n")

    # Compact data for the search website (docs/, served by GitHub Pages).
    site = {
        "repo": REPO,
        "marketplace": MARKETPLACE,
        "categories": taxonomy["categories"],
        "plugins": [{"n": p["name"], "c": p["category"], "d": p["description"], "k": len(p["skills"])}
                    for p in plugins],
        "skills": [{"n": s["name"], "d": s["description"], "p": p["name"], "c": p["category"],
                    "a": credit_line(s), "l": one_line(s["license"], 40), "u": s["path"]}
                   for p in plugins for s in p["skills"]],
    }
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    with open(os.path.join(ROOT, "docs", "skills.json"), "w", encoding="utf-8") as f:
        json.dump(site, f, ensure_ascii=False, separators=(",", ":"))

    total = sum(len(p["skills"]) for p in plugins)
    lines = ["# Skills Stack Catalog", "",
             f"{total} skills in {len(plugins)} plugins across {len(taxonomy['categories'])} categories, "
             f"plus {len(alternates)} alternate versions of duplicated skills.",
             "Generated by `tools/build_catalog.py`; do not edit by hand.", "", "## Contents", ""]
    for cat, cdesc in taxonomy["categories"].items():
        lines.append(f"- [{cat}](#{cat}) — {cdesc}")
    for cat, cdesc in taxonomy["categories"].items():
        lines += ["", f"## {cat}", "", cdesc + ".", ""]
        for p in [p for p in plugins if p["category"] == cat]:
            lines += [f"### {p['name']}", "", f"{p['description']}. Install with "
                      f"`/plugin install {p['name']}@{MARKETPLACE}`.", "",
                      "| Skill | What it does | Created by |", "|---|---|---|"]
            for s in p["skills"]:
                lines.append(f"| [{s['name']}]({s['path']}/SKILL.md) | {md_cell(one_line(s['description'], 160))} "
                             f"| {md_cell(credit_line(s))} |")
            lines.append("")
    if alternates:
        by_primary = collections.defaultdict(list)
        for a in alternates:
            by_primary[a["alternate_of"]].append(a)
        lines += ["## Alternate versions", "",
                  "These skills duplicate one already in a plugin. The plugin copy is the main one; "
                  "the alternates are kept for comparison and are not installed by any plugin.", "",
                  "| Main skill | Alternate | Alternate created by |", "|---|---|---|"]
        for primary, alts in sorted(by_primary.items(), key=lambda x: str(x[0])):
            for a in alts:
                lines.append(f"| [{a['name']}]({primary}/SKILL.md) | [{a['folder']}]({a['path']}/SKILL.md) "
                             f"| {md_cell(credit_line(a))} |")
        lines.append("")
    with open(os.path.join(ROOT, "CATALOG.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    with open(os.path.join(ROOT, "tools", "credits.json"), encoding="utf-8") as f:
        credits = json.load(f)
    every = [s for p in plugins for s in p["skills"]] + alternates
    per_repo = collections.Counter(s["source_repo"] for s in every)
    lines = ["# Credits", "",
             "Skills Stack exists because of the people and teams below, who wrote these skills and shared them "
             "openly. Skills Stack is a compilation: it collects their work in one place, sorts it into categories "
             "and packages it as installable plugins. **The authors keep all rights to their work.** Skills Stack "
             "does not claim ownership of any skill it collects.", "",
             "Generated by `tools/build_catalog.py` from each skill's `ATTRIBUTION.md`.", "",
             "## Projects", "",
             "| Project | Created by | Skills | License | License text |", "|---|---|---:|---|---|"]
    for repo, n in per_repo.most_common():
        c = credits.get(repo, {})
        lic_dir = c.get("license_dir")
        texts = ", ".join(f"[{fn}](licenses/{lic_dir}/{fn})"
                          for fn in sorted(os.listdir(os.path.join(ROOT, "licenses", lic_dir)))) if lic_dir else ""
        lines.append(f"| [{c.get('project', repo)}]({repo}) | {md_cell(c.get('credit', 'unknown'))} | {n} | "
                     f"{md_cell(c.get('license', 'unknown'))} | {texts} |")
    authors = collections.defaultdict(list)
    for s in every:
        if s["original_author"]:
            authors[(str(s["original_author"]), s["original_repo"] or "")].append(s)
    if authors:
        lines += ["", "## Individual skill authors", "",
                  "Some collections gather skills from many people. These authors are named in their skills' "
                  "own metadata:", "",
                  "| Author | Skills |", "|---|---|"]
        for (who, repo), skills in sorted(authors.items(), key=lambda x: x[0][0].lower()):
            name = f"[{md_cell(who)}]({repo})" if repo.startswith("http") else md_cell(who)
            lines.append(f"| {name} | " + ", ".join(f"[{s['name']}]({s['path']}/ATTRIBUTION.md)" for s in skills) + " |")
    changed = [s for s in every if s["modified"]]
    lines += ["", "## Changes Skills Stack made", "",
              "Every skill was moved into a category plugin and given an `ATTRIBUTION.md`. Beyond that, "
              f"Skills Stack changed files in {len(changed)} skills, and each one's `ATTRIBUTION.md` says what changed:",
              ""] + [f"- [{s['name']}]({s['path']}/ATTRIBUTION.md)" for s in changed] + [
              "", "## Questions, corrections and removal requests", "",
              "If you wrote a skill in Skills Stack and want your credit changed or the skill removed, open an issue "
              f"at https://github.com/{REPO}/issues and it will be handled promptly.", ""]
    with open(os.path.join(ROOT, "CREDITS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Refresh the plugin table in README.md between its markers.
    readme = os.path.join(ROOT, "README.md")
    start, end = "<!-- PLUGINS:START -->", "<!-- PLUGINS:END -->"
    with open(readme, encoding="utf-8") as f:
        text = f.read()
    if start in text and end in text:
        rows = [f"**{total} skills in {len(plugins)} plugins.**", "",
                "| Category | Plugin | Skills | What's inside |", "|---|---|---:|---|"]
        for cat in taxonomy["categories"]:
            for p in [p for p in plugins if p["category"] == cat]:
                rows.append(f"| {cat} | [`{p['name']}`]({p['path']}) | {len(p['skills'])} | {p['description']} |")
        text = text[: text.index(start) + len(start)] + "\n" + "\n".join(rows) + "\n" + text[text.index(end):]
        text = re.sub(r"badge/skills-\d+-", f"badge/skills-{total}-", text)
        text = re.sub(r"badge/plugins-\d+-", f"badge/plugins-{len(plugins)}-", text)
        text = re.sub(r"badge/categories-\d+-", f"badge/categories-{len(taxonomy['categories'])}-", text)
        with open(readme, "w", encoding="utf-8") as f:
            f.write(text)

    print(f"{total} skills, {len(plugins)} plugins, {len(alternates)} alternates")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
