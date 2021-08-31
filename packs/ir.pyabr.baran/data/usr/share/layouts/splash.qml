import QtQuick 2.0
import QtQuick.Window 2.3

Window {
    id: splash
    visible: true
    color: "white"

    Image {
        id: logo
        source: "../../../usr/share/icons/breeze-cloud.svg"
        fillMode: Image.PreserveAspectFit
        sourceSize: Qt.size( logo.width, logo.height )
        height: splash.width/3
        anchors.centerIn: parent
        width: splash.height/4
    }
}
