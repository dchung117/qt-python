import sys
import os
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication

import buttons
import sliders
import widgets
import menus
import toolbar
import windows
import message_box
import labels

from slots import tool_bar_basic_action, tool_bar_icon_action

if __name__ == "__main__":
    # Load environmental variables
    load_dotenv()

    # Create app
    app = QApplication(sys.argv)

    # Create tab widget
    rock_widget = widgets.RockWidget("Button 1", "Button 2")
    list_widget = widgets.ListWidget("To-do list", "clean my room")
    tab_widget = widgets.TabWidget("Tab widget", widgets=[rock_widget, list_widget], widget_names=["Rock widget", "To-do list"])

    tab_widget.show()

    # Begin event loop
    app.exec()