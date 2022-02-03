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
    id: app
    visible: true
    color: "#ABCDEF"
    width: 700
    height: 500

    Text {
        visible: false
        text: ''
        objectName: 'csel'
        id: csel
    }

    Text {
        visible: false
        text: ''
        objectName: 'xfullname'
        id: xfullname
    }

    Text {
        visible: false
        text: ''
        objectName: 'cid'
        id: cid
    }

    Text {
        visible: false
        text: ''
        objectName: 'csender'
        id: csender
    }

    Text {
        visible: false
        text: ''
        objectName: 'cgiver'
        id: cgiver
    }

    Text {
        visible: false
        text: ''
        objectName: 'cdata'
        id: cdata
    }

    Text {
        visible: false
        text: ''
        objectName: 'act'
        id: act
    }

    ToolBar {
        id: toolbar
        anchors.top: parent.top
        width: parent.width
        height: 70

        RowLayout {
            anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-back.svg'
                icon.color: "white"
                id: back
                objectName: "back"
                visible: false
                onClicked: {
                    csel.text = ".."
                }
            }

            ToolButton {
                id: profimg
                objectName: "profimg"
                visible: false
                Image {
                    anchors.fill: parent
                    objectName: "profimg2"
                    source: 'file:///usr/share/icons/breeze-users.svg'
                    sourceSize: Qt.size( parent.width, parent.height )
                }
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-adduser.svg'
                icon.color: "white"
                id: addcontact
                objectName: "addcontact"
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-new.svg'
                icon.color: "white"
                id: add
                objectName: "add"
            }
        }
        Text {
            anchors.centerIn: parent
            visible: true
            font.family: "IRANSans"
            font.pixelSize: 20
            color: "white"
            text: xfullname.text
            objectName: "title"
        }
    }

    Rectangle {
        width: parent.width
        height: parent.height-80
        anchors.top: toolbar.bottom
        id: recexec
        objectName: "recontact"

        Contacts {}
    }

    Rectangle {
        width: parent.width
        visible: false
        height: parent.height-80-70
        anchors.top: toolbar.bottom
        id: rechat
        color: "#ABCDEF"
        objectName: "rechat"

        Chats {}
    }

    Rectangle {
        anchors.top: rechat.bottom
        height: 70
        width: parent.width
        visible: false
        color: "white"
        radius: 200
        objectName: "place"
        id: place

        TextField {
            anchors.verticalCenter: parent.verticalCenter
            width: parent.width-70*2
            height: parent.height
            placeholderText: "Enter your message"
            objectName: "leSend"
            id: leSend
            font.family: "IRANSans"
            anchors.right: btnSend.left
            selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
        }

        ToolButton {
            anchors.verticalCenter: parent.verticalCenter
            width: 70
            anchors.right: parent.right
            height: 70
            icon.source: 'file:///stor/usr/share/icons/breeze-next.svg'
            icon.color: "gray"
            id: btnSend
            objectName: "btnSend"
        }
    }
}