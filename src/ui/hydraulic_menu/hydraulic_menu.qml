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
        ListElement { action: "set_cylinder"; buttonText: "Aseta sylinteri"; value: "" }
        ListElement { action: "set_position"; buttonText: "Aseta asento"; value: "" }
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
                        controller.goBackControlMenuSignal();
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
        parent: hydraulic

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
        parent: hydraulic

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
}