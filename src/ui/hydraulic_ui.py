from config.settings import DEVICE_1
import time


def get_cylinder_number():
    while True:
        cylinder = input("Enter a cylinder number (0-3): ")
        if cylinder in ["0", "1", "2", "3"]:
            return cylinder
        else:
            print("Invalid input, please try again.")
            time.sleep(2)


def get_cylinder_position():
    while True:
        position = int(input("Enter a position (0-180): "))
        if 0 <= position <= 180:
            return "set_position", position
        else:
            print("Invalid input, please try again.")
            time.sleep(2)


def hydraulic_ui():
    while True:
        cmd = get_cylinder_number()

        # Example command generation logic
        _, position = get_cylinder_position()
        topic = f"device/{DEVICE_1}/{cmd}"
        command = f"set_hydraulic:{position}"
        return topic, command
        # Publish the command
