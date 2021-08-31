import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0

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
