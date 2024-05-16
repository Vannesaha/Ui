# button_manager.py

import tkinter as tk


class ButtonManager:
    def __init__(self, parent):
        self.parent = parent
        self.buttons = []
        self.parent.bind("<Key>", self.key_press)

    # Handle key press events for keyboard
    def key_press(self, event):
        key = event.char
        if key.isdigit():
            index = int(key) - 1
            if 0 <= index < len(self.buttons):
                self.buttons[index].invoke()

    # Create other buttons for the menu
    def create_other_buttons(self, text, command, text_anchor="w", pdx=10, pdy=5):
        button = tk.Button(
            self.parent, text=text, command=command, anchor=text_anchor, padx=pdx
        )
        return button

    # Create buttons for the menu
    def create_menu_buttons(self, buttons):
        for i, button in enumerate(buttons, 1):
            btn = tk.Button(
                self.parent,
                text=button["text"],
                command=button["command"],
                width=20,  # Set the width of the button
                anchor="w",  # Set the anchor to the west
                padx=10,  # Set the padding for the button text
                bg="#FFFFFF",  # Set the background color of the button
            )

            # Add the button to the list of buttons
            btn.grid(
                row=i - 1, column=0, sticky="nsew", padx=5, pady=5
            )  # Place the button in the grid
            self.parent.grid_columnconfigure(
                0, weight=1
            )  # Make the button fill the column
            self.buttons.append(btn)  # Add the button to the list of buttons
        return self.buttons
