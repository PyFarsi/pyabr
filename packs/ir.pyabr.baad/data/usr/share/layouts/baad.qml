import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12
import QtGraphicalEffects 1.12

ApplicationWindow {
    id: app
    visible: true
    color: wt.background
    width: 1000
    height: 600
    
    WindowTheme {
        id: wt
    }

    background: Rectangle {
        Image {
            id: background
            objectName: "background"
        }
        FastBlur {
            anchors.fill: background
            source: background
            radius: 32
        }
        Text {
            color: wt.color
            text: ""
            objectName: "txtTemp"
            font.pixelSize: 100
            font.family: wt.fontFamily
            id: txtTemp
            anchors.centerIn: parent
        }
    }

    ToolBar {
        id: toolbar
        anchors.bottom: parent.bottom
        width: parent.width
        height: 70

        RowLayout {
            anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                text: "°C"
                id: tempC
                objectName: "tempC"
            }

            ToolButton {
                text: "°F"
                id: tempF
                objectName: "tempF"
            }

            ToolButton {
                text: "k"
                id: tempK
                objectName: "tempK"
            }

        }
    }
}