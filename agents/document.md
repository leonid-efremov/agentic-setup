---
name: documentation-and-adrs
description: Records architecture decisions and documentation. Fixing and explaining of the reasoning behind a design choice.
---

# Documentation and ADRs

## Overview
Document logic and essence of realization, not just code. The most valuable documentation captures the *why* — the context, constraints, and trade-offs that led to a decision. Code shows *what* was built; documentation explains *why it was built this way* and *what alternatives were considered*. This context is essential for future humans and agents working in the codebase.

## Architecture Decision Records (ADRs)
ADRs capture the reasoning behind significant technical decisions. It's the highest-value documentation.

### When to Write an ADR
- Choosing a framework, library, or major dependency
- Designing a data model or database schema
- Selecting an authentication strategy
- Deciding on an API architecture (REST vs. GraphQL vs. tRPC)
- Choosing between build tools, hosting platforms, or infrastructure
- Any decision that would be expensive to reverse

### Match the existing convention first
Before creating an ADR, inspect the available repository context for an established convention — existing ADRs, project instructions, and ADR-related configuration or tooling. An established convention overrides the defaults below.

### ADR Template
Store ADRs in `docs/decisions/` with sequential numbering and titles.
ADR template - (../../references/adr.md)

### ADR Lifecycle
```
PROPOSED → ACCEPTED → (SUPERSEDED or DEPRECATED)
```
- **Don't delete old ADRs.** They capture historical context.
- When a decision changes, write a new ADR that references and supersedes the old one.

## README Structure
Every project should have a README - (../../references/readme_structure.md)

## Changelog Maintenance
For shipped features fix what was added, when, changed features, new features.

## Documentation for Agents
Special consideration for AI agent context:
- **AGENTS.md / rules files** — Document project conventions so agents follow them
- **Spec files** — Keep specs updated so agents build the right thing
- **ADRs** — Help agents understand why past decisions were made (prevents re-deciding)
- **Inline gotchas** — Prevent agents from falling into known traps

## Common Rationalizations
| Rationalization | Reality |
|---|---|
| "The code is self-documenting" | Code shows what. It doesn't show why, what alternatives were rejected, or what constraints apply. |
| "We'll write docs when the API stabilizes" | APIs stabilize faster when you document them. The doc is the first test of the design. |
| "Nobody reads docs" | Agents do. Future engineers do. Your 3-months-later self does. |
| "ADRs are overhead" | A 10-minute ADR prevents a 2-hour debate about the same decision six months later. |
| "Comments get outdated" | Comments on *why* are stable. Comments on *what* get outdated — that's why you only write the former. |

## Red Flags
- Architectural decisions with no written rationale
- Public APIs with no documentation or types
- README that doesn't explain how to run the project
- Commented-out code instead of deletion
- TODO comments that have not been used for a long
- No ADRs in a project with significant architectural choices
- Documentation that restates the code instead of explaining intent

## Verification
After documenting:
- [ ] ADRs exist for all significant architectural decisions
- [ ] README covers quick start, commands, and architecture overview
- [ ] API functions have parameter and return type documentation
- [ ] Known gotchas are documented inline where they matter
- [ ] No commented-out code remains
- [ ] Rules files (CLAUDE.md etc.) are current and accurate
