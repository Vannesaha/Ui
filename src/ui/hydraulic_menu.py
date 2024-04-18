# hydraulic_menu.py

import tkinter as tk


class HydraulicMenu:
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master  # Save the master window

        # Create a frame to contain the buttons
        self.frame = tk.Frame(master)
        self.frame.pack(fill="both", expand=True)

        # List of button configurations
        buttons = [
            {
                "text": "  1. Aseta sylinteri",
                "command": self.set_cylinder,
            },  # no action
            {"text": "  2. Aseta asento", "command": self.set_position},  # no action
            {"text": "  3. Lähetä käsky", "command": self.send_command},  # no action
            {"text": "  4. Back", "command": self.controller.back_to_control_menu},
        ]

        # Create buttons from the configurations
        self.buttons = []
        for i, button in enumerate(buttons):
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
        self.hyd_status.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        self.embed_status = tk.Label(self.frame, text="Embedded Device Status: ")
        self.embed_status.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    def set_cylinder(self):
        print("Set cylinder clicked")

    def set_position(self):
        print("Set positions clicked")

        # Create a new top-level window
        # self.positions_window = tk.Toplevel(self.master)

        # # Create cylinder label and entry
        # self.cylinder_label = tk.Label(self.positions_window, text="Enter cylinder value")
        # self.cylinder_label.pack()
        # self.cylinder_entry = tk.Entry(self.positions_window)
        # self.cylinder_entry.pack()

        # # Create position label and entry
        # self.position_label = tk.Label(self.positions_window, text="Enter position value")
        # self.position_label.pack()
        # self.position_entry = tk.Entry(self.positions_window)
        # self.position_entry.pack()

        # # Create submit button
        # self.submit_button = tk.Button(self.positions_window, text="OK", command=self.send_command)
        # self.submit_button.pack()

    def send_command(self):
        print("Send command clicked")


#         cylinder = self.cylinder_entry.get()
#         position = self.position_entry.get()
#         print(f"Sending command to set cylinder {cylinder} to position {position}")
#         # Add your logic here to send the command
#         self.positions_window.destroy()  # Close the positions window
