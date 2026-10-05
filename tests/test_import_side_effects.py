"""Tests to ensure importing the package has no external side-effects.

These tests guard against accidental subprocess or network calls at import
time (e.g. attempting to install dependencies during import).
"""

import importlib
import importlib.util
import subprocess
import sys
from types import ModuleType


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
