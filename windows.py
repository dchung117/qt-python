from typing import Optional, Callable, Any
from PySide6.QtWidgets import QMainWindow, QMenuBar, QToolBar, QStatusBar, QPushButton, QWidget, QApplication
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize

import menus

class MainWindow(QMainWindow):
    def __init__(self, title: str, app: QApplication, menu_bar: Optional[QMenuBar] = None, tool_bar: Optional[QToolBar] = None,
        central_widget: Optional[QWidget] = None) -> None:
        super().__init__()
        self.app = app
        self.setWindowTitle(title)

        # menu bar
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

        # tool bar
        if tool_bar is None:
            tool_bar = QToolBar("Main toolbar")
            tool_bar.setIconSize(QSize(16, 16))

            basic_action = QAction("Basic Action", self)
            basic_action.setStatusTip("This is a status for a basic action.")
            basic_action.triggered.connect(self.tool_bar_basic_action)
            tool_bar.addAction(basic_action)

            icon_action = QAction(QIcon("imgs/start.png"), "Icon Action", self)
            icon_action.setStatusTip("This is a status for an icon action.")
            icon_action.triggered.connect(self.tool_bar_icon_action)
            tool_bar.addAction(icon_action)

        self.addToolBar(tool_bar)
        tool_bar.addAction(quit_action) # pass quit action endpoint to tool bar

        # separator
        tool_bar.addSeparator()
        tool_bar.addWidget(QPushButton("Separator"))

        # status bar
        self.setStatusBar(QStatusBar(self))

        # central widget
        if central_widget is None:
            central_widget = QPushButton("Main Button")
            central_widget.clicked.connect(self.main_button_clicked)
        self.setCentralWidget(central_widget)

    @classmethod
    def tool_bar_button_click_status(cls, self, button_name: str = "tool bar") -> None:
        self.statusBar().showMessage(f"You clicked on {button_name}!", 3000)

    def quit_app(self) -> None:
        self.app.quit()

    def tool_bar_basic_action(self) -> None:
        MainWindow.tool_bar_button_click_status(self, "Basic Action")
        print("Basic action triggered.")

    def tool_bar_icon_action(self) -> None:
        MainWindow.tool_bar_button_click_status(self, "Icon Action")
        print("Icon action triggered.")

    def main_button_clicked(self) -> None:
        print("Main button clicked.")