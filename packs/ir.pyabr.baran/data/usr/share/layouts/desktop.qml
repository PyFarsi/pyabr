import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: desktop
    visible: true
    font.family: "IRANSans"
    color: "blue"

    Text {
        id: background_app
        objectName: "background_app"
        text: ""
        visible: false
    }


    menuBar: MenuBar {
        Menu {
            title: "برنامه ها"
            id: applications
            objectName: "applications"

            Menu {
                title: "توسعه"
                id: developcat
                objectName: "developcat"

                Repeater{
                    model: EntryDevelop
                    MenuItem {
                        objectName: model.name
                        Image {
                                id: image
                                source: model.logo
                                width: parent.height
                                sourceSize: Qt.size( parent.width, parent.height )
                                height: parent.height
                        }
                        Text {
                            anchors.left: image.right
                            anchors.verticalCenter: image.verticalCenter
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            text: model.label
                            font.family: "IRANSans"
                        }
                        onTriggered: {
                            background_app.text = model.name
                        }
                    }
                }
            }

            Menu {
                title: "بازی ها"
                id: gamescat
                objectName: "gamescat"

                Repeater{
                    model: EntryGames
                    MenuItem {
                        objectName: model.name
                        onTriggered: {
                            background_app.text = model.name
                        }
                        Image {
                                id: image
                                source: model.logo
                                width: parent.height
                                sourceSize: Qt.size( parent.width, parent.height )
                                height: parent.height
                        }
                        Text {
                            anchors.left: image.right
                            anchors.verticalCenter: image.verticalCenter
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            text: model.label
                            font.family: "IRANSans"
                        }
                    }
                }
            }

            Menu {
                title: "اینترنت"
                id: internetcat
                objectName: "internetcat"

                Repeater{
                    model: EntryInternet
                    MenuItem {
                        objectName: model.name
                        onTriggered: {
                            background_app.text = model.name
                        }
                        Image {
                                id: image
                                source: model.logo
                                width: parent.height
                                sourceSize: Qt.size( parent.width, parent.height )
                                height: parent.height
                        }
                        Text {
                            anchors.left: image.right
                            anchors.verticalCenter: image.verticalCenter
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            text: model.label
                            font.family: "IRANSans"
                        }
                    }
                }
            }

            Menu {
                title: "چندرسانه ای"
                id: multimediacat
                objectName: "multimediacat"

                Repeater{
                    model: EntryMultimedia
                    MenuItem {
                        objectName: model.name
                        onTriggered: {
                            background_app.text = model.name
                        }
                        Image {
                                id: image
                                source: model.logo
                                width: parent.height
                                sourceSize: Qt.size( parent.width, parent.height )
                                height: parent.height
                        }
                        Text {
                            anchors.left: image.right
                            anchors.verticalCenter: image.verticalCenter
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            text: model.label
                            font.family: "IRANSans"
                        }
                    }
                }
            }
            Menu {
                title: "سیستمی"
                id: systemcat
                objectName: "systemcat"

                Repeater{
                    model: EntrySystem
                    MenuItem {
                        objectName: model.name
                        onTriggered: {
                            background_app.text = model.name
                        }
                        Image {
                                id: image
                                source: model.logo
                                width: parent.height
                                sourceSize: Qt.size( parent.width, parent.height )
                                height: parent.height
                        }
                        Text {
                            anchors.left: image.right
                            anchors.verticalCenter: image.verticalCenter
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            text: model.label
                            font.family: "IRANSans"
                        }
                    }
                }
            }
            Menu {
                title: "ابزارها"
                id: toolscat
                objectName: "toolscat"

                Repeater{
                    model: EntryTools
                    MenuItem {
                        objectName: model.name
                        onTriggered: {
                            background_app.text = model.name
                        }
                        Image {
                                id: image
                                source: model.logo
                                width: parent.height
                                height: parent.height
                                sourceSize: Qt.size( parent.width, parent.height )
                        }
                        Text {
                            anchors.left: image.right
                            anchors.verticalCenter: image.verticalCenter
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            text: model.label
                            font.family: "IRANSans"
                        }
                    }
                }
            }
            Menu {
                title: "سایر"
                id: otherscat
                objectName: "otherscat"

                Repeater{
                    model: EntryOthers
                    MenuItem {
                        objectName: model.name
                        onTriggered: {
                            background_app.text = model.name
                        }
                        Image {
                                id: image
                                source: model.logo
                                width: parent.height
                                height: parent.height
                                sourceSize: Qt.size( parent.width, parent.height )
                        }
                        Text {
                            anchors.left: image.right
                            anchors.verticalCenter: image.verticalCenter
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            text: model.label
                            font.family: "IRANSans"
                        }
                    }
                }
            }
        }
        Menu {
            title: "منوی اصلی"
            id: submenu
            objectName: "submenu"

            Menu {
                title: "حساب کاربری"
                id: account
                objectName: "account"

                Action {
                    text: "تنظیمات حساب کاربری"
                    id: account_setting
                    objectName: "account_setting"
                }
                Action {
                    text: "خروج از نشست"
                    id: logout
                    objectName: "logout"
                }
                Action {
                    text: "رفتن به نشستی دیگر"
                    id: switchuser
                    objectName: "switchuser"
                }
                Action {
                    text: "قفل میزکار"
                    id: lock
                    objectName: "lock"
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
            source: "../../../usr/share/backgrounds/breeze-next.png"
            id: background
            objectName: "background"
        }
    }

    Rectangle {
       color: "white"
       anchors.bottom: toolbar.top
       anchors.horizontalCenter: parent.horizontalCenter
       width: 560
       height: 560
       radius: 40
       anchors.bottomMargin: 20
       visible: false
       objectName: "menuApps"

       Rectangle {
        anchors.top: parent.top
       height: 20
       id: rex
       }

       ScrollView {
        anchors.top: rex.bottom
        anchors.bottom: rex2.top
        anchors.topMargin: 20
        anchors.bottomMargin: 20
        width: parent.width
        height: parent.height-40
        clip: true
        id: scroll

        Column {
            anchors.fill: parent
            spacing: 2
            Repeater {
                model: EntryAppApplications

                Rectangle {

                    width: parent.width
                    height: parent.width/8
                    color: "white"

                    Image {
                            source: model.logo
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex
                    }

                    Text {
                        text: model.label
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            background_app.text = model.name
                        }
                    }

                    Rectangle {
                        width: parent.width
                        height: 1
                        color: "silver"
                        anchors.top: parent.bottom
                    }
                }
            }
        }
    }
    Rectangle {
        anchors.bottom: parent.bottom
       height: 20
       id: rex2
       }
    }

    Rectangle {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottomMargin: 20
        width: 560
        height: 70
        radius: 100
        objectName: "toolbar"
        id: toolbar

        RowLayout {
            anchors.centerIn: parent
            ToolButton {
                width: toolbar.height
                height: toolbar.height
                objectName: "btnMenu"
                Image {
                    fillMode: Image.PreserveAspectFit
                    source: '../../../usr/share/icons/breeze-cloud.svg'
                    anchors.fill: parent
                    sourceSize: Qt.size( parent.width, parent.height )
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar.height
                        height: toolbar.height
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            background_app.text = model.name
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }
}