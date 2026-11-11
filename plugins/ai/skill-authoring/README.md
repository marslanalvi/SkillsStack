# ai-skill-authoring

Creating, testing, auditing and managing agent skills, rules and hooks.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install ai-skill-authoring@skills-stack
```

## Works best with

Some skills here hand off to skills in other Skills Stack plugins. Install these too so those steps work:

- **`engineering-dev-workflow`**: `setup-matt-pocock-skills` uses `to-spec`, `setup-matt-pocock-skills` uses `to-tickets`, `using-agent-skills` uses `incremental-implementation`, `using-agent-skills` uses `planning-and-task-breakdown` and 2 more
- **`engineering-code-review-quality`**: `skill-improver` uses `code-improver`, `using-agent-skills` uses `code-review-and-quality`, `using-agent-skills` uses `code-simplification`
- **`ai-coding-assistant-workflow`**: `skill-scout` uses `agent-sort`
- **`engineering-debugging`**: `using-agent-skills` uses `debugging-and-error-recovery`
- **`engineering-git-github`**: `setup-matt-pocock-skills` uses `triage`
- **`engineering-testing`**: `using-agent-skills` uses `test-driven-development`
- **`productivity-thinking-planning`**: `using-agent-skills` uses `idea-refine`

## Skills (16)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [agent-creator](skills/agent-creator/SKILL.md) | Create custom AI subagents with proper plugin structure, persona generation, and companion routing skills. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [diagnosing-superpowers](skills/diagnosing-superpowers/SKILL.md) | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't fire, "it took too long", "why is it so… | Jesse Vincent | MIT |
| [evaluation-methodology](skills/evaluation-methodology/SKILL.md) | PluginEval quality methodology, covering dimensions, rubrics, and scoring formulas. Use this skill when understanding how plugin quality is measured, when interpreting a low score on a specific dimen… | Seth Hobson | MIT |
| [hookify-rules](skills/hookify-rules/SKILL.md) | Create and configure hookify rules — markdown files with YAML frontmatter that match bash, file, prompt, or stop events by regex or conditions and show warn/block messages to the agent. Use when crea… | Affaan Mustafa | MIT |
| [rules-distill](skills/rules-distill/SKILL.md) | Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new rule files. Use when the same principle keeps recurring across skills and belongs in a rule… | Affaan Mustafa | MIT |
| [setup-matt-pocock-skills](skills/setup-matt-pocock-skills/SKILL.md) | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills. | Matt Pocock | MIT |
| [skill-comply](skills/skill-comply/SKILL.md) | Visualize whether skills, rules, and agent definitions are actually followed — auto-generates scenarios at 3 prompt strictness levels, runs agents, classifies behavioral sequences, and reports compli… | Affaan Mustafa | MIT |
| [skill-creator](skills/skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skil… | Anthropic, PBC | Apache-2.0 (set per skill) |
| [skill-host-compat](skills/skill-host-compat/SKILL.md) | Lint ECC skills for Codex/Cursor-safe frontmatter and Claude-only substitutions before a skill PR. | Affaan Mustafa | MIT |
| [skill-improver](skills/skill-improver/SKILL.md) | Runs an autonomous review-and-fix improvement loop over a Claude Code skill until a review comes back clean, with a cross-round findings ledger, escalation when fixes stop converging, and a mechanica… | Trail of Bits | CC-BY-SA-4.0 |
| [skill-scout](skills/skill-scout/SKILL.md) | Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the user wants to create, build, fork, or find a skill for a workflow. | Affaan Mustafa | MIT |
| [skill-stocktake](skills/skill-stocktake/SKILL.md) | Use when auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full Stocktake modes with sequential subagent batch evaluation. | Affaan Mustafa | MIT |
| [using-agent-skills](skills/using-agent-skills/SKILL.md) | Discovers and invokes agent skills. Use when starting a session, or when you need to decide which skill or workflow applies to the piece of work at hand. This is the meta-skill that governs how all o… | Addy Osmani | MIT |
| [using-superpowers](skills/using-superpowers/SKILL.md) | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions | Jesse Vincent | MIT |
| [writing-for-agents](skills/writing-for-agents/SKILL.md) | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. | Matt Pocock | MIT |
| [writing-skills](skills/writing-skills/SKILL.md) | Use when creating new skills, editing existing skills, or verifying skills work before deployment | Jesse Vincent | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
