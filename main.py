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

    # Create grid layout widget
    buttons = [buttons.ClickButton(s) for s in ("One", "Two", "Three", "Four", "Five", "Six", "Seven")]
    button_pos = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2)]
    button_spans = [None, (1, 2), (2, 1), None, None, None, None]
    size_policies = [None, ("expand", "fixed"), ("expand", "expand"), None, None, None, None]
    widget = widgets.GridWidget("QGrid Demo", buttons, button_pos, button_spans=button_spans, size_policies=size_policies)

    widget.show()

    # Begin event loop
    app.exec()