import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: file
    visible: true
    color: "white"
    width: 900
    height: 700
    title: "Pyket"
    Text {
        visible: false
        text: ''
        id: psel
        objectName: "psel"
    }

    Text {
        visible: false
        text: ''
        id: pselnamex
        objectName: "pselnamex"
    }

    Text {
        visible: false
        text: ''
        id: pselcopyright
        objectName: "pselcopyright"
    }

    Text {
        visible: false
        text: ''
        id: psellicense
        objectName: "psellicense"
    }

    Text {
        visible: false
        text: ''
        id: pselunpack
        objectName: "pselunpack"
    }

    Text {
        visible: false
        text: ''
        id: pselversion
        objectName: "pselversion"
    }

    Text {
        visible: false
        text: ''
        id: pselbuild
        objectName: "pselbuild"
    }

    Text {
        visible: false
        text: ''
        id: pselmirror
        objectName: "pselmirror"
    }

    Text {
        visible: false
        text: ''
        id: pseldescription
        objectName: "pseldescription"
    }

    Text {
        visible: false
        text: ''
        id: pseltype
        objectName: "pseltype"
    }

    Text {
        visible: false
        text: ''
        id: pselinstalled
        objectName: "pselinstalled"
    }

    Text {
        visible: false
        text: ''
        id: psellogo
        objectName: "psellogo"
    }

    Text {
        visible: false
        text: ''
        id: act
        objectName: "act"
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
                onClicked: {
                    psel.text = ''
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

    Rectangle {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        id: package_exec
        objectName: "package_exec"


        Image {
            source: 'file:///stor/usr/share/icons/breeze-archive.svg'
            anchors.top: parent.top
            anchors.left: parent.left
            width: parent.width/6
            height: parent.width/6
            anchors.leftMargin: 20
            anchors.rightMargin: 20
            objectName: "pkgImage"
            id: imagex2
            sourceSize: Qt.size( imagex2.width, imagex2.height )
        }

        RowLayout {
            width: parent.width/6
            height: parent.width/6
            anchors.left: imagex2.right
            anchors.leftMargin: 20
            anchors.rightMargin: 20
            anchors.topMargin: 20
            anchors.top: parent.top
            Text {
                
                text: "Commento"
                font.family: "IRANSans"
                font.pixelSize: 20
                objectName: "pkgTitle"
                id: titlex
            }        
        }

        RowLayout {
            width: parent.width/6
            height: parent.width/6
            anchors.right: parent.right
            anchors.leftMargin: 20
            anchors.rightMargin: 20
            anchors.topMargin: 20
            id: endlay
            anchors.top: parent.top
            Button {
                text: "Uninstall"
                id: btnUninstall
                objectName: "btnUninstall"
                visible: false
                onClicked: {
                    act.text = 'uninstall'
                }
            }
            Button {
                text: 'Update'
                id: btnUpdate
                objectName: "btnUpdate"
                visible: false
                onClicked: {
                    act.text = 'update'
                }
            }
            Button {
                text: 'Install'
                id: btnInstall
                objectName: "btnInstall"
                visible: false
                onClicked: {
                    act.text = 'install'
                }
            }
            Button {
                text: 'Open'
                id: btnOpen
                objectName: "btnOpen"
                visible: false
                onClicked: {
                    act.text = 'open'
                }
            }
        }
        ProgressBar {
            anchors.top: endlay.bottom
            width: parent.width
            height: 10
            //indeterminate: false
            value: 0
            objectName: "pro"
            id: pro
            visible: false
        }
        TextArea {
            width: parent.width/1.5
            height: parent.height/5
            enabled: false
            objectName: "pkgDescription"
            anchors.leftMargin: 30
            anchors.rightMargin: 30
            anchors.horizontalCenter: parent.horizontalCenter
            id: descriptionx
            anchors.top: pro.bottom
            text: "Commento is the best xterminal emulator"
        }
        Column {
            spacing: 2
            width: parent.width/2
            anchors.left: parent.left
            anchors.top: descriptionx.bottom
            anchors.bottomMargin: 20
            Text {
                text: 'Package name:  '
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.right: parent.right
                objectName: "pkgName"
            }
            Text {
                text: 'Package version:  '
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.right: parent.right
                objectName: "pkgVersion"
            }
            Text {
                text: 'Build date:  '
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.right: parent.right
                objectName: "pkgBuild"
            }
            Text {
                text: 'Copyright:  '
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.right: parent.right
                objectName: "pkgCopyright"
            }
            Text {
                text: 'License:  '
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.right: parent.right
                objectName: "pkgLicense"
            }
            Text {
                text: 'Installed in:  '
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.right: parent.right
                objectName: "pkgUnpack"
            }
            Text {
                text: 'Mirror:  '
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.right: parent.right
                objectName: "pkgMirror"
            }
            
        }

        Column {
            spacing: 2
            width: parent.width/2
            anchors.right: parent.right
            anchors.top: descriptionx.bottom
            anchors.bottomMargin: 20
            Text {
                text: 'ir.pyabr'
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.left: parent.left
                font.bold: true
                objectName: "pkgName1"
            }
            Text {
                text: '2.0.1'
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.left: parent.left
                font.bold: true
                objectName: "pkgVersion1"
            }
            Text {
                text: '1400-06-13'
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.left: parent.left
                font.bold: true
                objectName: "pkgBuild1"
            }
            Text {
                text: '(c) 2021 Mani Jamali'
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.left: parent.left
                font.bold: true
                objectName: "pkgCopyright1"
            }
            Text {
                text: 'GNU General Public License v3'
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.left: parent.left
                font.bold: true
                objectName: "pkgLicense1"
            }
            Text {
                text: '/'
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.left: parent.left
                font.bold: true
                objectName: "pkgUnpack1"
            }
            Text {
                text: 'mirror.pyabr.ir/aras'
                font.family: "IRANSans"
                font.pixelSize: 16
                anchors.left: parent.left
                font.bold: true
                objectName: "pkgMirror1"
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
        objectName: "scroll"
        Column {
            width: file.width
            height: file.height-70
            spacing: 2
            Repeater {
                model: PackageModel

                Rectangle {

                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onClicked: {
                            psel.text = model.name
                            pselnamex.text = model.namex
                            pselcopyright.text = model.copyright
                            psellicense.text = model.license
                            pselunpack.text = model.unpack
                            pselversion.text = model.version
                            pseldescription.text = model.description
                            pselmirror.text = model.mirror
                            pseltype.text = model.type
                            if (model.installed){
                                pselinstalled.text = 'Yes' 
                            }
                            else
                            {
                                pselinstalled.text = 'No'
                            }
                            psellogo.text = model.logo
                            pro.visible = false
                        }
                    }

                    Image {
                        source: model.logo
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                        width: parent.height
                        sourceSize: Qt.size( parent.width, parent.height )
                        height: parent.height
                        id: imagex
                    }

                    Text {
                        text: model.namex
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }
                   
                    ToolButton {
                        text: model.size
                        font.family: "IRANSans"
                        font.pixelSize: 14
                        icon.source: "file:///stor/usr/share/icons/breeze-next.svg"
                        icon.color: "gray"
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
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
}