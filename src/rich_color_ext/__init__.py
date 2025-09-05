from rich.color import Color

from rich_color_ext.main import _extended_parse  # type: ignore[import]


def install() -> None:
    """Install the extended color parser by patching Rich's Color.parse method."""
    Color.parse = _extended_parse  # type: ignore[assignment]


def uninstall() -> None:
    """Uninstall the extended color parser by restoring Rich's original Color.parse method."""
    from rich.color import Color as RichColor  # type: ignore[import]

    RichColor.parse = _extended_parse._original_parse  # type: ignore[assignment,attr-defined]
