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
    id: ask
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
            objectName: "txtText"
            color: wt.color
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
        font.family: wt.fontFamily
        width: parent.width/2
        height: parent.height/2
        anchors.top: txtText.bottom
    }
    Button {
        text: "Yes"
        objectName: "btnOK"
        width: parent.width/2
        font.family: wt.fontFamily
        height: parent.height/2
        anchors.left: cancel.right
        anchors.top: txtText.bottom
    }
}