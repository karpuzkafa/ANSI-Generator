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
) -> str:
    """
    
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


# Automaticaly fix for Windows
if os.name == "nt":
    try:
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        kernel32.SetConsoleMode(handle, 0x0001 | 0x0002 | 0x0004)
    except Exception:
        pass

help(ansi)