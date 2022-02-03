import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12
import QtWebEngine 1.2
import QtWebEngine 1.10
import QtWebEngine 1.0
import QtQuick.Layouts 1.11

ApplicationWindow {
    id: jooya
    visible: true
    color: "white"
    title: "Jooya"

    width: 1000
    height: 600

    Text {
        id: sesel
        objectName: "sesel"
        text: ""
        visible: false
    }

                ToolBar {
                    id: toolbar
                    anchors.top: parent.top
                    width: parent.width
                    height: 50

                    ToolButton {
                            icon.source: 'file:///stor/usr/share/icons/breeze-back.svg'
                            icon.color: "white"
                            id: back
                            objectName: "back"

                            anchors.left: parent.left
                            anchors.top: parent.top
                            anchors.bottom: parent.bottom
                            width: parent.height
                            height: parent.height

                            onClicked: {
                                webView.goBack()
                            }
                    }

                    ToolButton {
                            icon.source: 'file:///stor/usr/share/icons/breeze-next.svg'
                            icon.color: "white"
                            id: next
                            objectName: "next"

                            anchors.left: back.right
                            anchors.top: parent.top
                            anchors.bottom: parent.bottom
                            width: parent.height
                            height: parent.height

                            onClicked: {
                                webView.goForward()
                            }
                    }

                    ToolButton {
                            icon.source: 'file:///stor/usr/share/icons/breeze-reboot.svg'
                            icon.color: "white"
                            id: refresh
                            objectName: "refresh"

                            anchors.left: next.right
                            anchors.top: parent.top
                            anchors.bottom: parent.bottom
                            width: parent.height
                            height: parent.height

                            onClicked: {
                                webView.url = webView.url
                            }
                    }


                    TextField {
                        placeholderText: ""
                        anchors.centerIn: parent
                        width: parent.width/1.5
                        font.family: "IRANSans"
                        height: parent.height
                        id: txtURL
                        objectName: "txtURL"
                        font.pixelSize: 16
                        selectByMouse: true
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                    }

                    ToolButton {
                            icon.source: 'file:///stor/usr/share/icons/breeze-search.svg'
                            icon.color: "white"
                            id: search
                            objectName: "search"

                            width: parent.height
                            height: parent.height
                            anchors.top: parent.top
                            anchors.left: txtURL.right
                            anchors.bottom: parent.bottom
                    }

                    ToolButton {
                            icon.source: 'file:///stor/usr/share/icons/breeze-menu-panel.svg'
                            icon.color: "white"
                            id: menu
                            objectName: "menu"

                            anchors.right: parent.right
                            anchors.top: parent.top
                            anchors.bottom: parent.bottom
                            width: parent.height
                            height: parent.height

                            onClicked: {
                                contextMenu.popup();
                            }
                    }
                }

                WebEngineView {
                    id: webView
                    objectName: "webView"
                    url: "https://gerdoo.me"
                    anchors.top: toolbar.bottom
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: parent.height-toolbar.height

                }

    Menu {
        id: contextMenu
        font.family: "IRANSans"
        objectName: "contextMenu"

        Action {
            id: act_new_window
            objectName: "act_new_window"
            text: "New Window"
        }
        Action {
            id: act_history
            objectName: "act_history"
            text: "History"

            onTriggered: {
                popup_history.open();
            }
        }
        Menu {
            title: "Settings"
            Action {
                id: act_searchengines
                objectName: "act_searchengines"
                text: "Search Engines"

                onTriggered: {
                    popup_searchengine.open();
                }
            }
            Action {
                id: act_addsearchengine
                objectName: "act_addsearchengine"
                text: "Add a new search engine"

                onTriggered: {
                    popup_addsearchengine.open();
                }
            }
        }
        Menu {
            title: "View"
            Action {
                id: act_fullscreen
                objectName: "act_fullscreen"
                text: "Full Screen"
            }
        }
        Action {
            id: act_exit
            objectName: "act_exit"
            text: "Exit"
        }
    }

    /* History */
    Popup {
        id: popup_history
        anchors.centerIn: parent
        width: parent.width/2
        height: parent.height/2
        modal: false
        visible: false
        focus: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent

        ToolButton {
            anchors.top: parent.top
            anchors.right: parent.right
            anchors.rightMargin: 1
            anchors.leftMargin: 1
            width: 25
            height: 25
            id: btnClose

            Image {
                source: "file:///stor/usr/share/icons/breeze-close.svg"
                fillMode: Image.PreserveAspectFit
                sourceSize: Qt.size( parent.width, parent.height )
            }

            onClicked: {
                popup_history.close()
            }
        }

        Text {
            anchors.horizontalCenter: popup_history.horizontalCenter
            anchors.top: popup_history.top
            height: btnClose2.height
            text: "History"
            font.family: "IRANSans"
        }

        ScrollView {
            width: popup_history.width-18
            height: popup_history.height-btnClose.height
            anchors.top: btnClose.bottom
            anchors.bottom: popup_history.bottom
            clip: true
            id: scroll
            Column {
                width: popup_history.width
                height: popup_history.height-btnClose.height
                anchors.top: btnClose.bottom
                anchors.bottom: popup_history.bottom
                spacing: 2
                Repeater {
                    model: JooyaHistoryModel

                    ToolButton {

                        width: popup_history.width
                        height: parent.width/10

                        Image {
                                source: model.icon
                                anchors.left: parent.left
                                anchors.leftMargin: 20
                                anchors.rightMargin: 20
                                width: parent.height
                                sourceSize: Qt.size( parent.width, parent.height )
                                height: parent.height
                                id: imagex
                        }

                        Text {
                            text: model.title
                            font.family: "IRANSans"
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

                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                webView.url = model.link;
                                popup_history.close();
                            }
                        }
                    }
                }
            }
        }
    }

    /* Search Engines */
    Popup {
        id: popup_searchengine
        anchors.centerIn: parent
        width: parent.width/2
        height: parent.height/2
        modal: false
        visible: false
        focus: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent

        ToolButton {
            anchors.top: parent.top
            anchors.right: parent.right
            anchors.rightMargin: 1
            anchors.leftMargin: 1
            width: 25
            height: 25
            id: btnClose2

            Image {
                source: "file:///stor/usr/share/icons/breeze-close.svg"
                fillMode: Image.PreserveAspectFit
                sourceSize: Qt.size( parent.width, parent.height )
            }

            onClicked: {
                popup_searchengine.close()
            }
        }

        Text {
            anchors.horizontalCenter: popup_searchengine.horizontalCenter
            anchors.top: popup_searchengine.top
            height: btnClose2.height
            text: "Search Engines"
            font.family: "IRANSans"
        }

        ScrollView {
            width: popup_searchengine.width
            height: popup_searchengine.height-btnClose.height
            anchors.top: btnClose2.bottom
            anchors.bottom: popup_searchengine.bottom
            clip: true
            id: scrollse
            Column {
                width: popup_searchengine.width-18
                height: popup_searchengine.height-btnClose2.height
                anchors.top: btnClose2.bottom
                anchors.bottom: popup_searchengine.bottom
                spacing: 2
                Repeater {
                    model: JooyaSearchEngineModel

                    ToolButton {

                        width: popup_searchengine.width
                        height: parent.width/10

                        Text {
                            text: model.name
                            font.family: "IRANSans"
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

                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                sesel.text = model.id;
                                popup_searchengine.close();
                            }
                        }
                    }
                }
            }
        }
    }

    /* Search Engines */
    Popup {
        id: popup_addsearchengine
        objectName: "popup_addsearchengine"
        anchors.centerIn: parent
        width: parent.width/2
        height: 40*7
        modal: false
        visible: false
        focus: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent

        ToolButton {
            anchors.top: parent.top
            anchors.right: parent.right
            anchors.rightMargin: 1
            anchors.leftMargin: 1
            width: 25
            height: 25
            id: btnClose3

            Image {
                source: "file:///stor/usr/share/icons/breeze-close.svg"
                fillMode: Image.PreserveAspectFit
                sourceSize: Qt.size( parent.width, parent.height )
            }

            onClicked: {
                popup_addsearchengine.close()
            }
        }

        Text {
            anchors.horizontalCenter: popup_addsearchengine.horizontalCenter
            anchors.top: popup_addsearchengine.top
            height: btnClose3.height
            text: "Add a new search engine"
            font.family: "IRANSans"
        }


                TextField {
                        anchors.top: btnClose3.bottom
                        width: parent.width
                        height: 40
                        placeholderText: "ID (e.g google)"
                        font.family: "IRANSans"
                        id: seID
                        objectName: "seID"
                        selectByMouse: true
                        font.pixelSize: 12
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                }
                TextField {
                        anchors.top: seID.bottom
                        width: parent.width
                        height: 40
                        placeholderText: "Name (e.g. Google)"
                        font.family: "IRANSans"
                        id: seName
                        objectName: "seName"
                        font.pixelSize: 12
                        selectByMouse: true
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                }
                TextField {
                        anchors.top: seName.bottom
                        font.pixelSize: 12
                        width: parent.width
                        height: 40
                        placeholderText: "URL (e.g. https://google.com)"
                        font.family: "IRANSans"
                        id: seUrl
                        objectName: "seUrl"
                        selectByMouse: true
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                }
                TextField {
                        anchors.top: seUrl.bottom
                        width: parent.width
                        height: 40
                        placeholderText: "Query URL (e.g. https://google.com/search?={0})"
                        font.family: "IRANSans"
                        id: seQUrl
                        objectName: "seQUrl"
                        font.pixelSize: 12
                        selectByMouse: true
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                }
                TextField {
                        anchors.top: seQUrl.bottom
                        width: parent.width
                        height: 40
                        placeholderText: "Keyboard (e.g. :g)"
                        font.family: "IRANSans"
                        font.pixelSize: 12
                        id: seKey
                        objectName: "seKey"
                        selectByMouse: true
                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.IBeamCursor
                            acceptedButtons: Qt.NoButton
                        }
                }
                Button {
                    anchors.top: seQUrl.bottom
                    width: parent.width
                    font.pixelSize: 12
                    height: 40
                    objectName: "btnSeAdd"
                    id: btnSeAdd
                    text: "Add Search Engine"
                }
    }
}
