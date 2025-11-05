"""CSS Color Names Extension for Rich"""

from json import load
from pathlib import Path
from typing import Dict, List

from rich.align import Align
from rich.color_triplet import ColorTriplet
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

__all__ = ["CSSColor", "CSSColors", "get_css_colors"]


COLOR_DATA_PATH = Path(__file__).parent / "colors.json"
with open(COLOR_DATA_PATH, "r", encoding="utf-8") as f:
    CSS_COLOR_MAP: Dict[str, Dict[str, str | int]] = load(f)


class CSSColor:
    """Class to handle CSS color names and their corresponding hex values."""

    def __init__(self, name: str, hex_value: str, red: int, green: int, blue: int):
        self.name: str = name.lower()
        self.hex: str = hex_value
        self.red: int = red
        self.green: int = green
        self.blue: int = blue

    def __str__(self) -> str:
        """Return the name of the color.
        Returns:
            str: The name of the color."""
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"CSSColor(name={self.name}, hex_value={self.hex}, \
            rgb=({self.red}, {self.green}, {self.blue}))"

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
            title=f"[bold {self.hex}]{self.name.capitalize()}[/bold {self.hex}]",
            border_style=f"bold {self.hex}",
        )

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
        return item.lower() in self.keys() if isinstance(item, str) else False

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
        return [color.hex for color in self.values()]

    @property
    def triplets(self) -> List[ColorTriplet]:
        """Return a list of all CSS color RGB triplets."""
        return [color.triplet for color in self.values()]


if __name__ == "__main__":
    from rich.columns import Columns

    console = Console()
    css_colors = CSSColors()
    console.print(
        Columns(
            [color.panel() for color in css_colors.values()],
            equal=False,
            padding=(0, 0),
        )
    )

    # for c in CSSColors().values():
    #     rprint(c)
