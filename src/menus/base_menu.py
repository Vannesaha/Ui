# base_menu.py

import tkinter as tk


# Base class for all menus
class BaseMenu(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

    # Show the menu for all menus
    def show(self):
        self.grid(row=1, column=0, sticky="ew")
        self.focus_set()

    # Hide the menu for all menus
    def hide(self):
        self.grid_forget()
