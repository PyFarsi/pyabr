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
    id: enter
    visible: true
    color: "purple"

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
            font.family: "IRANSans"
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
        width: 440
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
                font.family: "IRANSans"
            }
            ToolButton {
                anchors.left: shutdown.right
                anchors.verticalCenter: parent.verticalCenter
                width: 100
                height: parent.height/2
                id: logout
                objectName: "logout"
                Image {
                    anchors.fill: parent
                    id: logout_img
                    objectName: "logout_img"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( logout.width, logout.height )
                }
            }
            Text {
                text: "Logout"
                objectName: "txtLogout"
                anchors.top: logout.bottom
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: logout.horizontalCenter
                font.family: "IRANSans"
            }
            ToolButton {
                anchors.left: logout.right
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
                font.family: "IRANSans"
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
                font.family: "IRANSans"
            }
    }

    background: Rectangle {
        anchors.fill: parent
        Image {
            anchors.fill: parent
            id: background
            objectName: "background"
        }
    }

    ColumnLayout {
        anchors.centerIn: parent

        Image {
            id: profile
            objectName: "profile"
            fillMode: Image.PreserveAspectFit
            width: enter.width/6
            Layout.alignment: Qt.AlignCenter
            height: enter.width/6
            sourceSize: Qt.size( profile.width, profile.height )
        }

        TextField {
            id: password
            objectName: "password"
            Layout.fillWidth: true
            echoMode: TextInput.Password
            placeholderText: "رمزعبور خود را وارد کنید"
            font.family: "IRANSans"
        }

        Button {
            id: login
            objectName: "login"
            text: "ورود"
            Layout.fillWidth: true
            font.family: "IRANSans"
        }
    }
}