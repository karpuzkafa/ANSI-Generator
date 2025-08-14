import ctypes
import os

# 8/16 color palettes
text_color_palette = {
    "black": 30, "red": 31, "green": 32, "yellow": 33,
    "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
    "bright_black": 90, "bright_red": 91, "bright_green": 92, "bright_yellow": 93,
    "bright_blue": 94, "bright_magenta": 95, "bright_cyan": 96, "bright_white": 97
}

bg_color_palette = {
    "black": 40, "red": 41, "green": 42, "yellow": 43,
    "blue": 44, "magenta": 45, "cyan": 46, "white": 47,
    "bright_black": 100, "bright_red": 101, "bright_green": 102, "bright_yellow": 103,
    "bright_blue": 104, "bright_magenta": 105, "bright_cyan": 106, "bright_white": 107
}

RESET = "\033[0m"

def ansi(
    text_color: str | list | tuple = "",
    bg_color: str | list | tuple = "",
    use_rgb: bool = False,
    color_mode: str = None,
    lcolor_mode: list = None,
    bold: bool = False,
    italic: bool = False,
    under_line: bool = False,
    blink: bool = False,
    reverse: bool = False,
    dim: bool = False,
    strike: bool = False
) -> str::
    """
    Generate ANSI escape codes for terminal text styling with flexible color modes and text effects.

    This function constructs ANSI escape sequences to apply foreground (text) and background colors, 
    as well as text attributes like bold, italic, underline, blink, reverse, dim, and strikethrough. 
    It supports multiple color modes including the 8/16 basic colors, 256-color palette, and true-color (24-bit RGB). 
    Both RGB tuples and hexadecimal color codes are accepted for high-color modes.
    
    Parameters
    ----------
    text_color : str | list | tuple, optional
        Foreground color.
        - For `"8/16"` mode: specify a color name from the predefined palette (`black`, `red`, `green`, `bright_blue`, etc.).
        - For `"256"` or `"true_color"`: specify either:
            - Hex string (e.g., "#FF8800") 
            - RGB list or tuple (e.g., [255, 136, 0] or (255, 136, 0)) if `use_rgb=True`.

    bg_color : str | list | tuple, optional
        Background color. Follows the same rules as `text_color`.

    use_rgb : bool, default=False
        If True, interprets `text_color` and `bg_color` as RGB values (list or tuple of three integers).

    color_mode : str, optional
        Global color mode applied to both text and background. Possible values:
        - `"8/16"` — use basic color palette
        - `"256"` — use 256-color mode
        - `"true_color"` — use 24-bit RGB color mode
        Ignored if `lcolor_mode` is specified.

    lcolor_mode : list, optional
        List specifying individual color modes `[text_mode, bg_mode]` for text and background, overriding `color_mode`.

    bold : bool, default=False
        Apply bold formatting.

    italic : bool, default=False
        Apply italic formatting (may not be supported in all terminals).

    under_line : bool, default=False
        Underline the text.

    blink : bool, default=False
        Make text blink (rarely supported; may display as bold).

    reverse : bool, default=False
        Swap foreground and background colors.

    dim : bool, default=False
        Dim the text appearance.

    strike : bool, default=False
        Apply strikethrough effect.

    Returns
    -------
    str
        ANSI escape sequence string. Concatenate with your text and reset formatting using `RESET`.

    Raises
    ------
    ValueError
        Raised if:
        - `color_mode` or `lcolor_mode` is not specified or invalid
        - `text_color` or `bg_color` does not match the selected mode
        - RGB values are not a list/tuple of three integers
        - Hex color code does not start with '#'

    8/16 Color Palette
    ------------------
    \033[30mblack\033[0m\t\033[90mbright_black\033[0m
    \033[31mred\033[0m\t\033[91mbright_red\033[0m
    \033[32mgreen\033[0m\t\033[92mbright_green\033[0m
    \033[33myellow\033[0m\t\033[93mbright_yellow\033[0m
    \033[34mblue\033[0m\t\033[94mbright_blue\033[0m
    \033[35mmagenta\033[0m\t\033[95mbright_magenta\033[0m
    \033[36mcyan\033[0m\t\033[96mbright_cyan\033[0m
    \033[37mwhite\033[0m\t\033[97mbright_white\033[0m


    Examples
    --------
    Basic 8/16 color usage:
    >>> print(ansi("red", "black", color_mode="8/16") + "Hello" + RESET)

    Using 256-color mode with RGB:
    >>> print(ansi([255, 136, 0], [0, 68, 255], use_rgb=True, color_mode="256") + "Hello" + RESET)

    True-color (24-bit) with hex strings:
    >>> print(ansi("#FF0000", "#00FF00", color_mode="true_color") + "Hello" + RESET)

    Different modes for text and background:
    >>> print(ansi("#FF0000", "bright_green", lcolor_mode=["256", "8/16"]) + "Hello" + RESET)

    Notes
    -----
    - Some terminals may not fully support italic, blink, or strike effects.
    - On Windows, ANSI escape sequences are automatically enabled if possible.
    - This function can be combined with other ANSI codes for more advanced styling.
    """

    
    code = ""
    
    # Select color palette
    if color_mode is None and lcolor_mode is None:
        raise ValueError("No color mode given")
    
    elif color_mode is None:
        try:
            text_color_mode = lcolor_mode[0]
            bg_color_mode = lcolor_mode[1] if bg_color else None
        except IndexError:
            raise ValueError("lcolor_mode is invalid")
    else:
        text_color_mode = color_mode
        bg_color_mode = color_mode
    
    # Generate text color
    if text_color:
        if text_color_mode in ["256", "true_color"]:
            if use_rgb:
                if not isinstance(text_color, (list, tuple)) or len(text_color) != 3:
                    raise ValueError("RGB color must be a tuple/list of 3 integers")
                r, g, b = text_color
            else:
                if not isinstance(text_color, str) or not text_color.startswith("#"):
                    raise ValueError("Hex color must be a string starting with '#'")
                hexval = text_color.lstrip("#")
                r, g, b = (int(hexval[i:i+2], 16) for i in (0, 2, 4))
            
            if text_color_mode == "256":
                code = "38;5;" + str(16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51))
            else:
                code = f"38;2;{r};{g};{b}"
        
        elif text_color_mode == "8/16":
            if text_color in text_color_palette:
                code = str(text_color_palette[text_color])
            else:
                raise ValueError(f"Invalid 8/16 color: {text_color}")
        
        else:
            raise ValueError(f"Invalid color mode: {text_color_mode}")
    
    # Generate background color
    if bg_color:
        if bg_color_mode in ["256", "true_color"]:
            if use_rgb:
                if not isinstance(bg_color, (list, tuple)) or len(bg_color) != 3:
                    raise ValueError("RGB color must be a tuple/list of 3 integers")
                r, g, b = bg_color
            else:
                if not isinstance(bg_color, str) or not bg_color.startswith("#"):
                    raise ValueError("Hex color must be a string starting with '#'")
                hexval = bg_color.lstrip("#")
                r, g, b = (int(hexval[i:i+2], 16) for i in (0, 2, 4))
            
            if bg_color_mode == "256":
                bgcolor = 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)
                code = f"48;5;{bgcolor};{code}"
            else:
                code = f"48;2;{r};{g};{b};{code}"
        
        elif bg_color_mode == "8/16":
            if bg_color in bg_color_palette:
                code = str(bg_color_palette[bg_color]) + ";" + code
            else:
                raise ValueError(f"Invalid 8/16 color: {bg_color}")
    
    # Add text styles
    if bold: code = '1;' + code
    if dim: code = '2;' + code
    if italic: code = '3;' + code
    if under_line: code = '4;' + code
    if blink: code = '5;' + code
    if reverse: code = '7;' + code
    if strike: code = '9;' + code

    return "\033[" + code.strip(";") + "m"

def get_basic_color_palette():
    """
    Print 8/16 color palette
    """
    for k, v in text_color_palette.items():
        print(f"\033[{v}m\"{k}\"")

# Automaticaly fix for Windows
if os.name == "nt":
    try:
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        kernel32.SetConsoleMode(handle, 0x0001 | 0x0002 | 0x0004)
    except Exception:
        pass
