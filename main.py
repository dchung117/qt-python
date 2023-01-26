import sys
from PySide6.QtWidgets import QApplication

from buttons import ButtonHolder

if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)

    # Create main window with button
    window = ButtonHolder()
    window.show()

    # Begin event loop
    app.exec()