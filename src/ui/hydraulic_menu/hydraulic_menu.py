# hydraulic_menu.py


from PyQt6.QtCore import QUrl, QObject, pyqtSlot as Slot, pyqtSlot

from config.settings import DEVICE_1

import sys, time


class Hydraulic_Menu(QObject):
    def __init__(self, controller, engine, mqtt_publisher):
        super().__init__()
        self.controller = controller
        self.engine = engine
        self.publisher = mqtt_publisher
        self.loaded = False
        self.engine.rootContext().setContextProperty("controller", controller)
        self.engine.rootContext().setContextProperty("hydraulic_menu", self)
        self.engine.load(QUrl.fromLocalFile("src/ui/hydraulic_menu/hydraulic_menu.qml"))
        if not self.engine.rootObjects():
            print("Failed to load hydraulic_menu.qml")
            sys.exit(-1)
        self.root = self.get_root_object()
        if self.root is None:
            sys.exit(-1)

    def get_root_object(self):
        for root in self.engine.rootObjects():
            if root.objectName() == "hydraulic_menu":
                return root
        print("Did not find hydraulic_menu object")
        return None

    def show(self):
        # print("Showing the hydraulic menu")
        if self.root is not None:
            self.root.setProperty("visible", True)

    def hide(self):
        if self.root is not None:
            self.root.setProperty("visible", False)

    @pyqtSlot(str, str)
    def setPositions(self, cylinder, position):
        print(f"Sending command to set cylinder {cylinder} to position {position}")
        topic = f"device/{DEVICE_1}/{cylinder}"
        command = f"set_hydraulic:{position}"
        self.publisher.publish_command(topic, command)
