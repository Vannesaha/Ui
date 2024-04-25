# start_menu.py
import tkinter as tk

# Define a dictionary to hold all the text
TEXTS = {
    "start": "  1. Aloita",
    "settings": "  2. Asetukset",
}


class StartMenu(tk.Frame):
    # A start menu frame with various buttons for starting the application and opening settings
    def __init__(self, master, controller):
        # Initialize the StartMenu with a master frame and a controller
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        # Create buttons from the configurations
        buttons = [
            {
                "text": TEXTS["start"],
                "command": self.controller.open_control_menu,
            },
            {
                "text": TEXTS["settings"],
                "command": self.settings_clicked,
            },
        ]

        for i, button in enumerate(buttons):
            btn = tk.Button(
                self,
                text=button["text"],
                command=button["command"],
                width=20,
                anchor="w",
                padx=10,
            )
            btn.grid(row=i, column=0, sticky="nsew", padx=5, pady=5)
            self.grid_columnconfigure(0, weight=1)
            self.buttons.append(btn)

    def show(self):
        # Show the StartMenu frame itself
        self.pack(fill="both", expand=True)

    def hide(self):
        # Hide the StartMenu frame
        self.pack_forget()

    def settings_clicked(self):
        # Handle the settings button click
        print("settings clicked in start menu")
