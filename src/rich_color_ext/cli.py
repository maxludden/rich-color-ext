"""Command-line interface for rich-color-ext.

Provides a tiny CLI to inspect CSS colors and to (un)install the
runtime patch that extends Rich's color parsing.
"""

import argparse
import importlib
import importlib.metadata
import importlib.resources
import json
from functools import lru_cache
from types import ModuleType
from typing import Iterable

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

import rich_color_ext as _pkg
from rich_color_ext.css import CSSColor

_CSS_CACHE: dict[str, str] | None = None


@lru_cache(maxsize=1024)
def get_css_color_map() -> dict[str, str]:
    """Return CSS color mapping with compatibility fallback."""

    global _CSS_CACHE  # pylint: disable=global-statement
    if _CSS_CACHE is not None:
        return _CSS_CACHE

    # Prefer a package-level loader if present (newer layout exposes get_css_map
    # on the package itself).
    pkg_loader = getattr(_pkg, "get_css_map", None)
    if callable(pkg_loader):
        try:
            result = pkg_loader()
            if isinstance(result, dict):
                _CSS_CACHE = {str(k).lower(): str(v) for k, v in result.items()}
            else:
                _CSS_CACHE = {}
            return _CSS_CACHE
        except (TypeError, ValueError, AttributeError, KeyError):
            # fall through to other loaders
            pass
    css_mod: ModuleType | None
    try:
        css_mod = importlib.import_module("rich_color_ext._css_colors")
    except ModuleNotFoundError:  # pragma: no cover - legacy distribution fallback
        css_mod = None
    if css_mod is not None:
        loader = None
        for attr in ("get_css_color_map", "get_css_map"):
            candidate = getattr(css_mod, attr, None)
            if callable(candidate):
                loader = candidate
                break
        if loader is not None:
            result = loader()
            normalized: dict[str, str] = {}
            if isinstance(result, dict):
                normalized = {str(k).lower(): str(v) for k, v in result.items()}
            else:
                items = getattr(result, "items", None)
                if callable(items):
                    for key, value in items():  # type: ignore[call-arg]
                        normalized[str(key).lower()] = str(value)
            _CSS_CACHE = normalized
            return _CSS_CACHE
    try:
        raw = (
            importlib.resources.files("rich_color_ext")
            .joinpath("colors.json")
            .read_text(encoding="utf-8")
        )
    except (FileNotFoundError, ModuleNotFoundError):
        _CSS_CACHE = {}
        return _CSS_CACHE
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        _CSS_CACHE = {}
        return _CSS_CACHE
    if isinstance(data, dict):
        _CSS_CACHE = {str(k).lower(): str(v) for k, v in data.items()}
        return _CSS_CACHE
    if isinstance(data, list):
        mapped: dict[str, str] = {}
        for item in data:
            if isinstance(item, dict):
                name = item.get("name") or item.get("color")
                value = item.get("hex") or item.get("value")
                if isinstance(name, str) and isinstance(value, str):
                    mapped[name.lower()] = value
        _CSS_CACHE = mapped
        return _CSS_CACHE
    _CSS_CACHE = {}
    return _CSS_CACHE


def _resolve_version() -> str:
    """Return package version even if the installed build is older."""

    if hasattr(_pkg, "__version__"):
        return str(_pkg.__version__)
    try:
        return importlib.metadata.version("rich_color_ext")
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


try:
    install = _pkg.install
    is_installed = _pkg.is_installed
    uninstall = _pkg.uninstall
except AttributeError as exc:  # pragma: no cover - legacy fallback guard
    raise RuntimeError(
        "rich_color_ext does not expose install/uninstall helpers; upgrade the package."
    ) from exc


__version__ = _resolve_version()


def list_colors() -> Iterable[str]:
    """List all available CSS color names."""
    css_map = get_css_color_map()
    return sorted(css_map.keys())


def install_panel() -> Panel:
    """Print installation message panel."""
    return Panel(
        "rich-color-ext [b i #99ff00]installed![/]",
        title="[#ffffff]rich-color-ext[/]",
        subtitle="[dim #00ff00]Success[/]",
        border_style="bold #008800",
        expand=False,
        subtitle_align="right",
        padding=(1, 4),
    )


