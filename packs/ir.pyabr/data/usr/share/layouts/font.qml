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
    id: font
    visible: true
    color: "white"

    width: 500
    height: 600

    Text {
        text: ""
        objectName: "bt"
        id: bt
    }

    ScrollView {
        width: parent.width
        height: parent.height-parent.height/12
        clip: true
        id: scroll
        Column {
            width: font.width
            height: font.height-font.height/12
            spacing: 2
            Repeater {
                model: fontList

                ToolButton {
                    width: parent.width
                    height: parent.width/6
                    //color: "white"

                    Text {
                        anchors.centerIn: parent
                        text: model.text
                        font.family: model.fontFamily
                        font.pixelSize: model.fontSize
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            bt.text = model.fontFamily
                        }
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
        id: cancel
        text: "Cancel"
        objectName: "btnCancel"
        width: parent.width/2
        height: parent.height/12
        anchors.bottom: parent.bottom
        font.family: "IRANSans"
    }
    Button {
        text: "Select"
        objectName: "btnSelect"
        anchors.bottom: parent.bottom
        width: parent.width/2
        font.family: "IRANSans"
        height: parent.height/12
        anchors.left: cancel.right
    }
}