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
    id: farayand
    visible: true
    color: wt.background
    width: 600
    height: 500
    title: "Downloads"
    
    WindowTheme {
        id: wt
    }

    Text {
        id: psel
        objectName: "psel"
        visible: false
    }

    ToolBar {
        id: toolbar
        anchors.top: parent.top
        width: parent.width
        height: 70

        RowLayout {
                    anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-kill.svg'
                icon.color: "red"
                id: kill
                objectName: "kill"
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
            width: farayand.width
            height: farayand.height-70
            spacing: 2
            Repeater {
                model: ProcessModel

                Rectangle {

                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            psel.text = model.name;
                        }
                    }

                    Image {
                            source: model.icon
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
                        font.family: wt.fontFamily
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        color: wt.color
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Text {
                        text: model.user
                        id: puser
                        font.family: wt.fontFamily
                        font.pixelSize: 16
                        color: wt.colorSmall
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }
                  
                    Rectangle {
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }
                }
            }
        }
    }
}