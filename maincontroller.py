# maincontroller.py

import tkinter as tk
import platform

from src.menus.control_menu import ControlMenu
from src.menus.start_menu import StartMenu
from src.menus.hydraulic_menu import HydraulicMenu
from src.utils.mqtt_publisher import MQTTPublisher  # Import the MQTTPublisher class
from src.utils.update_status import update_status  # Import the update_status function
from src.utils.window_utils import set_window_size  # Import the set_window_size
from src.menus.button_manager import ButtonManager


ROOT_TITLE = "Vannesaha"
MENU_FRAME_TITLE = "Valikko"
STATUS_FRAME_TITLE = "Laitteiden tila"
OTHER_FRAME_TITLE = "Navigointi"

# Define a dictionary of status labels and their corresponding texts
STATUS_LABELS = {
    "hydraulic": "Hydraulic Status: ",
    "embedded": "Embedded Device Status: ",
    # Add more labels here
}  # status comes from the MQTT message

EXAMPLE_BUTTON_1_TEXT = "Button 1"
EXAMPLE_BUTTON_2_TEXT = "Button 2"
EXAMPLE_BUTTON_3_TEXT = "Button 3"
EXAMPLE_BUTTON_4_TEXT = "Button 4"
EXAMPLE_BUTTON_5_TEXT = "Button 5"


class MainController:
    def __init__(self):
        # Create the root window
        self.root = tk.Tk()
        self.root.title(ROOT_TITLE)

        # Set the window size
        set_window_size(self.root)

        # Create frames for menu, status, and other
        self.menu_frame = self.create_menu_frame()
        self.status_frame = self.create_status_frame()
        self.other_frame = self.create_other_frame()

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
        self.other_frame.grid(row=1, column=1, sticky="nsew")

        # Create the start menu and control menu in the menu frame
        self.start_menu = StartMenu(self.menu_frame, self)
        self.control_menu = ControlMenu(self.menu_frame, self)
        self.hydraulic_menu = HydraulicMenu(self.menu_frame, self)

        # Initially, only the start menu is visible
        self.start_menu.pack(fill="both", expand=True)
        # self.control_menu.hide()  # Hide the control menu
        # self.hydraulic_menu.hide()  # Hide the hydraulic menu

        # Initialize and run the MQTT publisher
        self.mqtt_publisher = MQTTPublisher(self)
        self.mqtt_publisher.run()

        self.device_statuses = {}  # Add a dictionary to store device statuses

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

    def create_menu_frame(self):
        """Create the menu frame and its components."""
        menu_frame = tk.Frame(self.root, borderwidth=2, relief="solid")

        # Create a title label for the frame
        menu_frame_title = tk.Label(
            menu_frame, text=MENU_FRAME_TITLE, font=("Arial", 16)
        )
        menu_frame_title.pack(
            anchor="center", padx=10, pady=10
        )  # Add padding to the title

        # Configure menu_frame to fill the whole column and stick to the top
        menu_frame.pack(fill="both", expand=True, side="left")

        return menu_frame  # Return the menu_frame object

    def create_status_frame(self):
        """Create the status frame and its components."""
        status_frame = tk.Frame(self.root, borderwidth=2, relief="solid")

        # Create a title label for the frame
        status_frame_title = tk.Label(
            status_frame, text=STATUS_FRAME_TITLE, font=("Arial", 16)
        )
        status_frame_title.pack(fill="x", padx=10, pady=10)

        # Create labels and map device IDs to status labels
        self.device_labels = {}
        for device_id, label_text in STATUS_LABELS.items():
            label = tk.Label(status_frame, text=label_text)
            label.pack()
            self.device_labels[device_id] = label

        return status_frame  # Return the status frame

    def sendStatusUpdate(self, device_id, status):
        self.device_statuses[device_id] = status  # Update the status in the dictionary

        # Update the status in the status frame
        label = self.device_labels.get(device_id)
        if label is not None:
            update_status(
                label, status
            )  # Update the status label with update_status function

        print(device_id, status)  # Emit the signal with the provided parameters

    def create_other_frame(self):
        """Create the other frame and its components."""
        other_frame = tk.Frame(self.root, borderwidth=2, relief="solid")

        # Create a title for the other_frame
        other_frame_title = tk.Label(other_frame, text=OTHER_FRAME_TITLE)
        other_frame_title.grid(row=0, column=0, columnspan=5, sticky="ew")

        # Create a ButtonManager for the other_frame
        self.button_manager = ButtonManager(other_frame)

        # Create buttons in the other_frame using grid method
        example_button1 = self.button_manager.create_button(
            EXAMPLE_BUTTON_1_TEXT, self.example_button_command1
        )
        example_button1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        example_button2 = self.button_manager.create_button(
            EXAMPLE_BUTTON_2_TEXT, self.example_button_command2
        )
        example_button2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        example_button3 = self.button_manager.create_button(
            EXAMPLE_BUTTON_3_TEXT, self.example_button_command3
        )
        example_button3.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        example_button4 = self.button_manager.create_button(
            EXAMPLE_BUTTON_4_TEXT, self.example_button_command4
        )
        example_button4.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

        example_button5 = self.button_manager.create_button(
            EXAMPLE_BUTTON_5_TEXT, self.example_button_command5
        )
        example_button5.grid(row=1, column=4, padx=5, pady=5, sticky="ew")

        # Configure the columns to have equal weight
        for i in range(5):
            other_frame.grid_columnconfigure(i, weight=1)

        return other_frame

    def example_button_command1(self):
        print("Example button 1 was clicked!")

    def example_button_command2(self):
        print("Example button 2 was clicked!")

    def example_button_command3(self):
        print("Example button 3 was clicked!")

    def example_button_command4(self):
        print("Example button 4 was clicked!")

    def example_button_command5(self):
        print("Example button 5 was clicked!")
