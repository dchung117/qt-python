from PySide6.QtWidgets import QMainWindow, QPushButton
from slots import on_button_click

class ButtonHolder(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("This is the main window")

        self.button = QPushButton(text="Press me")

        self.setCentralWidget(self.button)

class ClickButton(QPushButton):
    def __init__(self, text: str) -> None:
        super().__init__(text)

        self.setCheckable(True) # Set button as checkable
        self.setChecked(False) # Initially unchecked

        # Set up signal to listen for button clicks
        self.clicked.connect(on_button_click)