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
    id: upstor
    visible: true
    color: wt.background

    width: 500
    height: 200
    
    WindowTheme {
        id: wt
    }

    Rectangle {
        id: txtText
        width: parent.width
        height: parent.height/2
        
        Image {
            anchors.left: parent.left
            anchors.leftMargin: 20
            id: imagex
            objectName: "logo"
            anchors.rightMargin: 20
            height: parent.height
            width: parent.height
            sourceSize: Qt.size( imagex.width, imagex.height )
        }

        Text {
            anchors.left: imagex.right
            text: "Pyabr 2.1.14 new release"
            font.family: wt.fontFamily
            font.pixelSize: 30
            color: wt.color
            anchors.leftMargin: 20
            objectName: "name"
            anchors.rightMargin: 20
            anchors.topMargin: 20
            anchors.top: parent.top
            id: titlex
        }

        ProgressBar {
            anchors.top: parent.top
            width: parent.width
            height: 10
            indeterminate: false
            objectName: "pro"
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
        font.family: wt.fontFamily
        width: parent.width/2
        height: parent.height/4
        anchors.bottom: parent.bottom
    }
    Button {
        text: "Upgrade"
        objectName: "btnUpgrade"
        width: parent.width/2
        font.family: wt.fontFamily
        height: parent.height/4
        anchors.left: cancel.right
        anchors.bottom: parent.bottom
    }
}