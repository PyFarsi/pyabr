import QtQuick
import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Material

ApplicationWindow {
    id: unlock
    visible: true
    color: "purple"

    Text {
        objectName: "keyless"
        id: keyless
        visible: false
        text: ''
    }

    menuBar: MenuBar {

        Menu {
            title: "منوی اصلی"
            font.family: "IRANSans"
            id: submenu
            objectName: "submenu"

            Menu {
                title: "زبان ها"
                id: lang
                objectName: "lang"
                Repeater{
                    model: Lang
                    MenuItem {
                        font.family: "IRANSans"
                        objectName: model.name
                        text: model.label

                        onTriggered: {
                            keyless.text = model.name
                        }
                    }
                }
            }
            CheckBox {
                id: virtualkeyboard
                objectName: "virtualkeyboard"
                text: "کیبورد مجازی"
                 visible: false
                font.family: "IRANSans"
            }
        }
    }

    background: Rectangle {
        anchors.fill: parent
        Image {
            anchors.fill: parent
            source: "../../../usr/share/backgrounds/breeze-splash.jpg"
            id: background
            objectName: "background"
        }
    }

    ColumnLayout {
        anchors.centerIn: parent

        Image {
            id: profile
            objectName: "profile"
            source: "../../../usr/share/icons/breeze-users.svg"
            fillMode: Image.PreserveAspectFit
            width: unlock.width/6
            Layout.alignment: Qt.AlignCenter
            height: unlock.width/6
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
            text: "بازکردن"
            font.family: "IRANSans"
            Layout.fillWidth: true
        }
    }
}