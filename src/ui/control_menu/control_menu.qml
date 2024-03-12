//control_menu.qml

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "../hydraulic_ui" as HydraulicUi

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Control Menu"

    property ListModel deviceModel: ListModel {
        ListElement { action: "Hydraulic"; status: "OFF" }
        ListElement { action: "Embedded"; status: "OFF" }
    }

    ListView {
        id: listView
        anchors.fill: parent
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
        }
    }

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