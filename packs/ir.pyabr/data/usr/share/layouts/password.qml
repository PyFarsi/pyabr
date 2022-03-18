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
    id: password
    visible: true
    color: wt.background

    width: 400
    height: 90
    
    WindowTheme {
        id: wt
    }

    Rectangle {
        id: txtText
        width: parent.width
        color: wt.background
        height: parent.height/2
        TextField {
            anchors.centerIn: parent
            font.family: wt.fontFamily
            color: wt.color
            width: parent.width
            echoMode: TextInput.Password
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
        height: parent.height/2
        font.family: wt.fontFamily
        anchors.top: txtText.bottom
    }
    Button {
        text: "OK"
        objectName: "btnOK"
        font.family: wt.fontFamily
        width: parent.width/2
        height: parent.height/2
        anchors.left: cancel.right
        anchors.top: txtText.bottom
    }
}