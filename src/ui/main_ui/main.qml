import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "../hydraulic_ui" as HydraulicUi

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Device Control"

    property ListModel deviceModel: ListModel {
        ListElement { action: "Hydraulic"; status: "OFF" }
        ListElement { action: "Embedded"; status: "OFF" }
        ListElement { action: "Hydraulic Status"; status: "OFF" }
        ListElement { action: "Embedded Status"; status: "OFF" }
        ListElement { action: "Exit"; status: "OFF"}
    }

    ListView {
        id: listView
        width: 200
        height: 300
        model: deviceModel
        delegate: Rectangle {
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
                onClicked: {
                    if (action === "Hydraulic Status")
                    {
                        gui.check_online_status(gui.DEVICE_1);
                    } else if (action === "Exit") {
                    gui.quit_application();
                } else if (action === "Hydraulic") {
                hydraulic.open();
            } else {
            var newStatus = status === "OFF" ? "ON" : "OFF";
            deviceModel.setProperty(index, "status", newStatus);  // Use setProperty
        }
    }
}
}
}

HydraulicUi.Hydraulic {
    id: hydraulic
    onHydraulicSet: function(cylinder, position) {
    var topic = "device/" + gui.DEVICE_1 + "/" + cylinder;
    var command = "set_hydraulic:" + position;
    gui.publish_command(topic, command);
}
}


Component.onCompleted: {
    gui.statusChecked.connect(function(device_id, status) {
    for (var i = 0; i < deviceModel.count; i++) {
        if (deviceModel.get(i).action === "Hydraulic Status")
        {
            var newStatus = status === "online" ? "ON" : "OFF";
            deviceModel.setProperty(i, "status", newStatus);
            break;
        }
    }
});
}}