import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "../hydraulic_ui" as HydraulicUi

// Define the main application window
ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Device Control"

    // Define a ListModel to hold the device actions and their statuses
    property ListModel deviceModel: ListModel {
        ListElement { action: "Hydraulic"; status: "OFF" }
        ListElement { action: "Embedded"; status: "OFF" }
        ListElement { action: "Check Statuses"}
        ListElement { action: "Exit"}
    }

    // Define a ListView to display the device actions and their statuses
    ListView {
        id: listView
        anchors.fill: parent  // This makes the ListView fill the entire parent
        width: 200
        height: 300
        model: deviceModel   // Set the model for the ListView
        delegate: Rectangle {  // Define how each item in the ListView should look
        width: listView.width
        height: 50
        border.color: "gray"
        border.width: 1

        RowLayout {
            anchors.fill: parent
            anchors.margins: 10
            Text { text: action }
            Text { text: status; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: status === "ON" ? "green" : "red" }
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {   // Define what happens when an item is clicked
            if (action === "Hydraulic")
            {
                hydraulic.open();
                //print("Hydraulic clicked");
            }
            else if (action === "Embedded")
            {
                //embedded.open();
                //print("Embedded clicked");
            }

            else if (action === "Check Statuses")
            {
                gui.check_online_status(gui.DEVICE_1);
                gui.check_online_status(gui.DEVICE_2);
                //print("Hydraulic Status clicked", gui.DEVICE_1);
            }
            else if (action === "Exit")
            {
                gui.quit_application();
                //print("Exit clicked");
            }
        }
    }
}
}

// Define a Hydraulic object from the custom module
HydraulicUi.Hydraulic {
    id: hydraulic
    onHydraulicSet: function(cylinder, position) {
    var topic = "device/" + gui.DEVICE_1 + "/" + cylinder;
    var command = "set_hydraulic:" + position;
    gui.publish_command(topic, command);
}
}

// Define what happens when the component is completed
Component.onCompleted: {
    function handleStatusChange(device_id, status)
    {
        for (var i = 0; i < deviceModel.count; i++) {
            if (deviceModel.get(i).action === "Hydraulic" && device_id === gui.DEVICE_1)
            {
                var newStatus = status === "online" ? "ON" : "OFF";
                deviceModel.setProperty(i, "status", newStatus);
            }
            else if (deviceModel.get(i).action === "Embedded" && device_id === gui.DEVICE_2)
            {
                var newStatus = status === "online" ? "ON" : "OFF";
                deviceModel.setProperty(i, "status", newStatus);
            }
        }
    }

    gui.statusChecked.connect(handleStatusChange);
    print("device_id: " + gui.DEVICE_1);
}}