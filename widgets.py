import functools
from typing import Callable, Any, Iterable, Optional, Literal, Union

from slots import on_button_click, on_button_press, on_button_release, get_line_edit_text, line_edit_cursor_changed, line_edit_finished, line_edit_track
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QLabel, QTextEdit, QGridLayout, QGroupBox, \
    QListWidget, QListWidgetItem, QAbstractItemView, QTabWidget

from buttons import ClickButton
from labels import LineEditQLabel, ImageLabel, SIZE_POLICIES

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

class ImageWidget(QWidget):
    def __init__(self, title: str, img_file: str) -> None:
        super().__init__()
        self.setWindowTitle(title)

        self.img_label = ImageLabel(img_file)

        layout = QVBoxLayout()
        layout.addWidget(self.img_label)
        self.setLayout(layout)

class SizeStretchWidget(QWidget):
    def __init__(self, title: str, label_title: str, button_titles: Iterable[str],
        button_stretches: Optional[Iterable[int]] = None, size_policy: tuple[Optional[str]] = (None, None)) -> None:
        super().__init__()
        self.setWindowTitle(title)

        # line edit widget
        line_edit_layout = QHBoxLayout()
        self.line_edit_label = LineEditQLabel(label_title, horizontal_size_policy=size_policy[0], vertical_size_policy=size_policy[1])
        line_edit_layout.addWidget(self.line_edit_label)
        line_edit_layout.addWidget(self.line_edit_label.line_edit)

        # buttons
        button_layout = QHBoxLayout()
        button_iter = zip(button_titles, [None]*len(button_titles))
        if button_stretches:
            button_iter = zip(button_titles, button_stretches)
        for bt, stretch in button_iter:
            if stretch:
                button_layout.addWidget(QPushButton(bt), stretch)
            else:
                button_layout.addWidget(QPushButton(bt))

        # overall layout
        layout = QVBoxLayout()
        layout.addLayout(line_edit_layout)
        layout.addLayout(button_layout)
        self.setLayout(layout)

class GridWidget(QWidget):
    def __init__(self, title: str, buttons: Iterable[QPushButton], button_positions: Iterable[tuple[int]],
        button_spans: Iterable[tuple[int]] | None = None, size_policies: Iterable[tuple[str]] | None = None) -> None:
        super().__init__()
        self.setWindowTitle(title)

        # Apply size policies
        if size_policies:
            for i, sz_p in enumerate(size_policies):
                if sz_p:
                    buttons[i].setSizePolicy(SIZE_POLICIES[sz_p[0]], SIZE_POLICIES[sz_p[1]])

        # Create grid layout
        grid_layout = QGridLayout()
        for i, (b, b_pos) in enumerate(zip(buttons, button_positions)):
            # Specify span if included
            if button_spans:
                if button_spans[i]:
                    grid_layout.addWidget(b, *b_pos, *button_spans[i])
                else:
                    grid_layout.addWidget(b, *b_pos)
            else:
                grid_layout.addWidget(b, *b_pos)
        self.setLayout(grid_layout)

class CheckBoxWidget(QWidget):
    def __init__(self, title: str, check_boxes: QGroupBox, exclusive_check_boxes: QGroupBox, radio_buttons: QGroupBox) -> None:
        super().__init__()
        self.setWindowTitle(title)

        # Add check group boxes to layout
        check_boxes_layout = QHBoxLayout()
        check_boxes_layout.addWidget(exclusive_check_boxes)
        check_boxes_layout.addWidget(check_boxes)

        # Add radio buttons to layout
        radio_button_layout = QVBoxLayout()
        radio_button_layout.addWidget(radio_buttons)

        # Create overall layout
        layout = QVBoxLayout()
        layout.addLayout(check_boxes_layout)
        layout.addLayout(radio_button_layout)
        self.setLayout(layout)

class ListWidget(QWidget):
    LIST_SELECTION_MODES = {
        "single": QAbstractItemView.SingleSelection,
        "contiguous": QAbstractItemView.ContiguousSelection,
        "extended": QAbstractItemView.ExtendedSelection,
        "multi": QAbstractItemView.MultiSelection,
        "none": QAbstractItemView.NoSelection
    }
    def __init__(self, title: str, items: Union[str, Iterable[str]] = [],
        selection_mode: Literal["single", "contiguous", "extended", "multi", "none"] = "multi") -> None:
        super().__init__()
        self.setWindowTitle(title)

        # set up list widget
        self.list_widget = QListWidget()
        mode = ListWidget.LIST_SELECTION_MODES.get(selection_mode)
        if mode is None:
            raise KeyError(f"Selection mode must be one of 'single', 'contiguous', 'extended', 'multi', 'none'")
        self.list_widget.setSelectionMode(mode)

        if isinstance(items, str):
            self.list_widget.addItem(items)
        else:
            self.list_widget.addItems(items)

        # set up slots
        self.list_widget.currentItemChanged.connect(self.item_select_changed)
        self.list_widget.currentTextChanged.connect(self.item_text_changed)

        # line edit
        self.line_edit_label = LineEditQLabel("Type new item here: ")

        # buttons
        add_button = ClickButton("Add item")
        add_button.set_click_signal(self.add_item)

        delete_button = ClickButton("Delete item")
        delete_button.set_click_signal(self.delete_item)

        count_button = ClickButton("Count items")
        count_button.set_click_signal(self.count_items)

        select_button = ClickButton("Selected items")
        select_button.set_click_signal(self.selected_items)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(self.line_edit_label)
        layout.addWidget(self.line_edit_label.line_edit)
        layout.addWidget(add_button)
        layout.addWidget(delete_button)
        layout.addWidget(count_button)
        layout.addWidget(select_button)

        self.setLayout(layout)

    def item_select_changed(self, curr_item: QListWidgetItem, prev_item: QListWidgetItem) -> None:
        if prev_item:
            print(f"Previous item selected: {prev_item.text()}")
        else:
            print("Previous item: None")

        if curr_item:
            print(f"Current item: {curr_item.text()}")
        else:
            print("Current item: None")

    def item_text_changed(self, curr_text: str) -> None:
        print(f"Current text: {curr_text}")

    def add_item(self) -> None:
        if len(self.line_edit_label.line_edit.text()):
            self.list_widget.addItem(self.line_edit_label.line_edit.text())

    def delete_item(self) -> None:
        self.list_widget.takeItem(self.list_widget.currentRow())

    def count_items(self) -> None:
        print(f"Number of items: {self.list_widget.count()}")
        print()

    def selected_items(self) -> None:
        print("Selected items: ")
        for item in self.list_widget.selectedItems():
            if item:
                print(item.text())
        print()

class TabWidget(QWidget):
    def __init__(self, title: str, widgets: Iterable[QWidget], widget_names: Iterable[str]) -> None:
        # assert that widget and names are provided
        assert len(widgets) == len(widget_names), "Must provide name for every widget."

        super().__init__()
        self.setWindowTitle(title)

        # tab widget
        tab_widget = QTabWidget(self)
        for w, w_name in zip(widgets, widget_names):
            tab_widget.addTab(w, w_name)

        # tab widget layout
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)