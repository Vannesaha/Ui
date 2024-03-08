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
        ListElement { action: "Hydraulic"; hydraulicResponse: ""; status: "OFF" }
        ListElement { action: "Embedded"; embeddedResponse: ""; status: "OFF" }
        ListElement { action: "Check Statuses"; statusCheckResponse: "" }
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
            Text { text: hydraulicResponse; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: "blue" }
            Text { text: embeddedResponse; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: "blue" }

            Text { text: status; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: status === "ON" ? "green" : "red" }
            Text { text: statusCheckResponse; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: "blue" }


        }
        MouseArea {
            anchors.fill: parent
            onClicked: {   // Define what happens when an item is clicked
            if (action === "Hydraulic")
            {
                var hydraulicStatus;
                for (var i = 0; i < deviceModel.count; i++) {
                    if (deviceModel.get(i).action === "Hydraulic")
                    {
                        hydraulicStatus = deviceModel.get(i).status;
                        deviceModel.setProperty(i, "hydraulicResponse", "");  // Clear the message here
                        if (hydraulicStatus === "OFF")
                        {
                            deviceModel.setProperty(i, "hydraulicResponse", "The hydraulic device is OFF. Please turn it ON before opening the hydraulic");
                            console.warn("The hydraulic device is OFF. Please turn it ON before opening the hydraulic dialog.");
                        }
                        else
                        {
                            // Check if the hydraulic device is ON
                            hydraulic.open();
                        }
                        break;
                    }
                }
            }

            else if (action === "Embedded")
            {
                for (var i = 0; i < deviceModel.count; i++) {
                    if (deviceModel.get(i).action === "Embedded")
                    {
                        deviceModel.setProperty(i, "embeddedResponse", "No function yet.");  // Clear the message here
                        break;
                    }
                }
            }

            else if (action === "Check Statuses")
            {
                gui.check_online_status(gui.DEVICE_1);
                gui.check_online_status(gui.DEVICE_2);
                for (var i = 0; i < deviceModel.count; i++) {
                    if (deviceModel.get(i).action === "Check Statuses")
                    {
                        var device1Status = "OFF";
                        var device2Status = "OFF";
                        for (var j = 0; j < deviceModel.count; j++) {
                            if (deviceModel.get(j).action === "Hydraulic")
                            {
                                device1Status = deviceModel.get(j).status;
                            } else if (deviceModel.get(j).action === "Embedded") {
                            device2Status = deviceModel.get(j).status;
                        }
                    }
                    deviceModel.setProperty(i, "statusCheckResponse", gui.DEVICE_1 + ": " + device1Status + ", " + gui.DEVICE_2 + ": " + device2Status);
                    break;
                }
            }
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
    x: (parent.width - width) / 2
    y: (parent.height - height) / 2
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
                gui.hydraulicResponseReceived.connect(updateHydraulicStatus);

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
}

function updateHydraulicStatus(response)
{
    for (var i = 0; i < deviceModel.count; i++) {
        if (deviceModel.get(i).action === "Hydraulic")
        {
            deviceModel.setProperty(i, "hydraulicResponse", response);
            break;
        }
    }
}
}