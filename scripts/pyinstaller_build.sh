#!/usr/bin/env bash
set -euo pipefail

# Build a single-file PyInstaller bundle for rich-color-ext.
# Usage: ./scripts/pyinstaller_build.sh [entry_script]

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
cd "$ROOT_DIR"

DEFAULT_SCRIPTS_ENTRY="scripts/src/rich_color_ext/cli.py"
DEFAULT_SRC_ENTRY="src/rich_color_ext/cli.py"

if [[ $# -gt 0 ]]; then
  ENTRY="$1"
else
  if [[ -f "$DEFAULT_SRC_ENTRY" ]]; then
    ENTRY="$DEFAULT_SRC_ENTRY"
  elif [[ -f "$DEFAULT_SCRIPTS_ENTRY" ]]; then
    ENTRY="$DEFAULT_SCRIPTS_ENTRY"
  else
    echo "Error: could not find a default entry script." >&2
    exit 1
  fi
fi

if [[ ! -f "$ENTRY" ]]; then
  echo "Error: entry script '$ENTRY' does not exist." >&2
  exit 1
fi

if [[ -n "${PYTHON:-}" ]]; then
  PYTHON_BIN="$PYTHON"
elif [[ -x "$ROOT_DIR/.venv/bin/python" ]]; then
  PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python3)"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python)"
else
  echo "Error: python3 (or python) interpreter not found." >&2
  exit 1
fi

PYTHON_VERSION="$("$PYTHON_BIN" -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')"
IFS=. read -r PYTHON_MAJOR PYTHON_MINOR _ <<< "$PYTHON_VERSION"
if (( PYTHON_MAJOR < 3 || (PYTHON_MAJOR == 3 && PYTHON_MINOR < 10) )); then
  echo "Error: Python $PYTHON_VERSION is too old; need >= 3.10 for rich-color-ext." >&2
  echo "Use 'PYTHON=/path/to/python3.10 ./scripts/pyinstaller_build.sh' to specify a newer interpreter." >&2
  exit 1
fi

case "$ENTRY" in
  scripts/src/*)
    PACKAGE_PATH="scripts/src"
    ;;
  src/*)
    PACKAGE_PATH="src"
    ;;
  *)
    PACKAGE_PATH=""
    ;;
esac

if [[ -z "$PACKAGE_PATH" ]]; then
  for candidate in scripts/src src; do
    if [[ -d "$candidate" ]]; then
      PACKAGE_PATH="$candidate"
      break
    fi
  done
fi

export RCE_ENTRY="$ENTRY"
export RCE_PYTHON_BIN="$PYTHON_BIN"

"$PYTHON_BIN" - <<'PY'
import os
from pathlib import Path

entry = Path(os.environ["RCE_ENTRY"]).resolve()

try:
    from rich.console import Console
    from rich.panel import Panel
except Exception:  # pragma: no cover - Rich missing
    print("Building with PyInstaller...")
    print(f"Entry: {entry}")
else:
    console = Console()
    panel = Panel.fit(
        f"Building with PyInstaller...\n[dim]{entry}[/dim]",
        title="PyInstaller",
        title_align="left",
        border_style="bold #99ff00",
        padding=(1, 4),
        subtitle=f"Entry: {entry}",
        subtitle_align="right",
    )
    console.print(panel)
PY

if ! "$PYTHON_BIN" -m PyInstaller --version >/dev/null 2>&1; then
  if ! "$PYTHON_BIN" -m pip --version >/dev/null 2>&1; then
    echo "Bootstrapping pip for $PYTHON_BIN..."
    if ! "$PYTHON_BIN" -m ensurepip --upgrade >/dev/null 2>&1; then
      echo "Error: pip is not available for $PYTHON_BIN. Install pip or set PYTHON to a different interpreter." >&2
      exit 1
    fi
    "$PYTHON_BIN" -m pip install --upgrade pip >/dev/null 2>&1 || true
  fi
  echo "Installing PyInstaller..."
  "$PYTHON_BIN" -m pip install --upgrade "pyinstaller>=6.11.0"
fi

BUILD_ARGS=(--noconfirm --onefile "$ENTRY")
if [[ -n "${PACKAGE_PATH:-}" ]]; then
  BUILD_ARGS+=(--paths "$PACKAGE_PATH")
fi

"$PYTHON_BIN" -m PyInstaller "${BUILD_ARGS[@]}"

if ! "$PYTHON_BIN" "$ROOT_DIR/scripts/build.py"; then
  python_fallback="$(command -v python || true)"
  if [[ -n "$python_fallback" && "$python_fallback" != "$PYTHON_BIN" ]]; then
    "$python_fallback" "$ROOT_DIR/scripts/build.py" || true
  fi
fi
