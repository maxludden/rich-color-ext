"""Generate an SVG example using rich_color_ext."""

from rich.console import Console
from rich.panel import Panel
from rich.terminal_theme import TerminalTheme

from rich_color_ext import install

install()

GRADIENT_TERMINAL_THEME = TerminalTheme(
    background=(0, 0, 0),
    foreground=(255, 255, 255),
    normal=[
        (33, 34, 44),  # rgb(40, 40, 40),
        (255, 85, 85),  # rgb(175, 0, 0),
        (20, 200, 20),  # rgb(0, 175, 0),
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

console.save_svg(
    "example.svg",
    theme=GRADIENT_TERMINAL_THEME,
    title="rich-color-ext",
)
