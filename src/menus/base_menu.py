# base_menu.py

import tkinter as tk


class BaseMenu(tk.Frame):  # Create a BaseMenu class
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)  # Initialize the BaseMenu with a master frame
        self.controller = controller  # Set the controller attribute

    def show(self):
        self.pack(fill="both", expand=True)  # Pack the BaseMenu to fill the whole frame
        self.focus_set()  # Set the focus to new menu

    def hide(self):
        self.pack_forget()  # Hide the BaseMenu
