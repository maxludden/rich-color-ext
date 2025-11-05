# test_main.py

import pytest
from rich.color import ColorParseError

from rich_color_ext.main import _extended_parse, get_css_color_triplet


def test_default_color():
    """Test that the default color is parsed correctly."""
    color = _extended_parse("default")
    assert color.name == "default"
    assert color.type.name == "DEFAULT"


def test_valid_css_name():
    """Test that a valid CSS color name is parsed correctly."""
    color = _extended_parse("rebeccapurple")
    assert color.name == "rebeccapurple"
    triplet = color.get_truecolor()
    assert triplet.red == 102
    assert triplet.green == 51
    assert triplet.blue == 153


def test_valid_three_digit_hex():
    """Test that a valid 3-digit hexadecimal color is parsed correctly."""
    color = _extended_parse("#09f")
    triplet = color.get_truecolor()
    assert triplet.red == 0x00
    assert triplet.green == 0x99
    assert triplet.blue == 0xFF


def test_valid_six_digit_hex():
    """Test that a valid 6-digit hexadecimal color is parsed correctly."""
    color = _extended_parse("#123456")
    triplet = color.get_truecolor()
    assert triplet.red == 0x12
    assert triplet.green == 0x34
    assert triplet.blue == 0x56


def test_invalid_color():
    """Test that an invalid color raises ColorParseError."""
    with pytest.raises(ColorParseError):
        _extended_parse("notacolor")


def test_get_css_color_triplet():
    """Test retrieving CSS color triplet."""
    triplet = get_css_color_triplet("aqua")
    assert (triplet.red, triplet.green, triplet.blue) == (0, 255, 255)


def test_get_css_color_triplet_invalid():
    """Test that retrieving an invalid CSS color raises ValueError."""
    with pytest.raises(ValueError):
        get_css_color_triplet("definitelynotacolor")
    with pytest.raises(ValueError):
        get_css_color_triplet("definitelynotacolor")
