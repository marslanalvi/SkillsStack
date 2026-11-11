# engineering-git-github

Git, GitHub, pull requests, releases, monorepos, build tooling and dependency upgrades.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install engineering-git-github@skills-stack
```

## Works best with

Some skills here hand off to skills in other Skills Stack plugins. Install these too so those steps work:

- **`engineering-architecture-api`**: `git-workflow-and-versioning` uses `api-and-interface-design`, `triage` uses `domain-modeling`
- **`engineering-dev-workflow`**: `git-workflow-and-versioning` uses `deprecation-and-migration`, `git-workflow-and-versioning` uses `shipping-and-launch`
- **`ai-skill-authoring`**: `triage` uses `setup-matt-pocock-skills`
- **`productivity-thinking-planning`**: `triage` uses `grilling`

## Skills (27)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [babysit-pr](skills/babysit-pr/SKILL.md) | Babysit a pull request through its bot review rounds: verify, fix, reply, resolve. Use for any babysit or watch-the-PR ask. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT |
| [bazel-build-optimization](skills/bazel-build-optimization/SKILL.md) | Optimize Bazel builds for large-scale monorepos. Use when configuring Bazel, implementing remote execution, or optimizing build performance for enterprise codebases. | Seth Hobson | MIT |
| [changelog-automation](skills/changelog-automation/SKILL.md) | Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. Use when setting up release workflows, generating release notes, or standardizing commit conventions. | Seth Hobson | MIT |
| [conventional-commit-review](skills/conventional-commit-review/SKILL.md) | Reviews staged changes and drafts a Conventional Commits-compliant commit message with the right type, scope, and length. Use before committing, or when the user asks to write, fix, or review a commi… | Affaan Mustafa | MIT |
| [dependency-upgrade](skills/dependency-upgrade/SKILL.md) | Manage major dependency version upgrades with compatibility analysis, staged rollout, and comprehensive testing. Use when upgrading framework versions, updating major dependencies, or managing breaki… | Seth Hobson | MIT |
| [devcontainer-setup](skills/devcontainer-setup/SKILL.md) | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development env… | Trail of Bits | CC-BY-SA-4.0 |
| [dx-optimizer](skills/dx-optimizer/SKILL.md) | Developer Experience specialist. Improves tooling, setup, and workflows. Use for requested project setup or measured development friction; respect existing team conventions. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [finishing-a-development-branch](skills/finishing-a-development-branch/SKILL.md) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | Jesse Vincent | MIT |
| [framework-migration-deps-upgrade](skills/framework-migration-deps-upgrade/SKILL.md) | You are a dependency management expert specializing in safe, incremental upgrades of project dependencies. Plan and execute dependency updates with minimal risk, proper testing, and clear migration p… | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [gh-attach](skills/gh-attach/SKILL.md) | Upload and download GitHub user-attachments (screenshots, PDFs, zips, videos) from the terminal; use when asked to attach or embed a file in a PR, issue, or comment, or download an attachment URL. | sudosubin | MIT |
| [gh-cli](skills/gh-cli/SKILL.md) | Enforces authenticated gh CLI workflows over unauthenticated curl, WebFetch, and MCP fetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues. | Trail of Bits | CC-BY-SA-4.0 |
| [git-advanced-workflows](skills/git-advanced-workflows/SKILL.md) | Master advanced Git workflows including rebasing, cherry-picking, bisect, worktrees, and reflog to maintain clean history and recover from any situation. Use when managing complex Git histories, coll… | Seth Hobson | MIT |
| [git-pr-review](skills/git-pr-review/SKILL.md) | Generate a concise and structured PR description from commit history with minimal token usage | community | MIT (code) / CC-BY-4.0 (written content) |
| [git-pr-workflows-onboard](skills/git-pr-workflows-onboard/SKILL.md) | You are an **expert onboarding specialist and knowledge transfer architect** with deep experience in remote-first organizations, technical team integration, and accelerated learning methodologies. You | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [git-workflow](skills/git-workflow/SKILL.md) | Git workflow patterns including branching strategies, commit conventions, keeping history clean and readable, tidying local commits before merging, merge vs rebase, conflict resolution, and collabora… | Affaan Mustafa | MIT |
| [git-workflow-and-versioning](skills/git-workflow-and-versioning/SKILL.md) | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitting uncommitted work in a messy working tree into clean atomic commits,… | Addy Osmani | MIT |
| [github-ops](skills/github-ops/SKILL.md) | GitHub repository operations, automation, and management. Issue triage, PR management, CI/CD operations, release management, and security monitoring using the gh CLI. Use when the user wants to manag… | Affaan Mustafa | MIT |
| [github-triage](skills/github-triage/SKILL.md) | Triages a repository's open GitHub issues and pull requests via the gh CLI. Optionally reviews and merges ready PRs — incrementally merging passing automated/bot PRs and maintainer-approved ones, and… | Trail of Bits | CC-BY-SA-4.0 |
| [monorepo-management](skills/monorepo-management/SKILL.md) | Master monorepo management with Turborepo, Nx, and pnpm workspaces to build efficient, scalable multi-package repositories with optimized builds and dependency management. Use when setting up monorep… | Seth Hobson | MIT |
| [nx-workspace-patterns](skills/nx-workspace-patterns/SKILL.md) | Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands. | Seth Hobson | MIT |
| [open-sourcing](skills/open-sourcing/SKILL.md) | This skill should be used when the user asks to "open source this project", "prepare this repository for public release", "make this repo public", "check open-source readiness", "choose a license for… | Trail of Bits | CC-BY-SA-4.0 |
| [opensource-pipeline](skills/opensource-pipeline/SKILL.md) | Open-source pipeline: fork, sanitize, and package private projects for safe public release. Chains 3 agents (forker, sanitizer, packager). Triggers: '/opensource', 'open source this', 'make this publ… | Affaan Mustafa | MIT |
| [pr](skills/pr/SKILL.md) | Use when writing a PR body. | Matt Pocock | MIT |
| [setup-pre-commit](skills/setup-pre-commit/SKILL.md) | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commi… | Matt Pocock | MIT |
| [triage](skills/triage/SKILL.md) | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. | Matt Pocock | MIT |
| [turborepo-caching](skills/turborepo-caching/SKILL.md) | Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelines, or implementing distributed caching. | Seth Hobson | MIT |
| [using-git-worktrees](skills/using-git-worktrees/SKILL.md) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback | Jesse Vincent | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
