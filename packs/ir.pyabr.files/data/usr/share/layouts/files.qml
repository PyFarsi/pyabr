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
    width: 1000
    height: 720

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
                onClicked: {
                    fsel.text = '..'
                }
            }
            ToolButton {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                icon.source: 'file:///stor/usr/share/icons/breeze-new.svg'
                icon.color: "white"
                onClicked: {
                    act.text = 'newfile'
                }
            }
            ToolButton {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                icon.source: 'file:///stor/usr/share/icons/breeze-newfolder.svg'
                icon.color: "white"
                onClicked: {
                    act.text = 'newfolder'
                }
            }
            ToolButton {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                icon.source: 'file:///stor/usr/share/icons/breeze-details.svg'
                icon.color: "white"
                onClicked: {
                    act.text = 'details'
                }
            }
        }
        Text {
            id: title
            objectName: "title"
            font.family: wt.fontFamily
            font.pixelSize: 18
            anchors.centerIn: parent
            color: wt.colorTitle
        }
    }

    Menu {
                      id: contextMenu
                      font.family: wt.fontFamily
                            objectName: "contextMenu"
                            Action { 
                                id: filex
                                objectName: "filex"
                                enabled: false
                            }
                            Menu {
                                title: "File"
                                Action { 
                                    text: "New File" 
                                    objectName: "newfile"
                                    id: newfile
                                    icon.source: "file:///stor/usr/share/icons/breeze-new.svg"
                                    onTriggered: {
                                        act.text = "newfile"
                                    }
                                }
                                Action { 
                                    text: "New Folder" 
                                    objectName: "newfolder"
                                    id: newfolder
                                    icon.source: "file:///stor/usr/share/icons/breeze-newfolder.svg"
                                    onTriggered: {
                                        act.text = "newfolder"
                                    }
                                }
                                Action { 
                                    text: "Open" 
                                    objectName: "open"
                                    id: open
                                    icon.source: "file:///stor/usr/share/icons/breeze-open.svg"
                                    onTriggered: {
                                        act.text = "open"
                                    }
                                }
                                Action { 
                                    text: "Open with..." 
                                    objectName: "openwith"
                                    id: openwith
                                    icon.source: "file:///stor/usr/share/icons/breeze-open.svg"
                                    onTriggered: {
                                        act.text = "openwith"
                                    }
                                }
                                Action { 
                                    text: "Execute" 
                                    objectName: "execute"
                                    id: execute
                                    icon.source: "file:///stor/usr/share/icons/breeze-execute.svg"
                                    onTriggered: {
                                        act.text = "execute"
                                    }
                                }
                                Action { 
                                    text: "Add to Desktop" 
                                    objectName: "shortcut"
                                    id: shortcut
                                    icon.source: "file:///stor/usr/share/icons/breeze-install.svg"
                                    onTriggered: {
                                        act.text = "shortcut"
                                    }
                                }
                            }
                           
                            Menu {
                                title: "Cloud Options"
                                objectName: "cloudops"
                                id: cloudops
                                Action { 
                                    text: "Upload" 
                                    objectName: "upcloud"
                                    id: upcloud
                                    icon.source: "file:///stor/usr/share/icons/breeze-save.svg"
                                    onTriggered: {
                                        act.text = "up"
                                    }
                                }
                                Action { 
                                    text: "Download" 
                                    objectName: "downcloud"
                                    id: downcloud
                                    icon.source: "file:///stor/usr/share/icons/breeze-downcloud.svg"
                                    onTriggered: {
                                        act.text = "down"
                                    }
                                }
                                Action {
                                    text: "Zero"
                                    objectName: "zero"
                                    id: zero
                                    
                                    icon.source: "file:///stor/usr/share/icons/breeze-delete.svg"
                                    onTriggered: {
                                        act.text = "zero"
                                    }
                                }
                                Action {
                                    text: "Unlink (Remove from cloud)"
                                    objectName: "unlink"
                                    id: unlink
                                    icon.color: "red"
                                    icon.source: "file:///stor/usr/share/icons/breeze-delete.svg"
                                    onTriggered: {
                                        act.text = "unlink"
                                    }
                                }
                                Action {
                                    text: "Share link"
                                    objectName: "link"
                                    id: link
                                    icon.source: "file:///stor/usr/share/icons/breeze-sharelink.svg"
                                    onTriggered: {
                                        act.text = "link"
                                    }
                                }
                            }
                            Menu {
                                title: "Edit"
                                    Action { 
                                    text: "Cut" 
                                    objectName: "cut"
                                    id: cut
                                    icon.source: "file:///stor/usr/share/icons/breeze-cut.svg"
                                    onTriggered: {
                                        act.text = "cut"
                                    }
                                }
                                Action { 
                                    text: "Copy" 
                                    objectName: "copy"
                                    id: copy
                                    icon.source: "file:///stor/usr/share/icons/breeze-copy.svg"
                                    onTriggered: {
                                        act.text = "copy"
                                    }
                                }
                                Action { 
                                    text: "Paste" 
                                    objectName: "paste"
                                    id: paste
                                    icon.source: "file:///stor/usr/share/icons/breeze-paste.svg"
                                    onTriggered: {
                                        act.text = "paste"
                                    }
                                }
                                Action { 
                                    text: "Rename" 
                                    objectName: "rename"
                                    id: rename
                                    icon.source: "file:///stor/usr/share/icons/breeze-rename.svg"
                                    onTriggered: {
                                        act.text = "rename"
                                    }
                                }
                                Action { 
                                    text: "Delete" 
                                    objectName: "delete"
                                    id: remove
                                    icon.source: "file:///stor/usr/share/icons/breeze-delete.svg"
                                    onTriggered: {
                                        act.text = "delete"
                                    }
                                }
                            }
                            
                            Menu {
                                title: "Compress to"
                                id: compressto
                                objectName: "compressto"

                                Action {
                                    text: ".zip archive"
                                    id: zipc
                                    objectName: "zipc"
                                    icon.source: "file:///stor/usr/share/icons/breeze-compress.svg"
                                    onTriggered: {
                                        act.text = "zipc"
                                    }
                                }
                                Action {
                                    text: ".tar archive"
                                    id: tarc
                                    objectName: "tarc"
                                    icon.source: "file:///stor/usr/share/icons/breeze-compress.svg"
                                    onTriggered: {
                                        act.text = "tarc"
                                    }
                                }
                                Action {
                                    text: ".tar.bz2 archive"
                                    id: bzc
                                    objectName: "bzc"
                                    icon.source: "file:///stor/usr/share/icons/breeze-compress.svg"
                                    onTriggered: {
                                        act.text = "bzc"
                                    }
                                }
                                Action {
                                    text: ".tar.xz archive"
                                    id: xzc
                                    objectName: "xzc"
                                    icon.source: "file:///stor/usr/share/icons/breeze-compress.svg"
                                    onTriggered: {
                                        act.text = "xzc"
                                    }
                                }
                                Action {
                                    text: ".tar.gz archive"
                                    id: gzc
                                    objectName: "gzc"
                                    icon.source: "file:///stor/usr/share/icons/breeze-compress.svg"
                                    onTriggered: {
                                        act.text = "gzc"
                                    }
                                }

                            }
                            Action {
                                text: "Extract"
                                icon.source: "file:///stor/usr/share/icons/breeze-extract.svg"
                                id: extract
                                objectName: "extract"
                                onTriggered: {
                                    act.text = 'extract'
                                }
                            }
                            Action {
                                text: "Open in Terminal"
                                //icon.source: "file:///stor/usr/share/icons/breeze-commento.svg"
                                id: terminal
                                objectName: "terminal"
                                onTriggered: {
                                    act.text = 'terminal'
                                }
                            }
                            Action { 
                                text: "Information" 
                                objectName: "info"
                                id: info
                                icon.source: "file:///stor/usr/share/icons/breeze-information.svg"
                                onTriggered: {
                                    act.text = "info"
                                }
                            }
                        }

    ScrollView {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.leftMargin: 10
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.rightMargin: 10
        objectName: "Details"
        anchors.top: toolbar.bottom
        clip: true
        visible: false
        id: scroll2

        Column {
            width: file.width
            height: file.height-70
            spacing: 2

            GridView {
                model: FileModel
                cellWidth: 150; cellHeight: 150
                highlight: highlight
                width: parent.width
                height: parent.height
                highlightFollowsCurrentItem: false
                focus: true

                delegate: Column {
                    Image { 
                        source: model.logo
                        width: 128
                        height: 128
                        NumberAnimation on opacity {
                                id: file_anim2
                                from: 0
                                to: 1
                                duration: 100
                        }
                        sourceSize: Qt.size( parent.width, parent.height )
                         anchors.horizontalCenter: parent.horizontalCenter
                        MouseArea {
                            anchors.fill: parent
                            acceptedButtons: Qt.LeftButton | Qt.RightButton
                            onDoubleClicked: {
                                file_anim2.start();
                                fsel.text = model.path
                            }
                            onClicked: {
                                file_anim2.start();
                                fsela.text = model.path;

                                if (mouse.button === Qt.RightButton)
                                    contextMenu.popup()

                            }

                            onPressAndHold: {
                                file_anim2.start();
                                if (mouse.source === Qt.MouseEventNotSynthesized)
                                    contextMenu.popup()
                            }
                        }   
                    }
                    Text { 
                        text: model.name
                        color: wt.color
                         anchors.horizontalCenter: parent.horizontalCenter
                          font.family: wt.fontFamily
    
                    }
                }
            }
        }
    }

    Component {
        id: highlight
        Rectangle {
            width: view.cellWidth; height: view.cellHeight
            color: "lightsteelblue"; radius: 5
            x: view.currentItem.x
            y: view.currentItem.y
            Behavior on x { SpringAnimation { spring: 3; damping: 0.2 } }
            Behavior on y { SpringAnimation { spring: 3; damping: 0.2 } }
        }
    }

    ScrollView {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        objectName: "ListView"
        anchors.top: toolbar.bottom
        clip: true
        visible: true
        id: scroll
        Column {
            width: file.width
            height: file.height-70
            spacing: 2
            Repeater {
                model: FileModel

                ToolButton {

                    width: parent.width
                    height: parent.width/10
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onDoubleClicked: {
                            fsel.text = model.path;
                            file_anim.start();
                            fsela.text = model.path;
                        }
                        onClicked: {

                            file_anim.start();

                            if (mouse.button === Qt.RightButton)
                                contextMenu.popup()

                        }

                        onPressAndHold: {
                            file_anim.start();
                            if (mouse.source === Qt.MouseEventNotSynthesized)
                                contextMenu.popup()
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
                            NumberAnimation on opacity {
                                id: file_anim
                                from: 0
                                to: 1
                                duration: 100
                            }
                    }

                    Text {
                        text: model.name
                        font.family: wt.fontFamily
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                        color: wt.color
                    }

                    Text {
                        text: model.mimetype
                        font.family: wt.fontFamily
                        font.pixelSize: 14
                        color: wt.colorSmall
                        anchors.right: parent.right
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.rightMargin: 100
                    }
                   
                    Text {
                        text: model.size
                        font.family: wt.fontFamily
                        font.pixelSize: 14
                        color: wt.colorSmall
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