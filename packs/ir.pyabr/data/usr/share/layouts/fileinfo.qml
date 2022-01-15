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
    color: "white"
    maximumWidth: 400
    maximumHeight: 350
    minimumWidth: 400
    minimumHeight: 350
    width: 400
    height: 350
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
                            font.family: "IRANSans"
                            id: name
                            objectName: "name"
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
                            id: name1
                            objectName: "name1"
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
                            id: type
                            objectName: "type"
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
                            id: type1
                            objectName: "type1"
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
                            id: location
                            objectName: "location"
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
                            id: location1
                            objectName: "location1"
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
                            id: size
                            objectName: "size"
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
                            id: size1
                            objectName: "size1"
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
                            id: created
                            objectName: "created"
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
                            id: created1
                            objectName: "created1"
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
                            id: modified
                            objectName: "modified"
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
                            id: modified1
                            objectName: "modified1"
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
                            id: ownership
                            objectName: "ownership"
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
                            id: ownership1
                            objectName: "ownership1"
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
                            id: perma
                            objectName: "perma"
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
                            id: perma1
                            objectName: "perma1"
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
                            id: permb
                            objectName: "permb"
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
                            id: permb1
                            objectName: "permb1"
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
                            id: permc
                            objectName: "permc"
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
                            id: permc1
                            objectName: "permc1"
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