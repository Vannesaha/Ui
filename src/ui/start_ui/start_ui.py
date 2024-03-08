# start_ui.py

from PyQt6.QtCore import QUrl, QObject, pyqtSignal as Signal
from PyQt6.QtCore import pyqtSlot as Slot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtQml import QQmlApplicationEngine, QQmlContext
from PyQt6.QtCore import pyqtProperty

from src.ui.main_ui.gui import Gui
from src.mqtt_publisher import MQTTPublisher

import sys
import time


class Start_ui(QObject):
    def __init__(self, publisher=None):
        super().__init__()
        self.publisher = publisher
        self.app = QGuiApplication.instance()
        self.engine = QQmlApplicationEngine()
        self.context = self.engine.rootContext()
        self.context.setContextProperty("start_ui", self)
        self.load("src/ui/start_ui/start_ui.qml")

        # Create an instance of Gui
        self.gui = Gui()

        # Create an instance of MQTTPublisher and pass the gui instance
        self.publisher = MQTTPublisher(self.gui)

        # Assign the publisher to the gui's publisher attribute
        self.gui.publisher = self.publisher
        self.gui.publisher.gui = self.gui

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
        self.gui.run

    @Slot()
    def quit_application(self):
        print("quit_application called")
        if self.publisher is not None:
            self.publisher.disconnect()
        QCoreApplication.quit()

    @Slot()
    def start_gui(self):
        self.gui = Gui(self.publisher)
        self.gui.show()
