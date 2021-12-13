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

    Text {
        objectName: "keyless"
        id: keyless
        visible: false
        text: ''
    }

    menuBar: MenuBar {

        Menu {
            title: "منوی اصلی"
            id: submenu
            objectName: "submenu"
            font.family: "IRANSans"

            Menu {
                title: "حساب کاربری"
                id: account
                objectName: "account"
                font.family: "IRANSans"

                Action {
                    text: "خروج از نشست"
                    id: logout
                    objectName: "logout"
                }
            }

            Menu {
                title: "خروج"
                id: exit
                objectName: "exit"
                font.family: "IRANSans"

                Action {
                    text: "خاموش کردن"
                    id: shutdown
                    objectName: "shutdown"
                }
                Action {
                    text: "راه اندازی مجدد"
                    id: restart
                    objectName: "restart"
                }
                Action {
                    text: "حالت خواب"
                    id: sleep
                    objectName: "sleep"
                }
            }
            Menu {
                title: "زبان ها"
                id: lang
                font.family: "IRANSans"
                objectName: "lang"
                Repeater{
                    model: Lang
                    MenuItem {
                        objectName: model.name
                        text: model.label
                        onTriggered: {
                            keyless.text = model.name
                        }
                        font.family: "IRANSans"
                    }
                }
            }
            CheckBox {
                id: virtualkeyboard
                objectName: "virtualkeyboard"
                 visible: false
                text: "کیبورد مجازی"
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