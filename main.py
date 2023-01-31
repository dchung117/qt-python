import sys
from PySide6.QtWidgets import QApplication

import buttons
import sliders
import widgets
import windows
import menus

if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)

    # Create menus
    edit_menu = menus.Menu("Edit", ["Cut", "Copy", "Paste", "Undo", "Redo"])
    window_menu = menus.Menu("Window", ["Zoom", "Unzoom"])
    settings_menu = menus.Menu("Settings", ["Tools"])
    help_menu = menus.Menu("Help", ["Get Started"])
    menu_bar = menus.MenuBar([edit_menu, window_menu, settings_menu, help_menu])

    # Create main window with button
    window = windows.MainWindow("My App", app, menu_bar=menu_bar)
    window.show()

    # Begin event loop
    app.exec()