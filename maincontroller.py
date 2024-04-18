# maincontroller.py

import tkinter as tk

from src.ui.control_menu import ControlMenu
from src.ui.start_menu import StartMenu
from src.ui.hydraulic_menu import HydraulicMenu
from src.utils.mqtt_publisher import MQTTPublisher  # Import the MQTTPublisher class
from src.utils.update_status import update_status  # Import the update_status function


class MainController:
    def __init__(self):
        # Create a StartMenu
        self.start_window = tk.Tk()
        self.start_window.title("Päävalikko")
        self.start_window.geometry("640x480")
        self.start_menu = StartMenu(self.start_window, self)

        # Initialize and run the MQTT publisher
        self.mqtt_publisher = MQTTPublisher(self)
        self.mqtt_publisher.run()

        self.device_statuses = {}  # Add a dictionary to store device statuses

    def start(self):
        # Run the Tkinter event loop
        self.start_window.mainloop()

    def open_control_menu(self):
        print("Control menu button clicked")
        # Hide the start window
        self.start_window.withdraw()
        # Create a ControlMenu
        control_window = tk.Toplevel()
        control_window.title("Control Menu")
        control_window.geometry("640x480")
        self.control_menu = ControlMenu(control_window, self)

        # Update the status in the control menu
        if "hydraulic" in self.device_statuses:
            update_status(
                self.control_menu.hyd_status, self.device_statuses["hydraulic"]
            )
        if "embedded" in self.device_statuses:
            update_status(
                self.control_menu.embed_status, self.device_statuses["embedded"]
            )

    def open_hydraulic_menu(self):
        print("Test hydraulics button clicked")

        # Check if the hydraulic device is offline
        if self.device_statuses.get("hydraulic") == "offline":
            raise ValueError("Hydraulic device is offline. Cannot open hydraulic menu.")

        # Hide the control window
        self.control_menu.master.withdraw()
        # Create a HydraulicMenu
        hydraulic_window = tk.Toplevel()
        hydraulic_window.title("Testaa hydrauliikka")
        hydraulic_window.geometry("640x480")
        self.hydraulic_menu = HydraulicMenu(
            hydraulic_window, self, self.device_statuses
        )

        # Update the status in the hydraulic menu
        if "hydraulic" in self.device_statuses:
            update_status(
                self.hydraulic_menu.hyd_status, self.device_statuses["hydraulic"]
            )
        if "embedded" in self.device_statuses:
            update_status(
                self.hydraulic_menu.embed_status, self.device_statuses["embedded"]
            )

    def back_to_start_menu(self):
        print("Back to start_menu button clicked")
        # Unhide the start window
        self.start_window.deiconify()
        # Hide the control window
        self.control_menu.master.withdraw()

    def back_to_control_menu(self):
        print("Back to control_menu button clicked")
        # Unhide the control window
        self.control_menu.master.deiconify()
        # Hide the hydraulic window
        self.hydraulic_menu.master.withdraw()

    # Method to emit the updateStatusSignal
    def sendStatusUpdate(self, device_id, status):
        self.device_statuses[device_id] = status  # Update the status in the dictionary

        # Update the status in the start menu
        if device_id == "hydraulic":
            update_status(self.start_menu.hyd_status, status)
        elif device_id == "embedded":
            update_status(self.start_menu.embed_status, status)

        # Update the status in the control menu
        if hasattr(self, "control_menu"):
            if device_id == "hydraulic":
                update_status(self.control_menu.hyd_status, status)
            elif device_id == "embedded":
                update_status(self.control_menu.embed_status, status)

        # Update the status in the hydraulic menu
        if hasattr(self, "hydraulic_menu"):
            if device_id == "hydraulic":
                update_status(self.hydraulic_menu.hyd_status, status)
            elif device_id == "embedded":
                update_status(self.hydraulic_menu.embed_status, status)

        print(device_id, status)  # Emit the signal with the provided parameters
