# Contributing to Skills Stack

Thanks for helping make Skills Stack the place people go to find AI agent skills. There are a few ways to help, and most don't need any code.

## Quick ways to help

- **Suggest a skill:** found a great skill on GitHub that isn't here? [Suggest it](https://github.com/marslanalvi/SkillsStack/issues/new?template=suggest-skill.yml). Include the link and its license.
- **Fix a category:** if a skill sits in the wrong plugin, [tell us where it belongs](https://github.com/marslanalvi/SkillsStack/issues/new?template=wrong-category.yml).
- **Report a broken skill:** a missing file, a broken link, or a skill that doesn't load? [Report it](https://github.com/marslanalvi/SkillsStack/issues/new?template=broken-skill.yml).
- **Authors:** if you wrote a skill here and want the credit changed or the skill removed, [let us know](https://github.com/marslanalvi/SkillsStack/issues/new?template=author-request.yml). We act on these first.
- **Star and share:** stars help other people find Skills Stack.

## Adding a skill yourself

### What we accept

- **A clear, focused job.** The skill should do one thing well, and its `description` should say when to use it.
- **An open license that allows redistribution,** such as MIT, Apache-2.0, BSD or CC-BY. We don't add skills with no license or a license that forbids sharing.
- **Nothing harmful.** Skills must not hide behavior, collect data without consent, or exist to attack systems their user doesn't own. Security skills for authorized testing are welcome.
- **No duplicates.** Search the [catalog](CATALOG.md) first. If yours is better than an existing skill, say why in the pull request.

### Steps

1. Fork the repo and create a branch.
2. Copy the skill folder, unchanged, into the plugin it fits: `plugins/<category>/<plugin>/skills/<skill-name>/`. It needs a `SKILL.md` whose frontmatter has `name` and `description`. Keep the author's own license and credit lines.
3. If the skill comes from a project Skills Stack doesn't credit yet:
   - add the project to [`tools/credits.json`](tools/credits.json) (project name, who created it, license, license folder), and
   - put its full license text in `licenses/<owner>__<repo>/`.
4. Add an `ATTRIBUTION.md` to the skill folder containing at least:

   ```markdown
   ---
   collected_from: https://github.com/<owner>/<repo>
   original_path: <path of the skill in that repository>
   ---
   ```

5. If you changed any of the skill's own files, describe the change in [`tools/changes.json`](tools/changes.json). Creative Commons licenses require this.
6. Rebuild the generated files and check them:

   ```bash
   pip install pyyaml
   python tools/attribution.py
   python tools/build_catalog.py
   claude plugin validate .
   ```

7. Commit everything, including the regenerated files, and open a pull request.

### New plugins or categories

Add the plugin to [`tools/taxonomy.json`](tools/taxonomy.json) with a one-line description, create its `skills/` folder, and rebuild. Propose a new category in an issue first, so we can agree on where it fits.

## Credit rules

Credit is the heart of Skills Stack. In every pull request:

- Never remove or change an author's name, license or copyright notice.
- Never present someone else's skill as your own.
- If you're adding your own skill, put your name in its `SKILL.md` frontmatter as `author:` so you're credited in [CREDITS.md](CREDITS.md).

## Code of conduct

Be kind and assume good intent. Harassment, discrimination or personal attacks aren't tolerated anywhere in this project.
