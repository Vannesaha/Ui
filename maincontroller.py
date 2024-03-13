# src/maincontroller.py

from PyQt6.QtCore import QObject, pyqtSignal as Signal
from src.ui.start_menu.start_menu import Start_Menu
from src.ui.control_menu.control_menu import Control_Menu


class MainController(QObject):
    # Define signals that will communicate across different parts of the application
    openControlMenuSignal = Signal()  # Signal to open the control menu

    def __init__(self):
        super().__init__()
        self.control_menu = None  # Initialize with None
        self.openControlMenuSignal.connect(self.openControlMenu)

    def startApplication(self):
        self.start_menu = Start_Menu(controller=self)
        self.start_menu.show()

    def openControlMenu(self):
        if not self.control_menu:
            self.control_menu = Control_Menu()
        self.control_menu.show()
