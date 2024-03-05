import QtQuick 2.15
import QtQuick.Controls 2.15

Dialog {
    id: hydraulic
    title: "Set Hydraulic"
    modal: true
    standardButtons: Dialog.Ok | Dialog.Cancel

    signal hydraulicSet(int cylinder, int position)

    SpinBox {
        id: cylinderSpinBox
        from: 0
        to: 3
        stepSize: 1
        prefix: "Cylinder: "
    }

    SpinBox {
        id: positionSpinBox
        from: 0
        to: 180
        stepSize: 1
        prefix: "Position: "
    }

    onAccepted: {
        hydraulicSet(cylinderSpinBox.value, positionSpinBox.value)
    }
}