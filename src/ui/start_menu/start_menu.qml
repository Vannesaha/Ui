import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Start Menu"

    property ListModel deviceModel: ListModel {
        ListElement { action: "Start"; startResponse: "" }
        ListElement { action: "Settings"; settingsResponse: "" }
    }

    ListView {
        id: listView
        anchors.fill: parent
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
                Text { text: settingsResponse }
                Text { text: startResponse }
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    if (action === "Settings")
                    {
                        deviceModel.setProperty(index, "settingsResponse", "Settings clicked");
                    }
                    else if (action === "Start")
                    {
                        deviceModel.setProperty(index, "startResponse", "Start clicked");
                        start_menu.start_gui();
                    }
                }
            }
        }
    }
}