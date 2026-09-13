#!/usr/bin/env bash
# =====================================================================
# 💳 SwipeSmart AI — macOS & Linux Startup Script
# =====================================================================

set -e

# Change to directory of this script
cd "$(dirname "$0")"

# Check if python3 is available
if command -v python3 >/dev/null 2>&1; then
    exec python3 run.py "$@"
elif command -v python >/dev/null 2>&1; then
    exec python run.py "$@"
else
    echo "❌ Error: Python 3 was not found on your system."
    echo "Please install Python 3.10+ from https://www.python.org/downloads/"
    exit 1
fi
