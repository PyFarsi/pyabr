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
    id: pishkhan
    visible: true
    color: "white"
    title: "Dashboard"
    width: 600
    height: 400

    WindowTheme {
        id: wt
    }

    ToolBar {
        id: toolbar
        anchors.top: parent.top
        width: parent.width
        height: 70

        RowLayout {
                    anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-new.svg'
                icon.color: "white"
                id: newproject
                objectName: "newproject"

                onClicked: {
                    newproject.visible = false;
                    back.visible = true;
                    scroll.visible = false;
                    recnewproject.visible = true;
                    txtNewProject.visible = true;
                }
            }

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-back.svg'
                icon.color: "white"
                id: back
                objectName: "back"
                visible: false

                onClicked: {
                    newproject.visible = true;
                    back.visible = false;
                    scroll.visible = true;
                    recnewproject.visible = false;
                    txtNewProject.visible = false;
                }
            }
        }
        Text {
            anchors.centerIn: parent
            text: "New Project"
            id: txtNewProject
            objectName: "txtNewProject"
            visible: false
            font.family: wt.fontFamily;
            color: wt.colorTitle;
            font.pixelSize: wt.fontPixelSize;
        }
    }

    Rectangle {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        visible: false
        id: recnewproject
        objectName: "recnewproject"

        Column {
                anchors.centerIn: parent
                width: parent.width/2

                TextField {
                    placeholderText: "Project Name"
                    width: parent.width
                    color: wt.color
                    font.family: wt.fontFamily
                    id: leProjectName
                    objectName: "leProjectName"
                    selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
                }
                TextField {
                    placeholderText: "Package Name"
                    width: parent.width
                    color: wt.color
                    font.family: wt.fontFamily
                    id: lePackageName
                    objectName: "lePackageName"
                    selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
                }
                
                ComboBox {
                    width: parent.width
                    font.family: wt.fontFamily
                    id: cbType
                    objectName: "cbType"
                    model: ["GUI Project (PyQt QML)","GUI Project (PyQt)","Web Application Project","Console Project (Python)","Console Project (Saye)","Console Project (Pashmak)","Cosnole Project (Hascal)","Console Project (C)","Console Project (C++)"]
                }
                Button {
                    width: parent.width
                    font.family: wt.fontFamily
                    id: btnCreate
                    objectName: "btnCreate"
                    text: "Create Project"
                }
                Text {
                    color: "red"
                    text: ""
                    width: parent.width
                    font.family: wt.fontFamily
                    font.pixelSize: wt.fontPixelSize
                    id: txtWrong
                    objectName: "txtWrong"
                }
        }

    }

    ScrollView {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        clip: true
        id: scroll
        Column {
            width: pishkhan.width
            height: pishkhan.height-70
            spacing: 2
            Repeater {
                model: ProjectModel

                ToolButton {

                    width: parent.width
                    height: parent.width/8

                    Text {
                        text: model.name
                        font.family: wt.fontFamily
                        font.pixelSize: 18
                        color: wt.color
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }
                   
                    Text {
                        text: model.language
                        font.family: wt.fontFamily
                        font.pixelSize: 14
                        color: "gray"
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Rectangle {
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {

                        }
                    }
                }
            }
        }
    }
}