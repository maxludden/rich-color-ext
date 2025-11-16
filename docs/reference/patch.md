---
title: Patch module
---

## Examples

Patch Rich's `Color.parse` at runtime to add CSS name and 3-digit hex support:

```python
from rich_color_ext.patch import install, uninstall, is_installed

install()
assert is_installed()

# ... use Rich with CSS colours here ...

uninstall()
assert not is_installed()
```

## API reference

::: rich_color_ext.patch
