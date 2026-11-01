from pathlib import Path
import yaml


class AgentConfig:
    def __init__(self, agent_id: str, prompt: str, permissions: dict):
        self.id = agent_id
        self.prompt = prompt
        self.permissions = permissions


class ConfigLoader:
    def __init__(self, agents_dir: Path, permissions_file: Path):
        self.agents_dir = agents_dir
        self.permissions_file = permissions_file
        self._load_permissions()

    def _load_permissions(self) -> dict:
        assert self.permissions_file.exists(), f"Permission file not found: {self.permissions_file}"
        with open(self.permissions_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
            self.permissions_matrix = config.get("agents", {})
        return self.permissions_matrix

    def collect_agents(self) -> list[AgentConfig]:
        agents = []

        for file_path in self.agents_dir.glob("*"):
            if file_path.suffix == ".md":
                agent_id = file_path.stem
                perm_config = self.permissions_matrix.get(agent_id)
                if not perm_config:
                    print(f"[!] Warning: access rules for '{agent_id}' not found in {self.permissions_file}. Skipping")
                    continue
                prompt_content = file_path.read_text(encoding="utf-8").strip()
                agents.append(AgentConfig(agent_id, prompt_content, perm_config))

        return agents
