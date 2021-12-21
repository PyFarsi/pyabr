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
    id: cleanup
    visible: true
    color: "white"
    title: "Clean Up"
    width: 600
    height: 500

    ToolButton {
        anchors.centerIn: parent
        width: parent.width/4
        height: parent.width/4
        objectName: "btnCleanup"
        id: btnCleanup
        Image {
            source: "file:///stor/usr/share/icons/breeze-reboot.svg"
            anchors.fill: parent
            sourceSize: Qt.size( parent.width, parent.height )
        }
    }

    ProgressBar {
        anchors.bottom: parent.bottom
        width: parent.width
        height: 10
        indeterminate: false
        value: 0
        objectName: "pro"
        id: pro
    }
}