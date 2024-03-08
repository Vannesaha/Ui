# main.py

from PyQt6.QtGui import QGuiApplication  # Import QGuiApplication
from PyQt6.QtCore import QCoreApplication
from src.ui.main_ui.gui import Gui
from src.ui.start_ui.start_ui import Start_ui

import sys  # Import sys


def main():
    global exit_flag

    # Create a QGuiApplication
    app = QGuiApplication(sys.argv)

    # Create an instance of Start_ui
    start_ui = Start_ui()
    start_ui.run()

    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
