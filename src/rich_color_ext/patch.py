# rich_color_ext/patch.py
"""
Monkey-patching support for rich.color.Color.parse.
"""

# from typing import Callable, Type, TypeAlias
from typing import TypeAlias

from rich.color import Color

from rich_color_ext.css import get_css_map
from rich_color_ext.hex_utils import expand_3digit_hex, is_3digit_hex

# _ORIGINAL_PARSE: Callable[[Type[Color], str], Color] = Color.parse # type: ignore
_Color: TypeAlias = Color

# Preserve original parser so that our patched parser can delegate to it
_ORIGINAL_PARSE = Color.parse

INSTALLED: bool = False


def _patched_parse(color: str = "") -> Color:
    """
    Replacement for RichColor.parse() that adds support for 3-digit hex codes (#ABC)
    and CSS color names (e.g. 'aliceblue').

    Args:
        cls: The Color class (should be rich.color.Color).
        color: The color string to parse.

    Returns:
        A rich Color instance.

    Raises:
        ColorParseError: If the parse fails in both our extensions and the original parse.
    """
    color_str = color.strip().lower()  # Normalize case and whitespace

    if is_3digit_hex(color_str):
        try:
            hex6 = expand_3digit_hex(color_str)
        except ValueError:
            # fall through to original
            return _ORIGINAL_PARSE(color)
        return _ORIGINAL_PARSE(hex6)
    # Handle CSS colour names
    css_map = get_css_map()
    if color_str in css_map:
        hex6 = css_map[color_str]
        return _ORIGINAL_PARSE(hex6)
    # fallback to original
    return _ORIGINAL_PARSE(color)


def install() -> None:
    """
    Install the monkey patch. After this call, rich.color.Color.parse will
    support 3‐digit hex and CSS colour names. Safe to call multiple times.
    """
    global INSTALLED  # pylint: disable=global-statement
    if INSTALLED:
        return
    Color.parse = _patched_parse  # type: ignore[assignment]
    INSTALLED = True


def is_installed() -> bool:
    """
    Return True if the monkey patch is currently installed.
    """
    return INSTALLED


def uninstall() -> None:
    """
    Uninstall the monkey patch, restoring the original rich.color.Color.parse.
    Safe to call multiple times.
    """
    global INSTALLED  # pylint: disable=global-statement
    if not INSTALLED:
        return
    Color.parse = _ORIGINAL_PARSE  # type: ignore[assignment]
    INSTALLED = False
