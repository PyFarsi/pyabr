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