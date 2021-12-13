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
            fillMode: Image.PreserveAspectFit
            width: parent.height/2
            objectName: "shutdown"
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
            fillMode: Image.PreserveAspectFit
            objectName: "lock"
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
            fillMode: Image.PreserveAspectFit
            objectName: "logout"
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
            fillMode: Image.PreserveAspectFit
            objectName: "reboot"
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
            fillMode: Image.PreserveAspectFit
            objectName: "suspend"
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
    }
}