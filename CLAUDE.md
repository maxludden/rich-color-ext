# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`rich-color-ext` extends [Rich](https://github.com/Textualize/rich)'s `Color.parse` to understand 3-digit hex colors (`#09F`) and CSS4 named colors (`rebeccapurple`) that Rich doesn't natively support. It's a foundational dependency of the other `rich-*` projects in this workspace (`rich-gradient`, `rich-gradient-cli`, `supergene`) — they call `install()` at import time to get this parsing behavior everywhere Rich parses a color.

## Commands

Use `uv` for everything.

- Install: `uv sync`
- Run tests: `uv run pytest` (pytest picks up `src` automatically via `pythonpath = ["src"]` in `pyproject.toml`)
- Run a single test: `uv run pytest tests/test_colors_param.py -k test_name`
- Type check: `uv run mypy`
- Docs: `mkdocs serve` (requires `dev` dependency group)
- CLI smoke test: `uv run rich-color-ext show '#f0f'` or `uv run rich-color-ext show rebeccapurple` (installed as both `rich-color-ext` and `rich-color` console scripts, both pointing at `rich_color_ext.cli:main`)

## Architecture

- **`patch.py`** is the core: `install()` monkeypatches `rich.color.Color.parse` with `_patched_parse`, which checks 3-digit hex and the CSS name map first, then falls back to Rich's original `Color.parse` (saved as `_ORIGINAL_PARSE`) for anything else. `uninstall()` restores the original. Both are idempotent (`INSTALLED` guard) — safe to call `install()` more than once.
- **`css.py`** owns `get_css_map()`, the CSS4 name → hex lookup. As of recent releases this map is embedded directly in the package rather than shipped as a standalone `colors.json` — prefer `get_css_map()` over reading a JSON file when working with the color table.
- **`hex_utils.py`** has `is_3digit_hex()` / `expand_3digit_hex()`, used by `patch.py` before falling through to Rich's parser.
- **`cli.py`** implements the `rich-color-ext`/`rich-color` console scripts.
- **`logger.py`** wraps `loguru` but the logger is **disabled by default at import** — importing this package must stay silent. Don't add global sinks or call `logger.remove()`/enable logging at import time (this was explicitly reverted once — see `install_rich_sink()` for the opt-in path, and `from rich_color_ext import log; log.enable("rich_color_ext")` for callers who want debug output).
- No `rich.traceback.install()` or other import-time global side effects belong in `__init__.py` or `css.py` — this was deliberately removed; only `install()` (the color patch, which callers must invoke explicitly) should mutate global state.

## Testing notes

- `tests/test_import_side_effects.py` specifically guards against reintroducing import-time global mutation (traceback installs, logging sinks, etc.) — if you're tempted to do package setup at import time, check this test first.
- `tests/test_cli.py` covers CLI error paths, e.g. `rich-color-ext show notacolor` must raise a clean error (catches `ValueError`), not a raw traceback.

## Packaging

If bundling with PyInstaller and relying on a legacy standalone `colors.json` (rather than the embedded map), use `scripts/pyinstaller_build.sh` — it picks the correct `--add-data` separator per platform.
