from PySide6.QtWidgets import QLabel, QLineEdit
from PySide6.QtGui import QPixmap

class LineEditQLabel(QLabel):
    def __init__(self, title: str):
        super().__init__(text=title)
        self.title = title

        # Create line edit
        self.line_edit = QLineEdit()

class ImageLabel(QLabel):
    def __init__(self, img_file: str) -> None:
        super().__init__()
        self.setPixmap(QPixmap(img_file)) # set up image