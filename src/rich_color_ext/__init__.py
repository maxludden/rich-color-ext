"""rich-color-ext.__init__.py

A `rich.color.Color` parser extensions package.

This package extends the Rich library's color parsing capabilities by adding support for:
- 3-digit hexadecimal color codes (e.g., `#abc`).
- CSS color names (e.g., `rebeccapurple`, `mediumslateblue`).
It achieves this by patching the `Color.parse` method in Rich with an extended parser.
Rich's own parser always runs first; the extensions are only used when Rich rejects
the input, so anything Rich already understands (e.g. ANSI `red`) is unchanged.
Call `install()` to enable the patch; importing the package does not apply it.

For more information, see https://maxludden.github.io/rich-color-ext/
"""

from rich_color_ext.css import CSSColor, CSSColors, get_css_map
from rich_color_ext.patch import install, is_installed, uninstall

__version__ = "3.0.0"

__all__: list[str] = [
    "CSSColor",
    "CSSColors",
    "__version__",
    "get_css_map",
    "install",
    "is_installed",
    "rce_install",
    "rce_uninstall",
    "uninstall",
]


def rce_install() -> None:
    """Backward-compatible wrapper for install()."""
    install()


def rce_uninstall() -> None:
    """Backward-compatible wrapper for uninstall()."""
    uninstall()
