---
title: CSS module
---

## Examples

Create a `CSSColor` from a hex value or name and inspect its attributes:

```python
from rich_color_ext.css import CSSColor

color = CSSColor.from_hex('#663399')
assert color.name == 'rebeccapurple'
assert color.hex == '#663399'
assert (color.red, color.green, color.blue) == (102, 51, 153)

color2 = CSSColor.from_name('aliceblue')
assert color2.hex == '#F0F8FF'
```

You can also convert hex to RGB directly:

```python
from rich_color_ext.css import CSSColor
assert CSSColor.hex_to_rgb('#ff0000') == (255, 0, 0)
```

## API reference

::: rich_color_ext.css
