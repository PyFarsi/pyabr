import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: app
    visible: true
    color: "white"
    width: 600
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
        objectName: 'xprofile'
        id: xprofile
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
                    source: xprofile.text
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
        objectName: "rechat"

        Chats {}
    }

    Rectangle {
        anchors.top: rechat.bottom
        height: 70
        width: parent.width
        visible: false
        color: "white"
        objectName: "place"
        id: place

        TextField {
            anchors.verticalCenter: parent.verticalCenter
            width: parent.width-70*3
            height: parent.height
            placeholderText: "Enter your message"
            objectName: "leSend"
            id: leSend
            anchors.left: parent.left
        }

        ToolButton {
            anchors.verticalCenter: parent.verticalCenter
            width: 70
            anchors.left: leSend.right
            height: 70
            icon.source: 'file:///stor/usr/share/icons/breeze-open.svg'
            icon.color: "gray"
            objectName: "btnFile"
            id: btnFile
        }

        ToolButton {
            anchors.verticalCenter: parent.verticalCenter
            width: 70
            anchors.left: btnFile.right
            height: 70
            icon.source: 'file:///stor/usr/share/icons/breeze-stickers.svg'
            icon.color: "gray"
            objectName: "btnStickers"
            id: btnStickers
        }

        ToolButton {
            anchors.verticalCenter: parent.verticalCenter
            width: 70
            anchors.left: btnStickers.right
            height: 70
            icon.source: 'file:///stor/usr/share/icons/breeze-next.svg'
            icon.color: "gray"
            objectName: "btnSend"
        }
    }
}