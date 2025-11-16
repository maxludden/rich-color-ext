"""CSS color utilities and rich renderables.

This module provides a small convenience wrapper, :class:`CSSColor`, for
working with CSS colour names and their hex/RGB representations, along with
helpers to iterate all known colours. Data comes from ``_css_colors.get_css_map``.
"""

from collections.abc import Generator
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

from rich.align import Align
from rich.color_triplet import ColorTriplet
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.traceback import install as tr_install

from rich_color_ext.logger import log

__all__ = ["CSSColor", "CSSColors", "get_css_map"]

tr_install()

# Console is only required for the demonstration block at module run-time.


@lru_cache(maxsize=1024)
def get_css_map() -> dict[str, str]:
    """
    Return the mapping of CSS colour name (lowercase) → hex string (‘#RRGGBB’).
    Loads the data on first call.

    Returns:
        Dict mapping colour name to hex.
    """
    css_map = {
        "aliceblue": "#f0f8ff",
        "antiquewhite": "#faebd7",
        "aqua": "#00ffff",
        "aquamarine": "#7fffd4",
        "azure": "#f0ffff",
        "beige": "#f5f5dc",
        "bisque": "#ffe4c4",
        "black": "#000000",
        "blanchedalmond": "#ffebcd",
        "blue": "#0000ff",
        "blueviolet": "#8a2be2",
        "brown": "#a52a2a",
        "burlywood": "#deb887",
        "cadetblue": "#5f9ea0",
        "chartreuse": "#7fff00",
        "chocolate": "#d2691e",
        "coral": "#ff7f50",
        "cornflowerblue": "#6495ed",
        "cornsilk": "#fff8dc",
        "crimson": "#dc143c",
        "cyan": "#00ffff",
        "darkblue": "#00008b",
        "darkcyan": "#008b8b",
        "darkgoldenrod": "#b8860b",
        "darkgray": "#a9a9a9",
        "darkgreen": "#006400",
        "darkgrey": "#a9a9a9",
        "darkkhaki": "#bdb76b",
        "darkmagenta": "#8b008b",
        "darkolivegreen": "#556b2f",
        "darkorange": "#ff8c00",
        "darkorchid": "#9932cc",
        "darkred": "#8b0000",
        "darksalmon": "#e9967a",
        "darkseagreen": "#8fbc8f",
        "darkslateblue": "#483d8b",
        "darkslategray": "#2f4f4f",
        "darkslategrey": "#2f4f4f",
        "darkturquoise": "#00ced1",
        "darkviolet": "#9400d3",
        "deeppink": "#ff1493",
        "deepskyblue": "#00bfff",
        "dimgray": "#696969",
        "dimgrey": "#696969",
        "dodgerblue": "#1e90ff",
        "firebrick": "#b22222",
        "floralwhite": "#fffaf0",
        "forestgreen": "#228b22",
        "fuchsia": "#ff00ff",
        "gainsboro": "#dcdcdc",
        "ghostwhite": "#f8f8ff",
        "gold": "#ffd700",
        "goldenrod": "#daa520",
        "gray": "#808080",
        "green": "#008000",
        "greenyellow": "#adff2f",
        "grey": "#808080",
        "honeydew": "#f0fff0",
        "hotpink": "#ff69b4",
        "indianred": "#cd5c5c",
        "indigo": "#4b0082",
        "ivory": "#fffff0",
        "khaki": "#f0e68c",
        "lavender": "#e6e6fa",
        "lavenderblush": "#fff0f5",
        "lawngreen": "#7cfc00",
        "lemonchiffon": "#fffacd",
        "lightblue": "#add8e6",
        "lightcoral": "#f08080",
        "lightcyan": "#e0ffff",
        "lightgoldenrodyellow": "#fafad2",
        "lightgray": "#d3d3d3",
        "lightgreen": "#90ee90",
        "lightgrey": "#d3d3d3",
        "lightpink": "#ffb6c1",
        "lightsalmon": "#ffa07a",
        "lightseagreen": "#20b2aa",
        "lightskyblue": "#87cefa",
        "lightslategray": "#778899",
        "lightslategrey": "#778899",
        "lightsteelblue": "#b0c4de",
        "lightyellow": "#ffffe0",
        "lime": "#00ff00",
        "limegreen": "#32cd32",
        "linen": "#faf0e6",
        "magenta": "#ff00ff",
        "maroon": "#800000",
        "mediumaquamarine": "#66cdaa",
        "mediumblue": "#0000cd",
        "mediumorchid": "#ba55d3",
        "mediumpurple": "#9370db",
        "mediumseagreen": "#3cb371",
        "mediumslateblue": "#7b68ee",
        "mediumspringgreen": "#00fa9a",
        "mediumturquoise": "#48d1cc",
        "mediumvioletred": "#c71585",
        "midnightblue": "#191970",
        "mintcream": "#f5fffa",
        "mistyrose": "#ffe4e1",
        "moccasin": "#ffe4b5",
        "navajowhite": "#ffdead",
        "navy": "#000080",
        "oldlace": "#fdf5e6",
        "olive": "#808000",
        "olivedrab": "#6b8e23",
        "orange": "#ffa500",
        "orangered": "#ff4500",
        "orchid": "#da70d6",
        "palegoldenrod": "#eee8aa",
        "palegreen": "#98fb98",
        "paleturquoise": "#afeeee",
        "palevioletred": "#db7093",
        "papayawhip": "#ffefd5",
        "peachpuff": "#ffdab9",
        "peru": "#cd853f",
        "pink": "#ffc0cb",
        "plum": "#dda0dd",
        "powderblue": "#b0e0e6",
        "purple": "#800080",
        "rebeccapurple": "#663399",
        "red": "#ff0000",
        "rosybrown": "#bc8f8f",
        "royalblue": "#4169e1",
        "saddlebrown": "#8b4513",
        "salmon": "#fa8072",
        "sandybrown": "#f4a460",
        "seagreen": "#2e8b57",
        "seashell": "#fff5ee",
        "sienna": "#a0522d",
        "silver": "#c0c0c0",
        "skyblue": "#87ceeb",
        "slateblue": "#6a5acd",
        "slategray": "#708090",
        "slategrey": "#708090",
        "snow": "#fffafa",
        "springgreen": "#00ff7f",
        "steelblue": "#4682b4",
        "tan": "#d2b48c",
        "teal": "#008080",
        "thistle": "#d8bfd8",
        "tomato": "#ff6347",
        "turquoise": "#40e0d0",
        "violet": "#ee82ee",
        "wheat": "#f5deb3",
        "white": "#ffffff",
        "whitesmoke": "#f5f5f5",
        "yellow": "#ffff00",
        "yellowgreen": "#9acd32",
    }
    return css_map


