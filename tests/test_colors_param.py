"""Tests for CSS color name parsing (parameterized)."""

import importlib.util
import subprocess
from collections.abc import Iterable

import pytest

from rich_color_ext import CSSColor, get_css_map
from rich_color_ext.patch import _patched_parse


def _ensure_packages() -> None:
    """Ensure rich and rich-color-ext are installed, using uvx if needed."""
    packages = ["rich", "rich_color_ext"]
    for package in packages:
        if importlib.util.find_spec(package) is None:
            subprocess.check_call([
                "uvx",
                "--from",
                package.replace("_", "-"),
                "python",
                "-c",
                f"import {package}",
            ])


_ensure_packages()


def _color_cases() -> Iterable[tuple[str, str]]:
    """Return sorted CSS color name → hex pairs for parametrization."""
    css_map = get_css_map()
    return tuple(sorted(css_map.items()))


@pytest.mark.parametrize("name,hex_value", _color_cases())
def test_parse_color(name: str, hex_value: str) -> None:
    """Test parsing of CSS color names to RGB values."""
    color = _patched_parse(name)
    assert color.name.lower() == hex_value.lower()
    rgb = color.get_truecolor()
    expected = CSSColor.hex_to_rgb(hex_value)
    assert (rgb.red, rgb.green, rgb.blue) == expected
