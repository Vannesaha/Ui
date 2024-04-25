# button_manager.py

import tkinter as tk


class ButtonManager:
    def __init__(self, parent):
        self.parent = parent
        self.buttons = []
        self.parent.bind("<Key>", self.key_press)

    def key_press(self, event):
        key = event.char
        if key.isdigit():
            index = int(key) - 1
            if 0 <= index < len(self.buttons):
                self.buttons[index].invoke()

    def create_other_buttons(self, text, command, text_anchor="w", pdx=10, pdy=5):
        button = tk.Button(
            self.parent, text=text, command=command, anchor=text_anchor, padx=pdx
        )
        return button

    def create_menu_buttons(self, buttons):
        for i, button in enumerate(buttons, 1):
            btn = tk.Button(
                self.parent,
                text=button["text"],
                command=button["command"],
                width=20,
                anchor="w",
                padx=10,
            )
            btn.grid(row=i - 1, column=0, sticky="nsew", padx=5, pady=5)
            self.parent.grid_columnconfigure(0, weight=1)
            self.buttons.append(btn)
        return self.buttons
