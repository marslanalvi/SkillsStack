# engineering-testing

TDD, unit/integration/E2E testing, test patterns and verification.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install engineering-testing@skills-stack
```

## Works best with

Some skills here hand off to skills in other Skills Stack plugins. Install these too so those steps work:

- **`engineering-architecture-api`**: `tdd` uses `codebase-design`
- **`engineering-code-review-quality`**: `tdd` uses `code-review`
- **`engineering-javascript-typescript`**: `tdd-workflow` uses `bun-runtime`

## Skills (16)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [agentic-verify](skills/agentic-verify/SKILL.md) | Check that a Python change is caught by tests: run every mutant of the changed lines and write tests until they catch them. Reports evidence instead of a diff to read. | Tim Richardson | MIT |
| [ai-regression-testing](skills/ai-regression-testing/SKILL.md) | Regression testing strategies for AI-assisted development. Sandbox-mode API testing without database dependencies, automated bug-check workflows, and patterns to catch AI blind spots where the same m… | Affaan Mustafa | MIT |
| [awt-e2e-testing](skills/awt-e2e-testing/SKILL.md) | AI-powered E2E web testing — eyes and hands for AI coding tools. Declarative YAML scenarios, Playwright execution, visual matching (OpenCV + OCR), platform auto-detection (Flutter/React/Vue), learnin… | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [browser-qa](skills/browser-qa/SKILL.md) | Run automated post-deploy UI verification with a browser automation MCP (claude-in-chrome, Playwright, or Puppeteer): console-error and Core Web Vitals smoke checks, form and auth-flow interaction te… | Affaan Mustafa | MIT |
| [browser-testing-with-devtools](skills/browser-testing-with-devtools/SKILL.md) | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. Use when you need to inspect the DOM, capture console errors, analyze network requests,… | Addy Osmani | MIT |
| [code-showcase-testing-patterns](skills/code-showcase-testing-patterns/SKILL.md) | Jest testing patterns, factory functions, mocking strategies, and TDD workflow. Use when writing unit tests, creating test factories, or following TDD red-green-refactor cycle. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT |
| [e2e-testing](skills/e2e-testing/SKILL.md) | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies. Use when writing Playwright tests, structuring page objects, or f… | Affaan Mustafa | MIT |
| [e2e-testing-patterns](skills/e2e-testing-patterns/SKILL.md) | Master end-to-end testing with Playwright and Cypress to build reliable test suites that catch bugs, improve confidence, and enable fast deployment. Use when implementing E2E tests, debugging flaky t… | Seth Hobson | MIT |
| [mutation-testing](skills/mutation-testing/SKILL.md) | Configures mewt or muton campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign results, identifying equivalent… | Trail of Bits | CC-BY-SA-4.0 |
| [tdd](skills/tdd/SKILL.md) | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. | Matt Pocock | MIT |
| [tdd-workflow](skills/tdd-workflow/SKILL.md) | Test-driven development workflow: write a failing test first, watch it fail, implement the smallest change to green, then refactor with 80%+ coverage across unit, integration, and E2E tests. Use when… | Affaan Mustafa | MIT |
| [test-collaboration](skills/test-collaboration/SKILL.md) | Inventory and govern a project's test assets. Connect requirements, business rules, risks, bugs, and cross-boundary contracts to stable TEST-IDs and executable evidence in the repository's existing t… | Affaan Mustafa | MIT |
| [test-driven-development](skills/test-driven-development/SKILL.md) | Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that code works, when a bug repo… | Addy Osmani | MIT |
| [verification-before-completion](skills/verification-before-completion/SKILL.md) | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidenc… | Jesse Vincent | MIT |
| [webapp-testing](skills/webapp-testing/SKILL.md) | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser… | Anthropic, PBC | Complete terms in LICENSE.txt |
| [windows-desktop-e2e](skills/windows-desktop-e2e/SKILL.md) | E2E testing for Windows native desktop apps (WPF, WinForms, Win32/MFC, Qt) using pywinauto and Windows UI Automation. Use when writing E2E tests for a Windows native desktop app with pywinauto or UI… | Affaan Mustafa | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
