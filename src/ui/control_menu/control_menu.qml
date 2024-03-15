//control_menu.qml

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "../hydraulic_menu" as HydraulicUi

ApplicationWindow {

    objectName: "control_menu"
    visible: true
    width: 640
    height: 480
    title: "Sahan käyttöönotto"

    property ListModel model_controlMenu: ListModel {
        ListElement { action: 'connection'; buttonText: "Testaa ja kytke yhteydet" }
        ListElement { action: 'hydraulic'; status: "OFF"; buttonText: "Testaa hydrauliikka" }
        ListElement { action: 'embedded'; status: "OFF"; buttonText: "Testaa Sahakelkka" }
        ListElement { action: 'steelMotor'; buttonText: "Testaa Terämoottori" }
        ListElement { action: 'steelGuide'; buttonText: "Testaa Teräohjuri" }
        ListElement { action: 'cuttingBlade'; buttonText: "Testaa perkkuuterä" }
        ListElement { action: 'Sensor'; buttonText: "Anturit" }
        ListElement { action: 'back'; buttonText: "Takaisin" }
    }

    ListView {
        id: listView
        anchors.fill: parent
        model: model_controlMenu
        delegate: Rectangle {
            width: listView.width
            height: 50
            border.color: "gray"
            border.width: 1

            RowLayout {
                anchors.fill: parent
                anchors.margins: 10
                Text { text: buttonText }
                Text { text: status; Layout.fillWidth: true; horizontalAlignment: Text.AlignRight; color: status === "ON" ? "green" : "red" }
            }
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    if (action === "connection")
                    {
                        controller.testAndConnectSignal(); // no function in controller yet
                    }
                    else if (action === "hydraulic")
                    {
                        controller.openHydraulicMenu();
                    }
                    else if (action === "embedded")
                    {
                        controller.testEmbeddedSignal(); // no function in controller yet
                    }
                    else if (action === "steelMotor")
                    {
                        controller.testSteelMotorSignal(); // no function in controller yet
                    }
                    else if (action === "steelGuide")
                    {
                        controller.testSteelGuideSignal(); // no function in controller yet
                    }
                    else if (action === "cuttingBlade")
                    {
                        controller.testCuttingBladeSignal(); // no function in controller yet
                    }
                    else if (action === "Sensor")
                    {
                        controller.testSensorSignal(); // no function in controller yet
                    }
                    else if (action === "back")
                    {
                        controller.goBackStartMenu();
                    }
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
            //console.log("form control_menu qml " + device_id + " status: " + status)
            var updatedStatus = status === "online" ? "ON" : "OFF";
            for (var i = 0; i < model_controlMenu.count; i++) {
                var item = model_controlMenu.get(i);
                if ((device_id === "hydraulic" && item.action === 'hydraulic') ||
                (device_id === "embedded" && item.action === 'embedded')) {
                model_controlMenu.setProperty(i, "status", updatedStatus);
            }
        }
    }

}