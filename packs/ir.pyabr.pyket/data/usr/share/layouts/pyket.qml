import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12
import QtWebEngine 1.0

ApplicationWindow {
    id: pyket
    visible: true
    color: wt.background
    width: 900
    maximumWidth: 900
    minimumWidth: 900
    height: 700
    maximumHeight: 700
    minimumHeight: 700
    title: "Pyket"
    WindowTheme {
        id: wt
    }
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
        id: pselurl
        objectName: "pselurl"
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
            font.family: wt.fontFamily
            font.pixelSize: 20
            color: wt.colorTitle
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
        color: wt.background


        Image {
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
                color: wt.color
                font.family: wt.fontFamily
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
        /* Pyket meta data */
        ScrollView{
            ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
            //ScrollBar.vertical.policy: ScrollBar.AlwaysOn
            clip: true
            anchors.top: pro.bottom
            anchors.bottom: parent.bottom
            width: pyket.width
            height: pyket.height

            Column {
                width: pyket.width
                height: pyket.height

                 WebEngineView {
                    anchors.horizontalCenter: pyket.horizontalCenter
                    width: parent.width
                    height: 450
                    objectName: "ScreenShot"
                    id: screenShot
                }

                Rectangle {
                    width: parent.width/1.5
                    height: parent.height/5
                    anchors.horizontalCenter: pyket.horizontalCenter
                    color: wt.background
                    TextArea {
                        enabled: false
                        objectName: "pkgDescription"
                        anchors.centerIn: parent
                        id: descriptionx
                        font.pixelSize: 16
                        font.bold: false
                        color: wt.color
                        font.family: wt.fontFamily
                        text: "Commento is the best xterminal emulator"
                    }
                }


                ToolButton {
                    width: pyket.width
                    height: 30
                    anchors.horizontalCenter: pyket.horizontalCenter
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        id: pkgName
                        objectName: "pkgName"
                        color: wt.colorSmall
                        font.pixelSize: 16
                        font.family: wt.fontFamily
                    }
                    Text {
                        color: wt.color
                        font.bold: true
                        anchors.right: parent.right
                        font.pixelSize: 16
                        anchors.rightMargin: 20
                        id: pkgName1
                        objectName: "pkgName1"
                        font.family: wt.fontFamily
                    }
                    Rectangle {
                        anchors.bottom: parent.bottom
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                    }
                }

                ToolButton {
                    width: pyket.width
                    height: 30
                    anchors.horizontalCenter: pyket.horizontalCenter
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        id: pkgVersion
                        font.family: wt.fontFamily
                        font.pixelSize: 16
                        objectName: "pkgVersion"
                        color: wt.colorSmall
                    }
                    Text {
                        color: wt.color
                        font.bold: true
                        anchors.right: parent.right
                        anchors.rightMargin: 20
                        font.pixelSize: 16
                        id: pkgVersion1
                        objectName: "pkgVersion1"
                        font.family: wt.fontFamily
                    }
                    Rectangle {
                        anchors.bottom: parent.bottom
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                    }
                }

                ToolButton {
                    width: pyket.width
                    anchors.horizontalCenter: pyket.horizontalCenter
                    height: 30
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        font.pixelSize: 16
                        id: pkgBuild
                        font.family: wt.fontFamily
                        objectName: "pkgBuild"
                        color: wt.colorSmall
                    }
                    Text {
                        color: wt.color
                        font.bold: true
                        font.pixelSize: 16
                        anchors.right: parent.right
                        anchors.rightMargin: 20
                        font.family: wt.fontFamily
                        id: pkgBuild1
                        objectName: "pkgBuild1"
                    }
                    Rectangle {
                        anchors.bottom: parent.bottom
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                    }
                }

                ToolButton {
                    width: pyket.width
                    height: 30
                    anchors.horizontalCenter: pyket.horizontalCenter
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        font.family: wt.fontFamily
                        id: pkgCopyright
                        objectName: "pkgCopyright"
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
                        id: pkgCopyright1
                        objectName: "pkgCopyright1"
                    }
                    Rectangle {
                        anchors.bottom: parent.bottom
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                    }
                }

                ToolButton {
                    width: pyket.width
                    height: 30
                    anchors.horizontalCenter: pyket.horizontalCenter
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        id: pkgLicense
                        objectName: "pkgLicense"
                        font.pixelSize: 16
                        color: wt.colorSmall
                        font.family: wt.fontFamily
                    }
                    Text {
                        color: wt.color
                        font.bold: true
                        anchors.right: parent.right
                        anchors.rightMargin: 20
                        font.family: wt.fontFamily
                        font.pixelSize: 16
                        id: pkgLicense1
                        objectName: "pkgLicense1"
                    }
                    Rectangle {
                        anchors.bottom: parent.bottom
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                    }
                }

                ToolButton {
                    width: pyket.width
                    height: 30
                    anchors.horizontalCenter: pyket.horizontalCenter
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        id: pkgUnpack
                        font.family: wt.fontFamily
                        objectName: "pkgUnpack"
                        color: wt.colorSmall
                        font.pixelSize: 16
                    }
                    Text {
                        color: wt.color
                        font.bold: true
                        anchors.right: parent.right
                        anchors.rightMargin: 20
                        id: pkgUnpack1
                        font.family: wt.fontFamily
                        objectName: "pkgUnpack1"
                        font.pixelSize: 16
                    }
                    Rectangle {
                        anchors.bottom: parent.bottom
                        width: parent.width
                        height: 1
                        color: wt.colorLine
                    }
                }

                ToolButton {
                    width: pyket.width
                    height: 30
                    anchors.horizontalCenter: pyket.horizontalCenter
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 20
                        id: pkgMirror
                        font.family: wt.fontFamily
                        objectName: "pkgMirror"
                        color: wt.colorSmall
                        font.pixelSize: 16
                    }
                    Text {
                        color: wt.color
                        font.bold: true
                        font.family: wt.fontFamily
                        anchors.right: parent.right
                        anchors.rightMargin: 20
                        id: pkgMirror1
                        objectName: "pkgMirror1"
                        font.pixelSize: 16
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
            width: pyket.width
            height: pyket.height-70
            spacing: 2
            Repeater {
                model: PackageModel

                ToolButton {

                    width: parent.width
                    height: parent.width/10
      

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
                            screenShot.url =  model.mirror+"/"+model.name
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
                        font.family: wt.fontFamily
                        font.pixelSize: 16
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        color: wt.color
                        anchors.rightMargin: 20
                    }
                   
                    ToolButton {
                        text: model.size
                        font.family: wt.fontFamily
                        font.pixelSize: 14
                        icon.source: "file:///stor/usr/share/icons/breeze-next.svg"
                        icon.color: wt.colorSmall
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
                }
            }
        }
    }
}