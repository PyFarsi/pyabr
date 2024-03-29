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

ApplicationWindow {
    id: login
    visible: true
    color: "purple"
    
    WindowTheme {
        id: wt
    }

    /* Topbar */
    Rectangle {
        color: "#A0FFFFFF"
        anchors.top: parent.top
        width: parent.width
        height: 30
        id: topbar

        Row {
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-shutdown.svg'
                icon.color: 'white'
                onClicked: {
                    popup_pysys.open()
                }
            }
        }

        Text {
            id: leClock
            anchors.centerIn: parent
            objectName: "leClock"
            font.family: wt.fontFamily
            font.pixelSize: 16
            color: "white"
            ToolButton {
                anchors.fill: parent
                objectName: "btnClock"
                id: btnClock
            }
        }
    }

    /* Popup PySys */
    Popup {
        id: popup_pysys
        objectName: "popup_pysys"
        anchors.centerIn: parent
        width: 350
        height: 200
        modal: true
        focus: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent

        ToolButton {
            anchors.top: parent.top
            anchors.right: parent.right
            anchors.rightMargin: 1
            anchors.leftMargin: 1
            width: 25
            height: 25

            Image {
                    source: "file:///stor/usr/share/icons/breeze-close.svg"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( parent.width, parent.height )
            }

            onClicked: {
                popup_pysys.close()
            }
        }

            ToolButton {
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                width: 100
                height: parent.height/2
                id: shutdown
                objectName: "shutdown"
                Image {
                    anchors.fill: parent
                    id: shutdown_img
                    objectName: "shutdown_img"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( shutdown.width, shutdown.height )
                }
            }
            Text {
                text: "Shutdown"
                objectName: "txtShutdown"
                anchors.top: shutdown.bottom
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: shutdown.horizontalCenter
                font.family: wt.fontFamily
            }
            ToolButton {
                anchors.left: shutdown.right
                anchors.verticalCenter: parent.verticalCenter
                width: 100
                height: parent.height/2
                id: reboot
                objectName: "reboot"
                Image {
                    anchors.fill: parent
                    id: reboot_img
                    objectName: "reboot_img"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( reboot.width, reboot.height )
                }
            }
            Text {
                text: "Restart"
                objectName: "txtReboot"
                anchors.top: reboot.bottom
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: reboot.horizontalCenter
                font.family: wt.fontFamily
            }
            ToolButton {
                anchors.left: reboot.right
                anchors.verticalCenter: parent.verticalCenter
                width: 100
                height: parent.height/2
                id: suspend
                objectName: "suspend"
                Image {
                    anchors.fill: parent
                    id: suspend_img
                    objectName: "suspend_img"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( suspend.width, suspend.height )
                }
            }
            Text {
                text: "Sleep"
                objectName: "txtSuspend"
                anchors.top: suspend.bottom
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: suspend.horizontalCenter
                font.family: wt.fontFamily
            }
    }

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
    }

    ColumnLayout {
        anchors.centerIn: parent

        Image {
            id: profile
            Layout.alignment: Qt.AlignCenter
            objectName: "profile"
            fillMode: Image.PreserveAspectFit
            width: login.width/6
            height: login.width/6
            sourceSize: Qt.size( profile.width, profile.height )
        }

        TextField {
            id: username
            objectName: "username"
            Layout.fillWidth: true
            font.family: wt.fontFamily
            placeholderText: "حساب کاربری"
            selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
        }

        ToolButton {
            id: next
            objectName: "next"
            font.family: wt.fontFamily
            text: "بعدی"
            Layout.fillWidth: true
        }
    }
}