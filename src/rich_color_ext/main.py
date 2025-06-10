# main.py
from typing import Dict, Optional

from rich.color import Color, ColorParseError, ColorType
from rich.color_triplet import ColorTriplet

from rich_color_ext._css import CSSColors, CSSColor

# Preserve a reference to Rich's original Color.parse (the bound method)
_original_parse = Color.parse

# Load CSS color definitions from JSON file
Colors: CSSColors = CSSColors()
names = Colors.names
css_triplet: Dict[str, ColorTriplet] = {color.name: color.triplet for color in Colors.values()}

def get_css_color_triplet(color_name: str) -> ColorTriplet:
    """Get the RGB triplet for a given CSS color name."""
    color_name = color_name.lower()
    if color_name in names:
        css_color: Optional[CSSColor] = Colors.get(color_name)
        if css_color:
            return css_color.triplet
    raise ValueError(f"Unknown CSS color name: {color_name}")

def _extended_parse(color: str) -> Color:
    """Extended Color.parse that handles #RGB and CSS4 names."""
    _original_input = color  # keep for error messages
    color = color.lower().strip()
    if color == "default":
        # Default color (no color) passes through
        return Color(color, type=ColorType.DEFAULT)
    try:
        # First, try Rich's original parser for any supported format/name
        return _original_parse(color)
    except ColorParseError:
        # If we get here, the color was not recognized by Rich. Apply extensions.
        if color.startswith("#") and len(color) == 4:
            # 3-digit hex code detected (e.g. "#abc")
            hex_digits = color[1:]  # e.g. "abc"
            expanded_hex = f"#{hex_digits[0] * 2}{hex_digits[1] * 2}{hex_digits[2] * 2}"  # -> "aabbcc"
            # Parse the expanded hex code using Rich's original parser
            return _original_parse(expanded_hex)

        if color.lower() in Colors.names:
            # CSS Level 4 or other extended color name
            css_color = Colors.get(color)
            if not css_color:
                raise ColorParseError(f"{_original_input!r} is not a valid color")
            triplet = css_color.triplet # e.g. "#663399" for "rebeccapurple"
            return Color(color, ColorType.TRUECOLOR, triplet=triplet)
        # If still not recognized, re-raise the parsing error to signal an invalid color
        raise ColorParseError(f"{_original_input!r} is not a valid color")

# Automatically patch Rich's Color parser when this module is imported
# Color.parse = _extended_parse  # type: ignore[assignment]



