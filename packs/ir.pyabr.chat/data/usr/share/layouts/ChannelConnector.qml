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
    color: "white"
    width: 400
    height: 200

    Column {
                anchors.centerIn: parent
                width: parent.width/2

                TextField {
                    placeholderText: "Channel host (URL)"
                    width: parent.width
                    font.family: "IRANSans"
                    id: leChannel
                    objectName: "leChannel"
                    selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
                }
                TextField {
                    placeholderText: "Username"
                    width: parent.width
                    font.family: "IRANSans"
                    id: leUsername
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
                    font.family: "IRANSans"
                    id: lePassword
                    objectName: "lePassword"
                    echoMode: TextInput.Password
                }
                Button {
                    text: "Connect"
                    width: parent.width
                    objectName: "btnConnect"
                    id: btnConnect
                }
    }
}