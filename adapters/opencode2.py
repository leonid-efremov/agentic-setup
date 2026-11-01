from pathlib import Path
from agent_config import AgentConfig
import yaml


class OpenCode2Adapter:
    def __init__(self, output_dir: Path):
        self.target_agents_dir = output_dir / "agents"

    def _translate_permissions(self, agent: AgentConfig) -> dict:
        file_cfg = agent.permissions.get("file_access", {})
        write_rules = file_cfg.get("write", [])

        if not write_rules:
            edit_policy = "deny"
        elif write_rules == ["**/*"] or write_rules == ["*"]:
            edit_policy = "allow"
        else:
            edit_policy = write_rules

        shell_cfg = agent.permissions.get("shell_access", {})
        if not shell_cfg.get("allow", False):
            bash_policy = "deny"
        else:
            allowed_cmds = shell_cfg.get("allowed_commands", [])
            bash_policy = "allow" if allowed_cmds == ["*"] else allowed_cmds

        return {
            "edit": edit_policy,
            "bash": bash_policy
        }

    def compile(self, agents: list[AgentConfig]):
        self.target_agents_dir.mkdir(parents=True, exist_ok=True)

        for agent in agents:
            mode = "primary" if agent.id in ["spec", "plan", "build", "test", "code-review", "document"] else "subagent"

            opencode2_frontmatter = {
                "name": agent.id,
                "description": "",
                "mode": mode,
                "permissions": self._translate_permissions(agent)
            }

            target_file = self.target_agents_dir / f"{agent.id}.md"
            with open(target_file, "w", encoding="utf-8") as f:
                f.write("---\n")
                yaml.dump(opencode2_frontmatter, f, allow_unicode=True, default_flow_style=False)
                f.write("---\n\n")
                f.write(agent.prompt)

            print(f"[+] Скомпилирован адаптер OpenCode 2.0: {target_file.name}")
