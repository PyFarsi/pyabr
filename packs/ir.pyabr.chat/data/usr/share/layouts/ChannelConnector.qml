import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

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
                }
                TextField {
                    placeholderText: "Username"
                    width: parent.width
                    font.family: "IRANSans"
                    id: leUsername
                    objectName: "leUsername"
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