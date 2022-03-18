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
    width: 600
    height: 600
    
    WindowTheme {
        id: wt
    }
    title: "Calendar"

    Text {
        id: dsel
        objectName: "dsel"
    }

    Text {
        id: dselm
        objectName: "dselm"
    }

    PersianCalendar {
        visible: false
        id: jalali_c
        anchors.top: parent.top
        width: parent.width
        height: parent.height-parent.height/8
        anchors.fill: parent
        objectName: "Jalali"
    }

    Calendar {
        anchors.top: parent.top
        width: parent.width
        height: parent.height-parent.height/8
        visible: false
        id: gregorian_c
        objectName: "Gregorian"
    }

    Rectangle {
        color: "white"
        anchors.bottom: parent.bottom
        width: parent.width
        height: parent.height/8

        Text {
            anchors.centerIn: parent
            text: ""
            id: txtD
            objectName: "txtD"
            font.family: wt.fontFamily
            font.pixelSize: 20
            color: wt.color
        }
    }
}