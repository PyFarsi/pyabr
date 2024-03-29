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
        id: txtText
        color: wt.background
        width: parent.width
        height: parent.height/2
        TextField {
            anchors.fill: parent
            font.family: wt.fontFamily
            objectName: "txtText"
            id: leText
            color: wt.color
            selectByMouse: true
            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.IBeamCursor
                acceptedButtons: Qt.NoButton
            }
        }
        anchors.topMargin: 5
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.top: parent.top
    }
    Button {
        text: "Open"
        objectName: "btnCopy"
        width: parent.width
        height: parent.height/2
        anchors.top: txtText.bottom
        font.family: wt.fontFamily
    }
}