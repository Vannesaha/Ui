#hydraulic_menu.qml
// Import necessary modules
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

// Define the main application window
ApplicationWindow {
    id: hydraulic  // Identifier for this window
    objectName: "hydraulic_menu"  // Name of this object
    width: 640  // Window width
    height: 480  // Window height
    title: "Testaa hydrauliikka"  // Window title

    // Define a ListModel property
    property ListModel model_hydraulicMenu: ListModel {
        // Define elements of the list
        ListElement { action: "set_cylinder"; buttonText: "Aseta sylinteri"; value: ""; status: "OFF"; }
        ListElement { action: "set_position"; buttonText: "Aseta asento"; value: "";}
        ListElement { action: "send_command"; buttonText: "Lähetä käsky"}
        ListElement { action: "back"; buttonText: "Takaisin"; value: "" }
    }

    // Define a ListView to display the list model
    ListView {
        id: listView  // Identifier for this ListView
        anchors.fill: parent  // Fill the parent element
        width: 200  // ListView width
        height: 300  // ListView height
        model: model_hydraulicMenu  // Use the previously defined ListModel

        // Define a delegate to customize the appearance of each item
        delegate: Rectangle {
            width: listView.width  // Width of each item
            height: 50  // Height of each item
            border.color: "gray"  // Border color
            border.width: 1  // Border width

            // Define a layout for the item
            RowLayout {
                anchors.fill: parent  // Fill the parent element
                anchors.margins: 10  // Margins around the layout
                Text { text: buttonText }  // Display the buttonText property
                    Text { text: value }  // Display the value property
                        // Display the status property, aligned to the right, with color depending on the status
                        Text { text: status; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: status === "ON" ? "green" : "red" }
                    }

                    // Define a MouseArea to handle mouse clicks
                    MouseArea {
                        anchors.fill: parent  // Fill the parent element
                        onClicked: {
                            // Perform different actions depending on the action property
                            if (action === "set_cylinder")
                            {
                                cylinderDialog.open();  // Open the cylinder dialog
                            }
                            else if (action === "set_position")
                            {
                                positionDialog.open();  // Open the position dialog
                            }
                            else if (action === "send_command")
                            {
                                // Parse the cylinder and position values and set the positions
                                var cylinderValue = JSON.parse(model_hydraulicMenu.get(0).value);
                                var positionValue = JSON.parse(model_hydraulicMenu.get(1).value);
                                hydraulic_menu.setPositions(cylinderValue.cylinder, positionValue.position);
                            }
                            else if (action === "back")
                            {
                                controller.goBackControlMenu();  // Go back to the control menu
                            }
                        }
                    }
                }
            }

            // Define a Popup for the cylinder dialog
            Popup {
                id: cylinderDialog  // Identifier for this Popup
                width: 300  // Popup width
                height: 200  // Popup height
                modal: true  // Make the Popup modal
                closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside  // Define the close policy

                // Define the content of the Popup
                Column {
                    anchors.centerIn: parent  // Center the content in the Popup

                    // Define a TextField for the cylinder value
                    TextField {
                        id: cylinderInput  // Identifier for this TextField
                        width: 200  // TextField width
                        placeholderText: "Enter cylinder value"  // Placeholder text
                    }

                    // Define a Button to close the Popup and set the cylinder value
                    Button {
                        text: "OK"  // Button text
                        onClicked: {
                            // Set the cylinder value and close the Popup
                            model_hydraulicMenu.get(0).value = JSON.stringify({ cylinder: cylinderInput.text });
                            cylinderDialog.close();
                        }
                    }
                }
            }

            // Define a Popup for the position dialog (similar to the cylinder dialog)
            Popup {
                id: positionDialog
                width: 300
                height: 200
                modal: true
                closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

                Column {
                    anchors.centerIn: parent

                    TextField {
                        id: positionInput
                        width: 200
                        placeholderText: "Enter position value"
                    }

                    Button {
                        text: "OK"
                        onClicked: {
                            model_hydraulicMenu.get(1).value = JSON.stringify({ position: positionInput.text });
                            positionDialog.close();
                        }
                    }
                }
            }

            // Define a Connections element to handle signals from the controller
            Connections {
                target: controller  // The object to connect to
                function onUpdateStatusSignal(device_id, status)
                { updatedStatus(device_id, status); }  // Call the updatedStatus function when the signal is emitted
                }

                // Define a function to update the status
                function updatedStatus(device_id, status)
                {
                    var updatedStatus = status === "online" ? "ON" : "OFF";  // Determine the updated status
                    for (var i = 0; i < model_hydraulicMenu.count; i++) {
                        var item = model_hydraulicMenu.get(i);  // Get the current item
                        // If the device_id matches, update the status
                        if ((device_id === "hydraulic" && item.action === 'set_cylinder') ||
                        (device_id === "embedded" )) {
                        model_hydraulicMenu.setProperty(i, "status", updatedStatus);
                    }
                }
            }
        }