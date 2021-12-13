import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12

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
