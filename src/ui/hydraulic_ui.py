from config.settings import DEVICE_1
import time


def get_user_command():
    # This function now asks the user for a cylinder number and a position
    position = int(input("Enter a position (0-99): "))
    return "set_position", position


def get_user_command_all():
    # This function now asks the user for a cylinder number and a position
    position = int(input("Enter a position for all (0-99): "))
    return "set_position", position


def hydraulic_ui():
    while True:
        print("Select a cylinder to control:")
        print("1: Cylinder 1")
        print("2: Cylinder 2")
        print("3: Cylinder 3")
        print("4: Cylinder 4")
        print("5: Move all cylinders")
        print("6: Main menu")

        cmd = input()  # Wait for user input

        if cmd in ["1", "2", "3", "4"]:
            # Example command generation logic
            _, position = get_user_command()
            topic = f"device/{DEVICE_1}/{cmd}"
            command = f"set_position:{position}"
            return topic, command

        elif cmd == "5":
            _, position = get_user_command_all()
            topic = f"device/{DEVICE_1}/all"
            command = f"set_position:{position}"
            return topic, command

        elif cmd == "6":
            return (
                "main_menu",
                None,
            )  # Return a special value to indicate that the user wants to return to the main menu

        else:
            print("Invalid input, please try again.")
            time.sleep(2)
            continue
        return topic, command
