Tamam, işte **ANSI Generator** için İngilizce README:

# ANSI Generator

ANSI Generator is a simple Python tool for creating colored text and effects in the terminal.  
It uses standard ANSI escape codes to style, colorize, and add effects to text.  
**ARGB simulation** support will be added in the future.

## Features
- Colorize text with predefined ANSI colors
- Bold, italic, underline, blink, and more effects
- Combine multiple styles and colors
- Cross-platform (Linux, macOS, Windows - if ANSI is supported)

## Installation
```bash
git clone https://github.com/username/ansi-generator.git
cd ansi-generator
python3 main.py
```

## Usage

Copy generator.py file to your project and:

```python
from generator import ansi, RESET

ansi_code = ansi(
    text_color = "#00FF00",
    bg_color = "#0000FF",
    color_mode = "true_color"
)

print(ansi_code + "Hello, world!" + RESET)
```

Use `help(ansi)` for full features.