# ------------------------------
# Internal helpers
# ------------------------------
def _normalize_name(value: str) -> str:
    """Normalize a CSS colour name: strip spaces/dashes and lowercase."""
    value = value.replace(" ", "").replace("-", "").strip().lower()
    return value


def _normalize_hex(value: str) -> str:
    """Normalize hex strings to canonical ``#RRGGBB``.

    Accepts forms like ``#abc``, ``abc``, ``#aabbcc`` or ``aabbcc``.
    Raises ValueError for invalid lengths.
    """
    if isinstance(value, str):
        value = value.strip()
    if value.startswith("#"):
        value = value[1:]
    if len(value) == 3:
        value = value[0] * 2 + value[1] * 2 + value[2] * 2
    elif len(value) != 6:
        raise ValueError(
            "Hex value must be a string in the format '#RGB' or '#RRGGBB'."
        )
    # Validate hex characters and return in canonical uppercase with leading '#'
    int(value, 16)  # will raise ValueError if not hex
    return f"#{value.upper()}"


def _find_name_by_hex(hex_value: str, css_map: dict[str, str]) -> Optional[str]:
    """Return the first colour name mapping to ``hex_value`` (case-insensitive)."""
    hex_low = hex_value.lower()
    return next((k for k, v in css_map.items() if v.lower() == hex_low), None)


def _hex_from_rgb(red: int, green: int, blue: int) -> str:
    return f"#{red:02X}{green:02X}{blue:02X}"


