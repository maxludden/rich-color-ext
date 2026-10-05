# rich_color_ext/patch.py
"""rich-color-ext.patch.py

Monkey-patching support for ``rich.color.Color.parse``.

The patched parser always tries Rich's own parser first and only falls back to
3-digit hex (``#abc``) and CSS color names when Rich rejects the input. Colors
Rich already understands (including ANSI names such as ``red``) are therefore
unchanged.
"""

import threading
from functools import lru_cache

from rich.color import Color, ColorParseError

from rich_color_ext.css import get_css_map
from rich_color_ext.hex_utils import expand_3digit_hex, is_3digit_hex

# Rich's ``parse`` as a callable (bound classmethod) and as the raw class attribute.
# The raw attribute is kept so ``uninstall`` restores ``Color.parse`` exactly.
_ORIGINAL_PARSE = Color.parse
_ORIGINAL_PARSE_ATTR = Color.__dict__["parse"]

# Serialises install()/uninstall(); _patched_parse itself is pure and needs no lock.
_LOCK = threading.Lock()

__all__: list[str] = ["install", "is_installed", "uninstall"]


@lru_cache(maxsize=1024)
def _patched_parse(color: str = "") -> Color:
    """
    Replacement for ``Color.parse`` that adds 3-digit hex and CSS color name support.

    Rich's parser is tried first; the extensions are only consulted if it raises
    :class:`~rich.color.ColorParseError`. Results are cached, like Rich's own.

    Args:
        color: The color string to parse (case- and whitespace-insensitive).

    Returns:
        A :class:`rich.color.Color` instance.

    Raises:
        ColorParseError: If neither Rich nor the extensions can parse ``color``.
    """
    try:
        return _ORIGINAL_PARSE(color)
    except ColorParseError:
        color_str: str = color.strip().lower()
        if is_3digit_hex(color_str):
            return _ORIGINAL_PARSE(expand_3digit_hex(color_str))
        hex6 = get_css_map().get(color_str)
        if hex6 is not None:
            return _ORIGINAL_PARSE(hex6)
        raise


def install() -> None:
    """
    Install the monkey patch. After this call, ``rich.color.Color.parse`` also
    accepts 3-digit hex (``#abc``) and CSS color names. Safe to call multiple times.
    """
    with _LOCK:
        if is_installed():
            return
        # staticmethod so the patch also works when called on a Color instance.
        setattr(Color, "parse", staticmethod(_patched_parse))


def is_installed() -> bool:
    """
    Return True if the monkey patch is currently installed.
    """
    return Color.__dict__["parse"] is not _ORIGINAL_PARSE_ATTR


def uninstall() -> None:
    """
    Uninstall the monkey patch, restoring the original ``rich.color.Color.parse``.
    Safe to call multiple times.
    """
    with _LOCK:
        if not is_installed():
            return
        setattr(Color, "parse", _ORIGINAL_PARSE_ATTR)
