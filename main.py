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

    # Create text edit widget
    default_text = "Type Here!"
    default_html = "<h1>Kigali Districts</h1><p>The city of Kigali has three districts : </br> <ul> <li>Gasabo</li> <li>Nyarugenge</li><li>Kicukiro</li></ul></p>"
    widget = widgets.TextEditWidget("Q Text Editor", default_text, default_html)

    widget.show()

    # Begin event loop
    app.exec()