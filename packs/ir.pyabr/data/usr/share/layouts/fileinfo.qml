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
    id: fileinfo
    visible: true
    color: "white"
    maximumWidth: 600
    maximumHeight: 400
    minimumWidth: 600
    minimumHeight: 400
    width: 600
    height: 400
    Column {
        spacing: 2
        width: parent.width/2
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        Text {
            text: 'Filename: '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "name"
        }
        Text {
            text: 'Type: '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "type"
        }
        Text {
            text: 'Location: '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "location"
        }
        Text {
            text: 'Size: '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "size"
        }
        Text {
            text: 'Created: '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "created"
        }
        Text {
            text: 'Modified: '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "modified"
        }
        Text {
            text: 'Owership:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "owership"
        }
        Text {
            text: 'Access for owner: '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "perma"
        }
        Text {
            text: 'Access for users: '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "permb"
        }
        Text {
            text: 'Access for guest: '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "permc"
        }
    }

    Column {
        spacing: 2
        width: parent.width/2
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        Text {
            text: 'vmabr.pyc'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "name1"
            font.bold: true
        }
        Text {
            text: 'Python bytecode'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "type1"
            font.bold: true
        }
        Text {
            text: '/'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "location1"
            font.bold: true
        }
        Text {
            text: '12 GB'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "size1"
            font.bold: true
        }
        Text {
            text: '1382-04-30 08:00:00'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "created1"
            font.bold: true
        }
        Text {
            text: '1400-04-30 08:00:00'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "modified1"
            font.bold: true
        }
        Text {
            text: 'Mani Jamali'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "owership1"
            font.bold: true
        }
        Text {
            text: 'Read, Write, Execute'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "perma1"
            font.bold: true
        }
        Text {
            text: 'Read, Write'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "permb1"
            font.bold: true
        }
        Text {
            text: 'Read'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            objectName: "permc1"
            font.bold: true
        }
    }
}