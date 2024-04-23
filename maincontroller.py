# maincontroller.py

import tkinter as tk
import platform

from src.ui.control_menu import ControlMenu
from src.ui.start_menu import StartMenu
from src.ui.hydraulic_menu import HydraulicMenu
from src.utils.mqtt_publisher import MQTTPublisher  # Import the MQTTPublisher class
from src.utils.update_status import update_status  # Import the update_status function


class MainController:
    def __init__(self):
        # Create the root window
        self.root = tk.Tk()
        self.root.title("Vannesaha")

        # Set the window size
        self.set_window_size(self.root)

        # Create frames for menu, status, and other
        self.menu_frame = tk.Frame(self.root, borderwidth=2, relief="solid")
        self.status_frame = tk.Frame(self.root, borderwidth=2, relief="solid")
        self.other_frame = tk.Frame(self.root, borderwidth=2, relief="solid")

        # Create a title label for the menu_frame
        menu_frame_title = tk.Label(
            self.menu_frame, text="Menu Frame", font=("Arial", 16)
        )
        menu_frame_title.pack()
        # Create a title label for the status_frame
        status_frame_title = tk.Label(
            self.status_frame, text="Status Frame", font=("Arial", 16)
        )
        status_frame_title.pack()
        # Create a title label for the other_frame
        other_frame_title = tk.Label(
            self.other_frame, text="Other Frame", font=("Arial", 16)
        )
        other_frame_title.pack()

        # Grid configuration
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)

        # Pack the frames into the root window
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.status_frame.grid(row=0, column=1, sticky="nsew")
        self.other_frame.grid(row=1, column=1, sticky="nsew")

        # Create the start menu in the menu frame
        self.start_menu = StartMenu(self.menu_frame, self)
        self.start_menu.pack(fill="both", expand=True)

        # Initialize and run the MQTT publisher
        self.mqtt_publisher = MQTTPublisher(self)
        self.mqtt_publisher.run()

        self.device_statuses = {}  # Add a dictionary to store device statuses

        # Add hydraulic and embedded device statuses
        self.hyd_status = tk.Label(self.status_frame, text="Hydraulic Status: ")
        self.hyd_status.pack()

        self.embed_status = tk.Label(self.status_frame, text="Embedded Device Status: ")
        self.embed_status.pack()

    def start(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    def set_window_size(self, window):
        # Get the screen size
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Set the maximum size for your application
        max_width = 1024  # Replace with your maximum width
        max_height = 600  # Replace with your maximum height
        # max_width = 800  # Replace with your maximum width
        # max_height = 480  # Replace with your maximum height

        # If the screen size is smaller than the maximum size, set the window size to the screen size
        if screen_width < max_width and screen_height < max_height:
            window.geometry(f"{screen_width}x{screen_height}")
        else:
            # If the screen size is larger than the maximum size, set the window size to the maximum size
            window.geometry(f"{max_width}x{max_height}")

    def update_status_frame(self, device_id, status):
        # Create a label for the status_frame
        status_label = tk.Label(
            self.status_frame, text=f"{device_id}: {status}", font=("Arial", 16)
        )
        status_label.pack()

    def open_control_menu(self):
        print("Control menu button clicked")
        # Hide the start menu
        self.start_menu.pack_forget()
        # Create a ControlMenu
        self.control_menu = ControlMenu(self.start_window, self)
        self.control_menu.pack(fill="both", expand=True)

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
        self.set_window_size(hydraulic_window)
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

        # Update the status in the status frame
        if device_id == "hydraulic":
            update_status(self.hyd_status, status)
        elif device_id == "embedded":
            update_status(self.embed_status, status)

        print(device_id, status)  # Emit the signal with the provided parameters
