from typing import Callable, Any, Optional
from PySide6.QtWidgets import QLabel

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

def get_line_edit_text(text: str, line_edit_holder: QLabel, label_title: Optional[str] = None, prefix: str = "") -> None:
    if label_title:
        print(f"{label_title} - {prefix}: {text}")
    else:
        print(f"{prefix}: {text}")

    # Set label text
    line_edit_holder.setText(text)

def line_edit_cursor_changed(old_pos: int, new_pos: int) -> None:
    print(f"Cursor moved: {old_pos} -> {new_pos}.")

def line_edit_finished() -> None:
    print(f"You pressed 'Enter' - editing finished.")

def line_edit_track(new_text: str) -> None:
    print(f"Text edited to: {new_text}")
