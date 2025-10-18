"""Create example.svg"""

from rich.console import Console
from rich.panel import Panel
from rich.terminal_theme import TerminalTheme

from rich_color_ext import install

install()

GRADIENT_TERMINAL_THEME = TerminalTheme(
    background=(0, 0, 0),
    foreground=(255, 255, 255),
    normal=[
        (33, 34, 44),  # rgb(35 35 35),
        (255, 85, 85),  # rgb(254 109 109),
        (20, 200, 20),  # rgb(24 195 24),
        (241, 250, 140),  # rgb(211 208 31),
        (189, 147, 249),  # rgb(122 65 202),
        (255, 121, 198),  # rgb(255 139 205),
        (139, 233, 253),  # rgb(0 115 255),
        (248, 248, 242),  # rgb(245 245 245),
    ],
    bright=[
        (0, 0, 0),  #       rgb(0, 0, 0),
        (255, 0, 0),  #     rgb(255, 0, 0),
        (0, 255, 0),  #     rgb(0, 255, 0),
        (255, 255, 0),  #   rgb(255, 255, 0),
        (214, 172, 255),  # rgb(136, 0, 255),
        (255, 146, 223),  # rgb(255, 0, 255),
        (164, 255, 255),  # rgb(0, 0, 255),
        (255, 255, 255),  # rgb(255, 255, 255),
    ],
)

console = Console(record=True, width=80)
console.line(2)
console.print(
    Panel(
        "This is the [b #00ff99]rich_color_ext[/b #00ff99] \
example for printing CSS named colors ([bold rebeccapurple]\
rebeccapurple[/bold rebeccapurple]), 3-digit hex \
colors ([bold #f0f]#f0f[/bold #f0f]), and [b #99ff00]\
rich.color_triplet.ColorTriplet[/b #99ff00] & [b #00ff00]\
rich.color.Color[/b #00ff00] instances.",
        padding=(1, 2),
    ),
    justify="center",
)

console.line(2)

console.save_svg(
    "example.svg",
    theme=GRADIENT_TERMINAL_THEME,
    title="Rich Color Ext Example",
)
