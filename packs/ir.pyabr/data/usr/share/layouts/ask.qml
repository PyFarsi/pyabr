import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: ask
    visible: true
    color: "white"

    width: 500
    height: 90

    Rectangle {
        id: txtText
        width: parent.width
        height: parent.height/2
        Text {
            anchors.centerIn: parent
            font.family: "Iran Sans"
            objectName: "txtText"
        }
        anchors.topMargin: 5
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.top: parent.top
    }
    Button {
        id: cancel
        text: "No"
        objectName: "btnCancel"
        font.family: "IRANSans"
        width: parent.width/2
        height: parent.height/2
        anchors.top: txtText.bottom
    }
    Button {
        text: "Yes"
        objectName: "btnOK"
        width: parent.width/2
        font.family: "IRANSans"
        height: parent.height/2
        anchors.left: cancel.right
        anchors.top: txtText.bottom
    }
}