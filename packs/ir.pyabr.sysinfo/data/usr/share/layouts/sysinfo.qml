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
    id: sysinfo
    visible: true
    color: wt.background
    maximumWidth: 400
    maximumHeight: 300
    minimumWidth: 400
    minimumHeight: 300
    width: 400
    height: 300
    
    WindowTheme {
        id: wt
    }

    Column {
                width: 400
                anchors.centerIn: parent
                height: 250

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: host
                            objectName: "host"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: host1
                            objectName: "host1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: cs
                            objectName: "cs"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: cs1
                            objectName: "cs1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: bl
                            objectName: "bl"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: bl1
                            objectName: "bl1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: os
                            objectName: "os"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: os1
                            objectName: "os1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: kname
                            objectName: "kname"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: kname1
                            objectName: "kname1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }


                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: su
                            objectName: "su"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: su1
                            objectName: "su1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: de
                            objectName: "de"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: de1
                            objectName: "de1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: gui
                            objectName: "gui"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: gui1
                            objectName: "gui1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: arch
                            objectName: "arch"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: arch1
                            objectName: "arch1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }
                }
}