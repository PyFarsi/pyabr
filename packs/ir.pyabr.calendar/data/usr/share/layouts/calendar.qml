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