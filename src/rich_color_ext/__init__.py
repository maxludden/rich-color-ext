"""Rich Color Extensions Package.

This package extends the Rich library's color parsing capabilities by adding support for:
- 3-digit hexadecimal color codes (e.g., `#abc`).
- CSS color names (e.g., `rebeccapurple`, `mediumslateblue`).
It achieves this by patching the `Color.parse` method in Rich with an extended parser.
"""

__version__ = "0.1.9"

from rich_color_ext.css import CSSColor, get_css_map
from rich_color_ext.patch import install, is_installed, uninstall

# Keep internal diagnostics quiet unless users explicitly enable them.


# Preload the CSS map so it's available quickly, but don't trigger any
# external side-effects.
CSS_MAP = get_css_map()

__all__ = [
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
    # Call uninstall once. Previous versions mistakenly called it twice.
    uninstall()