def uninstall_panel() -> Panel:
    """Print uninstallation message panel."""
    return Panel(
        "rich-color-ext [b i #ff0099]uninstalled![/]",
        title="[#ffffff]rich-color-ext[/]",
        subtitle="[dim #ff0000]Restored[/]",
        border_style="bold #880000",
        expand=False,
        subtitle_align="right",
        padding=(1, 4),
    )


def show_color(name: str) -> Panel:
    """Show hex and RGB for a given CSS color name.

    Returns a Rich Panel object for pretty printing.
    """
    color = CSSColor.from_name(name)
    return color.panel()


def _build_table(names: Iterable[str]) -> Table:
    table = Table(
        title="[b yellow]CSS Colors[/b yellow]", show_header=True, expand=False
    )
    table.add_column("sample")
    table.add_column("name")
    table.add_column("hex")
    table.add_column("rgb")
    css_map = get_css_color_map()
    for name in names:
        hex_str = css_map.get(name)
        if not hex_str:
            continue
        r = int(hex_str[1:3], 16)
        g = int(hex_str[3:5], 16)
        b = int(hex_str[5:7], 16)
        table.add_row(
            f"[on {hex_str}]{' ' * 10}[/]",
            f"[b {hex_str}]{name}[/]",
            Text(f" {hex_str} ", style=f"bold on {hex_str}"),
            Text.assemble(*[
                Text("rgb(", style=f"bold {hex_str}"),
                Text(f"{r: >3}", style="bold #FF0000"),
                Text(",", style=f"bold {hex_str}"),
                Text(f"{g: >3}", style="bold #00FF00"),
                Text(",", style=f"bold {hex_str}"),
                Text(f"{b: >3}", style="bold #0000FF"),
                Text(")", style=f"bold {hex_str}"),
            ]),
        )
    return table


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI.

    Args:
        argv: Command-line arguments (default: None, uses sys.argv).

    Returns:
        Exit status code.
    """
    parser = argparse.ArgumentParser(prog="rich-color-ext")
    parser.add_argument("--version", action="store_true", help="Print version and exit")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("install", help="Patch Rich to use the extended color parser")
    sub.add_parser("uninstall", help="Restore Rich's original color parser")

    ls = sub.add_parser("list", help="List available CSS color names")
    ls.add_argument(
        "--limit", type=int, default=0, help="Limit number of names printed"
    )
    ls.add_argument("--pretty", action="store_true", help="Show a pretty table")

    search = sub.add_parser("search", help="Search CSS color names by substring")
    search.add_argument("query", help="Substring to search for (case-insensitive)")
    search.add_argument(
        "--limit", type=int, default=0, help="Limit number of names printed"
    )
    search.add_argument("--pretty", action="store_true", help="Show a pretty table")

    show = sub.add_parser("show", help="Show hex and RGB for a CSS color name")
    show.add_argument("name", help="CSS color name to show")

    args = parser.parse_args(argv)
    console = Console()

    if args.version:
        console.print(
            f"\n[bold #99ff00]rich-color-ext[/] [bold #00ffff]v{__version__}[/]"
        )
        return 0

    if args.command == "install":
        install()
        console.print(install_panel())
        return 0

    if args.command == "uninstall":
        uninstall()
        console.print(uninstall_panel())
        return 0

    if args.command == "list":
        if not is_installed():
            install()
            console.print(install_panel())
        names = list_colors()
        if args.limit and args.limit > 0:
            names = list(names)[: args.limit]
        if getattr(args, "pretty", False):
            table = _build_table(names)
            console.print(table)
        else:
            console.print("[d i]Listing available CSS color names...[/]")
            console.print(", ".join([f"[b {n}]{n}[/]" for n in names]))
        return 0

    if args.command == "search":
        q = args.query.lower()
        all_names = list_colors()
        matches = [n for n in all_names if q in n.lower()]
        if args.limit and args.limit > 0:
            matches = matches[: args.limit]
        if getattr(args, "pretty", False):
            table = _build_table(matches)
            console.print(table)
        else:
            for n in matches:
                console.print(n)
        return 0

    if args.command == "show":
        try:
            panel = show_color(args.name)
        except KeyError:
            console.print(f"Unknown color: {args.name}")
            return 2
        console.print(panel)
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
