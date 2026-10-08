"""Additional tests for CSS color parsing utilities."""

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


def _unique_hex_cases() -> Iterable[tuple[str, str]]:
    """Return colour cases filtered to the first occurrence of each hex value."""
    seen: set[str] = set()
    unique: list[tuple[str, str]] = []
    for name, hex_value in _color_cases():
        key = hex_value.lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append((name, hex_value))
    return tuple(unique)


@pytest.mark.parametrize("name,hex_value", _color_cases())
def test_patched_parse_handles_case_insensitive_names(name: str, hex_value: str) -> None:
    """The patched parser should accept CSS colour names regardless of case."""
    color = _patched_parse(Color, name.upper())
    if _rich_knows(name):
        assert color == Color.parse(name)
        return
    assert color.name.lower() == hex_value.lower()
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == CSSColor.hex_to_rgb(hex_value)


@pytest.mark.parametrize("name,hex_value", _unique_hex_cases())
def test_csscolor_from_hex_roundtrip(name: str, hex_value: str) -> None:
    """CSSColor.from_hex should round-trip unique CSS colour hex values."""
    color = CSSColor.from_hex(hex_value)
    assert color.name == name
    assert color.hex.lower() == hex_value.lower()
    assert (color.red, color.green, color.blue) == CSSColor.hex_to_rgb(hex_value)


@pytest.mark.parametrize("name,hex_value", _unique_hex_cases())
def test_csscolor_from_rgb_roundtrip(name: str, hex_value: str) -> None:
    """CSSColor.from_rgb should derive the same canonical name and hex."""
    red, green, blue = CSSColor.hex_to_rgb(hex_value)
    color = CSSColor.from_rgb(red, green, blue)
    assert color.name == name
    assert color.hex.lower() == hex_value.lower()
    assert (color.red, color.green, color.blue) == (red, green, blue)


def test_csscolors_exported_from_package() -> None:
    import rich_color_ext

    assert "CSSColors" in rich_color_ext.__all__
    assert rich_color_ext.CSSColors.__name__ == "CSSColors"


def test_csscolor_rich_repr_is_balanced() -> None:
    """The plain text of CSSColor.rich() has matched quotes (no stray ``''``)."""
    text = CSSColor.from_name("rebeccapurple").rich().plain
    assert text == "CSSColor<hex='#663399', rgb='rgb(102,51,153)', name='rebeccapurple'>"


def test_csscolor_bare_3digit_hex_is_rejected() -> None:
    """Like the parser patch, 3-digit hex needs the leading '#'."""
    assert CSSColor.hex_to_rgb("#abc") == (0xAA, 0xBB, 0xCC)
    with pytest.raises(ValueError):
        CSSColor.hex_to_rgb("abc")
    with pytest.raises(ValueError):
        CSSColor.from_hex("bad")
    assert CSSColor.hex_to_rgb("aabbcc") == (0xAA, 0xBB, 0xCC)
