import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

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

            Menu {
                title: "حساب کاربری"
                id: account
                objectName: "account"

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
                text: "کیبورد مجازی"
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