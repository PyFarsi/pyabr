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
    id: backend
    visible: true
    color: wt.background

    width: 500
    height: 90
    
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
        font.family: wt.fontFamily
    }
}