# src/main.py

from PyQt6.QtGui import QGuiApplication
from maincontroller import MainController
from src.ui.start_menu.start_menu import Start_Menu
import sys


def main():
    app = QGuiApplication(sys.argv)
    controller = MainController()
    controller.startApplication()  # Start the application via the controller
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


""" # main.py


from PyQt6.QtGui import QGuiApplication  # Import QGuiApplication
from PyQt6.QtCore import QCoreApplication
from src.ui.start_menu.start_menu import Start_Menu  # Import the Gui class

import sys  # Import sys


def main():
    global exit_flag

    # Create a QGuiApplication
    app = QGuiApplication(sys.argv)

    # Create an instance of Start_ui
    start_menu = Start_Menu()
    start_menu.run()

    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
 """
