"""main.py
Extended Color Parsing for Rich Library.
Adds support for:
- 3-digit hexadecimal color codes (e.g., `#abc`).
- CSS color names (e.g., `rebeccapurple`, `mediumslateblue`).
"""

from collections.abc import Sequence
from typing import Any, Dict

from rich.color import Color, ColorParseError, ColorType
from rich.color_triplet import ColorTriplet

from rich_color_ext.css import CSSColors

# Preserve a reference to Rich's original Color.parse (the bound method)
_original_parse = Color.parse

# Load CSS color definitions from JSON file
COLORS: CSSColors = CSSColors()
names = COLORS.names
css_triplet: Dict[str, ColorTriplet] = {
    color.name: color.triplet for color in COLORS.values()
}


def get_css_color_triplet(color_name: str) -> ColorTriplet:
    """Get the RGB triplet for a given CSS color name."""
    color_name = color_name.lower()
    if color_name in names and (css_color := COLORS.get(color_name)):
        return css_color.triplet
    raise ValueError(f"Unknown CSS color name: {color_name}")


def extended_parse(color: Any) -> Color:
    """Extends Color.parse() that handles #RGB and CSS4 names.
    Args:
        color (Any): The color input to parse.
    Returns:
        Color: The parsed Color object.
    Raises:
        ColorParseError: If the color cannot be parsed.
    """
    _input: str = str(color)  # keep for error messages

    # Only normalize when the incoming value is a string. Preserve
    # non-string sequences (e.g., tuples of RGB values) so they can be
    # handled below.
    if isinstance(color, str):
        color = color.lower().strip()

    if color == "default":
        # Default color (no color) passes through
        return Color(color, type=ColorType.DEFAULT)

    elif isinstance(color, ColorTriplet):
        assert isinstance(color, ColorTriplet)
        return Color.from_triplet(color)

    elif isinstance(color, Sequence) and not isinstance(color, str) and len(color) == 3:
        red, green, blue = color
        if all(isinstance(c, int) and 0 <= c <= 255 for c in (red, green, blue)):
            triplet = ColorTriplet(red, green, blue)
            return Color.from_triplet(triplet)
        if all(isinstance(c, float) and 0 <= c <= 1 for c in (red, green, blue)):
            triplet = ColorTriplet(int(red * 255), int(green * 255), int(blue * 255))
            return Color.from_triplet(triplet)
        raise ColorParseError(
            f"{_input!r} is not a valid color: RGB must be an integer between \
                0-255 or a floating-point number between 0-1"
        )
    elif isinstance(color, Sequence) and not isinstance(color, str) and len(color) == 4:
        red, green, blue, _ = color
        if all(isinstance(c, int) and 0 <= c <= 255 for c in (red, green, blue)):
            triplet = ColorTriplet(red, green, blue)
            return Color.from_triplet(triplet)
        elif all(isinstance(c, float) and 0 <= c <= 1 for c in (red, green, blue)):
            triplet = ColorTriplet(int(red * 255), int(green * 255), int(blue * 255))
            return Color.from_triplet(triplet)
    elif isinstance(color, Color):
        return color

    try:
        # First, try Rich's original parser for any supported format/name
        return _original_parse(color)
    except ColorParseError as exc:
        # If we get here, the color was not recognized by Rich. Apply extensions.
        if str(color).startswith("#") and len(color) == 4:
            # 3-digit hex code detected (e.g. "#abc")
            hex_digits = color[1:]  # e.g. "abc"
            expanded_hex = f"#{hex_digits[0] * 2}\
{hex_digits[1] * 2}{hex_digits[2] * 2}"  # -> "aabbcc"
            # Parse the expanded hex code using Rich's original parser
            return _original_parse(expanded_hex)

        if str(color).lower() in COLORS.names:
            # CSS Level 4 or other extended color name
            css_color = COLORS.get(str(color).lower())
            if not css_color:
                raise ColorParseError(f"{_input!r} is not a valid color") from exc
            triplet = css_color.triplet  # e.g. "#663399" for "rebeccapurple"
            return Color(str(color), ColorType.TRUECOLOR, triplet=triplet)
        # If still not recognized, re-raise the parsing error to signal an invalid color
        raise ColorParseError(f"{_input!r} is not a valid color") from exc


# # Create an alias for backwards compatibility
_extended_parse = extended_parse
