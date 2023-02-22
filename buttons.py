from typing import Callable, Iterable

from PySide6.QtWidgets import QMainWindow, QPushButton, QGroupBox, QCheckBox, QRadioButton, QButtonGroup, QVBoxLayout

from slots import on_button_click

class ButtonHolder(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("This is the main window")

        self.button = QPushButton(text="Press me")

        self.setCentralWidget(self.button)

class ClickButton(QPushButton):
    def __init__(self, text: str, is_checkable: bool = False) -> None:
        super().__init__(text)

        if is_checkable:
            self.setCheckable(True) # Set button as checkable
            self.setChecked(False) # Initially unchecked

    def set_click_signal(self, func: Callable) -> None:
        self.clicked.connect(func)

    def set_pressed_signal(self, func: Callable) -> None:
        self.pressed.connect(func)

    def set_released_signal(self, func: Callable) -> None:
        self.released.connect(func)

class CheckBox(QCheckBox):
    def __init__(self, title: str) -> None:
        super().__init__(title)
        self.toggled.connect(self.create_toggle_func(title))

    def create_toggle_func(self, title: str) -> Callable:
        def func(is_checked: bool) -> None:
            if is_checked:
                print(f"{title} selected.")
            else:
                print(f"{title} unselected.")
        return func

class RadioButton(QRadioButton):
    def __init__(self, title: str) -> None:
        super().__init__(title)
        self.toggled.connect(self.create_toggle_func(title))

    def create_toggle_func(self, title: str) -> Callable:
        def func(is_checked: bool) -> None:
            if is_checked:
                print(f"{title} selected.")
            else:
                print(f"{title} unselected.")
        return func

class CheckGroupBox(QGroupBox):
    def __init__(self, title: str, check_boxes: Iterable[QCheckBox | QRadioButton]) -> None:
        super().__init__(title)

        # Set up checkboxes
        layout = QVBoxLayout()
        for cb in check_boxes:
            layout.addWidget(cb)
        self.setLayout(layout)

class ExclusiveCheckBoxes(QGroupBox):
    def __init__(self, title: str, check_boxes: Iterable[QCheckBox]) -> None:
        super().__init__(title)

        # Create exclusive button group, layout
        button_group = QButtonGroup(self)
        layout = QVBoxLayout()
        for cb in check_boxes:
            button_group.addButton(cb)
            layout.addWidget(cb)
        button_group.setExclusive(True)

        self.setLayout(layout)