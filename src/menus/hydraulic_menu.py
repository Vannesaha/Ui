# hydraulic_menu.py

import tkinter as tk
from tkinter import simpledialog
from config.settings import DEVICE_1


class HydraulicMenu(tk.Frame):
    def __init__(self, parent, controller):
        # Initialize the HydraulicMenu with a parent frame and a controller
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        # Create the widgets for the HydraulicMenu
        buttons = [
            {"text": "  1. Aseta sylinteri 0-3", "input": True},
            {"text": "  2. Aseta sylinterin paikka 0-180", "input": True},
            {"text": "  3. Send Command", "command": self.send_command},
            {"text": "  4. Back", "command": self.controller.back_to_control_menu},
        ]

        for i, button in enumerate(buttons):
            if button.get("input"):
                self.create_input_field(i, button)
            else:
                self.create_button(i, button)

    def create_input_field(self, i, button):
        # Create an input field with a label
        label = tk.Label(self, text=button["text"])
        label.grid(row=i, column=0, sticky="w", padx=5, pady=5)
        entry = tk.Entry(self)
        entry.grid(row=i, column=1, sticky="w", padx=5, pady=5)
        if button["text"] == "  1. Aseta sylinteri 0-3":
            self.cylinder_entry = entry
        else:
            self.position_entry = entry

    def create_button(self, i, button):
        # Create a button with the specified text and command
        btn = tk.Button(
            self,
            text=button["text"],
            command=button.get(
                "command", None
            ),  # If the command key is not found, set it to None
            width=20,
            anchor="w",
        )
        btn.grid(row=i, column=0, sticky="w", padx=5, pady=5)
        self.buttons.append(btn)

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

    def hide(self):
        # Hide the HydraulicMenu frame
        self.pack_forget()
