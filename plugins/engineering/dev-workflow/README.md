# engineering-dev-workflow

Planning, specs, tickets, documentation/ADRs, onboarding and implementation workflow.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install engineering-dev-workflow@skills-stack
```

## Skills (34)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [api-documentation-generator](skills/api-documentation-generator/SKILL.md) | Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [architecture-decision-records](skills/architecture-decision-records/SKILL.md) | Capture architectural decisions as numbered ADR markdown files in docs/adr/ with context, alternatives considered, consequences, and an index README. Use when the user says 'record this decision' or… | Affaan Mustafa | MIT |
| [blueprint](skills/blueprint/SKILL.md) | Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent engineering projects: one-PR-sized steps with self-contained context briefs, dependency graph with paral… | Affaan Mustafa | MIT |
| [brownfield-retrospective](skills/brownfield-retrospective/SKILL.md) | Run the ECC engineering process retroactively against an existing project slice. Audit current state, reconstruct past decisions, produce a four-axis gap register (thinking, coding practice, missing… | Affaan Mustafa | MIT |
| [code-tour](skills/code-tour/SKILL.md) | Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors. Use for onboarding tours, architecture walkthroughs, PR tours, RCA tours, and structured "… | Affaan Mustafa | MIT |
| [codebase-onboarding](skills/codebase-onboarding/SKILL.md) | Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions, and a starter CLAUDE.md. Use when joining a new project or setting up C… | Affaan Mustafa | MIT |
| [context-and-decisions](skills/context-and-decisions/SKILL.md) | Govern stable domain context with a narrowly scoped CONTEXT.md when needed, and route hard-to-reverse decisions to ECC's existing architecture-decision-records skill. Use when domain terms require re… | Affaan Mustafa | MIT |
| [deprecation-and-migration](skills/deprecation-and-migration/SKILL.md) | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when migrating a database schema in production, s… | Addy Osmani | MIT |
| [docs-governance](skills/docs-governance/SKILL.md) | Route broad documentation-governance requests to existing ECC skills and run an opt-in, read-only audit of mapped documentation roles, links, ADR indexes, and evidence references. Use when a user ask… | Affaan Mustafa | MIT |
| [documentation-and-adrs](skills/documentation-and-adrs/SKILL.md) | Records decisions and documentation. Use when you need to document an architecture decision (ADR) or the reasoning behind a design choice, when changing public APIs, shipping features, or when you ne… | Addy Osmani | MIT |
| [executing-plans](skills/executing-plans/SKILL.md) | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available | Jesse Vincent | MIT |
| [implement](skills/implement/SKILL.md) | Implement a piece of work based on a spec or set of tickets. | Matt Pocock | MIT |
| [implement-spec](skills/implement-spec/SKILL.md) | Implement the result of /to-spec and /to-tickets in code. | Matt Pocock | MIT |
| [incremental-implementation](skills/incremental-implementation/SKILL.md) | Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the next task from a plan. Use when rolling… | Addy Osmani | MIT |
| [intent-driven-development](skills/intent-driven-development/SKILL.md) | Turn ambiguous or high-impact product and engineering changes into scoped, verifiable acceptance criteria before or alongside implementation. Use when a user asks to clarify a feature, define accepta… | Affaan Mustafa | MIT |
| [jira-integration](skills/jira-integration/SKILL.md) | Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning issues. Provides Jira API patterns via MCP or direct REST calls. | Affaan Mustafa | MIT |
| [living-docs-governance](skills/living-docs-governance/SKILL.md) | Keep a long-lived project's documentation from rotting by assigning existing project docs clear constitution, map, status, and history roles, then wiring the active agent harness to those canonical s… | Affaan Mustafa | MIT |
| [module-regression](skills/module-regression/SKILL.md) | Govern cross-module regression in large repositories with a REGRESSION.md ledger that records each module's downstream consumers and executable acceptance command. After a change, run the changed mod… | Affaan Mustafa | MIT |
| [nerdzao-elite](skills/nerdzao-elite/SKILL.md) | Software engineering and product design workflow and Senior Product Designer. Full workflow with planning, architecture, TDD, clean code, and pixel-perfect UX validation. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [planning-and-task-breakdown](skills/planning-and-task-breakdown/SKILL.md) | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when you need to estimate sco… | Addy Osmani | MIT |
| [product-capability](skills/product-capability/SKILL.md) | Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions before multi-service… | Affaan Mustafa | MIT |
| [project-flow-ops](skills/project-flow-ops/SKILL.md) | Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub public-facing while Linear remains the internal execution layer. Use when… | Affaan Mustafa | MIT |
| [prototype](skills/prototype/SKILL.md) | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like. | Matt Pocock | MIT |
| [retro](skills/retro/SKILL.md) | Conduct a retrospective on a coding session. | Matt Pocock | MIT |
| [scaffold-exercises](skills/scaffold-exercises/SKILL.md) | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course sec… | Matt Pocock | MIT |
| [search-first](skills/search-first/SKILL.md) | Research-before-coding workflow: search npm/PyPI, MCP servers, skills, and GitHub for existing tools before writing custom code, then adopt, extend, or build. Launches the researcher agent for non-tr… | Affaan Mustafa | MIT |
| [shipping-and-launch](skills/shipping-and-launch/SKILL.md) | Prepares production launches. Use when preparing to deploy to production, or when asking what needs to be in place before shipping. Use when you need a pre-launch checklist, when setting up monitorin… | Addy Osmani | MIT |
| [source-driven-development](skills/source-driven-development/SKILL.md) | Grounds every implementation decision in official documentation. Use when you want to verify an approach against the official docs before implementing it, or when you want authoritative, source-cited… | Addy Osmani | MIT |
| [spec-driven-development](skills/spec-driven-development/SKILL.md) | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when drafting a PRD or requirements document with objectives and scop… | Addy Osmani | MIT |
| [story-lifecycle](skills/story-lifecycle/SKILL.md) | Manage a file-based epic → story → sprint development loop without requiring an external project management tool. Creates and tracks epics, breaks them into user stories, assigns them to sprints, and… | Affaan Mustafa | MIT |
| [to-spec](skills/to-spec/SKILL.md) | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. | Matt Pocock | MIT |
| [to-tickets](skills/to-tickets/SKILL.md) | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket local… | Matt Pocock | MIT |
| [wayfinder](skills/wayfinder/SKILL.md) | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear. | Matt Pocock | MIT |
| [writing-plans](skills/writing-plans/SKILL.md) | Use when you have a spec or requirements for a multi-step task, before touching code | Jesse Vincent | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
