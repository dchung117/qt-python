import sys
from PySide6.QtWidgets import QApplication

import buttons
import sliders
import widgets
import menus
import toolbar
import windows
import message_box

from slots import tool_bar_basic_action, tool_bar_icon_action

if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)

    # Create rock widget
    widget = widgets.RockWidget("Button 1", "Button 2")

    widget.show()

    # Begin event loop
    app.exec()