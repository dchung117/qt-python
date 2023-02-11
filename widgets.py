import functools
from typing import Callable, Any, Iterable

from slots import on_button_click, on_button_press, on_button_release, get_line_edit_text, line_edit_cursor_changed, line_edit_finished, line_edit_track
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QLabel, QTextEdit

from buttons import ClickButton
from labels import LineEditQLabel

class RockWidget(QWidget):
    def __init__(self, button_1_text: str, button_2_text: str, is_vertical: bool = False) -> None:
        super().__init__()
        self.setWindowTitle("Rock Widget")

        # Create buttons
        button_1 = ClickButton("Button 1")
        button_2 = ClickButton("Button 2")

        # Set up decorators
        click_button_1_partial = functools.partial(click_button_decorator, button_name=button_1_text)
        press_release_button_1_partial = functools.partial(press_release_button_decorator, button_name=button_1_text)
        click_button_2_partial = functools.partial(click_button_decorator, button_name=button_2_text)
        press_release_button_2_partial = functools.partial(press_release_button_decorator, button_name=button_2_text)


        # Set up signals to listen for button clicks, presses, releases
        button_1.set_click_signal(click_button_1_partial(on_button_click))
        button_1.set_pressed_signal(press_release_button_1_partial(on_button_press))
        button_1.set_released_signal(press_release_button_1_partial(on_button_release))
        button_2.set_click_signal(click_button_2_partial(on_button_click))
        button_2.set_pressed_signal(press_release_button_2_partial(on_button_press))
        button_2.set_released_signal(press_release_button_2_partial(on_button_release))

        # Set up button widget layout
        if is_vertical:
            button_layout = QVBoxLayout()
        else:
            button_layout = QHBoxLayout()
        button_layout.addWidget(button_1)
        button_layout.addWidget(button_2)
        self.setLayout(button_layout)


def click_button_decorator(func: Callable, button_name: str) -> Callable:
    @functools.wraps(func)
    def wrapper(data: bool) -> Any:
        print(f"Button name: {button_name}.")
        out = func(data)
        return out
    return wrapper

def press_release_button_decorator(func: Callable, button_name: str) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Button name: {button_name}.")
        out = func(*args, **kwargs)
        return out
    return wrapper

class MessageWidget(QWidget):
    def __init__(self, title: str, msg_boxes: Iterable[QMessageBox]) -> None:
        super().__init__()
        self.setWindowTitle(title)

        # Set up layout
        button_layout = QVBoxLayout()

        # set up message buttons
        self.msg_boxes = msg_boxes
        for i, msg_box in enumerate(msg_boxes):
            msg_button = QPushButton(msg_box.msg_type.capitalize())
            msg_button.clicked.connect(self.button_clicked(i))

            button_layout.addWidget(msg_button)
        self.setLayout(button_layout)

    def button_clicked(self, idx: int) -> Callable:
        @functools.wraps(self.msg_boxes[idx])
        def wrapper(*args, **kwargs) -> Any:
            self.msg_boxes[idx].listen()
            return
        return wrapper

class LineEditLabelWidget(QWidget):
    def __init__(self, title: str, edit_label: LineEditQLabel) -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.label = edit_label

        # Button to collect data
        button = QPushButton("Get data")
        self.text_holder_label = QLabel("I am here")
        # button.clicked.connect(self.line_edit_decorator(get_line_edit_text, self.label, self.text_holder_label)) # print text in line edit
        # self.label.line_edit.textChanged.connect(self.line_edit_decorator(get_line_edit_text, self.label, self.text_holder_label, prefix="Text changed")) # show text edit in label
        # self.label.line_edit.cursorPositionChanged.connect(line_edit_cursor_changed) # track line edit cursor
        # self.label.line_edit.editingFinished.connect(line_edit_finished) # listen for enter key presses
        # self.label.line_edit.selectionChanged.connect(self.line_edit_decorator(get_line_edit_text, self.label, self.text_holder_label, prefix="Selection changed")) # show highlighted text
        self.label.line_edit.textEdited.connect(self.line_edit_decorator(get_line_edit_text, self.label, self.text_holder_label, prefix="Text edited to")) # track edits in real time

        # Layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(edit_label)
        h_layout.addWidget(edit_label.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout) # h_layout w/ qlabel/line edit will be nested in a larger vertical layout
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    def line_edit_decorator(self, func: Callable, edit_label: LineEditQLabel, line_edit_holder: QLabel, prefix: str = "") -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Get text or selected text
            text = edit_label.line_edit.text()
            if "Select" in prefix:
                text = edit_label.line_edit.selectedText()

            func(text, line_edit_holder, edit_label.title, prefix=prefix)
            return
        return wrapper

class TextEditWidget(QWidget):
    def __init__(self, title: str, default_text: str, default_html: str):
        super().__init__()
        self.setWindowTitle(title)

        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(default_text)
        self.default_text = default_text
        self.default_html = default_html

        # print current text
        get_text_button = QPushButton("Get text")
        get_text_button.clicked.connect(self.print_text)

        # Set up buttons for copy, cut, paste, undo, redo, set plain text, etc.
        copy = QPushButton("Copy")
        copy.clicked.connect(self.text_edit.copy)

        cut = QPushButton("Cut")
        cut.clicked.connect(self.text_edit.cut)

        paste = QPushButton("Paste")
        paste.clicked.connect(self.text_edit.paste)

        undo = QPushButton("Undo")
        undo.clicked.connect(self.text_edit.undo)

        redo = QPushButton("Redo")
        redo.clicked.connect(self.text_edit.redo)

        set_plain_text = QPushButton("Set Plain Text")
        set_plain_text.clicked.connect(self.set_plain_text)

        set_html = QPushButton("Set HTML")
        set_html.clicked.connect(self.set_html)

        clear = QPushButton("Clear")
        clear.clicked.connect(self.text_edit.clear)

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(get_text_button)
        button_layout.addWidget(copy)
        button_layout.addWidget(cut)
        button_layout.addWidget(paste)
        button_layout.addWidget(undo)
        button_layout.addWidget(redo)
        button_layout.addWidget(set_plain_text)
        button_layout.addWidget(set_html)
        button_layout.addWidget(clear)

        # Widget layout
        layout = QVBoxLayout()
        layout.addLayout(button_layout)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def print_text(self) -> None:
        print(f"Entered text: {self.text_edit.toPlainText()}")

    def set_plain_text(self) -> None:
        self.text_edit.setPlainText(self.default_text)

    def set_html(self) -> None:
        self.text_edit.setHtml(self.default_html)