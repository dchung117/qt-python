import sys
import os
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication

import buttons
import sliders
import widgets
import menus
import toolbar
import windows
import message_box
import labels

from slots import tool_bar_basic_action, tool_bar_icon_action

if __name__ == "__main__":
    # Load environmental variables
    load_dotenv()

    # Create app
    app = QApplication(sys.argv)

    # Create check box/radio box widget
    check_boxes = [buttons.CheckBox(t) for t in ["Fries", "Onion rings", "Mac and cheese"]]
    exclusive_check_boxes = [buttons.CheckBox(t) for t in ["Burger", "Hot dog", "Chicken tenders"]]
    radio_buttons = [buttons.RadioButton(t) for t in ["Apple pie", "Fruit cup", "Milkshake"]]

    check_group_box = buttons.CheckGroupBox("Choose your sides: ", check_boxes)
    exclusive_check_group_box = buttons.ExclusiveCheckBoxes("Choose your entree: ", exclusive_check_boxes)
    radio_button_group_box = buttons.CheckGroupBox("Choose a dessert: ", radio_buttons)
    widget = widgets.CheckBoxWidget("Fast food", check_group_box, exclusive_check_group_box, radio_button_group_box)

    widget.show()

    # Begin event loop
    app.exec()