# rich_color_ext/patch.py
"""rich-color-ext.patch.py

Monkey-patching support for ``rich.color.Color.parse``.

The patched parser always tries Rich's own parser first and only falls back to
3-digit hex (``#abc``) and CSS color names when Rich rejects the input. Colors
Rich already understands (including ANSI names such as ``red``) are therefore
unchanged.
"""

import threading
from collections.abc import Callable
from functools import lru_cache
from typing import Any

from rich.color import Color, ColorParseError

from rich_color_ext.css import get_css_map
from rich_color_ext.hex_utils import expand_3digit_hex, is_3digit_hex

# Rich's raw ``parse`` class attribute (a classmethod). It is kept so ``uninstall``
# restores ``Color.parse`` exactly, and its ``__func__`` is Rich's cached
# ``(cls, color)`` implementation, which the patch delegates to so subclasses of
# ``Color`` get instances of themselves back.
_ORIGINAL_PARSE_ATTR = Color.__dict__["parse"]
_ORIGINAL_PARSE_FUNC: Callable[[type[Color], str], Color] = _ORIGINAL_PARSE_ATTR.__func__

# Serialises install()/uninstall(); _patched_parse itself is pure and needs no lock.
_LOCK = threading.Lock()

__all__: list[str] = ["install", "is_installed", "uninstall"]


@lru_cache(maxsize=1024)
def _patched_parse(cls: type[Color], color: str = "") -> Color:
    """
    Replacement for ``Color.parse`` that adds 3-digit hex and CSS color name support.

    Rich's parser is tried first; the extensions are only consulted if it raises
    :class:`~rich.color.ColorParseError`. Results are cached per receiving class,
    like Rich's own, and are instances of ``cls``.

    Args:
        cls: The class ``parse`` was called on (``Color`` or a subclass).
        color: The color string to parse (case- and whitespace-insensitive).

    Returns:
        An instance of ``cls``.

    Raises:
        ColorParseError: If neither Rich nor the extensions can parse ``color``.
    """
    try:
        return _ORIGINAL_PARSE_FUNC(cls, color)
    except ColorParseError:
        color_str: str = color.strip().lower()
        if is_3digit_hex(color_str):
            return _ORIGINAL_PARSE_FUNC(cls, expand_3digit_hex(color_str))
        hex6 = get_css_map().get(color_str)
        if hex6 is not None:
            return _ORIGINAL_PARSE_FUNC(cls, hex6)
        raise


# The exact descriptor we install, so ownership is checked by identity. A
# classmethod (like Rich's) so the receiving class is passed through.
_PATCHED_PARSE_ATTR: Any = classmethod(_patched_parse)  # type: ignore[arg-type]


def install() -> None:
    """
    Install the monkey patch. After this call, ``rich.color.Color.parse`` also
    accepts 3-digit hex (``#abc``) and CSS color names. Safe to call multiple times.
    """
    with _LOCK:
        if is_installed():
            return
        setattr(Color, "parse", _PATCHED_PARSE_ATTR)


def is_installed() -> bool:
    """
    Return True if the monkey patch is currently installed.
    """
    return Color.__dict__["parse"] is _PATCHED_PARSE_ATTR


def uninstall() -> None:
    """
    Uninstall the monkey patch, restoring the original ``rich.color.Color.parse``.
    Safe to call multiple times. If another library has replaced ``Color.parse``
    since ``install()``, that foreign patch is left untouched.
    """
    with _LOCK:
        if not is_installed():
            return
        setattr(Color, "parse", _ORIGINAL_PARSE_ATTR)
