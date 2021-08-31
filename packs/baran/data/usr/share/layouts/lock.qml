import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0

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
            Image {
                source: "../../../usr/share/backgrounds/breeze-splash.jpg"
                id: background
                objectName: "background"
            }
        }
    }
}
