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
    id: mails
    visible: true
    color: wt.background
    width: 600
    height: 500
    title: "Cloud Mails"
    
    WindowTheme {
        id: wt
    }

    ToolBar {
        id: toolbar
        anchors.top: parent.top
        width: parent.width
        height: 70

        RowLayout {
                    anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-new.svg'
                icon.color: "white"
                id: add
                objectName: "add"

                onClicked: {
                    add.visible = false;
                    back.visible = true;
                    scroll.visible = false;
                    sendMail.visible = true;
                    leUsername.visible = true;
                    leSubject.visible = true;
                    btnSend.visible = true;
                    textT.visible = true;
                }
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-back.svg'
                icon.color: "white"
                id: back
                visible: false
                objectName: "back"

                onClicked: {
                    add.visible = true;
                    back.visible = false;
                    textShow.visible = false;
                    showMail.visible = false;
                    scroll.visible = true;
                    sendMail.visible = false;
                    leUsername.visible = false;
                    leSubject.visible = false;
                    btnSend.visible = false;
                    textT.visible = false;
                }
            }

        }
    }

    Text {
        id: sel
        objectName: "sel"
        visible: false
        text: ""
    }

    Rectangle {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        id: showMail
        objectName: "showMail"
        visible: false
        color: wt.background

        Column {
                anchors.centerIn: parent
                width: parent.width/1.2
                height: parent.height/1.2
                
                TextArea {
                        id: textShow
                        color: wt.color
                        width: parent.width
                        font.family: wt.fontFamily
                        placeholderText: "Text"
                        objectName: "textShow"
                        enabled: false
                        anchors.fill: parent
                        selectByMouse: true
                        visible: false
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                }
        }
    }

    Rectangle {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        id: sendMail
        color: wt.background
        objectName: "sendMail"

        Column {
                anchors.centerIn: parent
                width: parent.width/1.2
                TextField {
                    width: parent.width
                    id: leUsername
                    font.family: wt.fontFamily
                    color: wt.color
                    placeholderText: "Giver"
                    visible: false
                    selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
                    objectName: "leUsername"
                }

                TextField {
                        width: parent.width
                        id: leSubject
                        font.family: wt.fontFamily
                        color: wt.color
                        visible: false
                        placeholderText: "Subject"
                        selectByMouse: true
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                        objectName: "leSubject"
                }
                

                TextArea {
                        id: textT
                        color: wt.color
                        width: parent.width
                        font.family: wt.fontFamily
                        placeholderText: "Text"
                        objectName: "text"
                        selectByMouse: true
                        visible: false
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                }
                Button {
                    id: btnSend
                    objectName: "btnSend"
                    visible: false
                    width: parent.width
                    text: "Send"
                }
        }
    }

    ScrollView {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        clip: true
        id: scroll
        objectName: "scroll"
        Column {
            width: mails.width
            height: mails.height-70
            spacing: 2
            Repeater {
                model: MailModel

                ToolButton {

                    width: parent.width
                    height: parent.width/8

                    Text {
                        text: model.subject
                        font.family: wt.fontFamily
                        font.pixelSize: 18
                        color: wt.color
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Text {
                        text: model.sender
                        font.family: wt.fontFamily
                        font.pixelSize: 14
                        color: wt.colorSmall
                        anchors.right: parent.right
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.rightMargin: 100
                    }

                    Rectangle {
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }

                    MouseArea 
                    {
                        anchors.fill: parent
                        onClicked: {
                            sel.text = model.data;
                        }
                    }
                }
            }
        }
    }
}