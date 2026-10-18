#!/usr/bin/env bash
set -euo pipefail

AGENTS_DST="$HOME/.config/opencode/agents"

# Custom agent files to unlink
AGENTS=(spec.md plan.md build.md test.md code-review.md document.md)

echo "Disabling custom agents"
echo "Target: $AGENTS_DST"
echo ""

REMOVED=0
for agent in "${AGENTS[@]}"; do
    dst="$AGENTS_DST/$agent"

    if [ -L "$dst" ]; then
        rm "$dst"
        echo "REMOVED: $agent (symlink)"
        REMOVED=$((REMOVED + 1))
    elif [ -e "$dst" ]; then
        echo "SKIP: $agent (regular file, not a symlink)"
    else
        echo "SKIP: $agent (not present)"
    fi
done

# Restore backups if they exist
BACKUPS=$(find "$AGENTS_DST" -maxdepth 1 -type d -name '.backup-*' 2>/dev/null | sort -r | head -1)
if [ -n "$BACKUPS" ]; then
    echo ""
    echo "Restoring backups from $BACKUPS:"
    for f in "$BACKUPS"/*.md; do
        [ -e "$f" ] || continue
        base="$(basename "$f")"
        mv "$f" "$AGENTS_DST/$base"
        echo "  Restored: $base"
    done
    rmdir "$BACKUPS" 2>/dev/null || true
fi

echo ""
echo "Done. $REMOVED custom agents removed."
echo ""
echo "Remaining agents:"
ls -la "$AGENTS_DST"/*.md 2>/dev/null || echo "  (none)"
echo ""
echo "Default agents (plan, build) are built into OpenCode and always available."
