## The Gated Workflow

First - design, then develop.
Development process is based on spec-driven development.

```
SPECIFY ──→ PLAN ──→ IMPLEMENT ──→ TEST ──→ REVIEW
```

### Agent Selection
| Stage | Agent | Output |
|-------|-------|--------|
| New project/feature | `spec` | Approved spec document |
| Planning & tasks | `plan` | Implementation plan with task list and acceptance criteria |
| Implementation | `build` | Working code with tests |
| Testing | `test` | Test coverage, bugfix reproduction |
| Quality gate | `code-review` | Approved changes |
| Documentation | `document` | ADRs, updated README |

### When to Use Full Workflow
- **Use full workflow:** new projects, complex features, multi-capability changes
- **Skip to build:** small bugfixes, routine edits, refactoring without behavior change
- **Use explore/general subagents:** for codebase research, parallel tasks

### Switching Agent Sets
```bash
# Enable custom agents
./scripts/enable.sh

# Disable (back to default)
./scripts/disable.sh
```
