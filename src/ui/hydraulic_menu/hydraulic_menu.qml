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
        ListElement { action: "set_cylinder"; buttonText: "Aseta sylinteri" }
        ListElement { action: "set_position"; buttonText: "Aseta asento" }
        ListElement { action: "back"; buttonText: "Takaisin" }
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
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    if (action === "set_cylinder")
                    {
                        // Open the dialog to set the cylinder
                    }
                    else if (action === "set_position")
                    {
                        // Open the dialog to set the position
                    }
                    else if (action === "back")
                    {
                        controller.goBackControlMenuSignal();
                    }
                }
            }
        }
    }
}
/* import QtQuick 2.15
import QtQuick.Controls 2.15

Dialog {
    id: hydraulic
    objectName: "hydraulic_menu"  // Add this line
    title: "Set Hydraulic"
    modal: true
    visible: true
    standardButtons: Dialog.Ok | Dialog.Cancel

    signal hydraulicSet(int cylinder, int position)

    Column {
        spacing: 10
        Row {
            Label {
                text: "Cylinder: "
            }
            SpinBox {
                id: cylinderSpinBox
                from: 0
                to: 3
                stepSize: 1
            }
        }

        Row {
            Label {
                text: "Position: "
            }
            SpinBox {
                id: positionSpinBox
                from: 0
                to: 180
                stepSize: 1
            }
        }
    }

    onAccepted: {
        hydraulicSet(cylinderSpinBox.value, positionSpinBox.value)
    }
} */