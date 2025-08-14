from generator import ansi, RESET

print("=== 8/16 Colors (Text Only) ===")
for name in text_color_palette.keys():
    print(ansi(text_color=name, color_mode="8/16") + f"{name}" + RESET)

print("\n=== 8/16 Colors (Text + Background) ===")
for tname in text_color_palette.keys():
    print(ansi(text_color=tname, bg_color="bright_black", color_mode="8/16") + f"{tname} on bright_black" + RESET)

print("\n=== 256 Colors (Hex) ===")
print(ansi(text_color="#FF0000", color_mode="256") + "Red (256)" + RESET)
print(ansi(text_color="#00FF00", bg_color="#0000FF", color_mode="256") + "Green on Blue (256)" + RESET)

print("\n=== 256 Colors (RGB Tuple) ===")
print(ansi(text_color=(255, 255, 0), color_mode="256", use_rgb=True) + "Yellow (256 RGB)" + RESET)
print(ansi(text_color=(0, 255, 255), bg_color=(255, 0, 255), color_mode="256", use_rgb=True) + "Cyan on Magenta (256 RGB)" + RESET)

print("\n=== True Color (Hex) ===")
print(ansi(text_color="#FFA500", color_mode="true_color") + "Orange (true_color)" + RESET)
print(ansi(text_color="#FFFFFF", bg_color="#800000", color_mode="true_color") + "White on Maroon (true_color)" + RESET)

print("\n=== True Color (RGB Tuple) ===")
print(ansi(text_color=(255, 105, 180), color_mode="true_color", use_rgb=True) + "Pink (true_color RGB)" + RESET)
print(ansi(text_color=(0, 0, 0), bg_color=(173, 216, 230), color_mode="true_color", use_rgb=True) + "Black on LightBlue (true_color RGB)" + RESET)

print("\n=== Mixed Color Modes (lcolor_mode) ===")
print(ansi(text_color="#FF0000", bg_color="bright_green", lcolor_mode=["256", "8/16"]) + "Red (256) on bright_green (8/16)" + RESET)
print(ansi(text_color="cyan", bg_color="#FF00FF", lcolor_mode=["8/16", "true_color"]) + "Cyan (8/16) on Magenta (true_color)" + RESET)

print("\n=== Text Styles ===")
print(ansi(text_color="yellow", color_mode="8/16", bold=True) + "Bold Yellow" + RESET)
print(ansi(text_color="yellow", color_mode="8/16", italic=True) + "Italic Yellow" + RESET)
print(ansi(text_color="yellow", color_mode="8/16", under_line=True) + "Underline Yellow" + RESET)
print(ansi(text_color="yellow", color_mode="8/16", blink=True) + "Blink Yellow" + RESET)
print(ansi(text_color="yellow", color_mode="8/16", reverse=True) + "Reverse Yellow" + RESET)
print(ansi(text_color="yellow", color_mode="8/16", dim=True) + "Dim Yellow" + RESET)
print(ansi(text_color="yellow", color_mode="8/16", strike=True) + "Strike Yellow" + RESET)
print(ansi(text_color="yellow", bg_color="blue", color_mode="8/16", bold=True, under_line=True, blink=True) + "Bold+Underline+Blink Yellow on Blue" + RESET)
