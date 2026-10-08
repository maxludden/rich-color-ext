"""Tests to ensure importing the package has no external side-effects.

These tests guard against accidental subprocess or network calls at import
time (e.g. attempting to install dependencies during import).
"""

import importlib
import importlib.util
import subprocess
import sys
from types import ModuleType

import pytest


def _reimport_package() -> ModuleType:
    # Remove package modules from sys.modules to force a fresh import.
    for module_name in list(sys.modules):
        if module_name == "rich_color_ext" or module_name.startswith("rich_color_ext."):
            sys.modules.pop(module_name, None)
    return importlib.import_module("rich_color_ext")


def test_import_does_not_call_subprocess_check_call(monkeypatch):
    """Ensure importing the package does not call subprocess.check_call.

    We patch subprocess.check_call to raise if called; import should succeed
    without invoking it.
    """
    called = []

    def _bad(*_args, **_kwargs):
        called.append(True)
        raise RuntimeError("subprocess.check_call should not be called during import")

    monkeypatch.setattr(subprocess, "check_call", _bad)

    # Import should not raise despite subprocess.check_call being 'dangerous'.
    mod = _reimport_package()
    assert mod is not None
    assert not called, "subprocess.check_call was invoked during import"


def test_import_safe_when_find_spec_returns_none(monkeypatch):
    """Simulate missing dependencies by making find_spec return None and ensure
    no subprocess invocation occurs during import.
    """
    called = []

    def _bad(*_args, **_kwargs):
        called.append(True)
        raise RuntimeError("subprocess.check_call should not be called during import")

    monkeypatch.setattr(subprocess, "check_call", _bad)
    monkeypatch.setattr(importlib.util, "find_spec", lambda name: None)

    mod = _reimport_package()
    assert mod is not None
    assert not called, "subprocess.check_call was invoked during import"


def test_import_is_lightweight_and_does_not_patch():
    """A fresh import leaves Color.parse alone and avoids display-only Rich modules (panel, table, columns)."""
    code = """
import sys
from rich.color import Color
orig = Color.__dict__["parse"]
import rich_color_ext
assert Color.__dict__["parse"] is orig
assert not rich_color_ext.is_installed()
assert not hasattr(rich_color_ext, "CSS_MAP")
for m in ("rich.panel", "rich.table", "rich.columns"):
    assert m not in sys.modules, m
"""
    subprocess.run([sys.executable, "-c", code], check=True)


@pytest.mark.parametrize("kind", ["classmethod", "staticmethod", "function"])
def test_import_when_color_parse_is_already_patched(kind: str) -> None:
    """Importing after another library replaced Color.parse must not fail, and install/uninstall must round-trip."""
    code = f"""
from rich.color import Color, ColorParseError

rich_parse = Color.parse  # Rich's real parser, which the foreign patch wraps

def foreign(*args):
    *_, color = args
    if color == "foreign":
        return Color.from_rgb(1, 2, 3)
    return rich_parse(color)

kind = {kind!r}
attr = {{"classmethod": classmethod, "staticmethod": staticmethod}}.get(kind, lambda f: f)(foreign)
setattr(Color, "parse", attr)

import rich_color_ext as rce  # must not raise at import time

assert Color.__dict__["parse"] is attr and not rce.is_installed()
rce.install()
assert rce.is_installed()
assert Color.parse("#09f").name == "#0099ff"  # fallback still applies
assert Color.parse("rebeccapurple").name == "#663399"
assert Color.parse("foreign").get_truecolor().red == 1  # delegated to the pre-existing parse
try:
    Color.parse("nonsense")
except ColorParseError:
    pass
else:
    raise AssertionError("expected ColorParseError")
rce.uninstall()
assert Color.__dict__["parse"] is attr
"""
    subprocess.run([sys.executable, "-c", code], check=True)
