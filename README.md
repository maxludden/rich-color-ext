<h1 align="center" width="100%">
    <a href="https://GitHub.com/maxludden/rich-color-ext">
        <img src="docs/img/rich-color-ext.svg" alt="rich-color-ext logo" width="100%">
    </a>
</h1>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10%2C%203.11%2C%203.12%2C%203.13-blue" alt="Python versions"></a>
  <a href="https://pypi.org/project/rich_color_ext/">
    <img src="https://img.shields.io/pypi/v/rich-color-ext"
        alt="PyPI version"></a>
  <a href="https://github.com/astral-sh/uv">
  <img src="docs/img/uv-badge.svg" alt="uv badge"></a>
</p>
<p align="center">
    <a href="https://github.com/maxludden/rich-color-ext/actions/workflows/docs-deploy.yml">
        <img src="https://github.com/maxludden/rich-color-ext/actions/workflows/docs-deploy.yml/badge.svg" alt="Docs build status"></a>
    <a href="https://maxludden.github.io/rich-color-ext/"><img src="https://img.shields.io/badge/docs-GitHub%20Pages-blue" alt="Docs"></a>
</p>

[`rich-color-ext`](https://GitHub.com/maxludden/rich-color-ext) extends the great [rich](http://GitHub.com/textualize/rich) library to be able to parse 3-digit hex colors (ie. <span style="color:#09f">`#09F`</span>) and [CSS color names](https://www.w3.org/TR/css-color-4/#css-color) (ie. <span style="color:rebeccapurple;">`rebeccapurple`</span>).

## Installation

### [uv](https://docs.astral.sh/uv/) (recommended)

```shell
# via uv directly
uv add rich-color-ext
```

or

```shell
# or via pip through uv
uv pip install rich-color-ext
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
        "This is the [b #00ff99]rich_color_ext[/b #00ff99] example for printing CSS named colors ([bold rebeccapurple]rebeccapurple[/bold rebeccapurple]), 3-digit hex colors ([bold #f0f]#f0f[/bold #f0f]), and [b #99ff00]rich.color_triplet.ColorTriplet[/b #99ff00] & [b #00ff00]rich.color.Color[/b #00ff00] instances.",
        padding=(1, 2),
    ),
    justify="center",
)
```

![example](docs/img/example.svg)

<p style="text-align:center;">
    <a href="https://github.com/maxludden/rich-color-ext"><code>rich-color-ext</code> by Max Ludden</a>
</p>

<div style="text-align:center">
    <a href="https://github.com/maxludden/rich-color-ext">
        <img src="docs/img/maxlogo.svg" alt="MaxLogo" style="width:40%; display:block; margin:0 auto;">
    </a>
</div>
