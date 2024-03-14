# control_menu.py

from PyQt6.QtCore import QUrl, QObject
import sys


# Define the Control_Menu class
class Control_Menu:
    # The constructor takes an engine as an argument
    def __init__(self, engine, controller):
        # Store the engine as an instance variable
        self.engine = engine
        self.loaded = False

        # Set the controller as a context property so it can be accessed from QML
        # This allows the QML code to interact with the controller object
        self.engine.rootContext().setContextProperty("controller", controller)

        # Load the QML file for the control menu
        self.engine.load(QUrl.fromLocalFile("src/ui/control_menu/control_menu.qml"))
        # If the QML file failed to load, print an error message and exit the program
        if not self.engine.rootObjects():
            print("Failed to load control_menu.qml")
            sys.exit(-1)

        # Get the root object of the control menu
        self.root = self.get_root_object()
        # If the root object couldn't be found, exit the program
        if self.root is None:
            sys.exit(-1)

    # Method to get the root object of the control menu
    def get_root_object(self):
        # Loop over all root objects in the engine
        for root in self.engine.rootObjects():
            # If the objectName of the root object is "control_menu", return it
            if root.objectName() == "control_menu":
                return root
        # If no root object with the objectName "control_menu" was found, print an error message and return None
        print("Did not find control_menu object")
        return None

    # Method to show the control menu
    def show(self):
        # If the root object is not None, set its "visible" property to True
        if self.root is not None:
            self.root.setProperty("visible", True)

    # Method to hide the control menu
    def hide(self):
        # If the root object is not None, set its "visible" property to False
        if self.root is not None:
            self.root.setProperty("visible", False)


""" # control_menu.py

from PyQt6.QtCore import QUrl, QObject, pyqtSignal as Signal
from PyQt6.QtCore import pyqtSlot as Slot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtQml import QQmlApplicationEngine, QQmlContext
from src.utils.device_status import check_online_status


import sys
from PyQt6.QtCore import pyqtProperty

from config.settings import (
    DEVICE_1,
    DEVICE_2,
)  # replace with the actual import statement


class Control_Menu(QObject):
    def __init__(self, parent=None, publisher=None):
        super().__init__()
        self.publisher = publisher
        self.app = QGuiApplication.instance()
        self.engine = QQmlApplicationEngine()
        self.context = self.engine.rootContext()
        self.statusChecked.connect(
            self.update_status
        )  # Connect the signal to the method

        self._device_1 = DEVICE_1
        self._device_2 = DEVICE_2

    #   self.load("src/ui/main_ui/main.qml")

    # Signals
    signalTest = Signal()  # Define the signal
    statusChecked = Signal(str, str)  # Define the signal
    hydraulicResponseReceived = Signal(str)  # Define the signal

    def load(self, qml_file):
        self.engine.clearComponentCache()
        self.engine.load(QUrl(qml_file))
        if not self.engine.rootObjects():
            sys.exit(-1)

    def show(self):
        self.context.setContextProperty("control_menu", self)
        self.load("src/ui/control_menu/control_menu.qml")
        if not self.engine.rootObjects():
            sys.exit(-1)

    def run(self):
        sys.exit(self.app.exec())

    @Slot()
    def quit_application(self):
        print("quit_application called")
        self.publisher.disconnect()
        QCoreApplication.quit()

    @Slot(str, str)
    def publish_command(self, topic, command):
        self.publisher.publish_command(topic, command)

    @pyqtProperty(str)
    def DEVICE_1(self):
        return self._device_1

    @pyqtProperty(str)
    def DEVICE_2(self):
        return self._device_2

    #  @Slot(str)
    # def check_online_status(self, device_id):
    #    print(f"Checking status for {device_id}")
    #   status = check_online_status(self.publisher.device_statuses, device_id)
    #  print(f"Status of {device_id}: {status}")
    # self.statusChecked.emit(device_id, status)  # Emit signal here

    @Slot(str, str)
    def update_status(self, device_id, status):
        print(f"control_menu update_status: Device {device_id} status: {status}")

    # Inside Control_Menu class
    def emitTestSignal(self):
        print("Emitting signalTest from Python")
        self.signalTest.emit()
 """
