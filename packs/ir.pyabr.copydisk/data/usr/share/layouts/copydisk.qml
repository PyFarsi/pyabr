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
    id: file
    visible: true
    color: "white"
    width: 400
    height: 400

    Text {
        visible: false
        text: ''
        id: dsel
        objectName: "dsel"
    }

    Text {
        visible: false
        text: ''
        id: harddisk
        objectName: "harddisk"
    }

    ScrollView {
        width: parent.width
        height: parent.height-file.height/10
        anchors.topMargin: 10
        anchors.top: parent.top
        clip: true
        id: scroll
        Column {
            width: file.width
            height: file.height-file.height/10
            spacing: 2
            Repeater {
                model: CopyDiskModel

                Rectangle {

                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            dsel.text = model.dev;
                            btnCopy.enabled = true;
                        }
                    }

                    Image {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex
                            source: 'file:///stor/usr/share/icons/breeze-harddisk.svg'
                    }

                    Text {
                        text: model.title
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }
                
                    Rectangle {
                        width: parent.width
                        height: 1
                        color: "silver"
                        anchors.top: parent.bottom
                    }
                }
            }
            anchors.bottom: cancel.top
        }
    }
    Button {
        id: cancel
        text: "Cancel"
        objectName: "btnCancel"
        width: parent.width/2
        height: parent.height/10
        anchors.bottomMargin: 0
        anchors.bottom: parent.bottom
        font.family: "IRANSans"
    }
    Button {
        text: "Format and Copy"
        objectName: "btnCopy"
        id: btnCopy
        width: parent.width/2
        enabled: false
        height: parent.height/10
        anchors.bottomMargin: 0
        anchors.left: cancel.right
        anchors.bottom: parent.bottom
        font.family: "IRANSans"
    }
}