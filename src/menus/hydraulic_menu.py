# hydraulic_menu.py

import tkinter as tk
from src.menus.base_menu import BaseMenu
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


class HydraulicMenu(BaseMenu):
    def __init__(self, parent, controller):
        # Initialize the HydraulicMenu with a parent frame and a controller
        tk.Frame.__init__(self, parent, bg="#0109D4")  # Ensure background color
        self.controller = controller
        self.buttons = []
        self.entries = []  # Define the entries attribute
        self.button_manager = ButtonManager(self)  # Initialize ButtonManager
        self.create_widgets()

    def create_widgets(self):
        # Create the widgets for the HydraulicMenu
        buttons = [
            {"text": BUTTON_TEXTS[0], "input": True},
            {"text": BUTTON_TEXTS[1], "input": True},
            {"text": BUTTON_TEXTS[2], "command": self.send_command},
            {
                "text": BUTTON_TEXTS[3],
                "command": lambda: self.controller.switch_to_menu("control_menu"),
            },
        ]

        for i, button in enumerate(buttons):
            if button.get("input"):
                self.create_input_field(i, button)
            else:
                self.create_button(i, button)

    def create_input_field(self, i, button):
        # Create a validation command
        vcmd = (self.register(self.validate_integer), "%P")

        # Create an input field with the validation command
        entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        entry.grid(row=i, column=1, sticky="w", padx=10, pady=5)

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

        # Bind a key to a function that sets the focus to the input field
        self.bind(str(i + 1), lambda event: entry.focus_set())

        # Store the Entry widget for later use
        self.entries.append(entry)

    def validate_integer(self, new_value):
        # If the new value is empty or a valid integer, allow the change
        if new_value == "" or new_value.isdigit():
            return True
        # Otherwise, discard the change
        return False

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

    def ok_command(self, event=None):
        if event is not None:
            # Stop the event from propagating further
            event.tkinter_event_stop_propagation()

        # Get the values from the Entry widgets
        cylinder = self.entries[0].get()
        position = self.entries[1].get()

        # Move focus back to the menu
        self.show()

    def delete_command(self):
        # Clear the Entry widgets
        for entry in self.entries:
            entry.delete(0, tk.END)

    def send_command(self):
        # Send the command to set the cylinder position
        # Check if the hydraulic device is offline
        # if self.device_statuses.get("hydraulic") != "online":
        #     raise ValueError("Hydraulic device is offline. Cannot send command.")

        # try:
        #     cylinder = int(self.cylinder_entry.get())
        #     position = int(self.position_entry.get())
        # except ValueError:
        #     print("Please enter valid integers for cylinder and position.")
        #     return

        # if not 0 <= cylinder <= 3:
        #     print("Cylinder value must be between 0 and 3.")
        #     return

        # if not 0 <= position <= 180:
        #     print("Position value must be between 0 and 180.")
        #     return

        # topic = f"device/{DEVICE_1}/set_cylinder_position"
        # message = f"set_cylinder:{cylinder},set_position:{position}"
        # self.controller.mqtt_publisher.publish_command(topic, message)

        cylinder = self.entries[0].get()
        position = self.entries[1].get()
        print("Send command button clicked: ", cylinder, position)
