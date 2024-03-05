# gui.py

from PyQt6.QtCore import QUrl, QObject, pyqtSignal as Signal
from PyQt6.QtCore import pyqtSlot as Slot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtQml import QQmlApplicationEngine, QQmlContext
import sys


class Gui(QObject):
    def __init__(self, publisher):
        super().__init__()
        self.publisher = publisher
        self.app = QGuiApplication([])
        self.engine = QQmlApplicationEngine()
        self.context = self.engine.rootContext()
        self.context.setContextProperty("gui", self)
        self.load("src/ui/main_ui/main.qml")

    def load(self, qml_file):
        self.engine.clearComponentCache()
        self.engine.load(QUrl(qml_file))
        if not self.engine.rootObjects():
            sys.exit(-1)

    def run(self):
        sys.exit(self.app.exec())

    @Slot(str, str)
    def update_status(self, device_name, status):
        for i in range(self.context.contextProperty("deviceModel").count()):
            if (
                self.context.contextProperty("deviceModel").get(i)["deviceName"]
                == device_name
            ):
                self.context.contextProperty("deviceModel").setProperty(
                    i, "status", status
                )
                break

    @Slot()
    def quit_application(self):
        print("quit_application called")
        self.publisher.disconnect()
        QCoreApplication.quit()

    @Slot(str, str)
    def publish_command(self, topic, command):
        self.publisher.publish_command(topic, command)
