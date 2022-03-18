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
    color: wt.background
    width: 600
    height: 472
    
    WindowTheme {
        id: wt
    }

    maximumWidth: 600
    maximumHeight: 472

    minimumWidth: 600
    minimumHeight: 472

    Column {
        anchors.bottom: toolbar.top
        height: parent.height-70
        width: parent.width
        id: page0
        visible: true
        objectName: "page0"

        Image {
            id: img0
            sourceSize: Qt.size( img0.width, img0.height )
            objectName: "img0"
        }
    }

    /* Host and users name */
    Column {
        anchors.bottom: toolbar.top
        height: parent.height-70
        width: parent.width
        id: page1
        objectName: "page1"
        visible: false

        Column {
            anchors.centerIn: parent
            width: parent.width/1.5
            TextField {
                placeholderText: "Enter a new hostname"
                width: parent.width
                objectName: "leHostname"
                font.family: wt.fontFamily
                selectByMouse: true
                color: wt.color
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
            }

            TextField {
                placeholderText: "Enter a new root password"
                width: parent.width
                echoMode: TextInput.Password
                color: wt.color
                objectName: "leRootCode"
                font.family: wt.fontFamily
                selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
            }

            TextField {
                placeholderText: "Pick a username"
                objectName: "leUsername"
                width: parent.width
                font.family: wt.fontFamily
                color: wt.color
                selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
            }

            TextField {
                placeholderText: "Enter a new password"
                width: parent.width
                echoMode: TextInput.Password
                objectName: "lePassword"
                color: wt.color
                font.family: wt.fontFamily
            }

            CheckBox {
                text: 'Enable Guest account'
                width: parent.width
                objectName: "chGuest"
                font.family: wt.fontFamily
            }
        }
    }

    /* Language and counter and etc */
    Column {
        anchors.bottom: toolbar.top
        height: parent.height-70
        width: parent.width
        id: page2
        objectName: "page2"
        visible: false

        Column {
            anchors.centerIn: parent
            width: parent.width/1.5

            Label {
                text: "Choose your language"
                color: wt.color
                anchors.horizontalCenter: parent.horizontalCenter
            }

            ComboBox {
                model: ["English", "فارسی","Türk","عربی","中国人","Deutsch","русский"]
                width: parent.width
                objectName: "cmLang"
                font.family: wt.fontFamily
            }
        }
    }

    /* Personal informations */
    Column {
        anchors.bottom: toolbar.top
        height: parent.height-70
        width: parent.width
        id: page3
        objectName: "page3"
        visible: false

        Column {
            anchors.centerIn: parent
            width: parent.width/1.5

            TextField {
                placeholderText: "Enter your fullname"
                width: parent.width
                color: wt.color
                objectName: "leFullName"
                font.family: wt.fontFamily
                selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
            }
        }
    }

    /* Finish */
    Column {
        anchors.bottom: toolbar.top
        height: parent.height-70
        width: parent.width
        id: page4
        objectName: "page4"
        visible: false

        Text {
            anchors.centerIn: parent
            text: "Setup is already complete;\n that you can signout and use your Pyabr is your Portable USB/SD"
            font.pixelSize: 15
            font.family: wt.fontFamily
            color: wt.color
            objectName: "setup_message"
        }
    }

    ToolBar {
        id: toolbar
        anchors.bottom: parent.bottom
        width: parent.width
        height: 70

        RowLayout {
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.right: parent.right

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-back.svg'
                icon.color: "white"
                id: back
                objectName: "back"
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-next.svg'
                icon.color: "white"
                id: next
                objectName: "next"
            }
        }
    }
}