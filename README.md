# agentic-setup
Personal setup for agentic development with OpenCode. Spec-driven gated workflow for complex projects.

## Overview
6 primary agents covering the full development cycle:
```
spec → plan → build → test → code-review → document
```

Each agent has a focused role with explicit gates between stages. The workflow ensures design happens before code, and every change is tested and reviewed.

## Enable / Disable
Switch between the custom agent set and OpenCode's default `plan` + `build`:
```bash
# Activate custom agents
./scripts/enable.sh

# Deactivate (revert to default plan + build)
./scripts/disable.sh
```

`enable.sh` creates symlinks from `~/.config/opencode/agents/` to this repository. `disable.sh` removes them and restores any backups.

## Agents
| Agent | Stage | When to Use |
|-------|-------|-------------|
| `spec` | Specify | New projects, complex features, multi-capability requirements |
| `plan` | Plan | After spec approval; decompose into tasks with acceptance criteria |
| `build` | Implement | Implement tasks from a plan, incrementally |
| `test` | Test | TDD, bug reproduction, coverage analysis |
| `code-review` | Review | Before commit; 5-axis quality review |
| `document` | Docs | ADRs, README updates, agent-facing documentation |

## Workflow Selection
| Scenario | Use |
|----------|-----|
| New project, complex feature | Full gated workflow (all 6 agents) |
| Small bugfix, routine edit | Skip to `build` |
| Codebase research | `explore` subagent |
| Parallel investigation | `general` subagent |

## Repository Structure
```
agents/           Agent definitions (primary agents)
references/       Templates, common instructions, shared docs
scripts/          enable.sh / disable.sh toggle scripts
skills/           OpenCode skills (optional)
AGENTS.md         Project-level agent workflow instructions
```

## References
- [agent-skills](https://github.com/addyosmani/agent-skills) — base principles and main concept
- [OpenSpec](https://github.com/Fission-AI/OpenSpec/tree/main) — spec-driven development framework
- [OpenCode Docs](https://opencode.ai/docs) — OpenCode configuration and agents
