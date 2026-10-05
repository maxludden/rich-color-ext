"""Tests for CSS color name parsing (parameterized)."""

from collections.abc import Iterable

import pytest
from rich.color import Color, ColorParseError

from rich_color_ext import CSSColor, get_css_map
from rich_color_ext.patch import _patched_parse


def _rich_knows(name: str) -> bool:
    """Return True if Rich's own parser accepts ``name`` (Rich wins for these)."""
    try:
        Color.parse(name)
    except ColorParseError:
        return False
    return True


def _color_cases() -> Iterable[tuple[str, str]]:
    """Return sorted CSS color name → hex pairs for parametrization."""
    css_map = get_css_map()
    return tuple(sorted(css_map.items()))


@pytest.mark.parametrize("name,hex_value", _color_cases())
def test_parse_color(name: str, hex_value: str) -> None:
    """Test parsing of CSS color names to RGB values."""
    color = _patched_parse(name)
    if _rich_knows(name):
        assert color == Color.parse(name)
        return
    assert color.name.lower() == hex_value.lower()
    rgb = color.get_truecolor()
    expected = CSSColor.hex_to_rgb(hex_value)
    assert (rgb.red, rgb.green, rgb.blue) == expected
