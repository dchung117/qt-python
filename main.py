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

    # Create Message Box(es)
    msg_boxes = [message_box.MessageBox((700, 200), "Message Box Custom", "Custom message", "This is info about this custom message.", "information"),
        message_box.CriticalMessageBox((700, 200), "Message Box Critical", "Critical message", "This is info about this criticalmessage.")
    ]

    # Create message box widget
    widget = widgets.MessageWidget("Message Boxes", msg_boxes)

    widget.show()

    # Begin event loop
    app.exec()