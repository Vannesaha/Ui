# control_menu.py
import tkinter as tk
from src.menus.base_menu import BaseMenu
from src.utils.button_manager import ButtonManager


# control_menu.py

# Define button texts
BUTTON_TEXTS = [
    "1. Testaa ja kytke yhteydet",
    "2. Testaa hydrauliikka",
    "3. Testaa sahakelkka",
    "4. Testaa terämoottori",
    "5. Testaa teräohjuri",
    "6. Testaa perkkuuterä",
    "7. Anturit",
    "8. takaisin",
]


class ControlMenu(BaseMenu):
    """A control menu frame with various buttons for testing different functionalities."""

    def __init__(self, parent, controller):
        """Initialize the ControlMenu with a parent frame and a controller."""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.button_manager = ButtonManager(self)
        self.create_buttons()

    def create_buttons(self):
        """Create buttons from the configurations."""
        buttons = [
            {"text": BUTTON_TEXTS[0], "command": self.test_connection},
            {"text": BUTTON_TEXTS[1], "command": self.test_hydraulics},
            {"text": BUTTON_TEXTS[2], "command": self.test_saw_movemend},
            {"text": BUTTON_TEXTS[3], "command": self.test_blade_motor},
            {"text": BUTTON_TEXTS[4], "command": self.test_blade_direction},
            {"text": BUTTON_TEXTS[5], "command": self.test_blade},
            {"text": BUTTON_TEXTS[6], "command": self.test_sensors},
            {
                "text": BUTTON_TEXTS[7],
                "command": lambda: self.controller.switch_to_menu("start_menu"),
            },
        ]
        self.buttons = self.button_manager.create_menu_buttons(buttons)

    def test_connection(self):
        print("Test connection button clicked")

    def test_hydraulics(self):
        print("Test hyrdraulics button clicked")
        # Open the hydraulic menu when the button is clicked
        self.controller.switch_to_menu("hydraulic_menu")

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
