"""Rich Color Extensions Package.

This package extends the Rich library's color parsing capabilities by adding support for:
- 3-digit hexadecimal color codes (e.g., `#abc`).
- CSS Level 4 color names (e.g., `rebeccapurple`, `mediumslateblue`).
It achieves this by patching the `Color.parse` method in Rich with an extended parser.
"""
__version__ = "0.1.5"

from rich.color import Color
from rich.console import Console

from rich_color_ext.main import _extended_parse, _original_parse


def install() -> None:
    """Install the extended color parser by patching Rich's Color.parse method."""
    Color.parse = _extended_parse  # type: ignore[assignment]

def rc_install() -> None:
    """Install the extended color parser by patching Rich's Color.parse method."""
    install()


def uninstall() -> None:
    """Uninstall the extended color parser by restoring Rich's original Color.parse method."""
    Color.parse = _original_parse  # type: ignore[assignment]

def rc_uninstall() -> None:
    """Uninstall the extended color parser by restoring Rich's original Color.parse method."""
    uninstall()


def is_installed() -> bool:
    """Return True if the extended color parser is currently installed."""
    console = Console()
    parse_attr = getattr(Color, "parse", None)
    console.log(f"Color.parse attribute: {parse_attr!r}")
    underlying = getattr(parse_attr, "__func__", parse_attr)
    console.log(f"Underlying function: {underlying!r}")
    return underlying is _extended_parse
