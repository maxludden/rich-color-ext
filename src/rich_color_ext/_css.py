from pathlib import Path
from typing import List, Dict
from json import load

from rich.color_triplet import ColorTriplet
from rich.text import Text

__all__ = ["CSSColor", "CSSColors", "get_css_colors"]


COLOR_DATA_PATH = Path(__file__).parent / "colors.json"
with open(COLOR_DATA_PATH, "r") as f:
    CSS_COLOR_MAP: Dict[str, Dict[str, str | int]] = load(f)

class CSSColor:
    """Class to handle CSS color names and their corresponding hex values."""

    def __init__(self, name: str, hex_value: str, red: int, green: int, blue: int):
        self.name: str = name.lower()
        self.hex_value: str = hex_value
        self.red: int = red
        self.green: int = green
        self.blue: int = blue

    def __repr__(self) -> str:
        return f"CSSColor(name={self.name}, hex_value={self.hex_value}, rgb=({self.red}, {self.green}, {self.blue}))"

    @property
    def triplet(self) -> ColorTriplet:
        """Return the RGB triplet for this color."""
        return ColorTriplet(self.red, self.green, self.blue)

    @classmethod
    def from_dict(cls, color: str) -> "CSSColor":
        """Create a CSSColor instance from a dictionary."""
        color_data = CSS_COLOR_MAP.get(color.lower())
        if not color_data:
            raise ValueError(f"Unknown color: {color}")
        name: str = str(color_data["name"])
        hex_value: str = str(color_data["hex"])
        red: int = int(color_data["r"])
        green: int = int(color_data["g"])
        blue: int = int(color_data["b"])
        return cls(name, hex_value, red, green, blue)

    def __rich__(self) -> Text:
        """Return a Rich Text representation of the color."""
        style = f"bold {self.hex_value}"
        return Text.assemble(
            *[
                Text("CSSColor", style="bold cyan"),
                Text("<", style="bold white"),
                Text("name", style="orange"),
                Text("=", style="bold #af00ff"),
                Text(f"{self.name:<20}", style=style),
                Text(", ", style="bold white"),
                Text("hex", style="orange"),
                Text("=", style="bold #af00ff"),
                Text(self.hex_value, style=style),
                Text(", ", style="bold white"),
                Text("rgb", style="orange"),
                Text("=", style="bold #af00ff"),
                Text("rgb", style=style),
                Text("(", style='i #cccccc'),
                Text(f"{self.red:>3}", style="bold #ff0000"),
                Text(",", style='i #cccccc'),
                Text(f"{self.green:>3}", style="bold #00ff00"),
                Text(",", style='i #cccccc'),
                Text(f"{self.blue:>3}", style="bold #0000ff"),
                Text(")", style='i #cccccc'),
                Text(">", style="bold white"),
            ]
        )

def get_css_colors() -> List[CSSColor]:
    """Return a list of all CSS colors defined in the JSON file."""
    return [CSSColor.from_dict(color) for color in CSS_COLOR_MAP.keys()]

class CSSColors(Dict[str, CSSColor]):
    """Dictionary-like class to access CSS colors by name."""

    def __init__(self):
        super().__init__()
        for color in get_css_colors():
            self[color.name] = color

    def __repr__(self) -> str:
        return f"CSSColors({list(self.keys())})"

    def __contains__(self, item: object) -> bool:
        if isinstance(item, str):
            return item.lower() in self.keys()
        return False

    def __getitem__(self, item: str) -> CSSColor:
        if isinstance(item, str):
            key = item.lower()
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
        return [color.hex_value for color in self.values()]

    @property
    def triplets(self) -> List[ColorTriplet]:
        """Return a list of all CSS color RGB triplets."""
        return [color.triplet for color in self.values()]


if __name__ == "__main__":
    CSS_COLORS: CSSColors = CSSColors()
    from rich import print
    for color in CSS_COLORS.values():
        print(color)
