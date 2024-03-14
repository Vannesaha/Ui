# maincontroller.py

from PyQt6.QtCore import QObject, pyqtSignal as Signal
from PyQt6.QtQml import QQmlApplicationEngine
from src.ui.start_menu.start_menu import Start_Menu
from src.ui.control_menu.control_menu import Control_Menu
from src.utils.mqtt_publisher import MQTTPublisher


class MainController(QObject):
    # Define signals that will communicate across different parts of the application
    openControlMenuSignal = Signal()  # Signal to open the control menu
    goBackStartMenuSignal = Signal()  # Signal to go back to the start menu

    def __init__(self):
        super().__init__()
        self.engine = QQmlApplicationEngine()
        self.control_menu = None  # Initialize with None

        # Initialize MQTTPublisher here but don't start it yet
        self.mqtt_publisher = MQTTPublisher(self)
        # Assuming MQTTPublisher takes a reference to MainController

        # Connect the signals to the methods
        self.openControlMenuSignal.connect(self.openControlMenu)
        self.goBackStartMenuSignal.connect(self.goBackStartMenu)

    def startApplication(self):
        self.start_menu = Start_Menu(controller=self, engine=self.engine)
        self.control_menu = Control_Menu(controller=self, engine=self.engine)
        self.start_menu.show()
        # Now that the GUI is ready, start the MQTT publisher
        self.mqtt_publisher.run()

    def openControlMenu(self):
        self.start_menu.hide()
        self.control_menu.show()

    def goBackStartMenu(self):
        self.control_menu.hide()
        self.start_menu.show()
