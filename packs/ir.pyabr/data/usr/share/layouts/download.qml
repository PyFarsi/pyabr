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
    id: download
    visible: true
    color: "white"

    width: 400
    height: 100
    title: "Download a file"

    Rectangle {
        id: txtText
        width: parent.width
        height: parent.height/2
        TextField {
            anchors.centerIn: parent
            font.family: "IRANSans"
            width: parent.width
            height: parent.height
            objectName: "leDownload"
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
    ProgressBar {
            anchors.top: txtText.bottom
            width: parent.width
            height: 10
            //indeterminate: false
            value: 0
            objectName: "pro"
            id: pro
    }
    Button {
        text: "Download"
        objectName: "btnDownload"
        width: parent.width
        height: parent.height/2
        font.family: "IRANSans"
        anchors.top: pro.bottom
    }
}