class CSSColor:
    """Class to handle CSS color names and their corresponding hex values."""

    def __init__(
        self,
        name: Optional[str] = None,
        hex: Optional[str] = None,  # pylint:disable=W0622
        red: Optional[int] = None,
        green: Optional[int] = None,
        blue: Optional[int] = None,
    ) -> None:
        """Create a CSSColor.

        You may provide any combination of name/hex/RGB sufficient to derive the
        remaining attributes. Values are normalised and validated.
        """
        log.debug(f"Creating CSSColor({name=}, {hex=}, {red=}, {green=}, {blue=})")

        self._name = ""
        self._hex = ""
        self._red = -1
        self._green = -1
        self._blue = -1

        # Apply provided values through property setters to keep invariants.
        if name is not None:
            self.name = name
        if hex is not None:
            self.hex = hex
        # Only set numeric channels if caller provided them (None means omitted)
        if red is not None:
            self.red = red
        if green is not None:
            self.green = green
        if blue is not None:
            self.blue = blue

        # Fill missing values when possible
        if self._name and not self._hex and self._name in get_css_map():
            self.hex = get_css_map()[self._name]

        if self._hex and (self._red < 0 or self._green < 0 or self._blue < 0):
            r, g, b = self.hex_to_rgb(self._hex)
            self._red, self._green, self._blue = r, g, b

        if not self._name and self._hex:
            css_map = get_css_map() or get_css_map()
            derived = _find_name_by_hex(self._hex, css_map)
            if derived:
                self._name = derived

        # Final validation
        if (
            not self._name
            or not self._hex
            or any(v < 0 or v > 255 for v in (self._red, self._green, self._blue))
        ):
            raise ValueError("Unable to determine color.")

    @classmethod
    def from_name(
        cls, name: str, css_map: Optional[dict[str, str]] = None
    ) -> "CSSColor":
        """Create a CSSColor instance from a color name."""
        if not name:
            raise ValueError("Name must be a non-empty string.")
        css_map = css_map or get_css_map()
        norm = _normalize_name(name)
        log.debug(f"Creating CSSColor from name: name={norm!r}")
        hex_value = css_map.get(norm)
        if not hex_value:
            raise ValueError(f"Unknown color name: {name}")
        red, green, blue = cls.hex_to_rgb(hex_value)
        return cls(name=norm, hex=hex_value, red=red, green=green, blue=blue)

    @classmethod
    def from_hex(cls, hex: str, css_map: Optional[dict[str, str]] = None) -> "CSSColor":  # pylint:disable=W0622
        """Create a CSSColor instance from a hex value."""
        if not hex:
            raise ValueError("Hex value must be a non-empty string.")
        css_map = css_map or get_css_map() or get_css_map()
        norm_hex = _normalize_hex(hex)
        name = _find_name_by_hex(norm_hex, css_map)
        if name is None:
            raise ValueError(f"Unknown hex value: {hex}")
        red, green, blue = cls.hex_to_rgb(norm_hex)
        return cls(name=name, hex=norm_hex, red=red, green=green, blue=blue)

    @classmethod
    def from_rgb(
        cls,
        red: int,
        green: int,
        blue: int,
        css_map: Optional[dict[str, str]] = None,
    ) -> "CSSColor":
        """Create a CSSColor instance from RGB values."""
        for channel, label in ((red, "red"), (green, "green"), (blue, "blue")):
            if not 0 <= channel <= 255:
                raise ValueError(
                    f"{label.capitalize()} value must be between 0 and 255."
                )
        css_map = css_map or get_css_map() or get_css_map()
        hex_str = _hex_from_rgb(red, green, blue)
        name = _find_name_by_hex(hex_str, css_map)
        if name is None:
            raise ValueError(f"Unknown RGB values: ({red}, {green}, {blue})")
        return cls(name=name, hex=hex_str, red=red, green=green, blue=blue)

    def __str__(self) -> str:
        """Return the name of the color.
        Returns:
            str: The name of the color."""
        return f"{self.name}"

    def __repr__(self) -> str:
        return (
            f"CSSColor(name={self.name}, hex={self.hex}, "
            f"rgb=({self.red}, {self.green}, {self.blue}))"
        )

    @staticmethod
    def hex_to_rgb(hex_str: str) -> Tuple[int, int, int]:
        """Return the RGB components as a tuple.
        Returns:
            Tuple[int, int, int]: The RGB components.
        """
        log.debug(f"Converting hex to RGB: hex_str={hex_str!r}")
        norm = _normalize_hex(hex_str)
        val = norm.lstrip("#")
        red, green, blue = (int(val[i : i + 2], 16) for i in (0, 2, 4))
        log.debug(f"Converted hex {norm} to RGB: red={red}, green={green}, blue={blue}")
        return (red, green, blue)

    @property
    def name(self) -> str:
        """Return the name of the color."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the name of the color."""
        log.debug(f"Setting name to: {value!r}")
        self._name = _normalize_name(value)
        if self._name in get_css_map() and not self._hex:
            self.hex = get_css_map()[self._name]
            log.debug(f"Set hex from name: {self.hex=}")
        if self._hex and any(v < 0 for v in (self._red, self._green, self._blue)):
            red, green, blue = self.hex_to_rgb(self._hex)
            self._red, self._green, self._blue = red, green, blue
            log.debug(f"Set RGB from hex: {self._red=}, {self._green=}, {self._blue=}")

    @property
    def hex(self) -> str:
        """Return the hex representation of the color."""
        log.debug(f"Getting hex: {self._hex=}")
        return self._hex

    @hex.setter
    def hex(self, value: str) -> None:
        """Set the hex representation of the color."""
        log.debug(f"Setting hex to: {value!r}")
        self._hex = _normalize_hex(value)
        if any(v < 0 for v in (self._red, self._green, self._blue)):
            red, green, blue = self.hex_to_rgb(self._hex)
            self._red, self._green, self._blue = red, green, blue
        if not self._name:
            css_map = get_css_map() or get_css_map()
            name = _find_name_by_hex(self._hex, css_map)
            if name:
                self._name = name

    @property
    def red(self) -> int:
        """Return the red component of the color."""
        log.debug(f"Getting red: {self._red=}")
        return self._red

    @red.setter
    def red(self, value: int) -> None:
        """Set the red component of the color."""
        log.debug(f"Setting red to: {value}")
        if 0 <= value <= 255:
            self._red = value
        else:
            raise ValueError("Red value must be between 0 and 255.")
        if self._green >= 0 and self._blue >= 0:
            hex_str = _hex_from_rgb(self._red, self._green, self._blue)
            self.hex = hex_str
            if not self._name:
                css_map = get_css_map() or get_css_map()
                name = _find_name_by_hex(self._hex, css_map)
                if name:
                    self._name = name

    @property
    def green(self) -> int:
        """Return the green component of the color."""
        log.debug(f"Getting green: {self._green=}")
        return self._green

    @green.setter
    def green(self, value: int) -> None:
        """Set the green component of the color."""
        log.debug(f"Setting green to: {value}")
        if 0 <= value <= 255:
            self._green = value
        else:
            raise ValueError("Green value must be between 0 and 255.")
        if self._red >= 0 and self._blue >= 0:
            hex_str = _hex_from_rgb(self._red, self._green, self._blue)
            self.hex = hex_str
            if not self._name:
                css_map = get_css_map() or get_css_map()
                name = _find_name_by_hex(self._hex, css_map)
                if name:
                    self._name = name

    @property
    def blue(self) -> int:
        """Return the blue component of the color."""
        log.debug(f"Getting blue: {self._blue=}")
        return self._blue

    @blue.setter
    def blue(self, value: int) -> None:
        """Set the blue component of the color."""
        log.debug(f"Setting blue to: {value}")
        if 0 <= value <= 255:
            self._blue = value
        else:
            raise ValueError("Blue value must be between 0 and 255.")
        if self._red >= 0 and self._green >= 0:
            hex_str = _hex_from_rgb(self._red, self._green, self._blue)
            self.hex = hex_str
            if not self._name:
                css_map = get_css_map() or get_css_map()
                name = _find_name_by_hex(self._hex, css_map)
                if name:
                    self._name = name

    def rich(self, reverse: bool = False) -> Text:
        """Return a Rich Text representation of the color."""
        class_style = f"bold {self.hex}" if not reverse else f"bold on {self.hex}"
        color_style = f"bold on {self.hex}" if reverse else f"bold {self.hex}"
        label_style = f"bold black on {self.hex}" if reverse else "bold white"
        return Text.assemble(*[
            Text("CSSColor", style=class_style),
            Text("<", style=color_style),
            Text("hex=", style=label_style),
            Text(f"'{self.hex}'", style=color_style),
            Text(", rgb='", style=label_style),
            self.rgb(reverse),
            Text(", name=", style=label_style),
            Text(f"{self.name!r}'", style=color_style),
            Text(">", style=color_style),
        ])

    def __rich__(self) -> Text:
        """Return a Rich Text representation of the color."""
        return self.rich()

    def rgb(self, reverse: bool = False) -> Text:
        """Return a Rich Text representation of the RGB values."""
        style = f"bold {self.hex}" if not reverse else f"bold on {self.hex}"
        red_style = "bold #AA0000" if not reverse else f"bold #AA0000 on {self.hex}"
        green_style = "bold #00AA00" if not reverse else f"bold #00AA00 on {self.hex}"
        blue_style = "bold #00AAFF" if not reverse else f"bold #00AAFF on {self.hex}"

        rgb = Text.assemble(*[
            Text("rgb(", style=style),
            Text(f"{self.red}", style=red_style),
            Text(",", style=style),
            Text(f"{self.green}", style=green_style),
            Text(",", style=style),
            Text(f"{self.blue}", style=blue_style),
            Text(")", style=style),
        ])
        return rgb

    def panel(self) -> Panel:
        """Return a Rich Table representation of the color."""
        table = Table(
            show_header=False,
            show_edge=False,
            show_lines=False,
            pad_edge=True,
            collapse_padding=False,
            border_style=f"bold {self.hex}",
        )

        table.add_column("Hex")
        table.add_column("RGB")
        table.add_row(
            Text(self.hex, style=f"bold {self.hex}"), Align(self.rgb(), align="center")
        )
        return Panel(
            table,
            title=f"[bold on {self.hex}] {self.name.capitalize()} [/bold on {self.hex}]",
            border_style=f"bold {self.hex}",
            expand=False,
            padding=(1, 4),
        )

    @property
    def triplet(self) -> ColorTriplet:
        """Return the RGB triplet for this color."""
        return ColorTriplet(self.red, self.green, self.blue)


