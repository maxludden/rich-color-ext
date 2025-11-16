---
title: Usage
CSS: styles/extra.css,
---

## Installing

Install from PyPI:

```bash
pip install rich-color-ext
```

Or using `uv` (recommended for some workflows):

```bash
# via uv directly
uv add rich-color-ext

# or via pip through uv
uv pip add rich-color-ext
```

## Basic usage

To enable the extended parsing behaviour, import and call `install()` once at
startup in your program.

```python
from rich_color_ext import install
from rich.console import Console

install()  # Patch Rich's Color.parse method

console = Console(width=64)
console.print("This text can include CSS colors like [bold rebeccapurple]rebeccapurple[/] or 3-digit hex like [#f0f]#f0f[/].")
```

The package also provides `CSSColor` helpers and a `get_css_map()` function to
inspect the canonical list of supported CSS named colours.

## Logging / Troubleshooting

The package uses `loguru` internally but keeps the logger disabled by default.
Enable it at runtime to see diagnostic information:

```python
from rich_color_ext import log
log.enable("rich_color_ext")
# ... do things that exercise the library ...
log.disable("rich_color_ext")
```

## Packaging notes (PyInstaller)

The CSS map is embedded in the package so a separate `colors.json` is usually
not required. See the README for legacy packaging tips if you need to include
the JSON resource manually.
