# start_menu.py

import tkinter as tk
from src.menus.base_menu import BaseMenu
from src.utils.button_manager import ButtonManager

# Define button texts
BUTTON_TEXTS = [
    "1. Aloita",
    "2. Asetukset",
]


class StartMenu(BaseMenu):
    # A start menu frame with various buttons for starting the application and opening settings
    def __init__(self, master, controller):
        # Initialize the StartMenu with a master frame and a controller
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.button_manager = ButtonManager(self)
        self.create_buttons()

    def create_buttons(self):
        # Create buttons from the configurations
        buttons = [
            {
                "text": BUTTON_TEXTS[0],
                "command": lambda: self.controller.switch_to_menu("control_menu"),
            },
            {
                "text": BUTTON_TEXTS[1],
                "command": self.settings_clicked,
            },
        ]

        self.buttons = self.button_manager.create_menu_buttons(buttons)

    def settings_clicked(self):
        # Handle the settings button click
        print("settings clicked in start menu")
