# [![rich-color-ext](static/img/rich-color-ext-banner.svg)](https://GitHub.com/maxludden/rich-color-ext)

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2C%203.11%2C%203.12%2C%203.13-blue" alt="Python versions"></a>
  <a href="https://pypi.org/project/rich_gradient/"><img src="https://img.shields.io/pypi/v/rich-color-ext" alt="PyPI version"></a>
  <a href="https://github.com/astral-sh/uv"><img src="static/img/uv-badge.svg" alt="uv badge"></a>
</p>

<p align="center">
    <a href="https://github.com/maxludden/rich-color-ext/actions/workflows/docs-deploy.yml"><img src="https://github.com/maxludden/rich-color-ext/actions/workflows/docs-deploy.yml/badge.svg" alt="Docs build status"></a>
    <a href="https://maxludden.github.io/rich-color-ext/"><img src="https://img.shields.io/badge/docs-GitHub%20Pages-blue" alt="Docs"></a>
</p>

[`rich-color-ext`](https://GitHub.com/maxludden/rich-color-ext) extends the great [rich](http://GitHub.com/textualize/rich) library to be able to parse 3-digit hex colors (ie. <span style="color:#09f">`#09F`</span>) and [CSS color names](https://www.w3.org/TR/css-color-4/#css-color) (ie. <span style="color:rebeccapurple;">`rebeccapurple`</span>).

> **Latest release:** `v0.1.9` (2025-11-19). See the [changelog](CHANGELOG.md) for the
> full list of updates and run the command below to confirm which version is
> installed locally.

```shell
python -c "import rich_color_ext; print(rich_color_ext.__version__)"
```

## Installation

### [uv](https://docs.astral.sh/uv/) (recommended)

```shell
# via uv directly
uv add rich-color-ext
```

or

```shell
# or via pip through uv
uv pip add rich-color-ext
```

### [pip](https://pypi.org/project/rich-color-ext/)

```shell
pip install rich-color-ext
```

## Usage

To make use of [`rich-color-ext`](https://pypi.org/project/rich-color-ext/) all you need to do is import and install it at the start of your program:

```python
from rich_color_ext import install
from rich.console import Console

install()  # Patch Rich's Color.parse method

console = Console(width=64)
console.print(
    Panel(
        "This is the [b #00ff99]rich_color_ext[/b #00ff99] \
example for printing CSS named colors ([bold rebeccapurple]\
rebeccapurple[/bold rebeccapurple]), 3-digit hex \
colors ([bold #f0f]#f0f[/bold #f0f]), and [b #99ff00]\
rich.color_triplet.ColorTriplet[/b #99ff00] & [b #00ff00]\
rich.color.Color[/b #00ff00] instances.",
        padding=(1,2)
    ),
    justify="center"
)
```

![example](example.svg)

## Logging

This package uses `loguru` for internal, developer-focused logging. By default the
logger is disabled so importing the package is quiet during normal usage. If you
need to enable internal debug output for troubleshooting, you can enable the
logger at runtime. For example:

```python
from rich_color_ext import log

# Enable internal logging emitted by rich-color-ext (useful for debugging)
log.enable("rich_color_ext")

# Revert to disabled state
log.disable("rich_color_ext")
```

Note: `loguru` is used only for internal diagnostics and is not required at
runtime for the library's primary functionality; it is disabled by default to
avoid noisy output.

<p style="text-align:center;">
    <a href="https://github.com/maxludden/rich-color-ext"><code>rich-color-ext</code> by Max Ludden</a>

<div style="text-align:center">
    <a href="https://github.com/maxludden/rich-color-ext">
        <img src="https://raw.githubusercontent.com/maxludden/rich-color-ext/a190326cccf4d5d14229a7e8d15867507b232750/static/img/MaxLogo.svg" alt="maxlogo" style="width:25%; display:block; margin:0 auto;">
    </a>
</div>

## Packaging with PyInstaller

As of recent releases the CSS colour map is embedded in the Python package and a separate `colors.json` file is not required for normal usage. The library and CLI prefer the package-level `get_css_map()` function, so PyInstaller bundles typically do not need any extra data files.

If you are building or packaging an older distribution that expects a
standalone `colors.json` file, or you intentionally rely on shipping the JSON resource, include it in the bundle using the legacy approaches below.

1) Pass the file with the command-line option `--add-data`:

     - macOS / Linux (colon separator):

         ```shell
         pyinstaller --onefile --add-data "static/json/colors.json:rich_color_ext" your_entry_script.py
         ```

     - Windows (semicolon separator):

         ```powershell
         pyinstaller --onefile --add-data "static\\json\\colors.json;rich_color_ext" your_entry_script.py
         ```

2) Add the file to the spec file's `Analysis.datas` list. Example snippet to paste into your `.spec` file:

     ```python
     a = Analysis(
             ['your_entry_script.py'],
             pathex=[],
             binaries=[],
             datas=[('static/json/colors.json', 'rich_color_ext')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=None,
     )
     ```

### Helper script

A small helper script is provided to build with PyInstaller and automatically choose the correct data separator for your platform. By default it builds the example `src/rich_color_ext/cli.py` entry script but you can pass any entry script as the first argument.

Usage:

```shell
./scripts/pyinstaller_build.sh [path/to/your_entry_script.py]  # src/rich_color_ext/cli.py
```
