import customtkinter as ctk

# Premium Cyberpunk & High-Tech Color Palette
NEON_BLUE = "#00f2ff"       # Primary Accent / Terminal Text
CYBER_PURPLE = "#a020f0"    # Secondary Accent / Storage Audit Button
DARK_BG = "#121212"         # Deep Space Main Background
SIDEBAR_BG = "#0a0a0a"      # Matrix Charcoal Sidebar Background
SUCCESS_GREEN = "#39ff14"   # Live Performance Monitor
ERROR_RED = "#ff3131"       # Critical Crash/Leak Indicators

def apply_neon_theme():
    """Applies the global system dark mode and custom color profiles."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")