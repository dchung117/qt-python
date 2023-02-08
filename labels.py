from PySide6.QtWidgets import QLabel, QLineEdit

class LineEditQLabel(QLabel):
    def __init__(self, title: str):
        super().__init__(text=title)
        self.title = title

        # Create line edit
        self.line_edit = QLineEdit()