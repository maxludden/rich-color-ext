# rich_color_ext/_hex_utils.py
"""
Helpers for handling hex color codes.
"""

__all__ = ["expand_3digit_hex", "is_3digit_hex", "is_dark", "is_light"]


def expand_3digit_hex(hex3: str) -> str:
    """
    Expand a 3-digit hex string (e.g. '#ABC' or 'ABC') into a 6-digit with leading '#',
    e.g. '#AABBCC'.

    Args:
        hex3: The 3-digit hex string including or excluding the '#'.

    Returns:
        A string of format '#RRGGBB'.

    Raises:
        ValueError: If input is not a valid 3-digit hex representation.
    """
    hex_str = hex3.strip()
    if hex_str.startswith("#"):
        hex_str = hex_str[1:]
    if len(hex_str) != 3:
        raise ValueError(f"Invalid 3-digit hex colour: {hex3!r}")
    if any(c not in "0123456789abcdefABCDEF" for c in hex_str):
        raise ValueError(f"Invalid hex digit in {hex3!r}")
    red, green, blue = hex_str[0], hex_str[1], hex_str[2]
    return f"#{red}{red}{green}{green}{blue}{blue}"


def is_3digit_hex(string: str) -> bool:
    """
    Test whether a string is a 3-digit hex colour code (#ABC or ABC) case-insensitive.

    Args:
        string: input string.

    Returns:
        True if matches 3-digit hex format.
    """
    hex_str = string.strip()
    if hex_str.startswith("#"):
        hex_str = hex_str[1:]
    return len(hex_str) == 3 and all(c in "0123456789abcdefABCDEF" for c in hex_str)


def is_dark(hex_str: str) -> bool:
    """
    Determine if a hex colour is 'dark' based on its luminance.

    Args:
        hex_str: A hex colour string of format '#RRGGBB'.
    Returns:
        True if the colour is dark, False otherwise.
    """
    hex_str = hex_str.lstrip("#")
    if len(hex_str) != 6:
        raise ValueError(f"Invalid hex colour: {hex_str!r}")
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    # Calculate luminance using the Rec. 709 formula
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return luminance < 128


def is_light(hex_str: str) -> bool:
    """
    Determine if a hex colour is 'light' based on its luminance.

    Args:
        hex_str: A hex colour string of format '#RRGGBB'.
    Returns:
        True if the colour is light, False otherwise.
    """
    return not is_dark(hex_str)
