"""Tests for rich_color_ext.patch."""

from rich.color import Color

from rich_color_ext.patch import install, is_installed, uninstall


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
    assert c1 == Color.parse("red")
    # Rich's ANSI "red" is untouched (not remapped to CSS #ff0000)
    assert c1.name == "red"
    assert Color.parse("#FF0000").name == "#ff0000"


def test_uninstall_patch():
    """Test that uninstalling the patch restores original behavior."""
    install()
    assert is_installed()
    uninstall()
    assert not is_installed()


def test_parse_on_instance_after_install():
    """Regression: the patch must not bind the instance as the color argument."""
    install()
    try:
        assert Color.from_rgb(1, 2, 3).parse("#abc") == Color.parse("#aabbcc")
    finally:
        uninstall()


def test_uninstall_restores_original_classmethod():
    """Uninstall restores Rich's own classmethod, usable from instances too."""
    original = Color.__dict__["parse"]
    install()
    uninstall()
    assert Color.__dict__["parse"] is original
    assert Color.from_rgb(1, 2, 3).parse("red").name == "red"


def test_bare_3digit_words_are_not_colors():
    """Bare hex-looking words must not parse; only '#'-prefixed 3-digit hex does."""
    import pytest
    from rich.color import ColorParseError

    install()
    try:
        for word in ("bad", "add", "09f", "#abcd"):
            with pytest.raises(ColorParseError):
                Color.parse(word)
        assert Color.parse("#09F") == Color.parse("#0099ff")
    finally:
        uninstall()


def test_rich_names_keep_rich_behaviour():
    """Names Rich knows (ANSI) are parsed by Rich first, not remapped to CSS hex."""
    from rich.color import ColorType

    install()
    try:
        assert Color.parse("red").type is ColorType.STANDARD
        assert Color.parse("rebeccapurple").type is ColorType.TRUECOLOR
    finally:
        uninstall()


def test_parse_is_cached():
    """The patched parser is memoised like Rich's."""
    from rich_color_ext.patch import _patched_parse

    _patched_parse.cache_clear()
    _patched_parse("#abc")
    _patched_parse("#abc")
    assert _patched_parse.cache_info().hits == 1


def test_concurrent_install_uninstall_is_consistent():
    """Hammering install/uninstall from threads never leaves a half-state."""
    from concurrent.futures import ThreadPoolExecutor

    def work(i: int) -> None:
        (install if i % 2 else uninstall)()

    with ThreadPoolExecutor(8) as pool:
        list(pool.map(work, range(200)))
    uninstall()
    assert not is_installed()
    assert Color.parse("red").name == "red"
