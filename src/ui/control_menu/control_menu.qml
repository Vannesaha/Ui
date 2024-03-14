//control_menu.qml

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "../hydraulic_ui" as HydraulicUi

ApplicationWindow {

    objectName: "control_menu"
    visible: true
    width: 640
    height: 480
    title: "Sahan käyttöönotto"

    property ListModel model_controlMenu: ListModel {
        ListElement { action: 'connection'; buttonText: "Testaa ja kytke yhteydet" }
        ListElement { action: 'hydraulic'; status: "OFF"; buttonText: "Testaa hydrauliikka" }
        ListElement { action: 'embedded'; status: "OFF"; buttonText: "Testaa Sahakelkka" }
        ListElement { action: 'steelMotor'; buttonText: "Testaa Terämoottori" }
        ListElement { action: 'steelGuide'; buttonText: "Testaa Teräohjuri" }
        ListElement { action: 'cuttingBlade'; buttonText: "Testaa perkkuuterä" }
        ListElement { action: 'Sensor'; buttonText: "Anturit" }
        ListElement { action: 'back'; buttonText: "Takaisin" }
    }

    ListView {
        id: listView
        anchors.fill: parent
        model: model_controlMenu
        delegate: Rectangle {
            width: listView.width
            height: 50
            border.color: "gray"
            border.width: 1

            RowLayout {
                anchors.fill: parent
                anchors.margins: 10
                Text { text: buttonText }
                Text { text: status; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: status === "ON" ? "green" : "red" }
            }
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    if (action === "back")
                    {
                        controller.goBackStartMenuSignal();
                    }
                }
            }
        }
    }

    Connections {
        target: controller
        onUpdateStatusSignal: function(device_id, status) { updatedStatus(device_id, status); }
    }

    function updatedStatus(device_id, status)
    {
        //console.log("form control_menu qml " + device_id + " status: " + status)
        var updatedStatus = status === "online" ? "ON" : "OFF";
        for (var i = 0; i < model_controlMenu.count; i++) {
            var item = model_controlMenu.get(i);
            if ((device_id === "hydraulic" && item.action === 'hydraulic') ||
            (device_id === "embedded" && item.action === 'embedded')) {
            model_controlMenu.setProperty(i, "status", updatedStatus);
        }
    }
}
/* Label {
id: statusLabel
text: "Not updated yet"
}

function updateStatus(device_id, status)
{
    // Update the status of the device in your QML UI here.
    // This is just an example. You need to replace it with your actual code.
    console.log("Device " + device_id + " status: " + status);
    statusLabel.text = "Device " + device_id + " status: " + status;

}

function testFunction(device_id, status)
{
    statusLabel.text = "Test function called";
} */


/* Component.onCompleted: {
if (control_menu) { // Check if control_menu is available
control_menu.statusChecked.connect(updateStatus);
control_menu.statusChecked.connect(testFunction);
console.log("control_menu is available");

} else {
console.log("control_menu is not available");
}
} */

/* Connections {
target: control_menu

function onSignalTest()
{
    console.log("Signal received in QML: Device");
    // Here you can update your UI accordingly
    // For example, updating a label's text:
    statusLabel.text = "Device status updated";
}
}
*/



/* Connections {
target: gui

function onStatusChecked(device_id, newStatus)
{
    var updatedStatus = newStatus === "online" ? "ON" : "OFF";
    for (var i = 0; i < deviceModel.count; i++) {
        var item = deviceModel.get(i);
        if ((device_id === gui.DEVICE_1 && item.action === "Hydraulic") ||
        (device_id === gui.DEVICE_2 && item.action === "Embedded")) {
        deviceModel.setProperty(i, "status", updatedStatus);
    } // Tämä sulje puuttui
}
}
} */
}