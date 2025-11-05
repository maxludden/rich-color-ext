# [rich-color-ext](https://GitHub.com/maxludden/rich-color-ext)

[`rich-color-ext`](https://GitHub.com/maxludden/rich-color-ext) extends the great [rich](http://GitHub.com/textualize/rich) library to be able to parse 3-digit hex colors (ie. <span style="color:#09f">`#09F`</span>) and [CSS color names](https://www.w3.org/TR/css-color-4/#css-color) (ie. <span style="color:rebeccapurple;">`rebeccapurple`</span>).

## Installation

### [uv](https://docs.astral.sh/uv/) (recommended)

```shell
# via uv directly
uv add rich-color-ext
````

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

console = Console(width=80)
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

<p style="text-align:center;">
    <a href="https://github.com/maxludden/rich-gradient"><code>rich-gradient</code> by Max Ludden</a>

<div style="text-align:center">
    <a href="https://github.com/maxludden/rich-gradient">
        <img src="https://raw.githubusercontent.com/maxludden/rich-gradient/a190326cccf4d5d14229a7e8d15867507b232750/docs/img/MaxLogo.svg" alt="maxlogo" style="width:25%; display:block; margin:0 auto;">
    </a>
</div>
