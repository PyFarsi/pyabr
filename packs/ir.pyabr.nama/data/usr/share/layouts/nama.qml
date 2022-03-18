import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12

ApplicationWindow {
    id: barge
    visible: true
    color: wt.background
    width: 1000
    height: 600

    WindowTheme {
        id: wt
    }

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