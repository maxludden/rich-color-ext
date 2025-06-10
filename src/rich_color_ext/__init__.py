from rich.color import Color

from rich_color_ext.main import _extended_parse

Color.parse = _extended_parse  # type: ignore[assignment]
