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
