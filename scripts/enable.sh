#!/usr/bin/env bash
set -euo pipefail

# Path to this repository (resolved from script location)
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENTS_SRC="$REPO_DIR/agents"
AGENTS_DST="$HOME/.config/opencode/agents"

# Custom agent files to link
AGENTS=(spec.md plan.md build.md test.md code-review.md document.md)

echo "Enabling custom agents from $AGENTS_SRC"
echo "Target: $AGENTS_DST"
echo ""

# Ensure target directory exists
mkdir -p "$AGENTS_DST"

# Check for existing regular files (not symlinks) that would conflict
CONFLICTS=()
for agent in "${AGENTS[@]}"; do
    dst="$AGENTS_DST/$agent"
    if [ -e "$dst" ] && [ ! -L "$dst" ]; then
        CONFLICTS+=("$agent")
    fi
done

if [ ${#CONFLICTS[@]} -gt 0 ]; then
    echo "WARNING: Regular files exist that would be replaced:"
    for c in "${CONFLICTS[@]}"; do
        echo "  - $c"
    done
    echo ""
    read -p "Back up and replace? [y/N] " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
    # Back up conflicting files
    BACKUP_DIR="$AGENTS_DST/.backup-$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    for c in "${CONFLICTS[@]}"; do
        mv "$AGENTS_DST/$c" "$BACKUP_DIR/$c"
        echo "  Backed up: $c -> $BACKUP_DIR/"
    done
    echo ""
fi

# Create symlinks
LINKED=0
for agent in "${AGENTS[@]}"; do
    src="$AGENTS_SRC/$agent"
    dst="$AGENTS_DST/$agent"

    if [ ! -f "$src" ]; then
        echo "SKIP: $agent (source not found)"
        continue
    fi

    # Remove existing symlink if present
    if [ -L "$dst" ]; then
        rm "$dst"
    fi

    ln -s "$src" "$dst"
    echo "LINKED: $agent -> $src"
    LINKED=$((LINKED + 1))
done

echo ""
echo "Done. $LINKED agents linked."
echo ""
echo "Active custom agents:"
ls -la "$AGENTS_DST" | grep '\.md' || echo "  (none)"
