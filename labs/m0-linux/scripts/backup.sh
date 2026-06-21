#!/usr/bin/env bash
# backup.sh — tar a folder into a timestamped .tar.gz archive.
# Usage:  ./backup.sh [folder]      (defaults to your home dir)
# Concepts shown: shebang, strict mode, positional args + defaults,
#                 command substitution $(...), tar, du.

set -euo pipefail   # -e: exit on any error  -u: error on unset var  -o pipefail: a failing
                    # command in a pipe fails the whole pipe (safer scripts)

SRC="${1:-$HOME}"                       # 1st arg, or $HOME if none given
STAMP="$(date +%Y%m%d-%H%M%S)"          # e.g. 20260620-103015
OUT="backup-${STAMP}.tar.gz"

# -c create, -z gzip, -f file; -C cd into the parent so paths in the archive are clean
tar -czf "$OUT" -C "$(dirname "$SRC")" "$(basename "$SRC")"

echo "Created $OUT ($(du -h "$OUT" | cut -f1))"
echo "Inspect with:  tar -tzf $OUT"
