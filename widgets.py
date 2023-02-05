import functools
from typing import Callable, Any, Iterable

from slots import on_button_click, on_button_press, on_button_release
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox

from buttons import ClickButton

class RockWidget(QWidget):
    def __init__(self, button_1_text: str, button_2_text: str, is_vertical: bool = False) -> None:
        super().__init__()
        self.setWindowTitle("Rock Widget")

        # Create buttons
        button_1 = ClickButton("Button 1")
        button_2 = ClickButton("Button 2")

        # Set up decorators
        click_button_1_partial = functools.partial(click_button_decorator, button_name=button_1_text)
        press_release_button_1_partial = functools.partial(press_release_button_decorator, button_name=button_1_text)
        click_button_2_partial = functools.partial(click_button_decorator, button_name=button_2_text)
        press_release_button_2_partial = functools.partial(press_release_button_decorator, button_name=button_2_text)


        # Set up signals to listen for button clicks, presses, releases
        button_1.set_click_signal(click_button_1_partial(on_button_click))
        button_1.set_pressed_signal(press_release_button_1_partial(on_button_press))
        button_1.set_released_signal(press_release_button_1_partial(on_button_release))
        button_2.set_click_signal(click_button_2_partial(on_button_click))
        button_2.set_pressed_signal(press_release_button_2_partial(on_button_press))
        button_2.set_released_signal(press_release_button_2_partial(on_button_release))

        # Set up button widget layout
        if is_vertical:
            button_layout = QVBoxLayout()
        else:
            button_layout = QHBoxLayout()
        button_layout.addWidget(button_1)
        button_layout.addWidget(button_2)
        self.setLayout(button_layout)


def click_button_decorator(func: Callable, button_name: str) -> Callable:
    @functools.wraps(func)
    def wrapper(data: bool) -> Any:
        print(f"Button name: {button_name}.")
        out = func(data)
        return out
    return wrapper

def press_release_button_decorator(func: Callable, button_name: str) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Button name: {button_name}.")
        out = func(*args, **kwargs)
        return out
    return wrapper

class MessageWidget(QWidget):
    def __init__(self, title: str, msg_boxes: Iterable[QMessageBox]) -> None:
        super().__init__()
        self.setWindowTitle(title)

        # Set up layout
        button_layout = QVBoxLayout()

        # set up message buttons
        self.msg_boxes = msg_boxes
        for i, msg_box in enumerate(msg_boxes):
            msg_button = QPushButton(msg_box.msg_type.capitalize())
            msg_button.clicked.connect(self.button_clicked(i))

            button_layout.addWidget(msg_button)
        self.setLayout(button_layout)

    def button_clicked(self, idx: int) -> Callable:
        @functools.wraps(self.msg_boxes[idx])
        def wrapper(*args, **kwargs) -> Any:
            self.msg_boxes[idx].listen()
            return
        return wrapper
