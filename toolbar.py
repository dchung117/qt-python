from typing import Union, Iterable, Callable, Optional
from PySide6.QtWidgets import QToolBar, QStatusBar
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize


class ToolBar(QToolBar):
    def __init__(self, title: str, actions: Union[Iterable[QAction], Iterable[tuple[str, str, Callable]]], icon_size: Optional[QSize] = QSize(16, 16)) -> None:
        super().__init__()
        self.setIconSize(icon_size)
        if isinstance(actions[0], QAction):
            [self.addAction(a) for a in actions]
        else:
            for a_name, a_status_msg, a_func in actions:
                action = QAction(a_name, self)
                action.setStatusTip(a_status_msg)
                action.triggered.connect(a_func)
                self.addAction(action)
