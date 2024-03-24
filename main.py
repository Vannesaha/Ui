# src/main.py

# Importing necessary modules
from PyQt6.QtGui import (
    QGuiApplication,
)  # QGuiApplication class is a part of PyQt6 library, it manages the GUI application's control flow and main settings
from maincontroller import (
    MainController,
)  # MainController is a custom class that controls the application's flow

import sys  # sys module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter


# Define the main function
def main():
    app = QGuiApplication(
        sys.argv
    )  # Create an instance of QGuiApplication. sys.argv is a list in Python, which contains the command-line arguments passed to the script
    controller = MainController()  # Create an instance of MainController
    controller.startApplication()  # Start the application via the controller
    sys.exit(
        app.exec()
    )  # Enter the main event loop and wait until exit() is called, then return the value that was set to exit(). This is a neat way to keep the script running


# This is a Python standard boilerplate that allows or prevents parts of code from being run when the modules are imported.
if __name__ == "__main__":
    main()  # Call the main function
