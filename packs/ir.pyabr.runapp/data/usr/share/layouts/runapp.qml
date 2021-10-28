import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: backend
    visible: true
    color: "white"

    width: 400
    height: 90


    TextField {
        width: parent.width
        height: parent.height/2
        id: leRun
        font.family: "Iran Sans"
        objectName: "leRun"
        anchors.top: parent.top
    }
    Button {
        text: "Run"
        objectName: "btnRun"
        width: parent.width
        height: parent.height/2
        anchors.top: leRun.bottom
    }
}