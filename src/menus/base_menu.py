# base_menu.py

import tkinter as tk


class BaseMenu(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

    def show(self):
        self.grid(row=1, column=0, sticky="ew")
        self.focus_set()

    def hide(self):
        self.grid_forget()
