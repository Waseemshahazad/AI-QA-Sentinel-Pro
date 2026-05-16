from gui import AppGUI
from theme import apply_neon_theme


def main():
    """Initializes styles and runs the core main event loop."""
    # 1. Apply customized cyberpunk color profiles
    apply_neon_theme()

    # 2. Fire up the graphical container interface
    app = AppGUI()
    app.mainloop()


if __name__ == "__main__":
    main()