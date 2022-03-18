import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12

ApplicationWindow {
    visible: true
    width: 400
    height: 400
    color: wt.background
    
    WindowTheme {
        id: wt
    }

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
        font.family: wt.fontFamily
        color: wt.color
        font.pixelSize: 40
        anchors.centerIn: parent
    }

    Text {
        text: ""
        objectName: "leStopwatch"
        color: wt.color
        font.family: wt.fontFamily
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