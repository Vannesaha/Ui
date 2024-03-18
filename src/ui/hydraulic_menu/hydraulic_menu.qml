#hydraulic_menu.qml

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    id: hydraulic
    objectName: "hydraulic_menu"
    width: 640
    height: 480
    title: "Testaa hydrauliikka"

    property ListModel model_hydraulicMenu: ListModel {
        ListElement { action: "set_cylinder"; buttonText: "Aseta sylinteri"; value: ""; status: "OFF"; }
        ListElement { action: "set_position"; buttonText: "Aseta asento"; value: ""; status: "OFF";}
        ListElement { action: "send_command"; buttonText: "Lähetä käsky"}
        ListElement { action: "back"; buttonText: "Takaisin"; value: "" }
    }

    ListView {
        id: listView
        anchors.fill: parent
        width: 200
        height: 300
        model: model_hydraulicMenu

        delegate: Rectangle {
            width: listView.width
            height: 50
            border.color: "gray"
            border.width: 1

            RowLayout {
                anchors.fill: parent
                anchors.margins: 10
                Text { text: buttonText }
                Text { text: value }
                Text { text: status; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: status === "ON" ? "green" : "red" }

            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    if (action === "set_cylinder")
                    {
                        cylinderDialog.open();
                    }
                    else if (action === "set_position")
                    {
                        positionDialog.open();
                    }
                    else if (action === "send_command")
                    {
                        var cylinderValue = JSON.parse(model_hydraulicMenu.get(0).value);
                        var positionValue = JSON.parse(model_hydraulicMenu.get(1).value);
                        hydraulic_menu.setPositions(cylinderValue.cylinder, positionValue.position);

                    }
                    else if (action === "back")
                    {
                        controller.goBackControlMenu();
                    }
                }
            }
        }
    }

    Popup {
        id: cylinderDialog
        width: 300
        height: 200
        modal: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

        Column {
            anchors.centerIn: parent

            TextField {
                id: cylinderInput
                width: 200
                placeholderText: "Enter cylinder value"
            }

            Button {
                text: "OK"
                onClicked: {
                    model_hydraulicMenu.get(0).value = JSON.stringify({ cylinder: cylinderInput.text });
                    cylinderDialog.close();
                }
            }
        }
    }

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

    Connections {
        target: controller
        function onUpdateStatusSignal(device_id, status)
        { updatedStatus(device_id, status); }
        }

        function updatedStatus(device_id, status)
        {
            var updatedStatus = status === "online" ? "ON" : "OFF";
            for (var i = 0; i < model_hydraulicMenu.count; i++) {
                var item = model_hydraulicMenu.get(i);
                if ((device_id === "hydraulic" && item.action === 'set_cylinder') ||
                (device_id === "embedded" && item.action === 'set_position')) {
                model_hydraulicMenu.setProperty(i, "status", updatedStatus);
            }
        }
    }

}