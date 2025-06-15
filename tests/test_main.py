import json
from pathlib import Path

import pytest
from rich.color import Color, ColorParseError, ColorType
from rich.color_triplet import ColorTriplet

from rich_color_ext import _extended_parse


def test_parse_css_colors():
    """Test the extended color parsing functionality with CSS colors."""

    def test_parse_css_colors():
        """Test the extended color parsing functionality with CSS colors."""
        # Test a few representative CSS color names
        assert _extended_parse("rebeccapurple") == Color(
            "rebeccapurple", ColorType.TRUECOLOR, triplet=ColorTriplet(102, 51, 153)
        )
        assert _extended_parse("cornflowerblue") == Color(
            "cornflowerblue", ColorType.TRUECOLOR, triplet=ColorTriplet(100, 149, 237)
        )
        # Test case insensitivity
        assert _extended_parse("RebeccaPurple") == Color(
            "rebeccapurple", ColorType.TRUECOLOR, triplet=ColorTriplet(102, 51, 153)
        )
        assert _extended_parse("CORNflowerBLUE") == Color(
            "cornflowerblue", ColorType.TRUECOLOR, triplet=ColorTriplet(100, 149, 237)
        )
        # Test leading/trailing whitespace
        assert _extended_parse("  rebeccapurple  ") == Color(
            "rebeccapurple", ColorType.TRUECOLOR, triplet=ColorTriplet(102, 51, 153)
        )
        # Test alias colors (grey/gray)
        assert _extended_parse("gray") == Color(
            "gray", ColorType.TRUECOLOR, triplet=ColorTriplet(128, 128, 128)
        )
        assert _extended_parse("grey") == Color(
            "grey", ColorType.TRUECOLOR, triplet=ColorTriplet(128, 128, 128)
        )

    with open(Path("src/rich_color_ext/colors.json")) as f:
        color_data = json.load(f)

    @pytest.mark.parametrize("name,entry", list(color_data.items()))
    def test_parse_all_css_colors(name, entry):
        """Test parsing of every CSS color in colors.json."""
        parsed = _extended_parse(name)
        assert parsed.name == name
        triplet = parsed.get_truecolor()
        assert triplet.red == entry["r"], (
            f"{name} red mismatch: {triplet.red} != {entry['r']}"
        )
        assert triplet.green == entry["g"], (
            f"{name} green mismatch: {triplet.green} != {entry['g']}"
        )
        assert triplet.blue == entry["b"], (
            f"{name} blue mismatch: {triplet.blue} != {entry['b']}"
        )

    def test_parse_css_hex_color():
        """Test the extended color parsing functionality with CSS hex colors."""
        assert _extended_parse("#000000") == Color(
            "#000000", ColorType.TRUECOLOR, triplet=ColorTriplet(0, 0, 0)
        )
        assert _extended_parse("#ffffff") == Color(
            "#ffffff", ColorType.TRUECOLOR, triplet=ColorTriplet(255, 255, 255)
        )
        assert _extended_parse("#1e90ff") == Color(
            "#1e90ff", ColorType.TRUECOLOR, triplet=ColorTriplet(30, 144, 255)
        )

    def test_parse_3_digit_hex_color():
        """Test the extended color parsing functionality with 3-digit hex colors."""
        assert _extended_parse("#abc") == Color(
            "#aabbcc", ColorType.TRUECOLOR, triplet=ColorTriplet(170, 187, 204)
        )
        assert _extended_parse("#123") == Color(
            "#112233", ColorType.TRUECOLOR, triplet=ColorTriplet(17, 34, 51)
        )
        # Test uppercase hex
        assert _extended_parse("#ABC") == Color(
            "#aabbcc", ColorType.TRUECOLOR, triplet=ColorTriplet(170, 187, 204)
        )

    def test_parse_invalid_colors():
        """Test the extended color parsing functionality with invalid colors."""
        with pytest.raises(ColorParseError):
            _extended_parse("notacolor")
        with pytest.raises(ColorParseError):
            _extended_parse("#12")  # too short
        with pytest.raises(ColorParseError):
            _extended_parse("#abcd")  # 4-digit hex not supported
        with pytest.raises(ColorParseError):
            _extended_parse("")  # empty string

    def test_default_color():
        """Test the parsing of the default color."""
        assert _extended_parse("default") == Color("default", ColorType.DEFAULT)
        assert _extended_parse(" DEFAULT ") == Color("default", ColorType.DEFAULT)


def test_parse_css_hex_color():
    """Test the extended color parsing functionality with CSS hex colors."""
    assert _extended_parse("#000000") == Color(
        "#000000", ColorType.TRUECOLOR, triplet=ColorTriplet(0, 0, 0)
    )


def test_parse_3_digit_hex_color():
    """Test the extended color parsing functionality with 3-digit hex colors."""
    assert _extended_parse("#abc") == Color(
        "#aabbcc", ColorType.TRUECOLOR, triplet=ColorTriplet(170, 187, 204)
    )


def test_parse_invalid_colors():
    """Test the extended color parsing functionality with invalid colors."""
    with pytest.raises(ColorParseError):
        _extended_parse("notacolor")


def test_default_color():
    """Test the parsing of the default color."""
    assert _extended_parse("default") == Color("default", ColorType.DEFAULT)
