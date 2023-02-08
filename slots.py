from typing import Callable, Any, Optional

def on_button_click(data) -> None:
    print(f"You clicked the button! Data: {data}")

def on_button_press() -> None:
    print(f"You pressed the button!")

def on_button_release() -> None:
    print(f"You released the button!")

def on_value_change(data: int) -> None:
    print(f"Slider value changed to: {data}")

def tool_bar_basic_action() -> None:
    print("Basic action triggered.")

def tool_bar_icon_action() -> None:
    print("Icon action triggered.")

def get_line_edit_text(text: str, label_title: Optional[str] = None) -> None:
    if label_title:
        print(f"{label_title}: {text}")
    else:
        print(text)