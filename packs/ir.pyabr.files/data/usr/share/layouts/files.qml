import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: file
    visible: true
    color: "white"
    width: 900
    height: 700

    Text {
        visible: false
        text: ''
        id: fsel
        objectName: "fsel"
    }

    Text {
        visible: false
        text: ''
        id: act
        objectName: "act"
    }

    Text {
        visible: false
        id: fsela
        text: ''
        objectName: 'fsela'
    }

    ToolBar {
        id: toolbar
        anchors.top: parent.top
        width: parent.width
        height: 70

        RowLayout {
                        anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                icon.source: 'file:///stor/usr/share/icons/breeze-back.svg'
                icon.color: "white"
                onClicked: {
                    fsel.text = '..'
                }
            }
            ToolButton {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                icon.source: 'file:///stor/usr/share/icons/breeze-new.svg'
                icon.color: "white"
                onClicked: {
                    act.text = 'newfile'
                }
            }
            ToolButton {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                icon.source: 'file:///stor/usr/share/icons/breeze-newfolder.svg'
                icon.color: "white"
                onClicked: {
                    act.text = 'newfolder'
                }
            }
        }
    }

    Menu {
                      id: contextMenu
                      font.family: "IRANSans"
                            objectName: "contextMenu"
                            Action { 
                                id: filex
                                objectName: "filex"
                                enabled: false
                            }
                            Action { 
                                text: "New File" 
                                objectName: "newfile"
                                id: newfile
                                icon.source: "file:///stor/usr/share/icons/breeze-new.svg"
                                onTriggered: {
                                    act.text = "newfile"
                                }
                            }
                            Action { 
                                text: "New Folder" 
                                objectName: "newfolder"
                                id: newfolder
                                icon.source: "file:///stor/usr/share/icons/breeze-newfolder.svg"
                                onTriggered: {
                                    act.text = "newfolder"
                                }
                            }
                            Action { 
                                text: "Open" 
                                objectName: "open"
                                id: open
                                icon.source: "file:///stor/usr/share/icons/breeze-open.svg"
                                onTriggered: {
                                    act.text = "open"
                                }
                            }
                            Action { 
                                text: "Open with..." 
                                objectName: "openwith"
                                id: openwith
                                icon.source: "file:///stor/usr/share/icons/breeze-open.svg"
                                onTriggered: {
                                    act.text = "openwith"
                                }
                            }
                            Action { 
                                text: "Execute" 
                                objectName: "execute"
                                id: execute
                                icon.source: "file:///stor/usr/share/icons/breeze-execute.svg"
                                onTriggered: {
                                    act.text = "execute"
                                }
                            }
                            Action { 
                                text: "Cut" 
                                objectName: "cut"
                                id: cut
                                icon.source: "file:///stor/usr/share/icons/breeze-cut.svg"
                                onTriggered: {
                                    act.text = "cut"
                                }
                            }
                            Action { 
                                text: "Copy" 
                                objectName: "copy"
                                id: copy
                                icon.source: "file:///stor/usr/share/icons/breeze-copy.svg"
                                onTriggered: {
                                    act.text = "copy"
                                }
                            }
                            Action { 
                                text: "Paste" 
                                objectName: "paste"
                                id: paste
                                icon.source: "file:///stor/usr/share/icons/breeze-paste.svg"
                                onTriggered: {
                                    act.text = "paste"
                                }
                            }
                            Action { 
                                text: "Rename" 
                                objectName: "rename"
                                id: rename
                                icon.source: "file:///stor/usr/share/icons/breeze-rename.svg"
                                onTriggered: {
                                    act.text = "rename"
                                }
                            }
                            Action { 
                                text: "Delete" 
                                objectName: "delete"
                                id: remove
                                icon.source: "file:///stor/usr/share/icons/breeze-delete.svg"
                                onTriggered: {
                                    act.text = "delete"
                                }
                            }
                            Action { 
                                text: "Information" 
                                objectName: "info"
                                id: info
                                icon.source: "file:///stor/usr/share/icons/breeze-information.svg"
                                onTriggered: {
                                    act.text = "info"
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
        Column {
            width: file.width
            height: file.height-70
            spacing: 2
            Repeater {
                model: FileModel

                Rectangle {

                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = model.path
                        }
                        onClicked: {
                            fsela.text = model.path

                            if (mouse.button === Qt.RightButton)
                                contextMenu.popup()

                        }

                        onPressAndHold: {
                            if (mouse.source === Qt.MouseEventNotSynthesized)
                                contextMenu.popup()
                        }
                    }

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
                        text: model.name
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Text {
                        text: model.mimetype
                        font.family: "IRANSans"
                        font.pixelSize: 14
                        color: "gray"
                        anchors.right: parent.right
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.rightMargin: 100
                    }
                   
                    Text {
                        text: model.size
                        font.family: "IRANSans"
                        font.pixelSize: 14
                        color: "gray"
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
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
}