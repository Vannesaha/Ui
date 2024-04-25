# hydraulic_menu.py

import tkinter as tk
from tkinter import simpledialog
from config.settings import DEVICE_1
from src.utils.button_manager import ButtonManager  # Import ButtonManager


# Define button texts
BUTTON_TEXTS = [
    "1. Aseta sylinteri 0-3",
    "2. Aseta sylinterin paikka 0-180",
    "3. Send Command",
    "4. Back",
]


class HydraulicMenu(tk.Frame):
    def __init__(self, parent, controller):
        # Initialize the HydraulicMenu with a parent frame and a controller
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.buttons = []
        self.button_manager = ButtonManager(self)  # Initialize ButtonManager
        self.create_widgets()

    def create_widgets(self):
        # Create the widgets for the HydraulicMenu
        buttons = [
            {"text": BUTTON_TEXTS[0], "input": True},
            {"text": BUTTON_TEXTS[1], "input": True},
            {"text": BUTTON_TEXTS[2], "command": self.send_command},
            {"text": BUTTON_TEXTS[3], "command": self.controller.back_to_control_menu},
        ]

        for i, button in enumerate(buttons):
            if button.get("input"):
                self.create_input_field(i, button)
            else:
                self.create_button(i, button)

    def create_input_field(self, i, button):
        # Create a button for the input field
        btn = self.button_manager.create_other_buttons(
            button["text"], lambda: entry.focus_set()
        )
        btn.grid(row=i, column=0, sticky="nsew", padx=5, pady=5)
        self.grid_columnconfigure(0, weight=1)  # Make the button fill the column
        self.buttons.append(btn)
        self.button_manager.buttons.append(
            btn
        )  # Add the button to ButtonManager's list

        # Create an input field
        entry = tk.Entry(self)
        entry.grid(row=i, column=1, sticky="w", padx=10, pady=5)
        if button["text"] == "1. Aseta sylinteri 0-3":
            self.cylinder_entry = entry
        else:
            self.position_entry = entry

        # Bind the 'Enter' key to the input field's associated button
        entry.bind("<Return>", lambda event: btn.invoke())

    def create_button(self, i, button):
        # Use ButtonManager to create a button
        btn = self.button_manager.create_other_buttons(
            button["text"], button["command"]
        )
        btn.grid(row=i, column=0, sticky="nsew", padx=5, pady=5)
        self.grid_columnconfigure(0, weight=1)  # Make the button fill the column
        self.buttons.append(btn)
        self.button_manager.buttons.append(
            btn
        )  # Add the button to ButtonManager's list

        # Bind the 'Enter' key to the button's command
        self.bind("<Return>", lambda event: button["command"]())

    def send_command(self):
        # Send the command to set the cylinder position
        # Check if the hydraulic device is offline
        if self.device_statuses.get("hydraulic") != "online":
            raise ValueError("Hydraulic device is offline. Cannot send command.")

        try:
            cylinder = int(self.cylinder_entry.get())
            position = int(self.position_entry.get())
        except ValueError:
            print("Please enter valid integers for cylinder and position.")
            return

        if not 0 <= cylinder <= 3:
            print("Cylinder value must be between 0 and 3.")
            return

        if not 0 <= position <= 180:
            print("Position value must be between 0 and 180.")
            return

        topic = f"device/{DEVICE_1}/set_cylinder_position"
        message = f"set_cylinder:{cylinder},set_position:{position}"
        self.controller.mqtt_publisher.publish_command(topic, message)

    def show(self):
        # Show the HydraulicMenu frame itself
        self.pack(fill="both", expand=True)
        self.focus_set()  # Add this line to focus on this frame when it's shown

    def hide(self):
        # Hide the HydraulicMenu frame
        self.pack_forget()
