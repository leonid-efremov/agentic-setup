import re
from pathlib import Path
import yaml


_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)


class AgentConfig:
    def __init__(
        self,
        agent_id: str,
        prompt: str,
        permissions: dict,
        description: str = "",
        mode: str | None = None,
    ):
        self.id = agent_id
        self.prompt = prompt
        self.permissions = permissions
        self.description = description
        self.mode = mode


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

    @staticmethod
    def _split_frontmatter(text: str) -> tuple[dict, str]:
        """Return (metadata, body) without the source frontmatter block."""
        match = _FRONTMATTER_RE.match(text)
        if not match:
            return {}, text.strip()

        metadata = yaml.safe_load(match.group(1)) or {}
        if not isinstance(metadata, dict):
            metadata = {}
        return metadata, text[match.end():].strip()

    def collect_agents(self) -> list[AgentConfig]:
        agents = []

        for file_path in self.agents_dir.glob("*.md"):
            agent_id = file_path.stem
            perm_config = self.permissions_matrix.get(agent_id)
            if not perm_config:
                print(f"[!] Warning: access rules for '{agent_id}' not found in {self.permissions_file}. Skipping")
                continue

            metadata, prompt_content = self._split_frontmatter(
                file_path.read_text(encoding="utf-8")
            )
            description = str(metadata.get("description") or "").strip()
            if not description:
                print(f"[!] Warning: description for '{agent_id}' is empty, using default")
                description = f"{agent_id} agent"

            mode = metadata.get("mode")
            if mode not in ("primary", "subagent", "all"):
                mode = None

            agents.append(
                AgentConfig(
                    agent_id,
                    prompt_content,
                    perm_config,
                    description=description,
                    mode=mode,
                )
            )

        return agents
