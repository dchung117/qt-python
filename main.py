import sys
from PySide6.QtWidgets import QApplication, QWidget

# Create app
app = QApplication(sys.argv)

# Create/display GUI window
window = QWidget()
window.show()

if __name__ == "__main__":
    # Run app
    app.exec()