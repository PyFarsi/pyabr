import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: barge
    visible: true
    color: "white"
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
                id: open
                objectName: "open"
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-redo.svg'
                icon.color: "white"
                id: redoz
                objectName: "redoz"

                onClicked: {
                    textT.redo()
                }
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-undo.svg'
                icon.color: "white"
                id: undoz
                objectName: "undoz"

                onClicked: {
                    textT.undo()
                }
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-save.svg'
                icon.color: "white"
                id: save
                objectName: "save"
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-saveas.svg'
                icon.color: "white"
                id: saveas
                objectName: "saveas"
            }

        }
    }
    TextArea {
        anchors.top: toolbar.bottom
        id: textT
        width: parent.width
        objectName: "text"
    }
    Text {
        visible: false
        objectName: "path"
        text: ''
    }
}