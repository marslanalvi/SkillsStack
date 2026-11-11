<div align="center">

# Skills Stack

### 1,000+ AI agent skills for almost any task, one install away

**The best open-source skills for Claude Code and other AI agents, written by the community and compiled under one roof.**

[![Skills](https://img.shields.io/badge/skills-985-blue)](CATALOG.md)
[![Plugins](https://img.shields.io/badge/plugins-45-blueviolet)](#plugins)
[![Categories](https://img.shields.io/badge/categories-9-orange)](#find-a-skill-for-your-task)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin%20marketplace-d97757)](#quick-start-claude-code)
[![Authors credited](https://img.shields.io/badge/authors-credited-brightgreen)](CREDITS.md)
[![GitHub stars](https://img.shields.io/github/stars/marslanalvi/SkillsStack?style=social)](https://github.com/marslanalvi/SkillsStack/stargazers)

**[🔍 Search all skills](https://marslanalvi.github.io/SkillsStack/)** · [Quick start](#quick-start-claude-code) · [Find a skill](#find-a-skill-for-your-task) · [Catalog](CATALOG.md) · [Credits](CREDITS.md) · [Contribute](CONTRIBUTING.md)

⭐ **If Skills Stack saves you time, star the repo** so others can find it, and so you get notified when new skills land.

</div>

Skills Stack brings together 1,000+ skills that developers, security researchers, marketers and companies have written and shared openly. We sort them into 45 installable plugins across 9 categories (engineering, DevOps, security, AI, data, design, marketing, business and productivity), so anyone can find the right skill for their task in one place. A skill is a folder with a `SKILL.md` that teaches an AI agent (Claude Code, and other agents that read `SKILL.md`) how to do one job well, such as writing a migration, auditing a smart contract, planning a launch or editing a PowerPoint.

**Skills Stack is a compilation, not the author.** Every skill here was created by someone else, and they keep all rights to their work. We credit each author in the skill's own `ATTRIBUTION.md`, list everyone in [CREDITS.md](CREDITS.md), and include the original license texts. Our work is finding, organizing, packaging and maintaining the collection. See [Credits and licensing](#credits-and-licensing).

## Quick start (Claude Code)

Add Skills Stack as a plugin marketplace once:

```bash
/plugin marketplace add marslanalvi/SkillsStack
```

Then install the plugins for the work you do:

```bash
/plugin install engineering-python@skills-stack
/plugin install marketing-seo@skills-stack
/plugin install productivity-documents-office@skills-stack
```

Run `/plugin` to browse every plugin interactively. Once a plugin is installed, Claude picks up its skills automatically when a task matches; you don't need to call them by name.

**Tip:** install only the plugins you need. Every installed skill adds its description to the agent's context, so a focused set works better than installing everything.

## Find a skill for your task

| I want to… | Install |
|---|---|
| Write better Python, TypeScript, Java, Go or Rust | `engineering-python`, `engineering-javascript-typescript`, `engineering-jvm`, `engineering-systems-languages` |
| Build a React, Vue, Next.js or mobile app | `engineering-frontend`, `engineering-mobile` |
| Design an API or a system architecture | `engineering-architecture-api`, `engineering-databases` |
| Write tests, review code, or fix a bug | `engineering-testing`, `engineering-code-review-quality`, `engineering-debugging` |
| Deploy to the cloud, Kubernetes or CI/CD | `devops-cloud`, `devops-containers-kubernetes`, `devops-ci-cd` |
| Audit code for security, pentest or fuzz | `security-appsec-review`, `security-offensive-security`, `security-fuzzing` |
| Audit a smart contract | `security-blockchain-web3` |
| Build AI agents, RAG apps or fine-tune a model | `ai-agent-engineering`, `ai-llm-applications`, `ai-machine-learning` |
| Get more out of Claude Code itself | `ai-coding-assistant-workflow`, `ai-skill-authoring` |
| Research a topic or analyze data | `data-research`, `data-data-engineering-analytics` |
| Design a UI, make videos, images or slides | `design-ui-ux`, `design-media-creative` |
| Rank on Google and in AI search | `marketing-seo` |
| Write copy, run ads, grow a product | `marketing-content-social`, `marketing-growth-ads` |
| Pitch investors, research a market, sell | `business-strategy-sales` |
| Create Word, PDF, Excel or PowerPoint files | `productivity-documents-office` |
| Write clearly, brainstorm, plan, decide | `productivity-writing-communication`, `productivity-thinking-planning` |

Install any of them with `/plugin install <name>@skills-stack`, or [search every skill](https://marslanalvi.github.io/SkillsStack/) by keyword.

## Other ways to use it

- **Search:** the [Skills Stack website](https://marslanalvi.github.io/SkillsStack/) searches every skill by keyword and category, and shows the install command for each.
- **Browse:** [CATALOG.md](CATALOG.md) lists every skill with a one-line description, grouped by category and plugin.
- **Copy a single skill:** copy any folder under `plugins/<category>/<plugin>/skills/` into your project's `.claude/skills/` (or `~/.claude/skills/` for all projects).
- **Search or build tools on it:** [catalog.json](catalog.json) has the same data in machine-readable form.

## Plugins

<!-- PLUGINS:START -->
**985 skills in 45 plugins.**

| Category | Plugin | Skills | What's inside |
|---|---|---:|---|
| engineering | [`engineering-python`](plugins/engineering/python) | 29 | Python patterns, packaging, typing, async, testing and frameworks (Django, FastAPI) |
| engineering | [`engineering-javascript-typescript`](plugins/engineering/javascript-typescript) | 14 | JavaScript, TypeScript, Node.js, Bun and server-side JS frameworks (NestJS, etc.) |
| engineering | [`engineering-jvm`](plugins/engineering/jvm) | 18 | Java, Kotlin and JVM frameworks (Spring Boot, Quarkus, Ktor, JPA) |
| engineering | [`engineering-systems-languages`](plugins/engineering/systems-languages) | 11 | Rust, Go, C and C++: systems programming, concurrency and memory safety |
| engineering | [`engineering-other-languages`](plugins/engineering/other-languages) | 25 | PHP/Laravel, Ruby/Rails, Perl, .NET/C#/F#, and other languages and frameworks |
| engineering | [`engineering-frontend`](plugins/engineering/frontend) | 34 | Web frontend: React, Vue, Angular, Next.js, Nuxt, CSS/Tailwind and frontend performance |
| engineering | [`engineering-mobile`](plugins/engineering/mobile) | 23 | iOS, Android, Flutter, React Native, SwiftUI, Expo and desktop apps |
| engineering | [`engineering-architecture-api`](plugins/engineering/architecture-api) | 27 | Software architecture, API design, microservices, event-driven systems and design patterns |
| engineering | [`engineering-databases`](plugins/engineering/databases) | 10 | SQL, Postgres, MySQL, Redis, ORMs, schema design and migrations |
| engineering | [`engineering-testing`](plugins/engineering/testing) | 16 | TDD, unit/integration/E2E testing, test patterns and verification |
| engineering | [`engineering-code-review-quality`](plugins/engineering/code-review-quality) | 27 | Code review, refactoring, simplification, code quality and technical debt |
| engineering | [`engineering-debugging`](plugins/engineering/debugging) | 20 | Debugging, root-cause analysis, error handling and regression hunting |
| engineering | [`engineering-dev-workflow`](plugins/engineering/dev-workflow) | 34 | Planning, specs, tickets, documentation/ADRs, onboarding and implementation workflow |
| engineering | [`engineering-git-github`](plugins/engineering/git-github) | 27 | Git, GitHub, pull requests, releases, monorepos, build tooling and dependency upgrades |
| engineering | [`engineering-game-development`](plugins/engineering/game-development) | 3 | Game engines and game development (Unity, Godot, Minecraft, etc.) |
| devops | [`devops-ci-cd`](plugins/devops/ci-cd) | 7 | CI/CD pipelines, GitHub Actions, GitLab CI, release and deployment automation |
| devops | [`devops-containers-kubernetes`](plugins/devops/containers-kubernetes) | 11 | Docker, Kubernetes, Helm, service mesh and GitOps |
| devops | [`devops-cloud`](plugins/devops/cloud) | 26 | AWS, Azure, GCP, Cloudflare, serverless and multi-cloud |
| devops | [`devops-observability-sre`](plugins/devops/observability-sre) | 16 | Monitoring, tracing, logging, SLOs, incident response and on-call |
| devops | [`devops-infrastructure-networking`](plugins/devops/infrastructure-networking) | 21 | Terraform/IaC, Linux administration, shell scripting, networking and homelab |
| security | [`security-appsec-review`](plugins/security/appsec-review) | 54 | Secure coding, security code review, static analysis (Semgrep, CodeQL) and audits |
| security | [`security-offensive-security`](plugins/security/offensive-security) | 23 | Penetration testing, bug bounty, vulnerability hunting, reverse engineering and threat modeling |
| security | [`security-fuzzing`](plugins/security/fuzzing) | 19 | Fuzzing, sanitizers, property-based and cryptographic testing |
| security | [`security-blockchain-web3`](plugins/security/blockchain-web3) | 19 | Smart-contract security, DeFi, Solidity and Web3 development |
| security | [`security-compliance-privacy`](plugins/security/compliance-privacy) | 5 | HIPAA, GDPR, PCI, SOC and other compliance, privacy and secrets management |
| ai | [`ai-agent-engineering`](plugins/ai/agent-engineering) | 54 | Building AI agents: harnesses, multi-agent orchestration, autonomous loops and agent evaluation |
| ai | [`ai-llm-applications`](plugins/ai/llm-applications) | 15 | LLM apps: prompting, RAG, embeddings, vector search, caching, evals and model APIs |
| ai | [`ai-machine-learning`](plugins/ai/machine-learning) | 26 | ML training, fine-tuning, MLOps, model serving, PyTorch and data science |
| ai | [`ai-coding-assistant-workflow`](plugins/ai/coding-assistant-workflow) | 70 | Getting more from AI coding assistants: setup, context and token management, memory, guardrails, subagents |
| ai | [`ai-skill-authoring`](plugins/ai/skill-authoring) | 16 | Creating, testing, auditing and managing agent skills, rules and hooks |
| data | [`data-data-engineering-analytics`](plugins/data/data-engineering-analytics) | 9 | Data pipelines (Airflow, dbt, Spark), analytics, dashboards and metrics |
| data | [`data-research`](plugins/data/research) | 25 | Deep research, web search, scientific literature, scraping and fact-finding |
| design | [`design-ui-ux`](plugins/design/ui-ux) | 26 | UI/UX design, design systems, visual styles, interaction and landing pages |
| design | [`design-media-creative`](plugins/design/media-creative) | 25 | Images, video, motion, animation, generative art, diagrams and presentations visuals |
| design | [`design-accessibility`](plugins/design/accessibility) | 6 | Accessibility audits, WCAG, screen readers and inclusive design |
| marketing | [`marketing-seo`](plugins/marketing/seo) | 17 | SEO, AI search optimization, schema markup, programmatic SEO and site architecture |
| marketing | [`marketing-content-social`](plugins/marketing/content-social) | 22 | Content strategy, copywriting for marketing, social media, newsletters and PR |
| marketing | [`marketing-growth-ads`](plugins/marketing/growth-ads) | 33 | Growth, CRO, ads, analytics tracking, A/B tests, pricing, email/SMS campaigns and launches |
| business | [`business-strategy-sales`](plugins/business/strategy-sales) | 21 | Startup strategy, market research, competitive analysis, sales, fundraising and investor work |
| business | [`business-operations-finance`](plugins/business/operations-finance) | 25 | Finance, billing, payments, logistics, supply chain, HR and operations |
| business | [`business-legal-industry`](plugins/business/legal-industry) | 12 | Legal documents, contracts and industry-specific work (healthcare, government, real estate, etc.) |
| productivity | [`productivity-documents-office`](plugins/productivity/documents-office) | 14 | Word, PDF, PowerPoint, Excel, Google Workspace and file conversion |
| productivity | [`productivity-writing-communication`](plugins/productivity/writing-communication) | 12 | Writing, editing, internal communication and avoiding AI-sounding prose |
| productivity | [`productivity-thinking-planning`](plugins/productivity/thinking-planning) | 18 | Brainstorming, idea evaluation, decision making, interviewing and learning |
| productivity | [`productivity-automation-personal`](plugins/productivity/automation-personal) | 20 | Personal and workplace automation: calendar, email, chat, daily routines, OS utilities, no-code workflows |
<!-- PLUGINS:END -->

## Repository layout

```text
SkillsStack/
├── .claude-plugin/marketplace.json   # lists every plugin for /plugin install
├── plugins/
│   └── <category>/<plugin>/
│       ├── .claude-plugin/plugin.json
│       ├── README.md                 # the plugin's skills, with who created each one
│       ├── LICENSES/                 # full license texts for this plugin's skills
│       └── skills/<skill>/
│           ├── SKILL.md              # the skill itself, as its author wrote it
│           ├── ATTRIBUTION.md        # who created it, its license, and any changes we made
│           └── ...                   # scripts, references, assets
├── alternates/                       # other versions of duplicated skills (not installed)
├── templates/skill-template/         # Anthropic's blank skill template, for reference (not installed)
├── licenses/                         # full license text of every upstream project
├── sources/                          # collection-level files kept from upstream
├── CREDITS.md                        # everyone whose work is in Skills Stack
├── NOTICE.md                         # compilation notice and licensing terms
├── CATALOG.md / catalog.json         # generated index of every skill
└── tools/                            # scripts that build and maintain the collection
```

## Duplicates

When the same skill came from more than one source, the most complete version is in the plugin and the others are kept in [`alternates/`](alternates). They're listed at the end of [CATALOG.md](CATALOG.md) so you can compare them. Alternates aren't installed by any plugin.

## Adding or changing skills

Only add skills whose license allows redistribution, and always credit the author.

1. Put the skill folder in the plugin it fits: `plugins/<category>/<plugin>/skills/<skill-name>/`. The folder needs a `SKILL.md` whose frontmatter has `name` and `description`. Don't remove the author's own license or credit lines.
2. If the skill comes from a project Skills Stack doesn't credit yet, add the project to [`tools/credits.json`](tools/credits.json) (project name, author, license) and put its full license text in `licenses/<owner>__<repo>/`.
3. Add an `ATTRIBUTION.md` with frontmatter `collected_from: <repo URL>` and `original_path: <where it came from>`. If you changed any of the skill's files, say what changed in [`tools/changes.json`](tools/changes.json).
4. Rebuild the generated files and check for problems:

   ```bash
   python tools/attribution.py
   python tools/build_catalog.py
   claude plugin validate .
   ```

To add a new plugin or category, add it to [`tools/taxonomy.json`](tools/taxonomy.json), create its `skills/` folder, and rebuild. `attribution.py` writes each skill's credit and copies the license texts into each plugin. `build_catalog.py` regenerates every `plugin.json`, the plugin READMEs, the marketplace file, `CATALOG.md`, `catalog.json`, `CREDITS.md` and the plugin table above. Both need Python 3 with PyYAML (`pip install pyyaml`).

## Credits and licensing

### Thank you

Every skill in Skills Stack was created by someone who chose to share their work with everyone. The credit belongs to them:

| Project | Created by | License |
|---|---|---|
| [Everything Claude Code (ECC)](https://github.com/affaan-m/ecc) | Affaan Mustafa | MIT |
| [Agentic Awesome Skills](https://github.com/sickn33/agentic-awesome-skills) | sickn33 and contributors, and the individual skill authors credited in each skill | MIT / CC-BY-4.0 |
| [Agents](https://github.com/wshobson/agents) | Seth Hobson | MIT |
| [Trail of Bits Skills](https://github.com/trailofbits/skills) | Trail of Bits | CC-BY-SA-4.0 |
| [Marketing Skills](https://github.com/coreyhaines31/marketingskills) | Corey Haines | MIT |
| [Skills](https://github.com/mattpocock/skills) | Matt Pocock | MIT |
| [Agent Skills](https://github.com/addyosmani/agent-skills) | Addy Osmani | MIT |
| [Anthropic Agent Skills](https://github.com/anthropics/skills) | Anthropic, PBC | Apache-2.0 (per skill) |
| [Superpowers](https://github.com/obra/superpowers) | Jesse Vincent | MIT |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Next Level Builder | MIT |
| [Security Audit Skill](https://github.com/cloudflare/security-audit-skill) | Cloudflare, Inc. | MIT |
| [Karpathy-Inspired Claude Code Guidelines](https://github.com/multica-ai/andrej-karpathy-skills) | Forrest Chang, based on Andrej Karpathy's observations | MIT |

[CREDITS.md](CREDITS.md) has the full list, including the individual authors of skills from community collections. If your work is here, thank you.

### How Skills Stack respects authors' rights

- **We compile; we don't claim.** Skills Stack doesn't claim ownership of any skill. The authors keep their copyright, and their own license applies to their work.
- **Credit travels with every skill.** Each skill folder has an `ATTRIBUTION.md` naming its creator, the project it came from, its license and a link to the original. The plugin READMEs and [CATALOG.md](CATALOG.md) show who created each skill.
- **License texts are included.** The full license and copyright notice for every upstream project is in [`licenses/`](licenses), and each plugin carries a copy of the licenses its skills need in its own `LICENSES/` folder, so the terms stay with the skills when a plugin is installed on its own. Skills that ship their own `LICENSE` file keep it, and that file is the one that applies.
- **Content is unchanged.** Skills are kept as their authors wrote them. Where we had to change a file (12 skills, mostly to fix links after moving folders), the skill's `ATTRIBUTION.md` says exactly what changed, as the Creative Commons licenses require.
- **Authors stay in control.** If you wrote a skill here and want the credit changed or the skill removed, [open an issue](https://github.com/marslanalvi/SkillsStack/issues) and we'll act on it promptly.

### Before you reuse a skill

Each skill's license is the one that applies to it, and you must follow its terms. Most skills are MIT, which lets you use, change and share them as long as you keep the copyright and license notice. A few licenses ask for more:

- **CC-BY-SA-4.0** (Trail of Bits skills, most of `security-*`): credit Trail of Bits, say what you changed, and share your adapted version under the same license.
- **CC-BY-4.0** (written content from Agentic Awesome Skills): credit the authors and say what you changed.
- **Apache-2.0** (Anthropic skills and some others): keep the license and any notices, and mark files you changed.

See [NOTICE.md](NOTICE.md) for the full compilation notice. This README is not legal advice.

## Known limitations

- Skills were sorted into categories automatically and reviewed by hand. A few could fit more than one plugin; suggestions are welcome.
- Some skills hand off to a skill in another plugin (for example, `grill-with-docs` uses `domain-modeling`). Each plugin's README lists these under **Works best with**; install those plugins too, or the hand-off step is skipped. A few file links between skills in different plugins also only resolve when both plugins are installed.
- Some skills link to files their upstream repositories never included in the collected folder. Those links were already broken before Skills Stack collected them.
- `plugins/ai/agent-engineering/skills/loki-mode` includes about 650 SWE-bench benchmark `.patch` files from upstream. They make the plugin larger to download, but they don't affect how the skill works.
