"""Additional tests for CSS color parsing utilities."""
from collections.abc import Iterable

import pytest

from rich_color_ext import CSSColor, get_css_map
from rich_color_ext.patch import _patched_parse


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
    color = _patched_parse(name.upper())
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
