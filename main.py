import sys
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
    # Create app
    app = QApplication(sys.argv)

    # Create label line-edit widget
    line_edit_label = labels.LineEditQLabel("Line Edit")
    widget = widgets.LineEditLabelWidget("Line Edit Widget", line_edit_label)

    widget.show()

    # Begin event loop
    app.exec()