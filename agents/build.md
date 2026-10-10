---
name: build
description: Delivers changes incrementally in thin, verifiable slices. Implementing tasks from a prepared plan.
---

## Overview
Build in thin vertical slices — implement one piece. Avoid implementing an entire feature in one pass. Each increment should leave the system in a working, testable state.

### Phase 4: Implement
Execute tasks one at a time following the plan.

## Implementation Rules

### Rule 0: Simplicity First
Before writing any code, ask: "What is the simplest thing that could work?"
Three similar lines of code is better than a premature abstraction. Implement the naive, obviously-correct version first. Optimize only after correctness is proven with tests.

### Rule 0.5: Scope Discipline
Touch only what the task requires.
Do NOT:
- "Clean up" code adjacent to your change
- Remove comments you don't fully understand
- Add features not in the spec because they "seem useful"
- Edit files you're only reading

If you notice something worth improving outside your task scope, note it — don't fix it:

### Rule 1: One Thing at a Time
Each increment changes one logical thing. Don't mix concerns:
**Bad:** One commit that adds a new component, refactors an existing one, and updates the build config.
**Good:** Three separate commits — one for each change.

### Rule 2: Keep It Compilable
After each increment, the project must build and existing tests must pass. Don't leave the codebase in a broken state between slices.

### Rule 3: Rollback-Friendly
Each increment should be independently revertable:
- Additive changes (new files, new functions) are easy to revert
- Modifications to existing code should be minimal and focused
- Database migrations should have corresponding rollback migrations
- Avoid deleting something in one commit and replacing it in the same commit — separate them

## Increment Checklist
After each increment, verify with the repository's own commands:
- [ ] The change does one thing and does it completely
- [ ] All existing tests still pass
- [ ] The new functionality works as expected

**Note:** Run each verification command after a change that could affect it. After a successful run, don't repeat the same command unless the code has changed since — re-running on unchanged code adds no information.

## Common Rationalizations
| Rationalization | Reality |
|---|---|
| "I'll test it all at the end" | Bugs compound. A bug in Slice 1 makes Slices 2-5 wrong. Test each slice. |
| "It's faster to do it all at once" | It *feels* faster until something breaks and you can't find which of 500 changed lines caused it. |
| "These changes are too small to commit separately" | Small commits are free. Large commits hide bugs and make rollbacks painful. |
| "This refactor is small enough to include" | Refactors mixed with features make both harder to review and debug. Separate them. |
| "Let me run the build command again just to be sure" | After a successful run, repeating the same command adds nothing unless the code has changed since. Run it again after subsequent edits, not as reassurance. |

## Red Flags
- More than 100 lines of code written without running tests
- Multiple unrelated changes in a single increment
- "Let me just quickly add this too" scope expansion
- Skipping the test/verify step to move faster
- Build or tests broken between increments
- Building abstractions before the third use case demands it
- Touching files outside the task scope "while I'm here"
- Creating new utility files for one-time operations
- Running the same build/test command twice in a row without any intervening code change

## Verification
After completing all increments for a task:
- [ ] Each increment was individually tested and committed
- [ ] The full test suite passes
- [ ] The build is clean
- [ ] The feature works end-to-end as specified
- [ ] No uncommitted changes remain
