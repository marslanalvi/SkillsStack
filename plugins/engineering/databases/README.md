# engineering-databases

SQL, Postgres, MySQL, Redis, ORMs, schema design and migrations.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install engineering-databases@skills-stack
```

## Works best with

Some skills here hand off to skills in other Skills Stack plugins. Install these too so those steps work:

- **`engineering-architecture-api`**: `mysql-patterns` uses `backend-patterns`, `postgres-patterns` uses `backend-patterns`, `redis-patterns` uses `backend-patterns`
- **`engineering-python`**: `redis-patterns` uses `django-patterns`
- **`security-appsec-review`**: `mysql-patterns` uses `security-review`

## Skills (10)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [clickhouse-io](skills/clickhouse-io/SKILL.md) | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. Use when writing ClickHouse schemas or queries, or when an… | Affaan Mustafa | MIT |
| [database-design](skills/database-design/SKILL.md) | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [database-migration](skills/database-migration/SKILL.md) | Execute database migrations across ORMs and platforms with zero-downtime strategies, data transformation, and rollback procedures. Use when migrating databases, changing schemas, performing data tran… | Seth Hobson | MIT |
| [database-migrations](skills/database-migrations/SKILL.md) | Safe, reversible database migration patterns: forward-only production changes, expand-contract zero-downtime renames, concurrent indexes, batched backfills, and per-tool workflows for PostgreSQL, Pri… | Affaan Mustafa | MIT |
| [mysql-patterns](skills/mysql-patterns/SKILL.md) | MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for production backends. Use when designing MySQL or MariaDB schemas and indexes, or when a query, tr… | Affaan Mustafa | MIT |
| [postgres-patterns](skills/postgres-patterns/SKILL.md) | PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase best practices. Use when designing PostgreSQL schemas, indexes, or RLS policies, or when… | Affaan Mustafa | MIT |
| [postgresql-table-design](skills/postgresql-table-design/SKILL.md) | Use this skill when designing or reviewing a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performance patterns, and advanced features | Seth Hobson | MIT |
| [prisma-patterns](skills/prisma-patterns/SKILL.md) | Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination, and critical traps like updateMany returning count not records, $transaction timeouts, migra… | Affaan Mustafa | MIT |
| [redis-patterns](skills/redis-patterns/SKILL.md) | Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection management for production applications. Use when adding caching, a distributed lock, rate… | Affaan Mustafa | MIT |
| [sql-optimization-patterns](skills/sql-optimization-patterns/SKILL.md) | Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database performance and eliminate slow queries. Use when debugging slow queries, designing database s… | Seth Hobson | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
