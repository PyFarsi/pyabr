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
    height: 472

    Column {
        anchors.bottom: toolbar.top
        height: parent.height-70
        width: parent.width
        id: page0
        visible: true
        objectName: "page0"

        Image {
            source: "file:///stor/usr/share/images/setup.png"
            //fillMode: Image.PreserveAspectFit
            //anchors.fill: parent
            id: img0
            sourceSize: Qt.size( img0.width, img0.height )
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
                font.family: "IRANSans"
            }

            TextField {
                placeholderText: "Enter a new root password"
                width: parent.width
                echoMode: TextInput.Password
                objectName: "leRootCode"
                font.family: "IRANSans"
            }

            TextField {
                placeholderText: "Pick a username"
                objectName: "leUsername"
                width: parent.width
                font.family: "IRANSans"
            }

            TextField {
                placeholderText: "Enter a new password"
                width: parent.width
                echoMode: TextInput.Password
                objectName: "lePassword"
                font.family: "IRANSans"
            }

            CheckBox {
                text: 'Enable Guest account'
                width: parent.width
                objectName: "chGuest"
                font.family: "IRANSans"
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
                anchors.horizontalCenter: parent.horizontalCenter
            }

            ComboBox {
                model: ["English", "فارسی"]
                width: parent.width
                objectName: "cmLang"
                font.family: "IRANSans"
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
                objectName: "leFullName"
                font.family: "IRANSans"
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
            font.family: "IRANSans"
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