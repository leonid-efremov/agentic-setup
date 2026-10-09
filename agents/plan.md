---
name: plan definition
description: Make a realization plan for concrete feature or project component. Aim is to form definitive step-by-step plan for realization of specific design aspect.
---

## Overview
Based on prepared design documents, write a realization guide for one selected feature.
Decompose work into small, verifiable tasks with explicit acceptance criteria. Every task should be small enough to implement, test, and verify in a single focused session.
Main goal - when high-level design and main goals is ready, human picks one feature and you form clear and transparent plan to implement it. Plan will be used in the next stage.

### Phase 2: Plan
With the validated spec, generate a technical implementation plan:
1. Identify the major components and their dependencies, build dependency graph
2. Determine the implementation order (what must be built first)
3. Note risks and mitigation strategies
4. Define verification checkpoints between phases

### Phase 3: Tasks
Break the plan into discrete, implementable tasks:
- Each task should be completable in a single focused session
- Each task has explicit acceptance criteria
- Each task includes a verification step (test, build, manual check)
- Tasks are ordered by dependency, not by perceived importance
- No task should require changing more than ~5 files

For long lists of tasks add explicit checkpoints to usnsure intermediate results and review it with human before proceeding.

Each task should be specific and solve only one concrete problem. Otherwise, tasks must be decomposed to few smaller tasks.
**When to break a task down further:**
- It would take more than one focused session (roughly 2+ hours of agent work)
- You cannot describe the acceptance criteria in 3 or fewer bullet points
- It touches two or more independent subsystems (e.g., auth and billing)
- You find yourself writing "and" in the task title (a sign it is two tasks)

## Output Files
- **Plan document:** Save the implementation plan to `tasks/plan.md`, following the reference for task format (../../references/plan_template.md)
- **Task list:** Record each task in the plan, following the reference for task format (../../references/task_template.md)

## Common Rationalizations
| Rationalization | Reality |
|---|---|
| "I'll figure it out as I go" | That's how you end up with a tangled mess and rework. 10 minutes of planning saves hours. |
| "The tasks are obvious" | Write them down anyway. Explicit tasks surface hidden dependencies and forgotten edge cases. |
| "Planning is overhead" | Planning is the task. Implementation without a plan is just typing. |
| "I can hold it all in my head" | Context windows are finite. Written plans survive session boundaries and compaction. |
| "The old `tasks/plan.md` is stale, I'll just replace it" | Unchecked tasks may be mid-build in another session. Overwriting them destroys work state that exists nowhere else. Stop and ask. |

## Red Flags
- Starting implementation without a written task list
- Overwriting a `tasks/plan.md` that still has unchecked tasks for different work, without asking
- Tasks that say "implement the feature" without acceptance criteria
- No verification steps in the plan
- All tasks are overwhelmed
- No checkpoints between tasks
- Dependency order isn't considered

## Verification
Before starting implementation, confirm:
- [ ] Every task has acceptance criteria
- [ ] Every task has a verification step
- [ ] Task dependencies are identified and ordered correctly
- [ ] Tasks are recorded in the task list target (`tasks/plan.md`)
- [ ] No pre-existing incomplete plan was overwritten without explicit user confirmation
- [ ] Checkpoints exist between major phases
- [ ] The human has reviewed and approved the plan
