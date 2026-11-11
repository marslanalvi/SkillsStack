# devops-observability-sre

Monitoring, tracing, logging, SLOs, incident response and on-call.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install devops-observability-sre@skills-stack
```

## Works best with

Some skills here hand off to skills in other Skills Stack plugins. Install these too so those steps work:

- **`engineering-code-review-quality`**: `observability-and-instrumentation` uses `performance-optimization`
- **`engineering-debugging`**: `observability-and-instrumentation` uses `debugging-and-error-recovery`
- **`engineering-dev-workflow`**: `observability-and-instrumentation` uses `shipping-and-launch`
- **`security-appsec-review`**: `observability-and-instrumentation` uses `security-and-hardening`

## Skills (16)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [azure-monitor-opentelemetry-ts](skills/azure-monitor-opentelemetry-ts/SKILL.md) | Auto-instrument Node.js applications with distributed tracing, metrics, and logs. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [canary-watch](skills/canary-watch/SKILL.md) | Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, static assets, console errors, and performance regressions after deploys, merges, or dependenc… | Affaan Mustafa | MIT |
| [dashboard-builder](skills/dashboard-builder/SKILL.md) | Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Use when turning metrics into a working dashboard instead of a vanity board. | Affaan Mustafa | MIT |
| [datadog](skills/datadog/SKILL.md) | Implement Datadog monitoring and APM for infrastructure and applications. | devops-skills | MIT |
| [devops-troubleshooter](skills/devops-troubleshooter/SKILL.md) | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [distributed-tracing](skills/distributed-tracing/SKILL.md) | Implement distributed tracing with Jaeger and Tempo to track requests across microservices and identify performance bottlenecks. Use when debugging microservices, analyzing request flows, or implemen… | Seth Hobson | MIT |
| [grafana-dashboards](skills/grafana-dashboards/SKILL.md) | Create and manage production Grafana dashboards for real-time visualization of system and application metrics. Use when building monitoring dashboards, visualizing metrics, or creating operational ob… | Seth Hobson | MIT |
| [incident-runbook-templates](skills/incident-runbook-templates/SKILL.md) | Create structured incident response runbooks with step-by-step procedures, escalation paths, and recovery actions. Use this skill when building a service outage runbook for a payment processing syste… | Seth Hobson | MIT |
| [observability-and-instrumentation](skills/observability-and-instrumentation/SKILL.md) | Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shipping any feature that runs in production and you need evidence… | Addy Osmani | MIT |
| [observability-engineer](skills/observability-engineer/SKILL.md) | Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and incident response workflows. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [on-call-handoff-patterns](skills/on-call-handoff-patterns/SKILL.md) | Master on-call shift handoffs with context transfer, escalation procedures, and documentation. Use this skill when transitioning on-call responsibilities between engineers and ensuring the incoming r… | Seth Hobson | MIT |
| [opentelemetry](skills/opentelemetry/SKILL.md) | Instrument applications and infrastructure with OpenTelemetry for unified traces, metrics, and logs. | devops-skills | MIT |
| [postmortem-writing](skills/postmortem-writing/SKILL.md) | Write effective blameless postmortems with root cause analysis, timelines, and action items. Use when conducting incident reviews, writing postmortem documents, or improving incident response process… | Seth Hobson | MIT |
| [prometheus-configuration](skills/prometheus-configuration/SKILL.md) | Set up Prometheus for comprehensive metric collection, storage, and monitoring of infrastructure and applications. Use when implementing metrics collection, setting up monitoring infrastructure, or c… | Seth Hobson | MIT |
| [service-mesh-observability](skills/service-mesh-observability/SKILL.md) | Implement comprehensive observability for service meshes including distributed tracing, metrics, and visualization. Use when setting up mesh monitoring, debugging latency issues, or implementing SLOs… | Seth Hobson | MIT |
| [slo-implementation](skills/slo-implementation/SKILL.md) | Define and implement Service Level Indicators (SLIs) and Service Level Objectives (SLOs) with error budgets and alerting. Use when establishing reliability targets, implementing SRE practices, or mea… | Seth Hobson | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
