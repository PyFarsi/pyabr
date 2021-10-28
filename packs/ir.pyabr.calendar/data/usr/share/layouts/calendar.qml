import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: app
    visible: true
    color: "white"
    width: 600
    height: 500
    title: "Calendar"

    PersianCalendar {
        visible: false
        anchors.fill: parent
        objectName: "Jalali"
    }

    Calendar {
        anchors.fill: parent
        visible: false
        objectName: "Gregorian"
    }
}