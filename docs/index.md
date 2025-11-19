---
title: Home
---

# [![rich-color-ext](img/rich-color-ext-banner-short.svg)](https://github.com/maxludden/rich-color-ext)

`rich-color-ext` extends the Rich library to parse 3-digit hex colors (`#09F`→`#0099FF`) and CSS color names (`rebeccapurple`→`#663399`). This project allows Rich users to write color names or short hex codes and have them correctly parsed into Rich Color instances.

??? info "Latest release"

    `rich-color-ext` is currently at **v0.1.9** (2025-11-19). Check the [changelog](https://github.com/maxludden/rich-color-ext/blob/main/CHANGELOG.md) for recent updates. To verify the version you have installed, run `python -c "import rich_color_ext; print(rich_color_ext.__version__)"`.

## Key features

- Parse 3-digit hex colors like `#abc` → `#AABBCC`
- Parse CSS color names `rebeccapurple`, `mediumslateblue`
- Lightweight monkey-patch to Rich's `Color.parse` to add the above support.

For installation instructions, usage examples, packaging notes and more,
see the sections linked from the navigation.

---

<div class="md-button-row md-button-row--align-end">
  <a class="md-button md-button--primary" href="usage/">Next: Usage</a>
</div>
