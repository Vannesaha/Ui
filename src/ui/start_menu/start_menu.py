from PyQt6.QtCore import QUrl
import sys


class Start_Menu:
    def __init__(self, controller, engine):
        # The engine is the QQmlApplicationEngine that runs the QML application
        self.engine = engine
        # Set the controller as a context property so it can be accessed from QML
        self.engine.rootContext().setContextProperty("controller", controller)
        # Load the QML file for the start menu
        self.engine.load(QUrl.fromLocalFile("src/ui/start_menu/start_menu.qml"))
        # If no root objects are found, exit the application
        if not self.engine.rootObjects():
            exit(-1)
        # Get the root object for the start menu
        self.root = self.get_root_object()
        # If no root object is found, exit the application
        if self.root is None:
            sys.exit(-1)

    def get_root_object(self):
        # Iterate over all root objects
        for root in self.engine.rootObjects():
            # If the object name of a root object is "start_menu", return it
            if root.objectName() == "start_menu":
                return root
        # If no root object with the object name "start_menu" is found, print a message and return None
        print("Did not find start_menu object")
        return None

    def show(self):
        # Set the "visible" property of the root object to True to show the start menu
        self.get_root_object().setProperty("visible", True)

    def hide(self):
        # Set the "visible" property of the root object to False to hide the start menu
        self.get_root_object().setProperty("visible", False)


""" # start_menu.py

from PyQt6.QtCore import QUrl, QObject, pyqtSignal as Signal
from PyQt6.QtCore import pyqtSlot as Slot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtQml import QQmlApplicationEngine, QQmlContext
from PyQt6.QtCore import pyqtProperty

from src.ui.control_menu.control_menu import Control_Menu
from src.utils.mqtt_publisher import MQTTPublisher

import sys
import time


class Start_Menu(QObject):
    def __init__(self, publisher=None):
        super().__init__()
        self.publisher = publisher
        self.app = QGuiApplication.instance()
        self.engine = QQmlApplicationEngine()
        self.context = self.engine.rootContext()
        self.context.setContextProperty("start_menu", self)
        self.load("src/ui/start_menu/start_menu.qml")

        # Create an instance of Gui
        self.control_menu = Control_Menu()

        # Create an instance of MQTTPublisher and pass the gui instance
        self.publisher = MQTTPublisher(self.control_menu)

        # Assign the publisher to the gui's publisher attribute
        self.control_menu.publisher = self.publisher
        self.control_menu.publisher.gui = self.control_menu

        self.publisher.run()

        # Wait until the connection is established before showing the gui
        while not self.publisher.is_connected():
            time.sleep(0.1)  # Sleep for a short time to avoid busy waiting

    def load(self, qml_file):
        self.engine.clearComponentCache()
        self.engine.load(QUrl(qml_file))
        if not self.engine.rootObjects():
            sys.exit(-1)

    def run(self):
        self.control_menu.run

    @Slot()
    def quit_application(self):
        print("quit_application called")
        if self.publisher is not None:
            self.publisher.disconnect()
        QCoreApplication.quit()

    @Slot()
    def start_gui(self):
        self.control_menu = Control_Menu(self.publisher)
        self.control_menu.show()
 """
