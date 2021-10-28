import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: openwith
    visible: true
    color: "white"
    width: 600
    height: 500
    title: "Open with"

    Text {
        id: asel
        objectName: "asel"
        text: ""
        visible: false
    }

    ScrollView {
        width: parent.width
        height: parent.height-(80)
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        clip: true
        id: scroll
        Column {
            width: openwith.width
            height: openwith.height-70
            spacing: 2
            Repeater {
                model: ApplicationModel

                Rectangle {

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            asel.text = model.name
                            always.enabled = true
                            atonce.enabled = true
                        }
                    }

                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    Image {
                            source: model.logo
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex
                    }

                    Text {
                        text: model.label
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
        }
    }
    Button {
        id: atonce
        text: "At Once"
        objectName: "atOnce"
        width: parent.width/2
        height: parent.height/10
        enabled: false
        anchors.bottomMargin: 0
        anchors.bottom: parent.bottom
        font.family: "IRANSans"
    }
    Button {
        text: "Always"
        objectName: "always"
        width: parent.width/2
        id: always
        enabled: false
        height: parent.height/10
        anchors.bottomMargin: 0
        anchors.left: atonce.right
        anchors.bottom: parent.bottom
        font.family: "IRANSans"
    }
}