# control_menu.py

import tkinter as tk


class ControlMenu:
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master  # Save the master window

        # Create a frame to contain the buttons
        self.frame = tk.Frame(master)
        self.frame.pack(fill="both", expand=True)

        # List of button configurations
        buttons = [
            {
                "text": "  1. Testaa ja kytke yhteydet",
                "command": self.test_connection,
            },  # no action
            {"text": "  2. Testaa hydrauliikka", "command": self.open_hydraulic_menu},
            # opens hydraulic menu
            {
                "text": "  3. Testaa sahakelkka",
                "command": self.test_saw_movemend,
            },  # no action
            {
                "text": "  4. Testaa terämoottori",
                "command": self.test_blade_motor,
            },  # no action
            {
                "text": "  5. Testaa teräohjuri",
                "command": self.test_blade_direction,
            },  # no action
            {
                "text": "  6. Testaa perkkuuterä",
                "command": self.test_blade,
            },  # no action
            {"text": "  7. Anturit", "command": self.test_sensors},
            # no action
            {
                "text": "  8. takaisin",
                "command": self.controller.back_to_start_menu,
            },  # back to start menu
        ]

        # Create buttons from the configurations
        self.buttons = []
        for i, button in enumerate(buttons):
            btn = tk.Button(
                self.frame,
                text=button["text"],
                command=button.get(
                    "command", None
                ),  # If the command key is not found, set it to None
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

    def test_connection(self):
        print("Test connection button clicked")
        # Add your logic here

    def open_hydraulic_menu(self):
        print("Test hyrdraulics button clicked")
        self.controller.open_hydraulic_menu()  # Call the open_hydraulic_menu method in the controller
        # Add your logic here

    def test_saw_movemend(self):
        print("Test saw movement button clicked")
        # Add your logic here

    def test_blade_motor(self):
        print("Test blade motor button clicked")
        # Add your logic here

    def test_blade_direction(self):
        print("Test blade direction button clicked")
        # Add your logic here

    def test_blade(self):
        print("Test blade button clicked")
        # Add your logic here

    def test_sensors(self):
        print("Test sensors button clicked")
        # Add your logic here