def get_css_colors(
    css_map: Optional[dict[str, str]] = None,
) -> Generator[CSSColor, None, None]:
    """Return a list of all CSS colors defined in the JSON file."""
    if css_map is None:
        css_map = get_css_map() or get_css_map()
    yield from (CSSColor.from_name(color, css_map) for color in css_map)


class CSSColors(Dict[str, CSSColor]):
    """Dictionary-like class to access CSS colors by name."""

    def __init__(self):
        super().__init__()
        for color in get_css_colors():
            self[color.name] = color

    def __repr__(self) -> str:
        return f"CSSColors({list(self.keys())})"

    def __contains__(self, item: object) -> bool:
        if not isinstance(item, str):
            return False
        key = _normalize_name(item)
        return key in self.keys()

    def __getitem__(self, item: str) -> CSSColor:
        if isinstance(item, str):
            key = _normalize_name(item)
            if key in self:
                return super().__getitem__(key)
            raise KeyError(item)
        raise KeyError(item)

    @property
    def names(self) -> List[str]:
        """Return a list of all CSS color names."""
        return list(self.keys())

    @property
    def hex_values(self) -> List[str]:
        """Return a list of all CSS color hex values."""
        return [color.hex for color in self.values()]

    @property
    def triplets(self) -> List[ColorTriplet]:
        """Return a list of all CSS color RGB triplets."""
        return [color.triplet for color in self.values()]


if __name__ == "__main__":  # pragma: no cover
    from rich.console import Console  # pylint:disable=C0412

    css_colors = CSSColors()
    console = Console()
    console.print(
        Columns(
            [color.panel() for color in css_colors.values()],
            equal=False,
            padding=(0, 0),
        )
    )
