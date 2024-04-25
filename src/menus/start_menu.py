# start_menu.py

import tkinter as tk
from src.utils.button_manager import ButtonManager

# start_menu.py

# Define button texts
BUTTON_TEXTS = [
    "1. Aloita",
    "2. Asetukset",
]


class StartMenu(tk.Frame):
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
                "command": self.controller.open_control_menu,
            },
            {
                "text": BUTTON_TEXTS[1],
                "command": self.settings_clicked,
            },
        ]

        self.buttons = self.button_manager.create_menu_buttons(buttons)

    # ... rest of your methods ...

    def show(self):
        # Show the StartMenu frame itself
        self.pack(fill="both", expand=True)
        self.focus_set()  # Add this line to focus on this frame when it's shown

    def hide(self):
        # Hide the StartMenu frame
        self.pack_forget()

    def settings_clicked(self):
        # Handle the settings button click
        print("settings clicked in start menu")
