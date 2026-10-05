---
title: Home
---

[![rich-color-ext](img/rich-color-ext-banner-short.svg)](https://github.com/maxludden/rich-color-ext)

`rich-color-ext` extends the Rich library to parse 3-digit hex colors (`#09F`→`#0099FF`, the `#` is required) and CSS color names (`rebeccapurple`→`#663399`). This project allows Rich users to write color names or short hex codes and have them correctly parsed into Rich Color instances.

## Key features

- Parse 3-digit hex colors like `#abc` → `#AABBCC` (the leading `#` is required)
- Parse CSS color names `rebeccapurple`, `mediumslateblue`
- Lightweight monkey-patch to Rich's `Color.parse` to add the above support.
- Rich-first: Rich's parser runs first and the extensions are only a fallback, so
  colors Rich already understands (e.g. ANSI `red`) are unchanged.
- Nothing is patched at import time; call `install()` explicitly. `install()` and
  `uninstall()` are idempotent and thread-safe.

For installation instructions, usage examples, packaging notes and more,
see the sections linked from the navigation.

---

<div class="md-button-row md-button-row--align-end">
  <a class="md-button md-button--primary" href="usage/">Next: Usage</a>
</div>
