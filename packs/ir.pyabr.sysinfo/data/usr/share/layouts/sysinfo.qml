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
    color: "white"
    maximumWidth: 400
    maximumHeight: 300
    minimumWidth: 400
    minimumHeight: 300
    width: 400
    height: 300

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
                            font.family: "IRANSans"
                            id: host
                            objectName: "host"
                            font.pixelSize: 16
                            color: "gray"
                        }
                        Text {
                            color: "black"
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: "IRANSans"
                            id: host1
                            objectName: "host1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: "silver"
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: "IRANSans"
                            id: cs
                            objectName: "cs"
                            font.pixelSize: 16
                            color: "gray"
                        }
                        Text {
                            color: "black"
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: "IRANSans"
                            id: cs1
                            objectName: "cs1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: "silver"
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: "IRANSans"
                            id: bl
                            objectName: "bl"
                            font.pixelSize: 16
                            color: "gray"
                        }
                        Text {
                            color: "black"
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: "IRANSans"
                            id: bl1
                            objectName: "bl1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: "silver"
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: "IRANSans"
                            id: os
                            objectName: "os"
                            font.pixelSize: 16
                            color: "gray"
                        }
                        Text {
                            color: "black"
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: "IRANSans"
                            id: os1
                            objectName: "os1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: "silver"
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: "IRANSans"
                            id: kname
                            objectName: "kname"
                            font.pixelSize: 16
                            color: "gray"
                        }
                        Text {
                            color: "black"
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: "IRANSans"
                            id: kname1
                            objectName: "kname1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: "silver"
                        }
                    }


                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: "IRANSans"
                            id: su
                            objectName: "su"
                            font.pixelSize: 16
                            color: "gray"
                        }
                        Text {
                            color: "black"
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: "IRANSans"
                            id: su1
                            objectName: "su1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: "silver"
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: "IRANSans"
                            id: de
                            objectName: "de"
                            font.pixelSize: 16
                            color: "gray"
                        }
                        Text {
                            color: "black"
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: "IRANSans"
                            id: de1
                            objectName: "de1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: "silver"
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: "IRANSans"
                            id: gui
                            objectName: "gui"
                            font.pixelSize: 16
                            color: "gray"
                        }
                        Text {
                            color: "black"
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: "IRANSans"
                            id: gui1
                            objectName: "gui1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: "silver"
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: "IRANSans"
                            id: arch
                            objectName: "arch"
                            font.pixelSize: 16
                            color: "gray"
                        }
                        Text {
                            color: "black"
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: "IRANSans"
                            id: arch1
                            objectName: "arch1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: "silver"
                        }
                    }
                }
}