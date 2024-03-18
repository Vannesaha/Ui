# control_menu.py

from PyQt6.QtCore import QUrl, QObject, pyqtSlot as Slot

import sys


# Define the Control_Menu class
class Control_Menu(QObject):
    # The constructor takes an engine as an argument
    def __init__(self, engine, controller):
        super().__init__()  # Call the __init__ method of the superclass

        self.controller = controller

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
