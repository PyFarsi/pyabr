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
    id: file
    visible: true
    color: wt.background
    width: 900
    height: 700
    
    WindowTheme {
        id: wt
    }

    Text {
        visible: false
        text: ''
        id: fsel
        objectName: "fsel"
    }

    Text {
        visible: false
        text: ''
        id: rsel
        objectName: 'rsel'
    }

    Text {
        visible: false
        text: ''
        id: wsel
        objectName: 'wsel'
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

    Text {
        visible: false
        id: usel
        objectName: "usel"
    }

    Text {
        visible: false
        id: lsel
        objectName: "lsel"
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

            ToolButton {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                icon.source: 'file:///stor/usr/share/icons/breeze-back.svg'
                icon.color: "white"
                objectName: "back_users"
                visible: false
                onClicked: {
                    fsel.text = 'users'
                }
            }
            ToolButton {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                icon.source: 'file:///stor/usr/share/icons/breeze-new.svg'
                icon.color: "white"
                objectName: "adduser"
                visible: false
            }
        }
        Text {
            anchors.centerIn: parent
            text: "Control"
            visible: true
            font.family: wt.fontFamily
            font.pixelSize: 20
            color: wt.colorTitle
            objectName: "title"
        }
    }

    /* Appearanc */
        Rectangle {
            objectName: "apper_exec"
            visible: false
            width: file.width
            anchors.top: toolbar.bottom
            height: file.height-70
            color: wt.background
            

            Text {
                text: "Change Wallpapers"
                objectName: "txtWallpapers"
                id: txtWallpapers
                anchors.top: parent.top
                color: wt.color
                anchors.horizontalCenter: parent.horizontalCenter
                font.family: wt.fontFamily
                font.pixelSize: 15
                height: parent.height/20
            }

            Rectangle {
                color: wt.background
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
                    objectName: "imgChange_desktop"
                }

                Button {
                    objectName: "btnChange_desktop"
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: parent.height-parent.height/1.5
                    text: "Change Desktop"
                    font.family: wt.fontFamily
                }
            }

            Rectangle {
                color: wt.background
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
                    objectName: "imgChange_lock"
                }

                Button {
                    objectName: "btnChange_lock"
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: parent.height-parent.height/1.5
                    text: "Change Lock"
                    font.family: wt.fontFamily
                }
            }

            Rectangle {
                anchors.leftMargin: 5
                anchors.rightMargin: 5
                color: wt.background
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
                    objectName: "imgChange_unlock"
                }

                Button {
                    objectName: "btnChange_unlock"
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: parent.height-parent.height/1.5
                    text: "Change Unlock"
                    font.family: wt.fontFamily
                }
            }

            Rectangle {
                color: wt.background
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
                    objectName: "imgChange_enter"
                }

                Button {
                    objectName: "btnChange_enter"
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: parent.height-parent.height/1.5
                    text: "Change Enter"
                    font.family: wt.fontFamily
                }
            }
            Rectangle {
                        width: parent.width
                        height: 1
                        id: line1
                        color: wt.colorLine
                        anchors.top: change_enter.bottom
            }
            Text {
                text: "Dock Location"
                objectName: "txtDock"
                id: txtDock
                color: wt.color
                anchors.top: line1.top
                anchors.horizontalCenter: parent.horizontalCenter
                font.family: wt.fontFamily
                font.pixelSize: 15
                height: parent.height/20
            }
            /* Change Dock */
            ComboBox {
                anchors.top: txtDock.bottom
                model: ['Bottom (default)','Top','Left','Right','Windows 11 (Bottom)','Windows 11 (Top)','Windows 11 (Left)','Windows 11 (Right)','Unity (bottom)','Unity (top)','Unity (left)','Unity (right)']
                anchors.horizontalCenter: parent.horizontalCenter
                width: parent.width/2
                id: dockLocation
                objectName: "cbDock"
            }
            Rectangle {
                width: parent.width
                height: 1
                id: line2
                color: wt.colorLine
                anchors.top: dockLocation.bottom
            }
            Text {
                text: "Window Manager Theme"
                objectName: "txtWMTheme"
                id: txtWMTheme
                color: wt.color
                anchors.top: line2.top
                anchors.horizontalCenter: parent.horizontalCenter
                font.family: wt.fontFamily
                font.pixelSize: 15
                height: parent.height/20
            }
            ComboBox {
                anchors.top: txtWMTheme.bottom
                model: ['Select one','Afterpiece (Default)','Windows 10','OS X (Light)','OS X (Dark)']
                anchors.horizontalCenter: parent.horizontalCenter
                width: parent.width/2
                id: wmTheme
                objectName: "wmTheme"
            }
            Button {
                text: "Apply"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                id: apply
                objectName: "apply"
                anchors.bottomMargin: 20
            }
            Button {
                text: "Cancel"
                anchors.bottom: parent.bottom
                font.family: wt.fontFamily
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

        /*Text {
            id: theme_sel
            objectName: "theme_sel"
            text: ""
            visible: false
        }*/

        /* Appearanc */
        Rectangle {
            objectName: "theme_exec"
            visible: false
            width: file.width
            anchors.top: toolbar.bottom
            color: wt.background
            height: file.height-70

            Column {
                anchors.fill: parent
                ToolButton {
                        width: parent.width
                        height: 60
                        anchors.horizontalCenter: parent.horizontalCenter
                        objectName: "btnGlobal"
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: txtGlobal
                            anchors.verticalCenter: parent.verticalCenter
                            text: "Global"
                            objectName: "txtGlobal"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            anchors.verticalCenter: parent.verticalCenter
                            id: txtGlobal1
                            objectName: "txtGlobal1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 60
                        anchors.horizontalCenter: parent.horizontalCenter
                        objectName: "btnGTK"
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: txtGTK
                            anchors.verticalCenter: parent.verticalCenter
                            text: "Application"
                            objectName: "txtGTK"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            anchors.verticalCenter: parent.verticalCenter
                            id: txtGTK1
                            objectName: "txtGTK1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 60
                        anchors.horizontalCenter: parent.horizontalCenter
                        objectName: "btnWindow"
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: txtWindow
                            anchors.verticalCenter: parent.verticalCenter
                            text: "Window"
                            objectName: "txtWindow"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            anchors.verticalCenter: parent.verticalCenter
                            id: txtWindow1
                            objectName: "txtWindow1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 60
                        anchors.horizontalCenter: parent.horizontalCenter
                        objectName: "btnIcon"
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: txtIcon
                            anchors.verticalCenter: parent.verticalCenter
                            objectName: "txtIcon"
                            font.pixelSize: 16
                            text: "Icon"
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: txtIcon1
                            objectName: "txtIcon1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 60
                        anchors.horizontalCenter: parent.horizontalCenter
                        objectName: "btnCursor"
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: txtCursor
                            anchors.verticalCenter: parent.verticalCenter
                            text: "Cursor"
                            objectName: "txtCursor"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            anchors.verticalCenter: parent.verticalCenter
                            id: txtCursor1
                            objectName: "txtCursor1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 60
                        anchors.horizontalCenter: parent.horizontalCenter
                        objectName: "btnShell"
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: txtShell
                            anchors.verticalCenter: parent.verticalCenter
                            text: "Shell"
                            objectName: "txtShell"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            anchors.verticalCenter: parent.verticalCenter
                            id: txtShell1
                            objectName: "txtShell1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }
            }
        }

        /* Network */
        Rectangle {
            objectName: "network_exec"
            visible: false
            id: network_exec
            anchors.top: toolbar.bottom
            width: file.width
            color: wt.background
            height: file.height-70

            ControlNetwork {}
        }

        /* Appearanc */
        Rectangle {
            objectName: "display_exec"
            visible: false
            id: display_exec
            anchors.top: toolbar.bottom
            width: file.width
            color: wt.background
            height: file.height-70
            
            ControlDisplayManager {}

            Button {
                text: "Change"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                id: change_reso
                objectName: "change_reso"
                anchors.bottomMargin: 20
            }
            Button {
                text: "Cancel"
                anchors.bottom: parent.bottom
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                anchors.right: change_reso.left
                id: cancel_reso
                objectName: "cancel_reso"
                onClicked: {
                    fsel.text = ".."
                }
                anchors.bottomMargin: 20
            }

        }

        /* Change password */
        Rectangle {
            objectName: "changepassword_exec"
            id: changepassword_exec
            anchors.top: toolbar.bottom
            color: wt.background
            visible: false
            width: file.width
            height: file.height-70

             Column {
                anchors.centerIn: parent
                width: parent.width/2

                TextField {
                    placeholderText: "Old Password"
                    width: parent.width
                    font.family: wt.fontFamily
                    id: leoldPassword_change
                    color: wt.color
                    objectName: "leoldPassword_change"
                    echoMode: TextInput.Password
                }
                TextField {
                    color: wt.color
                    placeholderText: "New Password"
                    width: parent.width
                    font.family: wt.fontFamily
                    id: leNewPassword_change
                    objectName: "leNewPassword_change"
                    echoMode: TextInput.Password
                }
                TextField {
                    placeholderText: "Confirm the new password"
                    width: parent.width
                    font.family: wt.fontFamily
                    id: leConfirmPassword_change
                    color: wt.color
                    echoMode: TextInput.Password
                    objectName: "leConfirmPassword_change"
                }
            }
            Button {
                text: "Change"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                id: savechanges2
                objectName: "savechanges2"
                anchors.bottomMargin: 20
            }
            Button {
                text: "Cancel"
                anchors.bottom: parent.bottom
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                anchors.right: savechanges2.left
                id: cancel3
                objectName: "cancel3"
                onClicked: {
                    fsel.text = "showuser"
                }
                anchors.bottomMargin: 20
            }
        }

        /* Show User */
        Rectangle {
            objectName: "showuser_exec"
            id: showuser_exec
            color: wt.background
            visible: false
            width: file.width
            anchors.top: toolbar.bottom
            height: file.height-70

            Column {
                anchors.centerIn: parent
                width: parent.width/2
                ToolButton {
                    anchors.horizontalCenter: parent.horizontalCenter   
                    width: parent.width/3
                    height: parent.width/3    
                    background: Image {
                        objectName: "imgProfile_show"
                        width: parent.width
                        height: parent.height
                        id: imgProfile_show
                        sourceSize: Qt.size( imgProfile_show.width, imgProfile_show.height )
                    }
                    objectName: "btnProfile_show"
                }


                TextField {
                    placeholderText: "Username"
                    width: parent.width
                    enabled: false
                    color: wt.color
                    font.family: wt.fontFamily
                    id: leUsername_show
                    objectName: "leUsername_show"
                    selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
                }
                TextField {
                    placeholderText: "Full name"
                    width: parent.width
                    color: wt.color
                    font.family: wt.fontFamily
                    id: leFullName_show
                    objectName: "leFullName_show"
                    selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
                }
                CheckBox {
                    text: "Sudoers"
                    objectName: "cbSudoers_show"
                }
            }
            Button {
                text: "Save changes"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                id: savechanges
                objectName: "savechanges"
                anchors.bottomMargin: 20
            }
            Button {
                text: "Change password"
                anchors.bottom: parent.bottom
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                anchors.right: savechanges.left
                id: changepassword
                objectName: "changepassword"
                anchors.bottomMargin: 20
            }
            Button {
                text: "Remove"
                anchors.bottom: parent.bottom
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                anchors.right: changepassword.left
                id: removeuser
                objectName: "removeuser"
                anchors.bottomMargin: 20
            }
        }

        /* Add User */
        Rectangle {
            objectName: "adduser_exec"
            id: adduser_exec
            anchors.top: toolbar.bottom
            visible: false
            color: wt.background
            width: file.width
            height: file.height-70

            Column {
                anchors.centerIn: parent
                width: parent.width/2

                TextField {
                    placeholderText: "Username"
                    width: parent.width
                    font.family: wt.fontFamily
                    id: leUsername
                    color: wt.color
                    objectName: "leUsername"
                    selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
                }
                TextField {
                    placeholderText: "Password"
                    color: wt.color
                    width: parent.width
                    font.family: wt.fontFamily
                    id: lePassword
                    objectName: "lePassword"
                    echoMode: TextInput.Password
                }
                TextField {
                    placeholderText: "Full name"
                    width: parent.width
                    font.family: wt.fontFamily
                    id: leFullName
                    objectName: "leFullName"
                    color: wt.color
                    selectByMouse: true
                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.IBeamCursor
                        acceptedButtons: Qt.NoButton
                    }
                }
                CheckBox {
                    text: "Sudoers"
                    objectName: "cbSudoers"
                }
            }
            Button {
                text: "Add"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                id: apply2
                objectName: "apply2"
                anchors.bottomMargin: 20
            }
            Button {
                text: "Cancel"
                anchors.bottom: parent.bottom
                font.family: wt.fontFamily
                anchors.right: apply2.left
                anchors.rightMargin: 20
                id: cancel2
                objectName: "cancel2"
                onClicked: {
                    fsel.text = 'users'
                }
                anchors.bottomMargin: 20
            }
        }

        /* Users */
        Rectangle {
            objectName: "users_exec"
            id: users_exec
            color: wt.background
            visible: false
            anchors.top: toolbar.bottom
            width: file.width
            height: file.height-70

            ControlUsers {}
            
        }
        /* Languages */
        Rectangle {
            objectName: "languages_exec"
            id: languages_exec
            visible: false
            anchors.top: toolbar.bottom
            color: wt.background
            width: file.width
            height: file.height-70

            Languages {}
            
            Button {
                text: "Apply"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.rightMargin: 20
                font.family: wt.fontFamily
                id: apply3
                objectName: "apply3"
                anchors.bottomMargin: 20
            }
            Button {
                text: "Cancel"
                anchors.bottom: parent.bottom
                font.family: wt.fontFamily
                anchors.right: apply3.left
                anchors.rightMargin: 20
                id: cancel4
                objectName: "cancel4"
                onClicked: {
                    fsel.text = '..'
                }
                anchors.bottomMargin: 20
            }
        }
        /* System Informations */
        Rectangle {
            objectName: "sysinfo_exec"
            visible: false
            width: file.width
            height: file.height-70
            color: wt.background
            anchors.top: toolbar.bottom

            Image {
                anchors.top: parent.top
                anchors.horizontalCenter: parent.horizontalCenter
                objectName: "logo"
                anchors.topMargin: 30
                width: parent.width/4
                height: parent.width/4
                sourceSize: Qt.size( parent.width, parent.height )
            }

            Column {
                width: parent.width
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 100
                height: 250

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: host
                            objectName: "host"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: host1
                            objectName: "host1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: cs
                            objectName: "cs"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: cs1
                            objectName: "cs1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: bl
                            objectName: "bl"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: bl1
                            objectName: "bl1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: os
                            objectName: "os"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: os1
                            objectName: "os1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: kname
                            objectName: "kname"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: kname1
                            objectName: "kname1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }


                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: su
                            objectName: "su"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: su1
                            objectName: "su1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: de
                            objectName: "de"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: de1
                            objectName: "de1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: gui
                            objectName: "gui"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: gui1
                            objectName: "gui1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }

                ToolButton {
                        width: parent.width
                        height: 30
                        anchors.horizontalCenter: parent.horizontalCenter
                        Text {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            font.family: wt.fontFamily
                            id: arch
                            objectName: "arch"
                            font.pixelSize: 16
                            color: wt.colorSmall
                        }
                        Text {
                            color: wt.color
                            font.bold: true
                            font.pixelSize: 16
                            anchors.right: parent.right
                            anchors.rightMargin: 20
                            font.family: wt.fontFamily
                            id: arch1
                            objectName: "arch1"
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: 1
                            color: wt.colorLine
                        }
                    }
                }
        }


    ScrollView {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        clip: true
        objectName: "scroll"
        id: scroll


        /* Control View */
        Column {
            width: file.width
            height: file.height-70
            objectName: "controlview"
            spacing: 2
                /* WiFi */
                ToolButton {
                    id: wifi
                    width: parent.width
                    height: parent.width/10
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'network'
                        }
                    }

                    Image {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex5
                            objectName: "w100"
                    }

                    Text {
                        text: 'WiFi'
                        font.family: wt.fontFamily
                        color: wt.color
                        objectName: 'network'
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex5.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Switch {
                        anchors.right: parent.right
                        anchors.verticalCenter: parent.verticalCenter
                        objectName: "stWifi"
                    }

                    Rectangle {
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }
                }
                /* Appearance */
                ToolButton {
                    id: apper
                    width: parent.width
                    height: parent.width/10
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'apper'
                        }
                    }

                    Image {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex1
                            objectName: "wallpaper"
                    }

                    Text {
                        text: 'System Informations'
                        color: wt.color
                        font.family: wt.fontFamily
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
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }
                }
                /* Themes */
                ToolButton {
                    id: theme
                    width: parent.width
                    height: parent.width/10
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'theme'
                        }
                    }

                    Image {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imgTheme
                            objectName: "imgTheme"
                    }

                    Text {
                        text: 'Themes'
                        color: wt.color
                        font.family: wt.fontFamily
                        objectName: 'txtTheme'
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imgTheme.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Rectangle {
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }
                }
                /* Languages */
                ToolButton {
                    id: languages
                    width: parent.width
                    height: parent.width/10
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'languages'
                        }
                    }

                    Image {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            objectName: "lang"
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex6
                    }

                    Text {
                        text: 'Languages'
                        font.family: wt.fontFamily
                        color: wt.color
                        objectName: 'languages'
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex6.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Rectangle {
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }
                }
                /* Display */
                ToolButton {
                    id: display
                    width: parent.width
                    height: parent.width/10
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'display'
                        }
                    }

                    Image {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            objectName: "displayimg"
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex4
                    }

                    Text {
                        text: 'Display'
                        font.family: wt.fontFamily
                        color: wt.color
                        objectName: 'display'
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex4.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Rectangle {
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }
                }
                /* Users */
                ToolButton {
                    id: users
                    width: parent.width
                    height: parent.width/10
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'users'
                        }
                    }

                    Image {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            objectName: "usersimg"
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex2
                    }

                    Text {
                        text: 'Users'
                        color: wt.color
                        font.family: wt.fontFamily
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
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }
                }
                /* System Informations */
                ToolButton {
                    id: sysinfo
                    width: parent.width
                    height: parent.width/10
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = 'sysinfo'
                        }
                    }

                    Image {
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            objectName: "info"
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex
                    }

                    Text {
                        text: 'System Informations'
                        font.family: wt.fontFamily
                        color: wt.color
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
                        color: wt.colorLine
                        anchors.top: parent.bottom
                    }
                }
        }
    }
}