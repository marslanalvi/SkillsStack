"""Write ATTRIBUTION.md for every skill and bundle license texts into each plugin.

For each skill under plugins/*/*/skills/ and alternates/, this credits:
  - the upstream project and its copyright holder (tools/credits.json),
  - the skill's own author and repository, when its SKILL.md frontmatter names them,
  - the license that applies, with a link to the full license text,
  - any changes Skills Stack made to the upstream files (tools/changes.json).

License texts live in licenses/<owner>__<repo>/. Each plugin gets its own copy of the
ones its skills need in plugins/<category>/<plugin>/LICENSES/, so credit and license
terms travel with a plugin when it is installed on its own.

The existing ATTRIBUTION.md frontmatter (original_path, alternate_of, source_repo) is
the record of where each skill came from; this script rewrites everything else.

Usage: python tools/attribution.py
"""
import json
import os
import shutil

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Skills whose upstream states no license. They are kept, credited, with this notice.
NO_LICENSE = {
    "collected-skills/repository/skills/doc-coauthoring",
    "collected-skills/repository/template",
}
NO_LICENSE_TEXT = (
    "**No license is stated for this skill.** The upstream repository has no license file for it, so no "
    "license is granted, by its authors or by Skills Stack. All rights remain with its authors. It is included "
    "here with full credit for reference, and will be removed if its authors ask. Don't copy, modify or "
    "redistribute it unless its authors give you permission."
)


def load(name):
    with open(os.path.join(ROOT, "tools", name), encoding="utf-8") as f:
        return json.load(f)


def frontmatter(path):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    try:
        meta = yaml.safe_load(text[3:end] if end != -1 else "")
        return meta if isinstance(meta, dict) else {}
    except yaml.YAMLError:
        return {}


def first(meta, *keys):
    for key in keys:
        node = meta
        for part in key.split("."):
            node = node.get(part) if isinstance(node, dict) else None
        if node:
            return " ".join(str(node).split())
    return None


def skill_dirs():
    for cat in sorted(os.listdir(os.path.join(ROOT, "plugins"))):
        for sub in sorted(os.listdir(os.path.join(ROOT, "plugins", cat))):
            sdir = os.path.join(ROOT, "plugins", cat, sub, "skills")
            for folder in sorted(os.listdir(sdir)):
                yield os.path.join(sdir, folder), os.path.join(ROOT, "plugins", cat, sub)
    for extra in ("alternates", "templates"):
        adir = os.path.join(ROOT, extra)
        if os.path.isdir(adir):
            for folder in sorted(os.listdir(adir)):
                yield os.path.join(adir, folder), None


def rel(path, start):
    return os.path.relpath(path, start).replace(os.sep, "/")


