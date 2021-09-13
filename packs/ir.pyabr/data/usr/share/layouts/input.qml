import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: input
    visible: true
    color: "white"

    width: 400
    height: 90

    Rectangle {
        id: txtText
        width: parent.width
        height: parent.height/2
        TextField {
            anchors.centerIn: parent
            font.family: "IRANSans"
            width: parent.width
            height: parent.height
            objectName: "leText"
        }
        anchors.topMargin: 5
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.top: parent.top
    }
    Button {
        id: cancel
        text: "Cancel"
        objectName: "btnCancel"
        width: parent.width/2
        font.family: "IRANSans"
        height: parent.height/2
        anchors.top: txtText.bottom
    }
    Button {
        text: "OK"
        objectName: "btnOK"
        width: parent.width/2
        height: parent.height/2
        font.family: "IRANSans"
        anchors.left: cancel.right
        anchors.top: txtText.bottom
    }
}