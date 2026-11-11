# engineering-architecture-api

Software architecture, API design, microservices, event-driven systems and design patterns.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install engineering-architecture-api@skills-stack
```

## Works best with

Some skills here hand off to skills in other Skills Stack plugins. Install these too so those steps work:

- **`productivity-thinking-planning`**: `improve-codebase-architecture` uses `grilling`

## Skills (27)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [api-and-interface-design](skills/api-and-interface-design/SKILL.md) | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or GraphQL endpoints, defining type contracts between modules, or e… | Addy Osmani | MIT |
| [api-connector-builder](skills/api-connector-builder/SKILL.md) | Build a new API connector or provider by matching the target repo's existing integration pattern exactly. Use when adding one more integration without inventing a second architecture. | Affaan Mustafa | MIT |
| [api-design](skills/api-design/SKILL.md) | REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs. Use when designing or reviewing REST endpo… | Affaan Mustafa | MIT |
| [api-design-principles](skills/api-design-principles/SKILL.md) | Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers. Use when designing new APIs, reviewing API specifications, or establishing A… | Seth Hobson | MIT |
| [api-integration](skills/api-integration/SKILL.md) | Designs event-driven architectures, webhook systems, API chaining flows, ETL pipelines, and integration patterns between services. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT |
| [api-patterns](skills/api-patterns/SKILL.md) | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [architecture-patterns](skills/architecture-patterns/SKILL.md) | Implement proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design. Use this skill when designing clean architecture for a new microservice,… | Seth Hobson | MIT |
| [auth-implementation-patterns](skills/auth-implementation-patterns/SKILL.md) | Master authentication and authorization patterns including JWT, OAuth2, session management, and RBAC to build secure, scalable access control systems. Use when implementing auth systems, securing API… | Seth Hobson | MIT |
| [backend-patterns](skills/backend-patterns/SKILL.md) | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. Use when building or reviewing Node.js, Express, or Next… | Affaan Mustafa | MIT |
| [codebase-design](skills/codebase-design/SKILL.md) | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-… | Matt Pocock | MIT |
| [content-hash-cache-pattern](skills/content-hash-cache-pattern/SKILL.md) | Cache expensive file processing results using SHA-256 content hashes — path-independent, auto-invalidating, with service layer separation. Use when repeated file processing is slow and results should… | Affaan Mustafa | MIT |
| [contract-first](skills/contract-first/SKILL.md) | Coordinate frontend/backend or service-to-service work through one authoritative machine-checkable contract (OpenAPI, AsyncAPI, Protocol Buffers, or JSON Schema), with generated consumer types and co… | Affaan Mustafa | MIT |
| [cqrs-implementation](skills/cqrs-implementation/SKILL.md) | Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing query performance, or building event-sourced systems. | Seth Hobson | MIT |
| [domain-modeling](skills/domain-modeling/SKILL.md) | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR. | Matt Pocock | MIT |
| [error-handling-patterns](skills/error-handling-patterns/SKILL.md) | Master error handling patterns across languages including exceptions, Result types, error propagation, and graceful degradation to build resilient applications. Use when implementing error handling,… | Seth Hobson | MIT |
| [event-store-design](skills/event-store-design/SKILL.md) | Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store technologies, or implementing event persistence patterns. | Seth Hobson | MIT |
| [graceful-shutdown](skills/graceful-shutdown/SKILL.md) | Implement graceful shutdown for servers and workers: drain connections, finish in-flight work, release resources, and exit cleanly on SIGTERM/SIGINT. | Prajeeth-12 | MIT |
| [hexagonal-architecture](skills/hexagonal-architecture/SKILL.md) | Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-case orchestration across TypeScript, Java, Kotlin, and Go services. Use… | Affaan Mustafa | MIT |
| [improve-codebase-architecture](skills/improve-codebase-architecture/SKILL.md) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | Matt Pocock | MIT |
| [json-schema-manual](skills/json-schema-manual/SKILL.md) | JSON Schema Manual: draft 2020-12 validation schema from a confirmed field list, with required and enum values only where confirmed. Use for an API or import contract. | WHOISABHISHEKADHIKARI | MIT (code) / CC-BY-4.0 (written content) |
| [latency-critical-systems](skills/latency-critical-systems/SKILL.md) | Optimize and verify latency-sensitive systems — realtime dashboards, market data feeds, streaming agents, execution gateways, queues, and caches — by tracking p50/p95/p99 latency, freshness age, and… | Affaan Mustafa | MIT |
| [mailtrap-email-integration](skills/mailtrap-email-integration/SKILL.md) | Guides agents through integrating transactional email sending via Mailtrap's Email API, including sandbox testing, domain verification, and API authentication. Use when implementing email-sending fea… | Affaan Mustafa | MIT |
| [microservices-patterns](skills/microservices-patterns/SKILL.md) | Design microservices architectures with service boundaries, event-driven communication, and resilience patterns. Use when building distributed systems, decomposing monoliths, or implementing microser… | Seth Hobson | MIT |
| [openapi-spec-generation](skills/openapi-spec-generation/SKILL.md) | Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. Use when creating API documentation, generating SDKs, or ensuring API contract compliance. | Seth Hobson | MIT |
| [projection-patterns](skills/projection-patterns/SKILL.md) | Build read models and projections from event streams. Use when implementing CQRS read sides, building materialized views, or optimizing query performance in event-sourced systems. | Seth Hobson | MIT |
| [saga-orchestration](skills/saga-orchestration/SKILL.md) | Implement saga patterns for distributed transactions and cross-aggregate workflows. Use this skill when implementing distributed transactions across microservices where 2PC is unavailable, designing… | Seth Hobson | MIT |
| [workflow-orchestration-patterns](skills/workflow-orchestration-patterns/SKILL.md) | Design durable workflows with Temporal for distributed systems. Covers workflow vs activity separation, saga patterns, state management, and determinism constraints. Use when building long-running pr… | Seth Hobson | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
