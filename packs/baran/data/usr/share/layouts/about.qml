import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: backend
    visible: true
    color: "white"

    Rectangle {
        id: reclogo
        width: parent.width
        height: parent.height/3

        Image {
            id: logo
            source: "../../../usr/share/icons/breeze-cloud.svg"
            fillMode: Image.PreserveAspectFit
            sourceSize: Qt.size( logo.width, logo.height )
            height: parent.width/1.5
            anchors.centerIn: parent
            width: parent.height/1.5
        }

        Text {
            text: "Pyabr OS"
            font.pixelSize: 30
            font.bold: true
            anchors.top: logo.bottom
        }
    }
}