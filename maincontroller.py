# maincontroller.py

from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSignal, pyqtSlot
from PyQt6.QtQml import QQmlApplicationEngine

from src.ui.start_menu.start_menu import Start_Menu
from src.ui.control_menu.control_menu import Control_Menu
from src.utils.mqtt_publisher import MQTTPublisher
from src.ui.hydraulic_menu.hydraulic_menu import Hydraulic_Menu


class MainController(QObject):
    # Define signals that will communicate across different parts of the application
    openControlMenuSignal = Signal()  # Signal to open the control menu
    openHydraulicMenuSignal = Signal()  # Signal to open the hydraulic menu

    goBackStartMenuSignal = Signal()  # Signal to go back to the start menu
    goBackControlMenuSignal = Signal()  # Signal to go back to the control menu

    updateStatusSignal = pyqtSignal(str, str)  # Signal to update the status of a device

    def __init__(self):
        super().__init__()
        self.engine = QQmlApplicationEngine()
        self.control_menu = None  # Initialize with None
        self.hydraulic_menu = None  # Initialize with None

        # Initialize MQTTPublisher here but don't start it yet
        self.mqtt_publisher = MQTTPublisher(self)
        # Assuming MQTTPublisher takes a reference to MainController

        # Connect the signals to the methods
        self.openControlMenuSignal.connect(self.openControlMenu)
        self.openHydraulicMenuSignal.connect(
            self.openHydraulicMenu
        )  # Connect the signal to the method

        # Connect the signals to the back methods
        self.goBackStartMenuSignal.connect(self.goBackStartMenu)
        self.goBackControlMenuSignal.connect(self.goBackControlMenu)

    def startApplication(self):
        self.start_menu = Start_Menu(controller=self, engine=self.engine)
        self.control_menu = Control_Menu(controller=self, engine=self.engine)
        self.hydraulic_menu = Hydraulic_Menu(
            controller=self, engine=self.engine, mqtt_publisher=self.mqtt_publisher
        )  # Initialize the Hydraulic_Menu
        self.start_menu.show()
        # Now that the GUI is ready, start the MQTT publisher
        self.mqtt_publisher.run()

    # Window functions
    def hideAllWindows(self):
        self.start_menu.hide()
        self.control_menu.hide()
        self.hydraulic_menu.hide()

    def openControlMenu(self):
        self.hideAllWindows()
        self.control_menu.show()

    def openHydraulicMenu(self):  # Method to open the hydraulic menu
        self.hideAllWindows()
        self.hydraulic_menu.show()

    def goBackStartMenu(self):
        self.hideAllWindows()
        self.start_menu.show()

    def goBackControlMenu(self):
        self.hideAllWindows()
        self.control_menu.show()

    # Emit signals functions
    def sendStatusUpdate(self, device_id, status):
        self.updateStatusSignal.emit(device_id, status)
