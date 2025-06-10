import pytest
from rich.color import Color, ColorParseError, ColorType
from rich.color_triplet import ColorTriplet
from rich_color_ext import _extended_parse

def test_parse_css_colors():
    """Test the extended color parsing functionality with CSS colors."""
    assert _extended_parse("rebeccapurple") == Color("rebeccapurple", ColorType.TRUECOLOR, triplet=ColorTriplet(102, 51, 153))
    assert _extended_parse("cornflowerblue") == Color("cornflowerblue", ColorType.TRUECOLOR, triplet=ColorTriplet(100, 149, 237))

def test_parse_css_hex_color():
    """Test the extended color parsing functionality with CSS hex colors."""
    assert _extended_parse("#663399") == Color("#663399", ColorType.TRUECOLOR, triplet=ColorTriplet(102, 51, 153))

def test_parse_3_digit_hex_color():
    """Test the extended color parsing functionality with 3-digit hex colors."""
    assert _extended_parse("#abc") == Color("#aabbcc", ColorType.TRUECOLOR, triplet=ColorTriplet(170, 187, 204))

def test_parse_invalid_colors():
    """Test the extended color parsing functionality with invalid colors."""
    with pytest.raises(ColorParseError):
        _extended_parse("notacolor")

def test_default_color():
    """Test the parsing of the default color."""
    assert _extended_parse("default") == Color("default", ColorType.DEFAULT)

def test_invalid_hex_colors():
    """Test the extended color parsing functionality with invalid hex colors."""
    with pytest.raises(ColorParseError):
        _extended_parse("#12345")  # Invalid hex length
