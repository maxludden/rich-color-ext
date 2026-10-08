---
title: Usage
CSS: styles/extra.css,
---

!!! note "Applies to v3.0.0"
    The steps below describe the behaviour shipped with `rich-color-ext`
    **v3.0.0**. If you are on an older release, upgrade with `uv pip
    install --upgrade rich-color-ext` before following along.

!!! warning "Breaking change in v3.0.0"
    Rich's parser now runs **first**; CSS names and 3-digit hex are only a fallback
    for colors Rich rejects. Names Rich already knows (`red`, `green`, `white`,
    `orchid`, ...) keep Rich's own color instead of the CSS truecolor value, and
    3-digit hex requires the leading `#` (`#09f`, not `09f`). The import-time
    `CSS_MAP` constant was removed; use `get_css_map()`. See
    [How to Upgrade to v3.0.0](upgrade-to-v3.md) and the
    [changelog](https://github.com/maxludden/rich-color-ext/blob/main/CHANGELOG.md).

## Installing

Install using `uv`/`uv pip` (recommended):

```shell
# via uv directly
uv add rich-color-ext

# or via pip through uv
uv pip install rich-color-ext
```

Install from PyPI:

```shell
pip install rich-color-ext
```

## Basic usage

To enable the extended parsing behaviour, import and call `install()` once at
startup in your program.

```python
from rich_color_ext import install
from rich.console import Console

install()  # Patch Rich's Color.parse method

console = Console(width=64)
console.print(
    "This text can include CSS colors like [bold rebeccapurple]rebeccapurple[/] or 3-digit hex like [#f0f]#f0f[/]."
)
```

## How parsing works

`rich-color-ext` parses with Rich's own parser first and falls back to
`rich-color-ext` only when Rich fails:

1. `Color.parse(text)` calls Rich's original parser first. If Rich can parse the
   text, that result is returned unchanged.
2. Only if Rich raises `ColorParseError` does `rich-color-ext` try its own parsing:
   `#abc`-style hex is expanded to `#aabbcc`, or the text is looked up
   (case-insensitively) in the CSS color map.
3. If `rich-color-ext` can't parse it either, Rich's original `ColorParseError` is
   re-raised.

!!! note "Only `Color.parse` is Rich-first"
    `get_css_map()` and the `CSSColor` helpers don't consult Rich:
    `get_css_map()["red"]` is the CSS hex `#ff0000`, while `Color.parse("red")` is
    Rich's ANSI `red`.

Results are cached with `functools.lru_cache`. Call `uninstall()` to restore Rich's
original `Color.parse`.

## Install, uninstall and thread safety

```python
from rich_color_ext import get_css_map, install, is_installed, uninstall

install()  # idempotent
assert is_installed()
get_css_map()["rebeccapurple"]  # '#663399'
uninstall()  # restores Rich's original Color.parse exactly
```

- `install()` and `uninstall()` are serialised with a lock, so they are safe to call
  from several threads. `is_installed()` inspects `Color.parse` itself rather than a
  separate flag. Parsing needs no lock.
- The patch is a `classmethod`, like Rich's own, so `Color.parse(...)` works on instances and `MyColor.parse(...)` on a `Color` subclass returns a `MyColor`.
- Importing the package has **no side effects**: nothing is patched until you call
  `install()`, and display-only Rich modules (`Panel`, `Table`, `Columns`) are
  imported lazily.

## Migrating from v2

| v2 | v3 |
| --- | --- |
| `Color.parse("red")` → CSS truecolor `#ff0000` | Rich's ANSI `red` (Rich wins) |
| `Color.parse("09f")` → `#0099ff` | `ColorParseError`; use `#09f` |
| `from rich_color_ext import CSS_MAP` | `from rich_color_ext import get_css_map` |

The package also provides `CSSColor` helpers and a `get_css_map()` function to
inspect the canonical list of supported CSS named colours.
