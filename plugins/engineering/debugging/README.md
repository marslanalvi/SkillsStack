# engineering-debugging

Debugging, root-cause analysis, error handling and regression hunting.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install engineering-debugging@skills-stack
```

## Skills (20)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [adjudicate-regression](skills/adjudicate-regression/SKILL.md) | Use when deciding whether source and live reproduction evidence establish a new regression or an exclusion. | Trail of Bits | CC-BY-SA-4.0 |
| [click-path-audit](skills/click-path-audit/SKILL.md) | Trace every user-facing button/touchpoint through its full state change sequence to find bugs where functions individually work but cancel each other out, produce wrong final state, or leave the UI i… | Affaan Mustafa | MIT |
| [debugger](skills/debugger/SKILL.md) | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [debugging-and-error-recovery](skills/debugging-and-error-recovery/SKILL.md) | Guides systematic root-cause debugging. Use when tests fail, builds break, something that worked yesterday broke, behavior doesn't match expectations, or you encounter any unexpected error. Use when… | Addy Osmani | MIT |
| [debugging-strategies](skills/debugging-strategies/SKILL.md) | Master systematic debugging techniques, profiling tools, and root cause analysis to efficiently track down bugs across any codebase or technology stack. Use when investigating bugs, performance issue… | Seth Hobson | MIT |
| [debugging-toolkit](skills/debugging-toolkit/SKILL.md) | Use when working with debugging toolkit smart debug (Alias for debugging-toolkit-smart-debug) | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [diagnosing-bugs](skills/diagnosing-bugs/SKILL.md) | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. | Matt Pocock | MIT |
| [error-detective](skills/error-detective/SKILL.md) | Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [error-handling](skills/error-handling/SKILL.md) | Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries, retries, circuit breakers, and user-facing error messages. Use when designing error types,… | Affaan Mustafa | MIT |
| [hunt-regressions](skills/hunt-regressions/SKILL.md) | Use when discovering possible regressions from a pinned change and its callers before reproduction. | Trail of Bits | CC-BY-SA-4.0 |
| [logic-review](skills/logic-review/SKILL.md) | Find logic bugs in a single file or function via semi-formal execution tracing (Premises → Trace → Divergence → Trigger → Remedy). | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT |
| [parallel-debugging](skills/parallel-debugging/SKILL.md) | Debug complex issues using competing hypotheses with parallel investigation, evidence collection, and root cause arbitration. Use this skill when debugging bugs with multiple potential causes, perfor… | Seth Hobson | MIT |
| [patching-bugs](skills/patching-bugs/SKILL.md) | Use when a known bug or falsifiable bug hypothesis in a local codebase needs a patch commit and reviewable proof report. | Trail of Bits | CC-BY-SA-4.0 |
| [prepare-regression](skills/prepare-regression/SKILL.md) | Use when pinning before/after sources and collecting PR or commit context for a regression investigation. | Trail of Bits | CC-BY-SA-4.0 |
| [regression-hunt](skills/regression-hunt/SKILL.md) | Use when investigating regressions in PRs or commits, coordinating a regression campaign, or resuming saved progress. | Trail of Bits | CC-BY-SA-4.0 |
| [replay-regression](skills/replay-regression/SKILL.md) | Use when independently verifying a supplied PoC against fresh live before/after deployments. | Trail of Bits | CC-BY-SA-4.0 |
| [report-regressions](skills/report-regressions/SKILL.md) | Use when assembling or refreshing an evidence-linked regression report from saved campaign decisions. | Trail of Bits | CC-BY-SA-4.0 |
| [reproduce-bug](skills/reproduce-bug/SKILL.md) | Use when a named runtime or compiler bug in a local repository needs independent reproduction. | Trail of Bits | CC-BY-SA-4.0 |
| [reproduce-regression](skills/reproduce-regression/SKILL.md) | Use when deploying before/after systems and building a live-system PoC for a regression candidate. | Trail of Bits | CC-BY-SA-4.0 |
| [systematic-debugging](skills/systematic-debugging/SKILL.md) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | Jesse Vincent | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
