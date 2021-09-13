import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.3


ApplicationWindow {
    id: login
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
                    }
                }
            }
            CheckBox {
                id: virtualkeyboard
                objectName: "virtualkeyboard"
                text: "کیبورد مجازی"
                font.family: "IRANSans"
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
            Layout.alignment: Qt.AlignCenter
            objectName: "profile"
            source: "../../../usr/share/icons/breeze-users.svg"
            fillMode: Image.PreserveAspectFit
            width: login.width/6
            height: login.width/6
            sourceSize: Qt.size( profile.width, profile.height )
        }

        TextField {
            id: username
            objectName: "username"
            Layout.fillWidth: true
            font.family: "IRANSans"
            placeholderText: "حساب کاربری"
        }

        Button {
            id: next
            objectName: "next"
            font.family: "IRANSans"
            text: "بعدی"
            Layout.fillWidth: true
        }
    }
}