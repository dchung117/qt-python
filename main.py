import sys
from PySide6.QtWidgets import QApplication

import buttons
import sliders
import widgets
import menus
import toolbar
import windows
from slots import tool_bar_basic_action, tool_bar_icon_action

if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)

    # Create menus
    edit_menu = menus.Menu("Edit", ["Cut", "Copy", "Paste", "Undo", "Redo"])
    window_menu = menus.Menu("Window", ["Zoom", "Unzoom"])
    settings_menu = menus.Menu("Settings", ["Tools"])
    help_menu = menus.Menu("Help", ["Get Started"])
    menu_bar = menus.MenuBar([edit_menu, window_menu, settings_menu, help_menu])

    # create tool bar
    toolbar_actions = [("Basic Action", "This is a status for basic action.", tool_bar_basic_action), ("Icon Action", "This is a status for icon action.", tool_bar_icon_action)]
    tool_bar = toolbar.ToolBar("Main ToolBar", toolbar_actions)

    # create rock widget
    central_widget = widgets.RockWidget("Button 1", "Button 2")

    # Create main window with rock widget
    window = windows.MainWindow("My App", app, menu_bar=menu_bar, tool_bar=tool_bar, central_widget=central_widget)
    window.show()

    # Begin event loop
    app.exec()