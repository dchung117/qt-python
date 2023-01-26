from PySide6.QtWidgets import QMainWindow, QPushButton
class ButtonHolder(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("This is the main window")

        self.button = QPushButton(text="Press me")

        self.setCentralWidget(self.button)