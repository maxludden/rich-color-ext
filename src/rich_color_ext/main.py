# main.py
from typing import Dict, Any

from rich.color import Color, ColorParseError, ColorType
from rich.color_triplet import ColorTriplet

from rich_color_ext._css import CSSColors # type: ignore[import]

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


def _extended_parse(color: Any) -> Color:
    """Extended Color.parse that handles #RGB and CSS4 names."""
    _original_input = color  # keep for error messages

    if not isinstance(color, str):
        color = str(color)  # sourcery skip: remove-unnecessary-cast
    color = color.lower().strip()

    if color == "default":
        # Default color (no color) passes through
        return Color(color, type=ColorType.DEFAULT)

    if isinstance(color, ColorTriplet):
        assert isinstance(color, ColorTriplet)
        return Color.from_triplet(color)

    elif isinstance(color, tuple) and len(color) == 3:
        r, g, b = color
        if all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b)):
            triplet = ColorTriplet(r, g, b)
            return Color.from_triplet(triplet)
        elif all(isinstance(c, float) and 0 <= c <= 1 for c in (r, g, b)):
            triplet = ColorTriplet(int(r * 255), int(g * 255), int(b * 255))
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
            expanded_hex = f"#{hex_digits[0] * 2}{hex_digits[1] * 2}{hex_digits[2] * 2}"  # -> "aabbcc"
            # Parse the expanded hex code using Rich's original parser
            return _original_parse(expanded_hex)

        if str(color).lower() in COLORS.names:
            # CSS Level 4 or other extended color name
            css_color = COLORS.get(str(color).lower())
            if not css_color:
                raise ColorParseError(f"{_original_input!r} is not a valid color") from exc
            triplet = css_color.triplet  # e.g. "#663399" for "rebeccapurple"
            return Color(str(color), ColorType.TRUECOLOR, triplet=triplet)
        # If still not recognized, re-raise the parsing error to signal an invalid color
        raise ColorParseError(f"{_original_input!r} is not a valid color") from exc


