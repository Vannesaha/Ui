# control_menu.py
import tkinter as tk


class ControlMenu(tk.Frame):
    """A control menu frame with various buttons for testing different functionalities."""

    def __init__(self, parent, controller):
        """Initialize the ControlMenu with a parent frame and a controller."""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        """Create buttons from the configurations."""
        buttons = [
            # List of button configurations
            {"text": "  1. Testaa ja kytke yhteydet", "command": self.test_connection},
            {"text": "  2. Testaa hydrauliikka", "command": self.test_hydraulics},
            {"text": "  3. Testaa sahakelkka", "command": self.test_saw_movemend},
            {"text": "  4. Testaa terämoottori", "command": self.test_blade_motor},
            {"text": "  5. Testaa teräohjuri", "command": self.test_blade_direction},
            {"text": "  6. Testaa perkkuuterä", "command": self.test_blade},
            {"text": "  7. Anturit", "command": self.test_sensors},
            {"text": "  8. takaisin", "command": self.controller.back_to_start_menu},
        ]

        for i, button in enumerate(buttons):
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

    def show(self):
        # Show the ControlMenu frame itself
        self.pack(fill="both", expand=True)

    def hide(self):
        # Hide the ControlMenu frame
        self.pack_forget()

    # def get_main_widget(self):
    #     # Return the main frame
    #     return self.main_frame

    def test_connection(self):
        print("Test connection button clicked")

    def test_hydraulics(self):
        print("Test hyrdraulics button clicked")
        # Open the hydraulic menu when the button is clicked
        self.controller.open_hydraulic_menu()

    def test_saw_movemend(self):
        print("Test saw movement button clicked")

    def test_blade_motor(self):
        print("Test blade motor button clicked")

    def test_blade_direction(self):
        print("Test blade direction button clicked")

    def test_blade(self):
        print("Test blade button clicked")

    def test_sensors(self):
        print("Test sensors button clicked")
