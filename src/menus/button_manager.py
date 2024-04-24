# button_manager.py

import tkinter as tk


class ButtonManager:
    def __init__(self, parent):
        self.parent = parent

    def create_button(self, text, command):
        button = tk.Button(self.parent, text=text, command=command)
        return button
