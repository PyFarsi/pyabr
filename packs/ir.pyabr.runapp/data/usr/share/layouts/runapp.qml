import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4

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