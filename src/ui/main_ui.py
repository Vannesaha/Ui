# main_ui.py

from config.settings import DEVICE_1, DEVICE_2, DEVICE_3
from src.ui.hydraulic_ui import hydraulic_ui
import time

# Import the UI functions for the other devices
# from src.ui.pneumatic_ui import pneumatic_ui
# from src.ui.electrical_ui import electrical_ui


def main_ui(publisher):
    while True:  # This creates an infinite loop
        print("Select a device to control:")
        print("1: Hydraulic")
        print("2: check online status")
        print("3: Electrical")
        print("4: Shut down")

        cmd = input()  # Wait for user input

        if cmd == "1":
            if publisher.check_online_status("hydraulic") == "online":
                topic, command = hydraulic_ui()
                return topic, command
            else:
                time.sleep(2)
                continue  # Return to the main menu
        elif cmd == "2":
            publisher.check_online_status("hydraulic")
            time.sleep(2)
            return None, None  # Return a tuple instead of None

        elif cmd == "3":
            print("There is no function yet")
            time.sleep(2)
            return None, None  # Return a tuple instead of None

        elif cmd == "4":
            print("Shutting down the application.")
            time.sleep(2)
            return "exit", None  # Return a tuple instead of None

            # Here you can call any cleanup or shutdown functions you have
            break  # This will break the infinite loop and exit the application
        else:
            print("Invalid input, please try again.")
            time.sleep(2)
            return None, None  # Return a tuple instead of Non
