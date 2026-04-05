from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def hex_to_rgb(hex_str: str) -> RGBColor:
    """Convert hex color string to RGBColor object."""
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 6:
        return RGBColor(int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))
    return RGBColor(0, 0, 0)

def apply_text_style(run, font_name: str, font_size: int, color_hex: str):
    """Apply font styles to a text run."""
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.color.rgb = hex_to_rgb(color_hex)
