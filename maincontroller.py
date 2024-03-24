# maincontroller.py

# Importing necessary modules
from PyQt6.QtCore import (
    QObject,
    pyqtSignal as Signal,
    pyqtSignal,
    pyqtSlot,
)  # QObject is the base class to most PyQt classes, pyqtSignal and pyqtSlot are used for inter-object communication
from PyQt6.QtQml import (
    QQmlApplicationEngine,
)  # QQmlApplicationEngine provides a convenient way to load an application from one or more QML files

# Importing custom modules
from src.ui.start_menu.start_menu import Start_Menu
from src.ui.control_menu.control_menu import Control_Menu
from src.utils.mqtt_publisher import MQTTPublisher
from src.ui.hydraulic_menu.hydraulic_menu import Hydraulic_Menu


# MainController class inherits from QObject
class MainController(QObject):
    # Define signals that will communicate across different parts of the application
    updateStatusSignal = pyqtSignal(
        str, str
    )  # Signal to update the status of a devices multiple locations

    # Constructor
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.engine = (
            QQmlApplicationEngine()
        )  # Create an instance of QQmlApplicationEngine
        self.control_menu = None  # Initialize with None
        self.hydraulic_menu = None  # Initialize with None

        # Initialize MQTTPublisher here but don't start it yet
        self.mqtt_publisher = MQTTPublisher(self)
        # Assuming MQTTPublisher takes a reference to MainController

    # Method to start the application
    def startApplication(self):
        # Create instances of Start_Menu, Control_Menu, and Hydraulic_Menu
        self.start_menu = Start_Menu(controller=self, engine=self.engine)
        self.control_menu = Control_Menu(controller=self, engine=self.engine)
        self.hydraulic_menu = Hydraulic_Menu(
            controller=self, engine=self.engine, mqtt_publisher=self.mqtt_publisher
        )  # Initialize the Hydraulic_Menu
        self.start_menu.show()  # Show the start menu
        # Now that the GUI is ready, start the MQTT publisher
        self.mqtt_publisher.run()

    # Method to hide all windows
    def hideAllWindows(self):
        self.start_menu.hide()
        self.control_menu.hide()
        self.hydraulic_menu.hide()

    # Slot to open the control menu
    @pyqtSlot()  # The @pyqtSlot() is a decorator in PyQt, a Python binding of the cross-platform GUI toolkit Qt.
    def openControlMenu(self):
        self.hideAllWindows()  # Hide all windows
        self.control_menu.show()  # Show the control menu

    # Slot to open the hydraulic menu
    @pyqtSlot()  # The @pyqtSlot() is a decorator in PyQt, a Python binding of the cross-platform GUI toolkit Qt.
    def openHydraulicMenu(self):  # Method to open the hydraulic menu
        self.hideAllWindows()  # Hide all windows
        self.hydraulic_menu.show()  # Show the hydraulic menu

    # Slot to go back to the start menu
    @pyqtSlot()  # The @pyqtSlot() is a decorator in PyQt, a Python binding of the cross-platform GUI toolkit Qt.
    def goBackStartMenu(self):  # this shoulbe maned as openStartMenu
        self.hideAllWindows()  # Hide all windows
        self.start_menu.show()  # Show the start menu

    # Slot to go back to the control menu
    @pyqtSlot()  # The @pyqtSlot() is a decorator in PyQt, a Python binding of the cross-platform GUI toolkit Qt.
    def goBackControlMenu(self):  # this should be named as openControlMenu
        self.hideAllWindows()  # Hide all windows
        self.control_menu.show()  # Show the control menu

    # Method to emit the updateStatusSignal in control_meny.qml and hydraulic_menu.qml
    def sendStatusUpdate(self, device_id, status):
        self.updateStatusSignal.emit(
            device_id, status
        )  # Emit the signal with the provided parameters
