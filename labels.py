from typing import Literal, Optional
from PySide6.QtWidgets import QLabel, QLineEdit, QSizePolicy
from PySide6.QtGui import QPixmap

SIZE_POLICIES = {
    "expand": QSizePolicy.Expanding,
    "fixed": QSizePolicy.Fixed
}
class LineEditQLabel(QLabel):
    def __init__(self, title: str, horizontal_size_policy: Optional[Literal["expand", "fixed"]] = None, vertical_size_policy: Optional[Literal["expand", "fixed"]] = None):
        super().__init__(text=title)
        self.title = title

        # Create line edit
        self.line_edit = QLineEdit()

        # Set size policy
        if horizontal_size_policy and vertical_size_policy:
            self.line_edit.setSizePolicy(SIZE_POLICIES[horizontal_size_policy], SIZE_POLICIES[vertical_size_policy]) # expand horizontally, fix vertically

class ImageLabel(QLabel):
    def __init__(self, img_file: str) -> None:
        super().__init__()
        self.setPixmap(QPixmap(img_file)) # set up image