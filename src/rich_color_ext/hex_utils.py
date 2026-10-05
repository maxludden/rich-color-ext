# rich_color_ext/hex_utils.py
"""rich-color-ext.hex_utils.py

Helpers for handling hex color codes.

"""

__all__: list[str] = ["expand_3digit_hex", "is_3digit_hex", "is_dark", "is_light"]


def expand_3digit_hex(hex3: str) -> str:
    """
    Expand a 3-digit hex string with a leading '#' (e.g. '#ABC') into 6 digits,
    e.g. '#AABBCC'.

    Args:
        hex3: The 3-digit hex string, including the leading '#'.

    Returns:
        A string of format '#RRGGBB'.

    Raises:
        ValueError: If input is not a valid '#'-prefixed 3-digit hex representation.
    """
    hex_str: str = hex3.strip()
    if not is_3digit_hex(hex_str):
        raise ValueError(f"Invalid 3-digit hex colour: {hex3!r}")
    hex_str = hex_str[1:]
    red: str = hex_str[0]
    green: str = hex_str[1]
    blue: str = hex_str[2]
    return f"#{red}{red}{green}{green}{blue}{blue}"


def is_3digit_hex(string: str) -> bool:
    """
    Test whether a string is a '#'-prefixed 3-digit hex colour code (e.g. '#ABC'),
    case-insensitive. Bare words such as 'bad' or 'add' are not hex colours.

    Args:
        string: input string.

    Returns:
        True if matches 3-digit hex format.
    """
    hex_str = string.strip()
    return (
        len(hex_str) == 4
        and hex_str[0] == "#"
        and all(c in "0123456789abcdefABCDEF" for c in hex_str[1:])
    )


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
    r = int(hex_str[0:2], base=16)
    g = int(hex_str[2:4], base=16)
    b = int(hex_str[4:6], base=16)

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
