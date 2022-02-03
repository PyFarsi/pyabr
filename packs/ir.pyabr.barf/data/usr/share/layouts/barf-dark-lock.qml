import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12
import QtGraphicalEffects 1.12

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
                id: background
                        smooth: true

                objectName: "background"
            }

            FastBlur {
                            anchors.fill: background
                            source: background
                            radius: 32
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
