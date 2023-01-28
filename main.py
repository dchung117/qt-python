import sys
from PySide6.QtWidgets import QApplication

import buttons
import sliders

if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)

    # Create main window with button
    val_min, val_max = 1, 100
    window = sliders.Slider(val_min, val_max, is_vertical=True)
    window.show()

    # Begin event loop
    app.exec()