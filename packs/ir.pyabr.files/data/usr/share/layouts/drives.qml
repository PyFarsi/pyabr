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
        id: dsel
        objectName: "dsel"
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
                icon.source: 'file:///stor/usr/share/icons/breeze-details.svg'
                icon.color: "white"
                objectName: "btnDetail"
            }
        }
    }

    ScrollView {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.leftMargin: 10
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.rightMargin: 10
        objectName: "Details"
        anchors.top: toolbar.bottom
        clip: true
        visible: false
        id: scroll2

        Column {
            width: file.width
            height: file.height-70
            spacing: 2

            GridView {
                model: DrivesModel
                cellWidth: 150; cellHeight: 150
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
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                dsel.text = model.dev;
                            }
                        }
                    }
                    Text { 
                        text: model.title
                         anchors.horizontalCenter: parent.horizontalCenter
                          font.family: "IRANSans"
                        width: parent.width
              
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
        height: parent.height-80
        objectName: "ListView"
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        clip: true
        visible: false
        id: scroll
        Column {
            width: file.width
            height: file.height-70
            spacing: 2
            Repeater {
                model: DrivesModel

                ToolButton {

                    width: parent.width
                    height: parent.width/8
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        onDoubleClicked: {
                            dsel.text = model.dev;
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
                        text: model.title
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
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