# start_menu.py

import tkinter as tk


class StartMenu(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

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
                self,
                text=button["text"],
                command=button["command"],
                width=20,
                anchor="w",
            )
            btn.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            self.buttons.append(btn)

    def show(self):
        self.pack(fill="both", expand=True)  # Show the StartMenu frame itself

    def hide(self):
        self.pack_forget()

    def settings_clicked(self):
        print("settings clicked in start menu")
        # Add your start action logic here
