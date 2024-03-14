import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {

    objectName: "start_menu"
    visible: false
    width: 640
    height: 480
    title: "Start Menu"

    property ListModel model_startMenu: ListModel {
        ListElement { action: 1; startResponse: ""; buttonText: "Start"}
        ListElement { action: 2; settingsResponse: ""; buttonText: "Settings"}
    }

    ListView {
        id: listView
        anchors.fill: parent
        width: 200
        height: 300
        model: model_startMenu

        delegate: Rectangle {
            width: listView.width
            height: 50
            border.color: "gray"
            border.width: 1

            RowLayout {
                anchors.fill: parent
                anchors.margins: 10
                Text { text: buttonText }
                Text { text: settingsResponse }
                Text { text: startResponse }
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    // This is a simplified way to check which button was clicked
                    if (action === 1)
                    {
                        controller.openControlMenuSignal() // Assuming you have a method connected to the signal
                    }
                }
            }
        }
    }
}