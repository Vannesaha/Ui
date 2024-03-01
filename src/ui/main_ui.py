# main_ui.py

from src.mqtt_publisher import MQTTPublisher
from src.ui.hydraulic_ui import hydraulic_ui
from src.utils.device_status import check_online_status

import time


# Import the UI functions for the other devices
# from src.ui.pneumatic_ui import pneumatic_ui
# from src.ui.electrical_ui import electrical_ui


def main_ui(publisher):
    while True:  # This creates an infinite loop
        print("Select a device to control:")
        print("1: Hydraulic")
        print("2: embedded")
        print("3: hydraulic status")
        print("4: embedded status")
        print("5: Exit")

        cmd = input()  # Wait for user input

        if cmd == "1":
            if check_online_status(publisher.device_statuses, "hydraulic") == "online":
                topic, command = hydraulic_ui()
                return topic, command
            else:
                print("The hydraulic device is offline. Please try again later.")
                continue  # Return to the main menu
        elif cmd == "2":
            print("No function yet. Please try again.")
            time.sleep(2)
            return None, None  # Return a tuple instead of None

        elif cmd == "3":
            publisher.publish_command("device/hydraulic", "get_status")
            status = check_online_status(publisher.device_statuses, "hydraulic")
            print(f"Hydraulic device status: {status}")
            time.sleep(2)
            return None, None  # Return a tuple instead of None

        elif cmd == "4":
            publisher.publish_command("device/embedded", "get_status")
            status = check_online_status(publisher.device_statuses, "embedded")
            print(f"Embedded device status: {status}")
            time.sleep(2)
            return None, None  # Return a tuple instead of None

        elif cmd == "5":
            print("Shutting down the application.")
            time.sleep(2)
            return "exit", None  # Return a tuple instead of None

        else:
            print("No function yet. Please try again.")
            time.sleep(2)
            return None, None  # Return a tuple instead of Non
