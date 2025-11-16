"""Tests to ensure importing the package has no external side-effects.

These tests guard against accidental subprocess or network calls at import
time (e.g. attempting to install dependencies during import).
"""

import importlib
import importlib.util
import subprocess
import sys


def _reimport_package():
    # Remove package from sys.modules to force a fresh import.
    sys.modules.pop("rich_color_ext", None)
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
    called = []

    def _bad(*_args, **_kwargs):
        called.append(True)
        raise RuntimeError("subprocess.check_call should not be called during import")

    monkeypatch.setattr(subprocess, "check_call", _bad)
    monkeypatch.setattr(importlib.util, "find_spec", lambda name: None)

    mod = _reimport_package()
    assert mod is not None
    assert not called, "subprocess.check_call was invoked during import"
