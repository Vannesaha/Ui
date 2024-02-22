from config.settings import DEVICE_1
import time


def get_user_command():
    # This function now asks the user for a cylinder number and a position
    cylinder = int(input("Enter the number of the cylinder (1-4): "))
    position = int(input("Enter a position (0-99): "))
    return "set_position", cylinder, position


def hydraulic_ui():
    while True:
        print("1: Set position")
        print("2: Main menu")

        cmd = input()  # Wait for user input

        if cmd == "2":
            return (
                "main_menu",
                None,
            )  # Return a special value to indicate that the user wants to return to the main menu

        if cmd == "1":
            # Example command generation logic
            action, cylinder, value = (
                get_user_command()
            )  # Assuming this is defined elsewhere
            topic = f"device/{DEVICE_1}"
            command = f"{action}:{cylinder}:{value}"
            time.sleep(2)
            # continue

        else:
            print("Invalid input, please try again.")
            time.sleep(2)
            continue
        return topic, command
