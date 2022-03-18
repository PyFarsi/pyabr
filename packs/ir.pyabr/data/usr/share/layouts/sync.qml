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
    id: app
    visible: true
    color: wt.background
    width: 400
    height: 200

    WindowTheme {
        id: wt
    }
    Column {
                anchors.centerIn: parent
                width: parent.width/2

                TextField {
                    placeholderText: "Username"
                    width: parent.width
                    font.family: wt.fontFamily
                    id: leUsername
                    color: wt.color
                    objectName: "leUsername"
                    selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
                }
                TextField {
                    placeholderText: "Password"
                    width: parent.width
                    font.family: wt.fontFamily
                    id: lePassword
                    color: wt.color
                    objectName: "lePassword"
                    echoMode: TextInput.Password
                }
                Button {
                    text: "Sync"
                    width: parent.width
                    objectName: "btnCreate"
                    id: btnCreate
                }
    }
}