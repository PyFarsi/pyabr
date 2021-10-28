import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Controls.Material

Window {
    id: lock
    visible: true
    color: "black"

    Button {
        anchors.centerIn: parent
        objectName: "unlock"
        height: lock.height
        width: lock.width
        id: unlock

        background: Rectangle {
            anchors.fill: parent
            Image {
                anchors.fill: parent
                source: "../../../usr/share/backgrounds/breeze-splash.jpg"
                id: background
                objectName: "background"
            }

            Text {
                color: "white"
                text: ""
                objectName: "txtClock"
                font.pixelSize: 100
                font.family: "IRANSans"
                id: txtClock
                anchors.centerIn: parent
            }
        }
    }
}
