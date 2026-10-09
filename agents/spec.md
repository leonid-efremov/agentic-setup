---
name: spec formation
description: Define high-level feature structure. Aim is to draft a PRD or requirements document with objectives and scope. Mandatory when a single requirement spans several different capabilities. Such cases must be decomposed into separate modules before specifying.
---

## Overview
Write a structured specification before implementation. The spec is the shared source of truth between you and the human engineer — it defines what we're building, why, and how we'll know it's done.
Two main possible tasks:
1. Spec formation - when starting a totaly new project or first integration into an existing project.
2. Spec actualization - when designing a new feature or extending project.

### Phase 0: Scope Check
Needed only for multy-capability or complex requests. Otherwise, just skip phase 0.

**Detection**
- The requirement names distinct capabilities
- Acceptance criteria cluster into groups that could ship and be verified separately
- One capability could be cut or replaced without rewriting the others' requirements

**Propose a capability map before writing any spec.** Small and reviewable — a module table plus a build order, not a project plan (../../references/capability_map.md)

**Important rules**
- Stable module ids - chosen once, fixed in capability map, never renamed mid-initiative.
- Dependency direction, no cycles - if two modules each need the other, they are one module.

**The map is gated like every phase.** The human reviews module boundaries, dependency direction, and build order before any module spec is written. Getting the map wrong is expensive.

### Phase 1: Specify

Start with a high-level vision. Ask the human clarifying questions until requirements are concrete.

**Surface assumptions immediately.** Before writing any spec content, list what you're assuming and ask for human confirmation.
Don't silently fill in ambiguous requirements. The spec's entire purpose is to surface misunderstandings *before* code gets written — assumptions are the most dangerous form of misunderstanding.

**Write a spec document covering these six core areas:**
1. **Objective** — What are we building and why? Who is the user? What does success look like?
2. **Project Structure** — (../../references/project_structure.md)
3. **Code Style**
4. **Commands** — Ways to interact with the project. Full executable commands with flags.
5. **Testing Strategy** — Framework, tests location, coverage expectations, which test levels for which concerns.
6. **Boundaries** — Three-tier system:
   - **Always do:** Run tests before commits, follow naming conventions, validate inputs
   - **Ask first:** Database schema changes, adding dependencies, changing CI config
   - **Never do:** Commit secrets, edit vendor directories, remove failing tests without approval

**Spec template:** — (../../references/project_spec.md)

**Reframe instructions as success criteria.** When receiving vague requirements, translate them into concrete conditions:
This lets you loop, retry, and problem-solve toward a clear goal rather than guessing what "faster" means.

**Stop after writing the spec (CRITICAL).** Once the spec is saved:
1. Summarize it and list any Open Questions.
2. Ask the human to approve it or request changes.
3. **STOP YOUR TURN IMMEDIATELY.** Do NOT start Phase 2, planning starts only after the human approves the spec in a later turn.

## Keeping the Spec Alive (spec actualization)
The spec is a living document, not a one-time artifact:
- **Update when decisions change** — If you discover the components needs to change significantly, update the spec first, then implement.
- **Update when scope changes** — Features added or cut should be reflected in the spec.

## Red Flags
- Starting to write code without any written requirements
- Asking "should I just start building?" before clarifying what "done" means
- Implementing features not mentioned in any spec or task list
- Making architectural decisions without documenting them
- Skipping the spec because "it's obvious what to build"
- Writing the spec and starting the plan or code in the same turn
- One spec whose requirements span several independently testable capabilities
- Module boundaries or build order decided implicitly during implementation because no capability map was approved up front

## Verification
Before proceeding to implementation, confirm:
- [ ] The spec covers all six core areas
- [ ] The human has reviewed and approved the spec
- [ ] The turn ended after saving the spec; approval came in a later turn
- [ ] Success criteria are specific and testable
- [ ] Boundaries (Always/Ask First/Never) are defined
- [ ] The spec is saved to a file in the repository
- [ ] If the request bundles several independently testable capabilities, a capability map (module ids, dependency direction, build order) was approved before any module spec was written
- [ ] Every module spec traces to a module id in the approved map
