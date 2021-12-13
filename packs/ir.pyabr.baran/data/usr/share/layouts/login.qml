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
                font.family: "IRANSans"
            }
            Menu {
                title: "زبان ها"
                id: lang
                objectName: "lang"
                font.family: "IRANSans"
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
            Layout.alignment: Qt.AlignCenter
            objectName: "profile"
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
            selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
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