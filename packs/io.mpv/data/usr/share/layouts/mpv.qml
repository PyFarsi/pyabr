import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: barge
    visible: true
    color: "black"
    width: 1000
    height: 600

    ToolBar {
        id: toolbar
        anchors.top: parent.top
        width: parent.width
        height: 70

        RowLayout {
                    anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-open.svg'
                icon.color: "white"
                objectName: "open"
            }

        }
    }
    Image {
        id: visibleImg
        anchors.centerIn: parent
        objectName: "image"
        width: parent.width/5
        height: parent.width/5
        sourceSize: Qt.size( visibleImg.width, visibleImg.height )
        fillMode: Image.PreserveAspectFit
    }
}