import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: file
    visible: true
    color: "white"
    width: 900
    height: 700

    Text {
        visible: false
        text: ''
        id: fsel
        objectName: "fsel"
    }

    Text {
        visible: false
        text: ''
        id: act
        objectName: "act"
    }

    Text {
        visible: false
        id: fsela
        text: ''
        objectName: 'fsela'
    }

    ToolBar {
        id: toolbar
        anchors.top: parent.top
        width: parent.width
        height: 70

        RowLayout {
                        anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                icon.source: 'file:///stor/usr/share/icons/breeze-back.svg'
                icon.color: "white"
                objectName: "back"
                visible: false
                onClicked: {
                    fsel.text = '..'
                }
            }
        }
        Text {
            anchors.centerIn: parent
            text: "Control"
            visible: true
            font.family: "IRANSans"
            font.pixelSize: 20
            color: "white"
            objectName: "title"
        }
    }

    ScrollView {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        clip: true
        id: scroll

        /* Appearanc */
        Rectangle {
            objectName: "apper_exec"
            visible: false
            width: file.width
            height: file.height-70
            

            Text {
                text: "Change Wallpapers"
                objectName: "txtWallpapers"
                id: txtWallpapers
                anchors.top: parent.top
                color: "gray"
                anchors.horizontalCenter: parent.horizontalCenter
                font.family: "IRANSans"
                font.pixelSize: 15
                height: parent.height/20
            }

            Rectangle {
                color: "white"
                objectName: "change_desktop"
                id: change_desktop
                anchors.top: txtWallpapers.bottom
                anchors.leftMargin: 5
                anchors.rightMargin: 5
                width: parent.width/4
                height: parent.height/4

                Image {
                    anchors.top: parent.top
                    width: parent.width
                    height: parent.height/1.2
                    source: "file:///stor/usr/share/backgrounds/breeze-next.png"
                    objectName: "imgChange_desktop"
                }

                Button {
                    objectName: "btnChange_desktop"
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: parent.height-parent.height/1.5
                    text: "Change Desktop"
                    font.family: "IRANSans"
                }
            }

            Rectangle {
                color: "white"
                objectName: "change_lock"
                anchors.leftMargin: 5
                anchors.rightMargin: 5
                id: change_lock
                anchors.top: txtWallpapers.bottom
                anchors.left: change_desktop.right
                width: parent.width/4
                height: parent.height/4

                Image {
                    anchors.top: parent.top
                    width: parent.width
                    height: parent.height/1.2
                    source: "file:///stor/usr/share/backgrounds/breeze-splash.jpg"
                    objectName: "imgChange_lock"
                }

                Button {
                    objectName: "btnChange_lock"
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: parent.height-parent.height/1.5
                    text: "Change Lock"
                    font.family: "IRANSans"
                }
            }

            Rectangle {
                anchors.leftMargin: 5
                anchors.rightMargin: 5
                color: "white"
                objectName: "change_unlock"
                id: change_unlock
                anchors.left: change_lock.right
                anchors.top: txtWallpapers.bottom
                width: parent.width/4
                height: parent.height/4

                Image {
                    anchors.top: parent.top
                    width: parent.width
                    height: parent.height/1.2
                    source: "file:///stor/usr/share/backgrounds/breeze-splash.jpg"
                    objectName: "imgChange_unlock"
                }

                Button {
                    objectName: "btnChange_unlock"
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: parent.height-parent.height/1.5
                    text: "Change Unlock"
                    font.family: "IRANSans"
                }
            }

            Rectangle {
                color: "white"
                objectName: "change_enter"
                id: change_enter
                anchors.left: change_unlock.right
                anchors.top: txtWallpapers.bottom
                width: parent.width/4
                height: parent.height/4
                anchors.leftMargin: 5
                anchors.rightMargin: 5

                Image {
                    anchors.top: parent.top
                    width: parent.width
                    height: parent.height/1.2
                    source: "file:///stor/usr/share/backgrounds/breeze-splash.jpg"
                    objectName: "imgChange_enter"
                }

                Button {
                    objectName: "btnChange_enter"
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: parent.height-parent.height/1.5
                    text: "Change Enter"
                    font.family: "IRANSans"
                }
            }
            Rectangle {
                        width: parent.width
                        height: 1
                        id: line1
                        color: "silver"
                        anchors.top: change_enter.bottom
            }
            Text {
                text: "Dock Location"
                objectName: "txtDock"
                id: txtDock
                color: "gray"
                anchors.top: line1.top
                anchors.horizontalCenter: parent.horizontalCenter
                font.family: "IRANSans"
                font.pixelSize: 15
                height: parent.height/20
            }
            /* Change Dock */
            ComboBox {
                anchors.top: txtDock.bottom
                model: ['Bottom (default)','Top','Left','Right','Windows 11 mode']
                anchors.horizontalCenter: parent.horizontalCenter
                width: parent.width/2
                id: dockLocation
                objectName: "cbDock"
            }
            Rectangle {
                width: parent.width
                height: 1
                id: line2
                color: "silver"
                anchors.top: dockLocation.bottom
            }
            Button {
                text: "Apply"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.rightMargin: 20
                font.family: "IRANSans"
                id: apply
                objectName: "apply"
                anchors.bottomMargin: 20
            }
            Button {
                text: "Cancel"
                anchors.bottom: parent.bottom
                font.family: "IRANSans"
                anchors.right: apply.left
                anchors.rightMargin: 20
                id: cancel
                objectName: "cancel"
                onClicked: {
                    fsel.text = '..'
                }
                anchors.bottomMargin: 20
            }
        }

        /* Users */
        Rectangle {
            objectName: "users_exec"
            id: users_exec
            visible: false
            width: file.width
            height: file.height-70

            Column {
                spacing: 2
                width: users_exec.width
                height: users_exec.height


                Repeater {
                    model: UserModel

                    Rectangle {
                        visible: true

                        width: parent.width
                        height: parent.width/10
                        color: "transparent"

                        MouseArea {
                            anchors.fill: parent
                            acceptedButtons: Qt.LeftButton | Qt.RightButton
                            onDoubleClicked: {
                            }
                        }

                        Image {
                                source: model.profile
                                anchors.left: parent.left
                                anchors.leftMargin: 20
                                anchors.rightMargin: 20
                                width: parent.height
                                sourceSize: Qt.size( parent.width, parent.height )
                                height: parent.height
                                id: imagexx
                        }

                        Text {
                            text: model.fullname
                            font.family: "IRANSans"
                            font.pixelSize: 18
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.left: imagexx.right
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
        /* System Informations */
        Rectangle {
            objectName: "sysinfo_exec"
            visible: false
            width: file.width
            height: file.height-70
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

        /* Control View */
        Column {
            width: file.width
            height: file.height-70
            objectName: "controlview"
            spacing: 2

                /* Appearance */
                Rectangle {
                    id: apper
                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'apper'
                        }
                    }

                    Image {
                            source: 'file:///stor/usr/share/icons/breeze-wallpaper.svg'
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex1
                    }

                    Text {
                        text: 'System Informations'
                        font.family: "IRANSans"
                        objectName: 'apper'
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex1.right
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
                /* Users */
                Rectangle {
                    id: users
                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'users'
                        }
                    }

                    Image {
                            source: 'file:///stor/usr/share/icons/breeze-users.svg'
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex2
                    }

                    Text {
                        text: 'Users'
                        font.family: "IRANSans"
                        objectName: 'users'
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex2.right
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
                /* System Informations */
                Rectangle {
                    id: sysinfo
                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'sysinfo'
                        }
                    }

                    Image {
                            source: 'file:///stor/usr/share/icons/breeze-info.svg'
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex
                    }

                    Text {
                        text: 'System Informations'
                        font.family: "IRANSans"
                        objectName: 'sysinfo'
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