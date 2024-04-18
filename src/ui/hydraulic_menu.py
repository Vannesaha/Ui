# hydraulic_menu.py

import tkinter as tk
from tkinter import simpledialog
from config.settings import DEVICE_1


class HydraulicMenu:
    def __init__(self, master, controller, device_statuses):
        self.controller = controller
        self.master = master  # Save the master window
        self.device_statuses = device_statuses  # Save the device statuses

        # Create a frame to contain the buttons
        self.frame = tk.Frame(master)
        self.frame.pack(fill="both", expand=True)

        # List of button configurations
        buttons = [
            {
                "text": "  1. Aseta sylinteri 0-3",
                "input": True,
            },
            {
                "text": "  2. Aseta sylinterin paikka 0-180",
                "input": True,
            },
            {"text": "  3. Send Command", "command": self.send_command},
            {"text": "  4. Back", "command": self.controller.back_to_control_menu},
        ]

        # Create buttons and input boxes from the configurations
        self.buttons = []
        for i, button in enumerate(buttons):
            if button.get("input"):
                label = tk.Label(self.frame, text=button["text"])
                label.grid(row=i, column=0, sticky="w", padx=5, pady=5)
                entry = tk.Entry(self.frame)
                entry.grid(row=i, column=1, sticky="w", padx=5, pady=5)
                if button["text"] == "  1. Aseta sylinteri 0-3":
                    self.cylinder_entry = entry
                else:
                    self.position_entry = entry
            else:
                btn = tk.Button(
                    self.frame,
                    text=button["text"],
                    command=button["command"],
                    width=20,
                    anchor="w",
                )
                btn.grid(row=i, column=0, sticky="w", padx=5, pady=5)
                self.buttons.append(btn)

        # Add hydraulic and embedded device statuses
        self.hyd_status = tk.Label(self.frame, text="Hydraulic Status: ")
        self.hyd_status.grid(row=len(buttons), column=0, sticky="w", padx=5, pady=5)

        self.embed_status = tk.Label(self.frame, text="Embedded Device Status: ")
        self.embed_status.grid(
            row=len(buttons) + 1, column=0, sticky="w", padx=5, pady=5
        )

    def send_command(self):

        # Check if the hydraulic device is offline
        if self.device_statuses.get("hydraulic") == "offline":
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

        topic = f"device/{DEVICE_1}/{cylinder}"
        command = f"set_hydraulic:{position}"
        self.controller.mqtt_publisher.publish_command(
            topic, command
        )  # Publish the command
