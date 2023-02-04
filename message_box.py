from typing import Literal
from PySide6.QtWidgets import QMessageBox

ICON_MAP = {
    "critical": QMessageBox.Critical,
    "question": QMessageBox.Question,
    "information": QMessageBox.Information,
    "warning": QMessageBox.Warning,
}

class MessageBox(QMessageBox):
    def __init__(self, min_size: tuple[int, int], title: str, text: str, verbose_text: str, icon: Literal["critical", "question", "information", "warning", "about"]) -> None:
        super().__init__()
        self.setMinimumSize(*min_size)
        self.setWindowTitle(title)
        self.setText(text)
        self.setInformativeText(verbose_text)

        # icon logic
        self.setIcon(ICON_MAP[icon])
        self.msg_type = icon
        self.title = title

        # set up buttons
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.setDefaultButton(QMessageBox.Ok)

    def listen(self) -> None:
        response = self.exec()
        if response == QMessageBox.Ok:
            print(f"{self.title} - Clicked ok.")
        else:
            print(f"{self.title} - Clicked cancel.")

class CriticalMessageBox(MessageBox):
    def __init__(self, min_size: tuple[int, int], title: str, text: str, verbose_text: str) -> None:
        super().__init__(min_size, title, text, verbose_text, "critical")

class QuestionMessageBox(MessageBox):
    def __init__(self, min_size: tuple[int, int], title: str, text: str, verbose_text: str) -> None:
        super().__init__(min_size, title, text, verbose_text, "question")

class InformationMessageBox(MessageBox):
    def __init__(self, min_size: tuple[int, int], title: str, text: str, verbose_text: str) -> None:
        super().__init__(min_size, title, text, verbose_text, "information")

class WarningMessageBox(MessageBox):
    def __init__(self, min_size: tuple[int, int], title: str, text: str, verbose_text: str) -> None:
        super().__init__(min_size, title, text, verbose_text, "warning")