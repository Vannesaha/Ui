# maincontroller.py

import tkinter as tk
import platform

from src.frames.navigation_frame import create_navigation_frame
from src.frames.status_frame import create_status_frame
from src.frames.menu_frame import create_menu_frame

from src.menus.control_menu import ControlMenu
from src.menus.start_menu import StartMenu
from src.menus.hydraulic_menu import HydraulicMenu

from src.utils.mqtt_publisher import MQTTPublisher  # Import the MQTTPublisher class
from src.utils.update_status import update_status  # Import the update_status function
from src.utils.window_utils import set_window_size  # Import the set_window_size
from src.utils.button_manager import ButtonManager


ROOT_TITLE = "Vannesaha"
MENU_FRAME_TITLE = "Valikko"
STATUS_FRAME_TITLE = "Laitteiden tila"
OTHER_FRAME_TITLE = "Navigointi"


class MainController:
    def __init__(self):
        # Create the root window
        self.root = tk.Tk()
        self.root.title(ROOT_TITLE)

        # Set the window size
        set_window_size(self.root)

        self.device_statuses = {}  # Add a dictionary to store device statuses
        self.device_labels = {}  # Add a dictionary to store device labels

        # Create frames for menu, status, and other
        self.menu_frame = create_menu_frame(self.root)
        self.status_frame = create_status_frame(self.root, self.device_labels)
        self.navigation_frame = create_navigation_frame(
            self.root,
            self.ok_button_command,
            self.back_button_command,
            self.delete_button_command,
        )

        # Grid configuration
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Place the frames
        self.menu_frame.grid(
            row=0, column=0, rowspan=2, sticky="nsew"
        )  # Set rowspan to 2
        self.status_frame.grid(row=0, column=1, sticky="nsew")
        self.navigation_frame.grid(row=1, column=1, sticky="nsew")

        # Create the start menu and control menu in the menu frame
        self.start_menu = StartMenu(self.menu_frame, self)
        self.control_menu = ControlMenu(self.menu_frame, self)
        self.hydraulic_menu = HydraulicMenu(self.menu_frame, self)

        # Initially, only the start menu is visible
        self.start_menu.show()  # Show the start menu

        # Initialize and run the MQTT publisher
        self.mqtt_publisher = MQTTPublisher(self)
        self.mqtt_publisher.run()

    def start(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    # Add a method to switch between menus
    def switch_menu(self, menu_to_hide, menu_to_show):
        menu_to_hide.hide()
        menu_to_show.show()  # Show the new menu
        self.root.update_idletasks()  # Update the window to show the new menu

    def open_control_menu(self):
        print("Control menu button clicked")
        self.switch_menu(self.start_menu, self.control_menu)

    def open_hydraulic_menu(self):
        print("Test hydraulics button clicked")

        # Check if the hydraulic device is offline
        # if self.device_statuses.get("hydraulic") != "online":
        #  raise ValueError("Hydraulic device is offline. Cannot open hydraulic menu.")

        self.switch_menu(self.control_menu, self.hydraulic_menu)

    def back_to_start_menu(self):
        print("Back to start_menu button clicked")
        self.switch_menu(self.control_menu, self.start_menu)

    def back_to_control_menu(self):
        print("Back to control_menu button clicked")
        self.switch_menu(self.hydraulic_menu, self.control_menu)

    def sendStatusUpdate(self, device_id, status):
        self.device_statuses[device_id] = status  # Update the status in the dictionary

        # Update the status in the status frame
        label = self.device_labels.get(device_id)
        if label is not None:
            update_status(
                label, status
            )  # Update the status label with update_status function

        print(device_id, status)  # Emit the signal with the provided parameters

    def ok_button_command(self, event=None):
        print("OK button was clicked!")

    def back_button_command(self, event=None):
        print("Back button was clicked!")

    def delete_button_command(self, event=None):
        print("Delete button was clicked!")
