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

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-fullscreen.svg'
                icon.color: "white"
                objectName: "fullscreen"
                visible: false
            }
        }
    }
    Image {
        id: visibleImg
        anchors.top: toolbar.bottom
        width: parent.width
        objectName: "image"
        fillMode: Image.PreserveAspectFit
    }
}