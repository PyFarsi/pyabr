import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Controls.Material

Window {
    id: sleep
    visible: true
    color: "black"

    Button {
        anchors.centerIn: parent
        objectName: "wakeup"
        height: sleep.height
        width: sleep.width
        background: Rectangle {
            color: "black"
        }
    }
}
