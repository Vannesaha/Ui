//start_menu.qml

// Import necessary modules
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

// Define an ApplicationWindow
ApplicationWindow {

    // Set properties of the window
    objectName: "start_menu"  // Name of the object
    width: 640  // Width of the window
    height: 480  // Height of the window
    title: "Päävalikko"  // Title of the window

    // Define a ListModel property
    property ListModel model_startMenu: ListModel {
        // Define ListElements
        ListElement { action: "start"; startResponse: ""; buttonText: "1. Aloita "}
        ListElement { action: "settings"; settingsResponse: ""; buttonText: "Asetukset"}
    }

    // Define a ListView
    ListView {
        id: listView  // ID of the ListView
        anchors.fill: parent  // Fill the parent
        width: 200  // Width of the ListView
        height: 300  // Height of the ListView
        model: model_startMenu  // Set the model

        // Define a delegate
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
                    Text { text: settingsResponse }  // Display the settingsResponse
                        Text { text: startResponse }  // Display the startResponse
                        }

                        // Define a MouseArea
                        MouseArea {
                            anchors.fill: parent  // Fill the parent
                            onClicked: {
                                // This is a simplified way to check which button was clicked
                                if (action === "start")
                                {
                                    controller.openControlMenu() //  openControlMenuSignal()
                                }
                                else if (action === "settings")
                                {
                                    controller.openSettingsMenuSignal() // no function yet
                                }
                            }
                        }
                    }
                }
            }