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

    width: 400
    height: 90

    WindowTheme {
        id: wt
    }

    TextField {
        width: parent.width
        height: parent.height/2
        id: leRun
        font.family: wt.fontFamily
        color: wt.color
        selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
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