# maincontroller.py

import tkinter as tk
import platform

from src.frames.main_frame import create_main_frame
from src.frames.info_frame import create_info_frame
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


class MainController:
    def __init__(self):
        # Create the root window

        self.root = create_main_frame()
        self.root.title(ROOT_TITLE)

        # Set the window size
        set_window_size(self.root)

        self.device_statuses = {}  # Add a dictionary to store device statuses
        self.device_labels = {}  # Add a dictionary to store device labels

        # Create frames for menu, status, and other
        self.info_frame = create_info_frame()
        self.menu_frame = create_menu_frame(
            self.root, self.ok_button_command, self.back_button_command
        )
        self.status_frame = create_status_frame(self.root, self.device_labels)
        self.navigation_frame = create_navigation_frame(
            self.root,
            self.up_command,
            self.down_command,
            self.left_command,
            self.right_command,
        )

        # Grid configuration
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Place the menu_frame
        self.menu_frame.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=(10, 5))
        # Place the navigation_frame and add padding on left and right sides
        self.navigation_frame.grid(
            row=1, column=0, sticky="nsew", padx=(10, 5), pady=(5, 10)
        )
        # Place the status_frame and add padding on left and right sides
        self.status_frame.grid(
            row=0, column=1, sticky="nsew", padx=(5, 10), pady=(10, 5)
        )
        # place the info_frame
        self.info_frame.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=(5, 10))

        # Create the start menu and control menu in the menu frame
        self.start_menu = StartMenu(self.menu_frame, self)
        self.control_menu = ControlMenu(self.menu_frame, self)
        self.hydraulic_menu = HydraulicMenu(self.menu_frame, self)

        # Initially, only the start menu is visible
        self.start_menu.show()  # Show the start menu

        self.current_menu = self.start_menu  # Keep track of the current menu
        self.menu_stack = []  # Add a stack to keep track of the menu history

        # Initialize and run the MQTT publisher
        self.mqtt_publisher = MQTTPublisher(self)
        self.mqtt_publisher.run()

    def start(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    # Add a method to uodate statuses of devices in the status frame
    def sendStatusUpdate(self, device_id, status):
        self.device_statuses[device_id] = status  # Update the status in the dictionary

        # Update the status in the status frame
        label = self.device_labels.get(device_id)
        if label is not None:
            update_status(
                label, status
            )  # Update the status label with update_status function

        print(device_id, status)  # Emit the signal with the provided parameters

    # Add a method to switch between menus
    def switch_to_menu(self, menu_name):
        new_menu = getattr(self, f"{menu_name}")  # Get the menu object by name
        self.current_menu.hide()  # Hide the current menu
        new_menu.show()  # Show the new menu
        self.root.update_idletasks()  # Update the window to show the new menu
        self.menu_stack.append(
            self.current_menu
        )  # Push the current menu onto the stack
        self.current_menu = new_menu  # Update the current menu

    # Add method to handle back button click
    def back_button_command(self, event=None):
        if self.menu_stack:  # If there is a previous menu
            self.current_menu.hide()  # Hide the current menu
            previous_menu = (
                self.menu_stack.pop()
            )  # Pop the previous menu from the stack
            previous_menu.show()  # Show the previous menu
            self.root.update_idletasks()  # Update the window to show the previous menu
            self.current_menu = previous_menu  # Update the current menu
        print("Back button was clicked!")

    # Add method to handle ok button click in current_menu.ok_command() function
    def ok_button_command(self, event=None):
        self.current_menu.ok_command()
        print("OK button was clicked!")

    # Add method to handle delete button click in current_menu.delete_command() function
    def delete_button_command(self, event=None):
        self.current_menu.delete_command()
        print("Delete button was clicked!")

    def up_command(self, event=None):
        print("Ylös clicked")

    def down_command(self, event=None):
        print("Alas clicked")

    def left_command(self, event=None):
        print("Vasen clicked")

    def right_command(self, event=None):
        print("Oikea clicked")
