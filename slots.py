from typing import Callable, Any

def on_button_click(data: bool) -> None:
    print(f"You pressed the button! Data: {data}")

def on_value_change(data: int) -> None:
    print(f"Slider value changed to: {data}")