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
    id: fileinfo
    visible: true
    color: wt.background
    maximumWidth: 400
    maximumHeight: 350
    minimumWidth: 400
    minimumHeight: 350
    width: 400
    height: 350
    WindowTheme {
        id: wt
    }
    Column {
        spacing: 2
        width: parent.width
        height: parent.height
        anchors.fill: parent
        ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: name
                            objectName: "name"
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
                            id: name1
                            objectName: "name1"
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
                            id: type
                            objectName: "type"
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
                            id: type1
                            objectName: "type1"
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
                            id: location
                            objectName: "location"
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
                            id: location1
                            objectName: "location1"
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
                            id: size
                            objectName: "size"
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
                            id: size1
                            objectName: "size1"
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
                            id: created
                            objectName: "created"
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
                            id: created1
                            objectName: "created1"
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
                            id: modified
                            objectName: "modified"
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
                            id: modified1
                            objectName: "modified1"
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
                            id: ownership
                            objectName: "ownership"
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
                            id: ownership1
                            objectName: "ownership1"
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
                            id: perma
                            objectName: "perma"
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
                            id: perma1
                            objectName: "perma1"
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
                            id: permb
                            objectName: "permb"
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
                            id: permb1
                            objectName: "permb1"
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
                            id: permc
                            objectName: "permc"
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
                            id: permc1
                            objectName: "permc1"
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