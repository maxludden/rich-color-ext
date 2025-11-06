"""scripts/build.py
Build rich-color-ext
"""

from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich.text import Text

console = Console()
dist = Path("dist")
GREY = Style.parse("italic #999999")
WHITE = Style.parse("bold white")
try:
    if dist.exists():
        STYLE = Style.parse("bold #00aa00")
        MSG: Text = Text.assemble(*[
                Text("See the '", style=GREY, end=""),
                Text("dist", style=WHITE, end=""),
                Text("' directory: ", style=GREY, end="\n"),
                Text(f"{dist.resolve()}", style=GREY)

            ],
            justify="center"
        )
        SUBTITLE = Text("Build finished!", style=STYLE)
        console.print(
            Panel(
                MSG,
                title="[bold #00ff00]PyInstaller[/]",
                padding=(1, 4),
                border_style="bold #008800",
                expand=False,
                subtitle=SUBTITLE,
                subtitle_align="right",
            ),
            justify="center"
        )
    else:
        STYLE = Style.parse("bold #aa0000")
        MSG = Text.assemble(
            *[
                Text("No '", style=GREY, end=""),
                Text("dist", style=WHITE, end=""),
                Text("' directory found.", style=GREY)
            ]
        )
        SUBTITLE = Text("Build failed!", style=STYLE)
        console.print(
            Panel(
                MSG,
                title="[bold #ff0000]PyInstaller[/]",
                padding=(1, 2),
                border_style="bold #880000",
                expand=False,
                subtitle=SUBTITLE,
                subtitle_align="right",
            )
        )
except ImportError:
    import os

    if os.path.isdir("dist"):
        print(f"Build finished. See the 'dist' directory: {os.path.abspath('dist')}")
    else:
        print("Build finished. No 'dist' directory found.")
