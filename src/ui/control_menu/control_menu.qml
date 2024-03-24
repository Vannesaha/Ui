//control_menu.qml

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "../hydraulic_menu" as HydraulicUi

// Define an ApplicationWindow
ApplicationWindow {

    // Set properties of the window
    objectName: "control_menu"  // Name of the object
    visible: true  // Make the window visible
    width: 640  // Width of the window
    height: 480  // Height of the window
    title: "Sahan käyttöönotto"  // Title of the window

    // Define a ListModel property
    property ListModel model_controlMenu: ListModel {
        // Define ListElements
        ListElement { action: 'connection'; buttonText: "Testaa ja kytke yhteydet" }
        ListElement { action: 'hydraulic'; status: "OFF"; buttonText: "Testaa hydrauliikka" }
        ListElement { action: 'embedded'; status: "OFF"; buttonText: "Testaa Sahakelkka" }
        ListElement { action: 'steelMotor'; buttonText: "Testaa Terämoottori" }
        ListElement { action: 'steelGuide'; buttonText: "Testaa Teräohjuri" }
        ListElement { action: 'cuttingBlade'; buttonText: "Testaa perkkuuterä" }
        ListElement { action: 'Sensor'; buttonText: "Anturit" }
        ListElement { action: 'back'; buttonText: "Takaisin" }
    }

    // Define a ListView
    ListView {
        id: listView  // ID of the ListView
        anchors.fill: parent  // Fill the parent
        model: model_controlMenu  // Set the model

        // Define a delegate, The delegate in a ListView in QML is a component that provides a template defining each item instantiated by the view.
        delegate: Rectangle {
            width: listView.width  // Width of the Rectangle
            height: 50  // Height of the Rectangle
            border.color: "gray"  // Border color
            border.width: 1  // Border width

            // Define a RowLayout
            RowLayout {
                anchors.fill: parent  // Fill the parent
                anchors.margins: 10  // Set margins
                Text { text: buttonText }  // Display the buttonText
                    // Display the status with color based on its value
                    Text { text: status; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: status === "ON" ? "green" : "red" }
                }

                // Define a MouseArea
                MouseArea {
                    anchors.fill: parent
                    onClicked: {                     // Check which action was clicked and call the corresponding method on the controller

                    if (action === "connection")
                    {
                        controller.testAndConnectSignal(); // no function in controller yet
                    }
                    else if (action === "hydraulic")
                    {
                        controller.openHydraulicMenu(); // opens the hydraulic menu and close the control menu
                    }
                    else if (action === "embedded")
                    {
                        controller.testEmbeddedSignal(); // no function in controller yet
                    }
                    else if (action === "steelMotor")
                    {
                        controller.testSteelMotorSignal(); // no function in controller yet
                    }
                    else if (action === "steelGuide")
                    {
                        controller.testSteelGuideSignal(); // no function in controller yet
                    }
                    else if (action === "cuttingBlade")
                    {
                        controller.testCuttingBladeSignal(); // no function in controller yet
                    }
                    else if (action === "Sensor")
                    {
                        controller.testSensorSignal(); // no function in controller yet
                    }
                    else if (action === "back")
                    {
                        controller.goBackStartMenu();
                    }
                }
            }
        }
    }

    // Define a Connections object to handle signals from the controller
    Connections {
        target: controller  // Set the target to the controller
        // Define a function to handle the onUpdateStatusSignal signal
        function onUpdateStatusSignal(device_id, status)
        { updatedStatus(device_id, status); }
        }

        // Define a function to update the status of a device
        function updatedStatus(device_id, status)
        {
            // Determine the updated status
            var updatedStatus = status === "online" ? "ON" : "OFF";
            // Update the status of the corresponding device in the model
            for (var i = 0; i < model_controlMenu.count; i++) {
                var item = model_controlMenu.get(i);
                if ((device_id === "hydraulic" && item.action === 'hydraulic') ||
                (device_id === "embedded" && item.action === 'embedded')) {
                model_controlMenu.setProperty(i, "status", updatedStatus);
            }
        }
    }

}