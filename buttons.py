from typing import Callable

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

    def set_click_signal(self, func: Callable) -> None:
        self.clicked.connect(func)

    def set_pressed_signal(self, func: Callable) -> None:
        self.pressed.connect(func)

    def set_released_signal(self, func: Callable) -> None:
        self.released.connect(func)