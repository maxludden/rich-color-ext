---
title: How to Upgrade to v3.0.0
---

# How to Upgrade to v3.0.0

v3.0.0 changes how `rich-color-ext` decides what a color string means. Most
projects upgrade with no code changes, but three behaviors are **breaking**. This
page shows what changed, how to find affected code, and how to fix it.

## 1. Upgrade

```shell
uv add "rich-color-ext>=3.0.0"
# or
uv pip install --upgrade rich-color-ext
```

Confirm the installed version:

```shell
python -c "import rich_color_ext; print(rich_color_ext.__version__)"
```

## 2. Breaking changes

### Rich's parser now runs first

In v2, CSS color names were checked **before** Rich's parser. In v3, Rich always
parses first and the CSS map is only a fallback for colors Rich rejects.

Names that both Rich and CSS know now resolve to **Rich's** color (an ANSI or
256-color value that follows the user's terminal theme), not the CSS truecolor hex.

| Input | v2 | v3 |
| --- | --- | --- |
| `red` | `#ff0000` (truecolor) | Rich's ANSI `red` |
| `orchid` | `#da70d6` (truecolor) | Rich's 256-color `orchid` |
| `rebeccapurple` | `#663399` | `#663399` (unchanged, Rich rejects it) |
| `#abc` | `#aabbcc` | `#aabbcc` (unchanged) |

The affected names are those in the CSS map that Rich also accepts, including
`black`, `blue`, `cyan`, `green`, `magenta`, `orchid`, `purple`, `red`, `tan`,
`violet`, `white` and `yellow`.

**If you need the exact CSS color**, use the hex value directly:

```python
from rich_color_ext import get_css_map

hex_red = get_css_map()["red"]  # '#ff0000'
console.print("exact CSS red", style=hex_red)
```

### 3-digit hex requires the `#`

`09f` and `abc` are no longer parsed, so ordinary words such as `bad` or `add` can
never be mistaken for colors. Write `#09f` and `#abc`.

`is_3digit_hex()` and `expand_3digit_hex()` follow the same rule: they require the
leading `#`, and `expand_3digit_hex("abc")` now raises `ValueError`.

### `CSS_MAP` was removed

The import-time `CSS_MAP` constant is gone. Call `get_css_map()` instead; it builds
the map on first use and caches it.

```python
# v2
from rich_color_ext import CSS_MAP

# v3
from rich_color_ext import get_css_map

CSS_MAP = get_css_map()
```

## 3. Find code that needs changes

Search your project for the old patterns:

```shell
# bare 3-digit hex without '#', e.g. style="09f" or "[abc]text[/]"
grep -rnE "\[[0-9a-fA-F]{3}\]|\"[0-9a-fA-F]{3}\"" src/

# the removed constant
grep -rn "CSS_MAP" src/
```

Also review any place you pass the names listed above (`red`, `green`, `white`, ...)
and rely on them being exact CSS truecolors, such as snapshot tests or exported SVG
and HTML.

## 4. Verify

```python
from rich.color import Color, ColorParseError, ColorType

from rich_color_ext import install, uninstall

install()
try:
    assert Color.parse("#09F").name == "#0099ff"
    assert Color.parse("rebeccapurple").name == "#663399"
    assert Color.parse("red").type is ColorType.STANDARD  # Rich wins

    try:
        Color.parse("09f")
    except ColorParseError:
        print("bare hex rejected, as expected")
finally:
    uninstall()
```

## What else is new

- **Instance calls work.** `Color.parse(...)` can be called on a `Color` instance
  again; v2 raised a `TypeError` once the patch was installed.
- **Cached parsing.** The patched parser uses `functools.lru_cache`, like Rich's own.
- **Thread-safe install.** `install()` and `uninstall()` are serialised with a
  lock, and `is_installed()` inspects `Color.parse` directly.
- **Lighter import.** Importing the package patches nothing, and `Panel`, `Table`
  and `Columns` are only imported when needed.
- **Exact restore.** `uninstall()` puts back Rich's original `classmethod`.

## Upgrading from v1 or earlier

v3 includes everything from v2.0.0: the CLI (`rich-color-ext`, `rich-color`) and the
`loguru` logger were removed, along with the `loguru` dependency. If you used either,
remove those calls before upgrading. See the
[changelog](https://github.com/maxludden/rich-color-ext/blob/main/CHANGELOG.md) for
the full history.
