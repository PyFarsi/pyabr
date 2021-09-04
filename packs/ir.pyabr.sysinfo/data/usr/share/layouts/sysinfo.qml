import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: sysinfo
    visible: true
    color: "white"
    maximumWidth: 600
    maximumHeight: 300
    minimumWidth: 600
    minimumHeight: 300
    width: 600
    height: 300
    Image {
        source: 'file:///stor/usr/share/icons/breeze-cloud.svg'
        anchors.top: parent.top
        anchors.topMargin: 20
        width: parent.height
        sourceSize: Qt.size( parent.width, parent.height )
        height: parent.height
    }

    Column {
        spacing: 2
        width: parent.width/2
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        Text {
            text: 'Static hostname:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "host"
        }
        Text {
            text: 'Cloud distro:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "cs"
        }
        Text {
            text: 'Build date:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "bl"
        }
        Text {
            text: 'Operating System:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "os"
        }
        Text {
            text: 'Kernel:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "kname"
        }
        Text {
            text: 'Switched User:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "su"
        }
        Text {
            text: 'Desktop Enviroment:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "de"
        }
        Text {
            text: 'Graphical Toolkit:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "gui"
        }
        Text {
            text: 'Architecture:  '
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.right: parent.right
            objectName: "arch"
        }
    }

    Column {
        spacing: 2
        width: parent.width/2
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        Text {
            text: 'pyabr'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            font.bold: true
            objectName: "host1"
        }
        Text {
            text: 'Pyabr 2.1 (Aras)'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            font.bold: true
            objectName: "cs1"
        }
        Text {
            text: '1400-06-13'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            font.bold: true
            objectName: "bl1"
        }
        Text {
            text: 'Pyabr'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            font.bold: true
            objectName: "os1"
        }
        Text {
            text: 'Linux 5'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            font.bold: true
            objectName: "kname1"
        }
        Text {
            text: 'root'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            font.bold: true
            objectName: "su1"
        }
        Text {
            text: 'Baran Desktop Enviroment'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            font.bold: true
            objectName: "de1"
        }
        Text {
            text: 'Qt Framework'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            font.bold: true
            objectName: "gui1"
        }
        Text {
            text: 'AMD, Intel 64-bit'
            font.family: "IRANSans"
            font.pixelSize: 16
            anchors.left: parent.left
            font.bold: true
            objectName: "arch1"
        }
    }
}