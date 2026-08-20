"""rich-color-ext.__init__.py

A `rich.color.Color` parser extensions package.

This package extends the Rich library's color parsing capabilities by adding support for:
- 3-digit hexadecimal color codes (e.g., `#abc`).
- CSS color names (e.g., `rebeccapurple`, `mediumslateblue`).
It achieves this by patching the `Color.parse` method in Rich with an extended parser.

For more information, see the documentation at
"""

from rich_color_ext.css import CSSColor, get_css_map
from rich_color_ext.patch import install, is_installed, uninstall

__version__ = "2.0.0"

CSS_MAP: dict[str, str] = get_css_map()  # Preload the CSS map so it's available quickly

__all__: list[str] = [
    "CSSColor",
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
