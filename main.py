# Assuming this file is at the root of your project structure
# run_ui.py

from src.mqtt_publisher import MQTTPublisher  # Import the MQTTPublisher class
from src.ui.hydraulic_ui import hydraulic_ui  # Import the main_ui function

import time  # Import the time module


def main():
    publisher = MQTTPublisher()
    publisher.run()

    # Wait until the connection is established before entering the loop
    while not publisher.is_connected():
        time.sleep(0.1)  # Sleep for a short time to avoid busy waiting

    while True:
        # Obtain command from the UI
        topic, command = hydraulic_ui()

        if topic and command:
            # Publish the command
            publisher.publish_command(topic, command)
        else:
            break  # Exit loop if any other input

    # Clean up and disconnect
    publisher.disconnect()


if __name__ == "__main__":
    main()
