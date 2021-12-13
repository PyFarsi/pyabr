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
    id: splash
    visible: true
    color: "black"

    Image {
        id: logo
        fillMode: Image.PreserveAspectFit
        objectName: "logo"
        sourceSize: Qt.size( logo.width, logo.height )
        height: splash.width/3
        anchors.centerIn: parent
        width: splash.height/4
    }
}
