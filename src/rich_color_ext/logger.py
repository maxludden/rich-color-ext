"""A Rich-based loguru logger sink."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from loguru import logger
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

if TYPE_CHECKING:
    from loguru import Logger

__all__: list[str] = ["get_logger", "install_rich_sink", "log"]

console = Console()
LEVEL_STYLES: dict[str, dict[str, str | int]] = {
    "TRACE": {
        "text": "#FFFFFF",
        "title": "bold #FFFFFF on #00AA82",
        "border": "bold #0051FF",
    },
    "DEBUG": {
        "text": "#B4F1FF",
        "title": "bold #FFFFFF on #009F9F",
        "border": "bold #0099FF",
        "left": 2,
        "right": 1,
    },
    "INFO": {
        "text": "#C6FFC6",
        "title": "bold #FFFFFF on #006A00",
        "border": "bold #00FF00",
        "left": 3,
        "right": 3,
    },
    "WARNING": {
        "text": "#FFFFAC",
        "title": "bold #FFFFFF on #555500",
        "border": "bold #FFFF00",
        "left": 2,
        "right": 1,
    },
    "ERROR": {
        "text": "#FFC4C4",
        "title": "bold #FFFFFF on #550000",
        "border": "bold #FF0000",
        "left": 2,
        "right": 1,
    },
    "CRITICAL": {
        "text": "#FFCAFF",
        "title": "bold #FFFFFF on #A8005A",
        "border": "bold #FF00FF",
        "left": 1,
        "right": 0,
    },
}


def rich_sink(msg: Any) -> None:
    """A Rich-based loguru sink."""
    record = msg.record
    # inspect(record, all=True, console=console, private=True, dunder=True)
    level_name = record["level"].name
    level_icon = record["level"].icon
    file = record["file"].name
    line = record["line"]
    line_str: str = f"Line {line}"
    style: dict[str, str | int] = LEVEL_STYLES[level_name]
    left_pad: str = " " * int(style.get("left", 0))
    right_pad: str = " " * int(style.get("right", 0))
    title_str: str = f"{level_icon} {left_pad}{level_name}{right_pad} \
 {level_icon}  {file:>12}:{line_str:9}"
    title_text = Text(title_str, style=str(style["title"]))
    msg_str = str(record["message"])
    msg_text = Text(msg_str, style=str(style["text"]))
    console.print(
        Panel(
            msg_text,
            title=title_text,
            title_align="left",
            border_style=str(style["border"]),
            padding=(1, 2),
        )
    )


log: Logger = logger.bind(module=__name__)
logger.disable("rich_color_ext")


def get_logger() -> Any:
    """Get the configured loguru logger."""
    return log


def install_rich_sink(level: str = "DEBUG") -> int:
    """Install the Rich loguru sink and return its handler id."""
    logger.enable("rich_color_ext")
    return logger.add(rich_sink, level=level)


if __name__ == "__main__":
    logger.remove()
    install_rich_sink()
    log.debug("This is a debug message.")
    log.info("This is an info message.")
    log.warning("This is a warning message.")
    log.error("This is an error message.")
    log.critical("This is a critical message.")
