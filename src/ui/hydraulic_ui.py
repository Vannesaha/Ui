from config.settings import DEVICE_1


def get_user_command():
    # This function now asks the user for a cylinder number and a position
    cylinder = int(
        input("Enter the number of the cylinder you want to control (1-4): ")
    )
    position = int(input("Enter a position (0-99): "))
    return "set_position", cylinder, position


def hydraulic_ui():
    print("Press '1' then Enter to set a position, or just Enter to exit.")
    cmd = input()  # Wait for user input

    if cmd == "1":
        # Example command generation logic
        action, cylinder, value = (
            get_user_command()
        )  # Assuming this is defined elsewhere
        topic = f"device/{DEVICE_1}"
        command = f"{action}:{cylinder}:{value}"
    else:
        topic = command = None

    return topic, command
