import rich_color_ext
from rich.console import Console
from rich.panel import Panel
from rich_gradient.theme import  GRADIENT_TERMINAL_THEME

console = Console(record=True, width=60)
console.line(2)
console.print(
    Panel(
        "This is the rich_color_ext example for printing CSS named colors like, \
[bold rebeccapurple]rebeccapurple[/bold rebeccapurple] and 3-digit hex \
colors like, [bold #f0f]#f0f[/bold #f0f].",
        padding=(1,2),
    )
)
console.line(2)

console.save_svg(
    "example.svg",
    theme=GRADIENT_TERMINAL_THEME,
    title="Rich Color Ext Example",)
