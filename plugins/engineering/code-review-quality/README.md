# engineering-code-review-quality

Code review, refactoring, simplification, code quality and technical debt.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install engineering-code-review-quality@skills-stack
```

## Skills (27)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [ai-debt-detector](skills/ai-debt-detector/SKILL.md) | Use after generating code, after accepting AI suggestions, or when reviewing AI-written modules. Also use when code works but feels brittle, when error handling seems thin, when orphaned resources or… | Seth Hobson | MIT |
| [benchmark](skills/benchmark/SKILL.md) | Measure performance baselines and detect regressions across browser Core Web Vitals (LCP, INP, CLS, page weight), API endpoint latency percentiles, and build/test feedback times, with before/after co… | Affaan Mustafa | MIT |
| [benchmark-optimization-loop](skills/benchmark-optimization-loop/SKILL.md) | Convert 'make it faster' requests into a bounded measured optimization loop — baseline first, generate one-hypothesis variants, benchmark each against a correctness gate, and promote the fastest safe… | Affaan Mustafa | MIT |
| [brooks-lint](skills/brooks-lint/SKILL.md) | AI code reviewer grounded in classic software engineering books for catching design smells, coupling issues, and architectural risks. | hyhmrright | MIT |
| [change-impact](skills/change-impact/SKILL.md) | Perform evidence-backed impact analysis before changing code, data, interfaces, or governance documents, then compare the planned impact with the actual diff after implementation. Covers call paths,… | Affaan Mustafa | MIT |
| [code-improver](skills/code-improver/SKILL.md) | Runs an autonomous review-and-fix improvement loop over any code target — a skill, plugin, module, or directory — using a reviewer the user names: any installed skill or agent. Keeps a cross-round fi… | Trail of Bits | CC-BY-SA-4.0 |
| [code-review](skills/code-review/SKILL.md) | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match wha… | Matt Pocock | MIT |
| [code-review-and-quality](skills/code-review-and-quality/SKILL.md) | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimens… | Addy Osmani | MIT |
| [code-review-checklist](skills/code-review-checklist/SKILL.md) | Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [code-review-excellence](skills/code-review-excellence/SKILL.md) | Master effective code review practices to provide constructive feedback, catch bugs early, and foster knowledge sharing while maintaining team morale. Use when reviewing pull requests, establishing r… | Seth Hobson | MIT |
| [code-reviewer](skills/code-reviewer/SKILL.md) | Elite code review expert specializing in modern AI-powered code | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [code-simplification](skills/code-simplification/SKILL.md) | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than it should be. Use when reviewing code… | Addy Osmani | MIT |
| [codehealth-mcp](skills/codehealth-mcp/SKILL.md) | Real-time structural Code Health via CodeScene MCP — review before edits, verify score deltas after changes, gate commits and PRs. Use when reviewing code quality, refactoring, checking if AI changes… | Affaan Mustafa | MIT |
| [coding-standards](skills/coding-standards/SKILL.md) | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use detailed frontend or backend skills for framework-specific patterns. Use when reviewing c… | Affaan Mustafa | MIT |
| [debate-review](skills/debate-review/SKILL.md) | Two-model debate review of a GitHub PR, GitLab MR, Azure DevOps PR, or local working tree, posted as inline comments or printed. Use for any PR/MR review request, or a local review before a PR exists. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT |
| [issue-review](skills/issue-review/SKILL.md) | Review a GitHub issue the way /code-review reviews a PR. Fetches the issue with the gh CLI, checks the report against the current codebase, searches for duplicates and prior fixes, scores completenes… | Affaan Mustafa | MIT |
| [multi-reviewer-patterns](skills/multi-reviewer-patterns/SKILL.md) | Coordinate parallel code reviews across multiple quality dimensions with finding deduplication, severity calibration, and consolidated reporting. Use this skill when organizing multi-reviewer code re… | Seth Hobson | MIT |
| [panel-review](skills/panel-review/SKILL.md) | Reviews a code target by launching a panel of specialist auditor agents and merging their reports. Use when asked to run a panel review. | Trail of Bits | CC-BY-SA-4.0 |
| [performance-optimization](skills/performance-optimization/SKILL.md) | Optimizes application performance across frontend, backend, queries, and databases. Use when performance requirements exist, when you suspect performance regressions, when Core Web Vitals or load tim… | Addy Osmani | MIT |
| [plankton-code-quality](skills/plankton-code-quality/SKILL.md) | Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on every file edit via hooks. Use when setting up write-time formatting, linting, or auto-fix h… | Affaan Mustafa | MIT |
| [pr-improver](skills/pr-improver/SKILL.md) | Runs an autonomous review-and-fix improvement loop over the current branch's changes until a PR review comes back clean, scoped mechanically to the directories the branch touched. Reviews are perform… | Trail of Bits | CC-BY-SA-4.0 |
| [production-audit](skills/production-audit/SKILL.md) | Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what breaks in prod?" questions without sending repo data to an external audit service. Use whe… | Affaan Mustafa | MIT |
| [receiving-code-review](skills/receiving-code-review/SKILL.md) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performativ… | Jesse Vincent | MIT |
| [requesting-code-review](skills/requesting-code-review/SKILL.md) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | Jesse Vincent | MIT |
| [review-pr](skills/review-pr/SKILL.md) | Reviews the current branch's changes against its base branch as a pull request: correctness of new and modified code, test coverage for it, and documentation accuracy. Use when asked to review a bran… | Trail of Bits | CC-BY-SA-4.0 |
| [review-walkthrough](skills/review-walkthrough/SKILL.md) | Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called. | Trail of Bits | CC-BY-SA-4.0 |
| [second-opinion](skills/second-opinion/SKILL.md) | Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits. Use when the user requests an external review, a second opinion on code, a codex review, a… | Trail of Bits | CC-BY-SA-4.0 |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
