from typing import Union, Iterable
from PySide6.QtWidgets import QMenuBar, QMenu, QComboBox

class MenuBar(QMenuBar):
    def __init__(self, menus: Union[list[tuple[str, list[str]]], list[QMenu]]) -> None:
        super().__init__()
        if isinstance(menus[0], QMenu):
            for m in menus:
                self.addMenu(m)
        else:
            for m_title, m_actions in menus:
                menu = self.addMenu("&" + m_title)
                [menu.addAction(a) for a in m_actions]

class Menu(QMenu):
    def __init__(self, title: str, actions: list[str]) -> None:
        super().__init__()
        self.setTitle("&" + title)
        for a in actions:
            self.addAction(a)

class ComboBox(QComboBox):
    def __init__(self, choices: Iterable[str]) -> None:
        super().__init__()
        # Add choices to combo box
        for c in choices:
            self.addItem(c)