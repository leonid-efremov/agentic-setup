# agentic-setup
Personal setup for agentic development with OpenCode. Spec-driven gated workflow for complex projects.

## Overview
6 primary agents covering the full development cycle:
```
spec → plan → build → test → code-review → document
```

Each agent has a focused role with explicit gates between stages. The workflow ensures design happens before code, and every change is tested and reviewed.

## Usage
Custom agents are loaded only when `OPENCODE_CONFIG_DIR` points at an adapter directory. The adapter lives outside the repository so OpenCode never picks it up as a project config:

```bash
# one-time setup
mkdir -p "$HOME/.config/opencode-custom"
ln -sfn "$PWD/agents" "$HOME/.config/opencode-custom/agents"
ln -sfn "$PWD/opencode-permissions.json" "$HOME/.config/opencode-custom/opencode.json"
```

```bash
# custom agent set
export OPENCODE_CONFIG_DIR="$HOME/.config/opencode-custom"
opencode
# unset OPENCODE_CONFIG_DIR
```

Without the variable, `opencode` starts with the default `plan` + `build` agents from any directory. The global config is never modified; OpenCode installs its plugin dependencies into the adapter directory, not into this repository.

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

## Agent Permissions
Tool boundaries live in `opencode-permissions.json` (object syntax, last matching rule wins), exposed to OpenCode as `opencode.json` in the adapter directory:

| Agent | `edit` boundary | Rationale |
|-------|-----------------|-----------|
| `spec` | only `docs/**` and root `*.md` | designs, must not touch code |
| `plan` | only `docs/**` and root `*.md` | decomposes, must not touch code |
| `document` | only `docs/**` and root `*.md` | documents, must not change logic |
| `build` | `allow` | implements code |
| `test` | `allow` | writes tests/fixes |
| `code-review` | `deny` | read-only reviewer — reports, never edits |

Read-only agents still get read access; only `edit` is constrained here. Extend `opencode-permissions.json` (e.g. `shell` rules) to tighten further.

## Repository Structure
```
agents/                   Agent definitions (primary agents)
opencode-permissions.json Per-agent tool permissions (adapter config)
references/               Templates, common instructions, shared docs
skills/                   OpenCode skills (optional)
AGENTS.md                 Project-level agent workflow instructions
```

The adapter directory `~/.config/opencode-custom/` contains only symlinks to `agents/` and `opencode-permissions.json` (as `opencode.json`). Remove it to uninstall.

## References
- [agent-skills](https://github.com/addyosmani/agent-skills) — base principles and main concept
- [OpenSpec](https://github.com/Fission-AI/OpenSpec/tree/main) — spec-driven development framework
- [OpenCode Docs](https://opencode.ai/docs) — OpenCode configuration and agents
