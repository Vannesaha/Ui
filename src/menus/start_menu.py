# start_menu.py

import tkinter as tk
from src.menus.button_manager import ButtonManager

# Define a dictionary to hold all the text
TEXT = {
    "start": "1. Aloita",
    "settings": "2. Asetukset",
}


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
                "text": TEXT["start"],
                "command": self.controller.open_control_menu,
            },
            {
                "text": TEXT["settings"],
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
