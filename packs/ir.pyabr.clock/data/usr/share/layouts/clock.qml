import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    visible: true
    width: 400
    height: 400

    ToolBar {
        id: toolbar
        anchors.top: parent.top
        width: parent.width
        height: 70

        RowLayout {
            anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-time.svg'
                icon.color: "white"
                id: time
                objectName: "time"
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-chronometer.svg'
                icon.color: "white"
                id: stopwatch
                objectName: "stopwatch"
            }
        }
    }

    Text {
        text: ""
        objectName: "leClock"
        font.family: "IRANSans"
        font.pixelSize: 40
        anchors.centerIn: parent
    }

    Text {
        text: ""
        objectName: "leStopwatch"
        font.family: "IRANSans"
        font.pixelSize: 40
        id: lestopwatch
        visible: false
        anchors.centerIn: parent
    }

    RowLayout {
        anchors.top: lestopwatch.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        ToolButton {
            icon.source: 'file:///stor/usr/share/icons/breeze-time-start.svg'
            icon.color: "gray"
            id: start
            objectName: "start"
            visible: false
        }
        ToolButton {
            icon.source: 'file:///stor/usr/share/icons/breeze-time-pause.svg'
            icon.color: "gray"
            id: pause
            objectName: "pause"
            visible: false
        }
        ToolButton {
            icon.source: 'file:///stor/usr/share/icons/breeze-reboot.svg'
            icon.color: "gray"
            id: restart
            objectName: "restart"
            visible: false
        }
    }
}