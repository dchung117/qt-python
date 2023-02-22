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

    # Create to-do list widget
    widget = widgets.ListWidget("To-do list", items=["clean room", "take out trash", "cook dinner"])

    widget.show()

    # Begin event loop
    app.exec()