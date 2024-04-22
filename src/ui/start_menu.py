# start_menu.py

import tkinter as tk


class StartMenu:
    def __init__(self, master, controller):
        self.controller = controller

        # Create a frame to contain the buttons and statuses
        self.frame = tk.Frame(master)
        self.frame.pack(fill="both", expand=True)

        # List of button configurations
        buttons = [
            {
                "text": "  1. Aloita",
                "command": self.controller.open_control_menu,
            },  # Added whitespace
            {
                "text": "  2. Asetukset",
                "command": self.settings_clicked,
            },  # Added whitespace
        ]

        # Create buttons from the configurations
        self.buttons = []
        for i, button in enumerate(buttons):
            btn = tk.Button(
                self.frame,
                text=button["text"],
                command=button["command"],
                width=20,
                anchor="w",
            )
            btn.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            self.buttons.append(btn)

        # Add hydraulic and embedded device statuses
        self.hyd_status = tk.Label(self.frame, text="Hydraulic Status: ")
        self.hyd_status.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        self.embed_status = tk.Label(self.frame, text="Embedded Device Status: ")
        self.embed_status.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    def settings_clicked(self):
        print("settings clicked in start menu")
        # Add your start action logic here
