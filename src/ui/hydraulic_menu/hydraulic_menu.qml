#hydraulic_menu.qml

import QtQuick 2.15
import QtQuick.Controls 2.15

Dialog {
    id: hydraulic
    title: "Set Hydraulic"
    modal: true
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
}