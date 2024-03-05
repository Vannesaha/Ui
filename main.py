# run_ui.py

from src.mqtt_publisher import MQTTPublisher  # Import the MQTTPublisher class
from PyQt6.QtCore import QCoreApplication
from src.ui.main_ui.gui import Gui  # Import the Gui class
import time  # Import the time module


def main():
    global exit_flag

    publisher = MQTTPublisher()
    publisher.run()

    # Wait until the connection is established before entering the loop
    while not publisher.is_connected():
        time.sleep(0.1)  # Sleep for a short time to avoid busy waiting

    # Create an instance of Gui and run it
    gui = Gui(publisher)
    gui.run()

    # Clean up and disconnect
    publisher.disconnect()


if __name__ == "__main__":
    main()
