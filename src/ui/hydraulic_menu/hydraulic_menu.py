# hydraulic_menu.py


from PyQt6.QtCore import QUrl, QObject, pyqtSlot as Slot

from config.settings import DEVICE_1

import sys, time


class Hydraulic_Menu(QObject):
    def __init__(self, engine, controller):
        super().__init__()
        self.controller = controller
        self.engine = engine
        self.loaded = False
        self.engine.rootContext().setContextProperty("controller", controller)
        self.engine.load(QUrl.fromLocalFile("src/ui/hydraulic_menu/hydraulic_menu.qml"))
        if not self.engine.rootObjects():
            print("Failed to load hydraulic_menu.qml")
            sys.exit(-1)
        self.root = self.get_root_object()
        if self.root is None:
            sys.exit(-1)

        # connect the signal to the method
        self.controller.cylinderPositionCommand.connect(self.setPositions)

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

    def setPositions(self, cylinder, position):
        print(f"Sending command to set cylinder {cylinder} to position {position}")
        pass

    """  def get_cylinder_number():
            while True:
                cylinder = input("Enter a cylinder number (0-3): ")
                if cylinder in ["0", "1", "2", "3"]:
                    return cylinder
                else:
                    print("Invalid input, please try again.")
                    time.sleep(2)


        def get_cylinder_position():
            while True:
                position = int(input("Enter a position (0-180): "))
                if 0 <= position <= 180:
                    return "set_position", position
                else:
                    print("Invalid input, please try again.")
                    time.sleep(2)


        def hydraulic_ui(publisher):
            while True:
                cmd = get_cylinder_number()

                # Example command generation logic
                _, position = get_cylinder_position()
                topic = f"device/{DEVICE_1}/{cmd}"
                command = f"set_hydraulic:{position}"
                # Send the position
                publisher.publish_command(topic, command)
 """
