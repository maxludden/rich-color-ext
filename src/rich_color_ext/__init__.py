"""Rich Color Extensions Package.

This package extends the Rich library's color parsing capabilities by adding support for:
- 3-digit hexadecimal color codes (e.g., `#abc`).
- CSS color names (e.g., `rebeccapurple`, `mediumslateblue`).
It achieves this by patching the `Color.parse` method in Rich with an extended parser.
"""

__version__ = "0.1.9"

from rich.traceback import install as tr_install

from rich_color_ext.css import CSSColor, get_css_map
from rich_color_ext.logger import log
from rich_color_ext.patch import install, is_installed, uninstall

# Enable rich tracebacks in development/imports, but avoid any heavy
# side-effects (network installs or subprocesses) during import.
tr_install()
log.disable("rich_color_ext")

# Preload the CSS map so it's available quickly, but don't trigger any
# external side-effects.
CSS_MAP = get_css_map()

__all__ = [
    "install",
    "is_installed",
    "uninstall",
    "rce_install",
    "rce_uninstall",
    "CSSColor",
    "get_css_map",
    "__version__",
]


def rce_install() -> None:
    """Backward-compatible wrapper for install()."""
    install()


def rce_uninstall() -> None:
    """Backward-compatible wrapper for uninstall()."""
    # Call uninstall once. Previous versions mistakenly called it twice.
    uninstall()
