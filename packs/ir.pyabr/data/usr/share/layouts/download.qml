import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

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