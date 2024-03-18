import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {

    objectName: "start_menu"
    width: 640
    height: 480
    title: "Päävalikko"

    property ListModel model_startMenu: ListModel {
        ListElement { action: "start"; startResponse: ""; buttonText: "Aloita "}
        ListElement { action: "settings"; settingsResponse: ""; buttonText: "Asetukset"}
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
                    if (action === "start")
                    {
                        controller.openControlMenu() // Assuming you have a method connected to the signal
                    }
                    else if (action === "settings")
                    {
                        controller.openSettingsMenuSignal() // no function yet
                    }
                }
            }
        }
    }
}