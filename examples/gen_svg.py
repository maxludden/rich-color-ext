"""Generate the README/docs SVG example using rich_color_ext.

Usage:
    uv run python examples/gen_svg.py [OUTPUT_PATH]

Writes ``docs/img/example.svg`` by default.
"""

import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.terminal_theme import TerminalTheme

from rich_color_ext import install, uninstall

DEFAULT_OUTPUT: Path = Path(__file__).resolve().parent.parent / "docs" / "img" / "example.svg"

TERMINAL_THEME = TerminalTheme(
    background=(0, 0, 0),
    foreground=(255, 255, 255),
    normal=[
        (33, 34, 44),  #    rgb(40, 40, 40),
        (255, 85, 85),  #   rgb(175, 0, 0),
        (20, 200, 20),  #   rgb(0, 175, 0),
        (241, 250, 140),  # rgb(220, 220, 0),
        (189, 147, 249),  # rgb(0, 125, 255),
        (255, 121, 198),  # rgb(205, 0, 205),
        (139, 233, 253),  # rgb(0, 188, 188),
        (248, 248, 242),  # rgb(235, 235, 235),
    ],
    bright=[
        (0, 0, 0),  #       rgb(0, 0, 0),
        (255, 0, 0),  #     rgb(255, 0, 0),
        (0, 255, 0),  #     rgb(0, 255, 0),
        (255, 255, 0),  #   rgb(255, 255, 0),
        (214, 172, 255),  # rgb(0, 85, 255),
        (255, 146, 223),  # rgb(255, 0, 255),
        (164, 255, 255),  # rgb(0, 255, 255),
        (255, 255, 255),  # rgb(255, 255, 255),
    ],
)


def main(output: Path = DEFAULT_OUTPUT) -> None:
    """Render the example panel and save it as an SVG."""
    install()  # Patch Rich's Color.parse: 3-digit hex and CSS names as a fallback.
    try:
        console = Console(record=True, width=64)
        console.line(2)
        console.print(
            Panel(
                "This is the [b #0f9]rich_color_ext[/b #0f9] \
example for printing CSS named colors ([bold rebeccapurple]\
rebeccapurple[/bold rebeccapurple]), 3-digit hex \
colors ([bold #f0f]#f0f[/bold #f0f]), and [b #9f0]\
rich.color_triplet.ColorTriplet[/b #9f0] & [b #0f0]\
rich.color.Color[/b #0f0] instances.",
                padding=(1, 4),
            ),
            justify="center",
        )
        console.line(2)
        console.save_svg(str(output), theme=TERMINAL_THEME, title="rich-color-ext")
    finally:
        uninstall()


if __name__ == "__main__":

    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT)
