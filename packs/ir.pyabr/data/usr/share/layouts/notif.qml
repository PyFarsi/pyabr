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
    id: notif
    visible: true
    color: wt.background
    width: 500
    height: 90
    flags: Qt.FramelessWindowHint | Qt.Window
    x: Screen.width/2-width/2
    y: Screen.height/8-height/2
    
    WindowTheme {
        id: wt
    }

    Rectangle {
        color: wt.background
        id: txtText
        width: parent.width
        height: parent.height/2
        Text {
            anchors.centerIn: parent
            font.family: wt.fontFamily
            color: wt.color
            objectName: "txtText"
        }
        Image {
            width: parent.height-15
            height: parent.height-15
            sourceSize: Qt.size( parent.height-15, parent.height-15 )
            objectName: "imgNotif"
            anchors.left: parent.left
            anchors.leftMargin: 15
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 15
            anchors.top: parent.top
            anchors.topMargin: 15
        }
        anchors.topMargin: 5
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.top: parent.top
    }
    ToolButton {
        text: "View"
        objectName: "btnView"
        width: parent.width
        height: parent.height/2
        anchors.top: txtText.bottom
        font.family: wt.fontFamily
    }
}