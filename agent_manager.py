import sys
import shutil
from pathlib import Path
from agent_config import ConfigLoader
from adapters.opencode2 import OpenCode2Adapter


REPO_ROOT = Path(__file__).parent.resolve()
AGENTS_DIR = REPO_ROOT / "agents"
PERMISSIONS_FILE = REPO_ROOT / "permissions.yaml"

OPENCODE_TARGET_CONFIG_DIR = REPO_ROOT / ".config" / "opencode-custom"


def opencode_enable():
    loader = ConfigLoader(AGENTS_DIR, PERMISSIONS_FILE)
    core_agents = loader.collect_agents()

    adapter = OpenCode2Adapter(OPENCODE_TARGET_CONFIG_DIR)
    adapter.compile(core_agents)

    print(f"\n[+] Профиль собран! Запуск:")
    print(f"export OPENCODE_CONFIG_DIR=\"{OPENCODE_TARGET_CONFIG_DIR}\" && opencode")


def opencode_disable():
    shutil.rmtree(OPENCODE_TARGET_CONFIG_DIR, ignore_errors=True)
    print("[+] Кастомный профиль отключен.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "opencode-on":
        opencode_enable()
    elif cmd == "opencode-off":
        opencode_disable()
    else:
        print("Использование: python agent_manager.py [opencode-on|opencode-off]")
