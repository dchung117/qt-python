from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSlider

from slots import on_value_change

class Slider(QSlider):
    def __init__(self, val_min: int, val_max: int, def_value: Optional[int] = None, is_vertical: bool = False) -> None:
        if is_vertical:
            super().__init__(Qt.Vertical)
        else:
            super().__init__(Qt.Horizontal)

        self.setMinimum(val_min)
        self.setMaximum(val_max)

        # Set default value to midpoint if invalid or None
        if def_value != None:
            if val_min <= def_value <= val_max:
                self.setValue(def_value)
            else:
                self.setValue((val_min + val_max) // 2)
        else:
            self.setValue((val_min + val_max) // 2)

        # Listen for value changes
        self.valueChanged.connect(on_value_change)