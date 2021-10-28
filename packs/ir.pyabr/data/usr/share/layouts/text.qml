import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: backend
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
            font.family: "IRANSans"
            objectName: "txtText"
        }
        anchors.topMargin: 5
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.top: parent.top
    }
    Button {
        text: "OK"
        objectName: "btnOK"
        width: parent.width
        height: parent.height/2
        anchors.top: txtText.bottom
        font.family: "IRANSans"
    }
}