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
                icon.source: 'file:///stor/usr/share/icons/breeze-details.svg'
                icon.color: "white"
                objectName: "btnDetail"
            }
         }

        Text {
            color: "white"
            id: title
            objectName: "title"
            font.family: "IRANSans"
            font.pixelSize: 18
            anchors.centerIn: parent
        }
    }

    ScrollView {
        width: parent.width
        height: parent.height-80-file.height/10
        anchors.topMargin: 10
        objectName: "Details"
        anchors.top: toolbar.bottom
        clip: true
        visible: false
        id: scroll2

        Column {
            width: file.width
            height: file.height-70-file.height/10
            spacing: 2

            GridView {
                model: FileModel
                cellWidth: 128; cellHeight: 150
                highlight: highlight
                width: parent.width
                height: parent.height
                highlightFollowsCurrentItem: false
                focus: true

                delegate: Column {
                    Image { 
                        source: model.logo
                        width: 128
                        height: 128
                        sourceSize: Qt.size( parent.width, parent.height )
                         anchors.horizontalCenter: parent.horizontalCenter
                         NumberAnimation on opacity {
                                id: file_anim2
                                from: 0
                                to: 1
                                duration: 100
                        }
                        MouseArea {
                            anchors.fill: parent
                            acceptedButtons: Qt.LeftButton | Qt.RightButton
                            onDoubleClicked: {
                                file_anim2.start();
                                fsel.text = model.path
                            }
                            onClicked: {
                                file_anim2.start();
                                fsela.text = model.path;

                                if (mouse.button === Qt.RightButton)
                                    contextMenu.popup()

                            }

                            onPressAndHold: {
                                file_anim2.start();
                                if (mouse.source === Qt.MouseEventNotSynthesized)
                                    contextMenu.popup()
                            }
                        }   
                    }
                    Text { 
                        text: model.name
                        anchors.horizontalCenter: parent.horizontalCenter
                        font.family: "IRANSans"
              
                    }
                }
            }
        }
    }

    Component {
        id: highlight
        Rectangle {
            width: view.cellWidth; height: view.cellHeight
            color: "lightsteelblue"; radius: 5
            x: view.currentItem.x
            y: view.currentItem.y
            Behavior on x { SpringAnimation { spring: 3; damping: 0.2 } }
            Behavior on y { SpringAnimation { spring: 3; damping: 0.2 } }
        }
    }

    ScrollView {
        width: parent.width
        height: parent.height-80-file.height/10
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        clip: true
        objectName: "ListView"
        id: scroll
        Column {
            width: file.width
            height: file.height-70-file.height/10
            spacing: 2
            Repeater {
                model: FileModel

                Rectangle {

                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            file_anim.start();
                            fsel.text = model.path
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
                            NumberAnimation on opacity {
                                id: file_anim
                                from: 0
                                to: 1
                                duration: 100
                            }
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
            anchors.bottom: cancel.top
        }
    }
    Button {
        id: cancel
        text: "Cancel"
        objectName: "btnCancel"
        width: parent.width/2
        height: parent.height/10
        anchors.bottomMargin: 0
        anchors.bottom: parent.bottom
        font.family: "IRANSans"
    }
    Button {
        text: "Select"
        objectName: "btnSelect"
        width: parent.width/2
        enabled: false
        height: parent.height/10
        anchors.bottomMargin: 0
        anchors.left: cancel.right
        anchors.bottom: parent.bottom
        font.family: "IRANSans"
    }
}