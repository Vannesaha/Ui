# control_menu.py

from PyQt6.QtCore import QUrl
from PyQt6.QtQml import QQmlApplicationEngine
import sys


class Control_Menu:
    def __init__(self):
        self.engine = QQmlApplicationEngine()

    def show(self):
        self.engine.load(QUrl.fromLocalFile("src/ui/control_menu/control_menu.qml"))
        if not self.engine.rootObjects():
            sys.exit(-1)


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