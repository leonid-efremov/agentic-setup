from pathlib import Path
from agent_config import AgentConfig
import yaml


PRIMARY_AGENTS = {"spec", "plan", "build", "test", "code-review", "document"}


class OpenCode2Adapter:
    def __init__(self, output_dir: Path):
        self.target_agents_dir = output_dir / "agents"

    @staticmethod
    def _edit_policy(write_rules: list) -> str | dict:
        if not write_rules:
            return "deny"
        if write_rules in (["**/*"], ["*"]):
            return "allow"
        return {"*": "deny", **{rule: "allow" for rule in write_rules}}

    @staticmethod
    def _bash_policy(shell_cfg: dict) -> str | dict:
        if not shell_cfg.get("allow", False):
            return "deny"
        allowed_cmds = shell_cfg.get("allowed_commands", [])
        if allowed_cmds == ["*"]:
            return "allow"
        if not allowed_cmds:
            return "deny"
        return {"*": "deny", **{cmd: "allow" for cmd in allowed_cmds}}

    def _translate_permissions(self, agent: AgentConfig) -> dict:
        file_cfg = agent.permissions.get("file_access", {})
        return {
            "edit": self._edit_policy(file_cfg.get("write", [])),
            "bash": self._bash_policy(agent.permissions.get("shell_access", {})),
        }

    def compile(self, agents: list[AgentConfig]):
        self.target_agents_dir.mkdir(parents=True, exist_ok=True)

        for agent in agents:
            if agent.mode:
                mode = agent.mode
            else:
                mode = "primary" if agent.id in PRIMARY_AGENTS else "subagent"

            opencode2_frontmatter = {
                "description": agent.description,
                "mode": mode,
                "permission": self._translate_permissions(agent),
            }

            target_file = self.target_agents_dir / f"{agent.id}.md"
            with open(target_file, "w", encoding="utf-8", newline="\n") as f:
                f.write("---\n")
                yaml.dump(
                    opencode2_frontmatter,
                    f,
                    allow_unicode=True,
                    default_flow_style=False,
                    sort_keys=False,
                )
                f.write("---\n\n")
                f.write(agent.prompt)

            print(f"[+] Скомпилирован адаптер OpenCode 2.0: {target_file.name}")
