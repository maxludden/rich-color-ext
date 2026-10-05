# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`rich-color-ext` extends [Rich](https://github.com/Textualize/rich)'s `Color.parse` to understand 3-digit hex colors (`#09F`, `#` required) and CSS4 named colors (`rebeccapurple`) that Rich doesn't natively support. It's a foundational dependency of the other `rich-*` projects in this workspace (`rich-gradient`, `supergene`) — they call `install()` to get this parsing behavior everywhere Rich parses a color.

## Commands

Use `uv` for everything.

- Install: `uv sync`
- Run tests: `uv run pytest` (pytest picks up `src` automatically via `pythonpath = ["src"]` in `pyproject.toml`)
- Run a single test: `uv run pytest tests/test_main.py -k test_name`
- Type check: `uv run mypy`
- Lint: `uv run ruff check .`
- Docs: `mkdocs serve` (requires `dev` dependency group)

## Architecture

- **`patch.py`** is the core: `install()` sets `Color.parse` to `staticmethod(_patched_parse)` (so instance calls work). `_patched_parse` is `lru_cache`d and is **Rich-first**: it calls Rich's original parse and only on `ColorParseError` tries `#abc` hex expansion and the CSS name map, otherwise re-raising. `uninstall()` restores Rich's original classmethod object. Both are idempotent and serialised by a module-level lock; `is_installed()` inspects `Color.__dict__["parse"]` (no flag).
- **`css.py`** owns `get_css_map()`, the CSS4 name → hex lookup, embedded in the package, plus the `CSSColor`/`CSSColors` helpers.
- **`hex_utils.py`** has `is_3digit_hex()` / `expand_3digit_hex()` (both require the leading `#`), plus `is_dark`/`is_light`.
- The CLI and loguru logger were removed in v2.0.0; don't reintroduce them.
- Only `install()` should mutate global state. No `rich.traceback.install()` or other import-time side effects in `__init__.py` or `css.py`.

## Testing notes

- `tests/test_import_side_effects.py` guards against import-time side effects.
- Names Rich already knows (`red`, `orchid`, ...) must resolve to Rich's color, not the CSS hex; parametrized tests account for this via `_rich_knows`.

## Versioning

Version lives in `src/rich_color_ext/__init__.py` (`__version__`, read by hatch). Update `CHANGELOG.md`, README and docs together for behavior changes.
