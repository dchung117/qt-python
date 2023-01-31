from typing import Optional
from PySide6.QtWidgets import QMainWindow, QMenuBar, QApplication
from PySide6.QtGui import QAction

import menus

class MainWindow(QMainWindow):
    def __init__(self, title: str, app: QApplication, menu_bar: Optional[QMenuBar] = None) -> None:
        super().__init__()
        self.app = app
        self.setWindowTitle(title)

        # menu  bar
        if menu_bar is None:
            menu_bar = self.menuBar()

            edit_menu = menu_bar.addMenu("&Edit")
            edit_menu.addAction("Cut")
            edit_menu.addAction("Copy")
            edit_menu.addAction("Paste")
            edit_menu.addAction("Undo")
            edit_menu.addAction("Redo")

            menu_bar.addMenu("&Window")
            menu_bar.addMenu("&Settings")
            menu_bar.addMenu("&Help")
        else:
            self.setMenuBar(menu_bar)

        file_menu = menu_bar.addMenu("&File") # file menu
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)
    def quit_app(self) -> None:
        self.app.quit()