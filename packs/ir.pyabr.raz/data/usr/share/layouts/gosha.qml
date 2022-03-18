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
    id: mails
    visible: true
    color: wt.background
    width: 600
    height: 500
    title: "Gosha"
    
    WindowTheme {
        id: wt
    }

    Rectangle {
        width: parent.width
        height: parent.height
        anchors.fill: parent
        visible: true
        id: encrypt
        color: wt.background
        objectName: "encrypt"

        Column {
                anchors.centerIn: parent
                width: parent.width/1.2
                height: parent.height/1.2
                
                TextArea {
                        id: textT
                        color: wt.color
                        width: parent.width
                        font.family: wt.fontFamily
                        anchors.fill: parent
                        placeholderText: "Text"
                        enabled: false
                        objectName: "text"
                        selectByMouse: true
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                }
        }
    }
}