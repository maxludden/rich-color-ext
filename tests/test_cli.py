"""Tests for rich_color_ext.cli module."""
import os
import subprocess
import sys
from pathlib import Path


def run_module(args):
    """Run the rich_color_ext.cli module with given arguments."""
    cmd = [sys.executable, "-m", "rich_color_ext.cli"] + args
    env = os.environ.copy()
    # ensure subprocess can import package from local src/ during tests
    repo_root = Path(__file__).resolve().parents[1]
    src_path = str(repo_root / "src")
    env["PYTHONPATH"] = src_path + (os.pathsep + env.get("PYTHONPATH", ""))
    return subprocess.run(cmd, check=False, capture_output=True, text=True, env=env)


def test_version():
    """Test that the --version command works."""
    res = run_module(["--version"])
    assert res.returncode == 0
    assert res.stdout.strip() != ""


def test_list_pretty_limit():
    """Test the 'list' command with pretty output and limit."""
    # request a small pretty table and ensure header appears
    res = run_module(["list", "--pretty", "--limit", "3"])
    assert res.returncode == 0
    out = res.stdout.lower()
    assert "name" in out
    assert "hex" in out
    assert "rgb" in out


def test_search_found():
    """Test the 'search' command finds expected colors."""
    # search for 'red' which should match at least 'red' and 'darkred'
    res = run_module(["search", "red", "--limit", "5"])
    assert res.returncode == 0
    assert "red" in res.stdout.lower()
