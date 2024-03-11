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
    def __init__(self):
        super().__init__()
        self.app = QGuiApplication.instance()
        self.engine = QQmlApplicationEngine()

        # Luo instanssi MQTTPublisher-luokasta ja välitetään Gui-instanssi sille.
        self.gui = Gui()  # Oletetaan, että Gui:n konstruktori ei vaadi argumentteja.

        # Luodaan sitten MQTTPublisher-instanssi ja välitetään Gui-instanssi sille.
        self.publisher = MQTTPublisher(self.gui)

        # Varmistetaan, että Gui ja MQTTPublisher tietävät toisistaan.
        self.gui.publisher = self.publisher
        self.publisher.gui = self.gui

        # Käynnistetään MQTTPublisher.
        self.publisher.run()

        # Odota, kunnes yhteys MQTT-palvelimeen on muodostettu.
        while not self.publisher.is_connected():
            time.sleep(0.1)

        # Asetetaan Gui kontekstiksi QML-ympäristöön.
        # Tämä on jo tehty tässä vaiheessa, joten "self.context" ei ole tarpeen määritellä uudelleen.
        self.engine.rootContext().setContextProperty("gui", self.gui)
        self.engine.rootContext().setContextProperty(
            "start_ui", self
        )  # Oikea tapa asettaa konteksti

        # Ladataan QML-moottori.
        self.engine.load(QUrl("src/ui/start_ui/start_ui.qml"))

    def load(self, qml_file):
        self.engine.clearComponentCache()
        self.engine.load(QUrl(qml_file))
        if not self.engine.rootObjects():
            sys.exit(-1)

    def run(self):
        self.gui.run()

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
