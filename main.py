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

    # Create size policy/stretch widget
    widget = widgets.SizeStretchWidget("Size policy and stretch demo", "Line editor", button_titles=["One", "Two", "Three"], button_stretches=[2, 1, 1], size_policy=("expand", "fixed"))

    widget.show()

    # Begin event loop
    app.exec()