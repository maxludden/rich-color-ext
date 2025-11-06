"""Tests for rich_color_ext.patch."""
from rich.color import Color
from rich_color_ext.patch import is_installed, install, uninstall

def test_patch_installed():
    """Test that the patch can be installed and uninstalled."""
    assert not is_installed()
    install()
    assert is_installed()

def test_parse_3digit_hex():
    """Test parsing of 3-digit hex colour codes."""
    c = Color.parse("#ABC")
    # Should equal Color.parse("#AABBCC")
    assert c == Color.parse("#AABBCC")

def test_parse_css_name():
    """Test parsing of CSS colour names."""
    c = Color.parse("aliceblue")
    assert c == Color.parse("#f0f8ff")

def test_parse_standard():
    """Test that standard color parsing still works."""
    c1 = Color.parse("red")
    c2 = Color.parse("red")
    assert c1 == c2
    # ensure still works with full hex
    c3 = Color.parse("#FF0000")
    assert c3 == c1

def test_uninstall_patch():
    """Test that uninstalling the patch restores original behavior."""
    install()
    assert is_installed()
    uninstall()
    assert not is_installed()
