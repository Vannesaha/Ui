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