def main():
    credits = load("credits.json")
    changes = load("changes.json")
    needed = {}  # plugin dir -> set of license dirs
    count = 0
    for skill_dir, plugin_dir in skill_dirs():
        if not os.path.isfile(os.path.join(skill_dir, "SKILL.md")):
            continue
        old = frontmatter(os.path.join(skill_dir, "ATTRIBUTION.md"))
        skill = frontmatter(os.path.join(skill_dir, "SKILL.md"))
        repo = old.get("collected_from") or old.get("source_repo")
        info = credits.get(repo)
        if not info:
            raise SystemExit(f"No credits entry for {repo} ({skill_dir})")
        name = first(skill, "name") or os.path.basename(skill_dir)

        # License text: inside the plugin for plugin skills, the root copy for alternates.
        lic_root = os.path.join(ROOT, "licenses", info["license_dir"])
        if plugin_dir:
            needed.setdefault(plugin_dir, set()).add(info["license_dir"])
            lic_dir = os.path.join(plugin_dir, "LICENSES", info["license_dir"])
        else:
            lic_dir = lic_root
        lic_files = sorted(os.listdir(lic_root))
        own = sorted(fn for fn in os.listdir(skill_dir) if fn.upper().startswith(("LICENSE", "LICENCE")))

        author = first(skill, "author", "metadata.author", "metadata.skill-author")
        skill_repo = first(skill, "source_repo", "metadata.repository", "metadata.source")
        if skill_repo and not skill_repo.startswith("http"):
            skill_repo = "https://github.com/" + skill_repo
        if skill_repo and skill_repo.rstrip("/").lower() == repo.rstrip("/").lower():
            skill_repo = None
        skill_license = first(skill, "license")
        license_source = first(skill, "license_source")
        rel_key = rel(skill_dir, ROOT)
        made = changes.get(rel_key, [])
        unlicensed = old.get("original_path") in NO_LICENSE and not own
        if unlicensed:
            skill_license = "None stated (all rights reserved by its authors)"

        fm = {
            "skill": name,
            "credit": info["credit"],
            "original_author": author,
            "original_repo": skill_repo,
            "collected_from": repo,
            "license": skill_license or info["license"],
            "original_path": old.get("original_path"),
            "alternate_of": old.get("alternate_of"),
            "modified": bool(made),
        }
        fm = {k: v for k, v in fm.items() if v not in (None, "")}

        lines = ["---", yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000).strip(), "---", "",
                 f"# Credit for `{name}`", ""]
        if author or skill_repo:
            who = author or "its original author"
            where = f" ([{skill_repo}]({skill_repo}))" if skill_repo else ""
            lines.append(f"This skill was created by **{who}**{where}. "
                         f"Skills Stack collected it from {info['project']} by **{info['credit']}**: "
                         f"[{repo}]({repo}).")
        else:
            lines.append(f"This skill was created by **{info['credit']}** as part of "
                         f"{info['project']}: [{repo}]({repo}).")
        lines += ["", "Skills Stack is a compilation: it gathers skills like this one in one place so people can "
                  "find and install them. The skill's authors keep all rights to their work. Skills Stack does not "
                  "claim ownership of it.", "", "## License", ""]

        if unlicensed:
            lines += [NO_LICENSE_TEXT, "",
                      f"Other skills in the {info['project']} collection are licensed per skill; see " +
                      ", ".join(f"[{fn}]({rel(os.path.join(lic_dir, fn), skill_dir)})" for fn in lic_files) + "."]
        elif own:
            links = ", ".join(f"[{fn}]({fn})" for fn in own)
            lines.append(f"This skill ships its own license file ({links}), which is the license that applies.")
            if skill_license:
                lines.append(f"Its frontmatter declares: {skill_license}.")
        elif skill_license:
            src = f" ([license source]({license_source}))" if license_source else ""
            lines.append(f"This skill declares the **{skill_license}** license{src}.")
        if not unlicensed:
            lines.append(f"The {info['project']} collection is licensed **{info['license']}**. Full text: " +
                         ", ".join(f"[{fn}]({rel(os.path.join(lic_dir, fn), skill_dir)})" for fn in lic_files) + ".")
            if info.get("note"):
                lines += ["", info["note"]]

        lines += ["", "## Changes made by Skills Stack", "",
                  "- Moved the skill into a Skills Stack plugin folder and added this ATTRIBUTION.md."]
        lines += [f"- {c}" for c in made]
        if not made:
            lines.append("- No changes were made to the skill's own files.")
        lines += ["", "## Original source", "",
                  f"- Upstream repository: [{repo}]({repo})"]
        if skill_repo:
            lines.append(f"- Skill's own repository: [{skill_repo}]({skill_repo})")
        lines += [f"- Path in the original Skills Stack collection: `{old.get('original_path')}`", "",
                  "If you are an author of this skill and want the credit changed or the skill removed, open an "
                  "issue at https://github.com/marslanalvi/SkillsStack/issues.", ""]

        with open(os.path.join(skill_dir, "ATTRIBUTION.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        count += 1

    for plugin_dir, lic_dirs in needed.items():
        target = os.path.join(plugin_dir, "LICENSES")
        if os.path.isdir(target):
            shutil.rmtree(target)
        for d in sorted(lic_dirs):
            shutil.copytree(os.path.join(ROOT, "licenses", d), os.path.join(target, d))
    print(f"{count} ATTRIBUTION.md files written; licenses bundled into {len(needed)} plugins")


if __name__ == "__main__":
    main()
