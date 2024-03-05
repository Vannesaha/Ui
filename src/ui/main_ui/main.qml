import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "src/ui/hydraulic_ui/hydraulic.qml" as Hydraulic_ui

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Device Control"

    ListView {
        id: listView
        width: 200
        height: 300
        model: ListModel {
            id: deviceModel
            ListElement { action: "Hydraulic"; status: "OFF" }
            ListElement { action: "Embedded"; status: "OFF" }
            ListElement { action: "Hydraulic Status"; status: "OFF" }
            ListElement { action: "Embedded Status"; status: "OFF" }
            ListElement { action: "Exit"; status: "OFF"}
        }
        delegate: Item {
            width: listView.width
            height: 50
            RowLayout {
                Text { text: action }
                Text { text: status; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight }
            }
            // ...

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    if (action === "Exit")
                    {
                        console.log("Exit clicked");
                        gui.quit_application();
                    } else if (action === "Hydraulic") {
                    hydraulicDialog.open();
                } else {
                var newStatus = status === "OFF" ? "ON" : "OFF";
                deviceModel.set(index, {"status": newStatus});
            }
        }
    }

    Hydraulic_ui {
    id: hydraulic
    onHydraulicSet: {
        var topic = "device/" + DEVICE_1 + "/" + cylinder;
        var command = "set_hydraulic:" + position;
        gui.publish_command(topic, command);
    }
}
}
}
}