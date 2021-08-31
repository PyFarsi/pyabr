import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.3


ApplicationWindow {
    id: enter
    visible: true
    color: "purple"

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
        Image {
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
        }

        Button {
            id: login
            objectName: "login"
            text: "ورود"
            Layout.fillWidth: true
        }
    }
}