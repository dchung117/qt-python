import sys
from PySide6.QtWidgets import QApplication

import buttons
import sliders
import widgets

if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)

    # Create main window with button
    window = widgets.RockWidget(button_1_text = "Button1", button_2_text = "Button2", is_vertical=True)
    window.show()

    # Begin event loop
    app.exec()