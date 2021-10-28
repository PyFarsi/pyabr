import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: backend
    visible: true
    color: "white"

    width: 600
    height: 200

    Text {
        id: background_text
        objectName: "background_text"
        visible: false
    }

    RowLayout {
        width: parent.width
        height: parent.height
        spacing: 2
        Image {
            id: shutdown
            source: "../../../usr/share/icons/breeze-shutdown.svg"
            fillMode: Image.PreserveAspectFit
            width: parent.height/2
            height: parent.height/2
            sourceSize: Qt.size( shutdown.width, shutdown.height )

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    background_text.text = "shutdown"
                }
            }
        }
        Image {
            id: lock
            source: "../../../usr/share/icons/breeze-lock.svg"
            fillMode: Image.PreserveAspectFit
            width: parent.height/2
            height: parent.height/2
            sourceSize: Qt.size( lock.width, lock.height )

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    background_text.text = "lock"
                }
            }
        }
        Image {
            id: logout
            source: "../../../usr/share/icons/breeze-logout.svg"
            fillMode: Image.PreserveAspectFit
            width: parent.height/2
            height: parent.height/2
            sourceSize: Qt.size( logout.width, logout.height )
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    background_text.text = "logout"
                }
            }
        }
        Image {
            id: reboot
            source: "../../../usr/share/icons/breeze-reboot.svg"
            fillMode: Image.PreserveAspectFit
            width: parent.height/2
            height: parent.height/2
            sourceSize: Qt.size( reboot.width, reboot.height )
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    background_text.text = "reboot"
                }
            }
        }
        Image {
            id: suspend
            source: "../../../usr/share/icons/breeze-suspend.svg"
            fillMode: Image.PreserveAspectFit
            width: parent.height/2
            height: parent.height/2
            sourceSize: Qt.size( suspend.width, suspend.height )
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    background_text.text = "suspend"
                }
            }
        }
        Image {
            id: switchuser
            source: "../../../usr/share/icons/breeze-switchuser.svg"
            fillMode: Image.PreserveAspectFit
            width: parent.height/2
            height: parent.height/2
            sourceSize: Qt.size( switchuser.width, switchuser.height )
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    background_text.text = "switchuser"
                }
            }
        }
    }
}