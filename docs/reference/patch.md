---
title: Patch module
---

## Examples

Patch Rich's `Color.parse` at runtime to add CSS name and 3-digit hex support
(Rich's parser runs first; the extensions are a fallback for colors Rich rejects):

```python
from rich_color_ext.patch import install, uninstall, is_installed

install()
assert is_installed()

# ... use Rich with CSS colours here ...

uninstall()
assert not is_installed()
```

`install()` and `uninstall()` are idempotent and serialised with a lock, and
`is_installed()` inspects `Color.parse` directly.

## API reference

::: rich_color_ext.patch
