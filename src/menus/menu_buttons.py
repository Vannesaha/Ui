# menu_buttons.py
import tkinter as tk


class BaseMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.buttons = []

    def update_buttons(self):
        # Get the current active widget
        active_widget = self.controller.get_active_widget()

        # Define the button configurations for each widget
        button_configs = self.get_button_configs()

        # Get the button configurations for the active widget
        buttons = button_configs.get(active_widget, [])

        # Delete the current buttons
        for button in self.buttons:
            button.destroy()
        self.buttons = []

        # Create the new buttons
        for i, button in enumerate(buttons, 1):
            btn = tk.Button(
                self,
                text=button["text"],
                command=button["command"],
                width=20,
                anchor="w",
                padx=10,
            )
            btn.grid(row=i - 1, column=0, sticky="w", padx=5, pady=5)
            self.grid_columnconfigure(0, weight=1)
            self.buttons.append(btn)

        # Bind number keys to corresponding actions
        for i, button in enumerate(self.buttons, 1):
            cmd = button["command"]
            button.bind("<KeyPress-" + str(i) + ">", lambda event, cmd=cmd: cmd())

    def get_button_configs(self):
        # This method should be overridden by subclasses
        return {}
