import functools
from typing import Callable, Any

from slots import on_button_click
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

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
        click_button_2_partial = functools.partial(click_button_decorator, button_name=button_2_text)

        # Set up signals to listen for button clicks
        button_1.set_click_signal(click_button_1_partial(on_button_click))
        button_2.set_click_signal(click_button_2_partial(on_button_click))

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
    def wrapper(data: Any) -> Any:
        print(f"Button name: {button_name}.")
        out = func(data)
        return out
    return wrapper