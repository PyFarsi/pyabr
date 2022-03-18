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
//import QtWebEngine 1.10
import QtQuick.Layouts 1.11


ApplicationWindow {
    id: jooya
    visible: true
    color: wt.background
    title: "Jooya"

    width: 1000
    height: 600

    WindowTheme {
        id: wt
    }


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
                                webView.url = webView.url;
                                //webView.url = "file:///stor/usr/share/samples/sample.html";
                            }
                    }


                    TextField {
                        placeholderText: ""
                        anchors.centerIn: parent
                        width: parent.width/1.5
                        font.family: wt.fontFamily
                        color: wt.colorTitle
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
                            icon.source: 'file:///stor/usr/share/icons/breeze-bookmark-new.svg'
                            icon.color: "white"
                            id: addbookmark
                            objectName: "addbookmark"

                            width: parent.height
                            height: parent.height
                            anchors.top: parent.top
                            anchors.left: search.right
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
        font.family: wt.fontFamily
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
                popup_history.show();
            }
        }
        Action {
            id: act_bookmarks
            objectName: "act_bookmarks"
            text: "Bookmarks"

            onTriggered: {
                popup_bookmarks.show();
            }
        }
        Menu {
            title: "Settings"
            font.family: wt.fontFamily
            objectName: "men_controls"
            Action {
                id: act_searchengines
                objectName: "act_searchengines"
                text: "Search Engines"

                onTriggered: {
                    popup_searchengine.show();
                }
            }
            Action {
                id: act_addsearchengine
                objectName: "act_addsearchengine"
                text: "Add a new search engine"

                onTriggered: {
                    popup_addsearchengine.show();
                }
            }
        }
        Menu {
            title: "View"
            font.family: wt.fontFamily
            objectName: "men_view"
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
    Window {
        id: popup_history
        objectName: "popup_history"
        width: 400
        height: 200
        visible: false
        title: "History"

        ScrollView {
            width: popup_history.width
            height: popup_history.height
            anchors.fill: parent
            clip: true
            id: scroll
            Column {
                width: popup_history.width
                height: popup_history.height
               anchors.fill: parent
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
                            font.family: wt.fontFamily
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

    /* Bookmarks */
    Window {
        id: popup_bookmarks
        objectName: "popup_bookmarks"
        width: 400
        height: 200
        visible: false
        title: "Bookmarks"

        ScrollView {
            width: popup_bookmarks.width
            height: popup_bookmarks.height
            anchors.fill: parent
            clip: true
            id: scrollb
            Column {
                width: popup_bookmarks.width
                height: popup_bookmarks.height
               anchors.fill: parent
                spacing: 2
                Repeater {
                    model: JooyaBookmarkModel

                    ToolButton {

                        width: popup_bookmarks.width
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
                            font.family: wt.fontFamily
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

                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                webView.url = model.link;
                                popup_bookmarks.close();
                            }
                        }
                    }
                }
            }
        }
    }

    /* Search Engines */
    Window {
        id: popup_searchengine
        objectName: "popup_searchengine"
        width: 400
        height: 200
        visible: false
        title: "Search Engines"

        ScrollView {
            width: popup_searchengine.width
            height: popup_searchengine.height
            anchors.fill: parent
            clip: true
            id: scrollse
            Column {
                width: popup_searchengine.width
                height: popup_searchengine.height
                anchors.fill: parent
                spacing: 2
                Repeater {
                    model: JooyaSearchEngineModel

                    ToolButton {

                        width: popup_searchengine.width
                        height: parent.width/10

                        Text {
                            text: model.name
                            font.family: wt.fontFamily
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
    Window {
        id: popup_addsearchengine
        objectName: "popup_addsearchengine"
        width: 400
        height: 200
        visible: false
        title: "Add a new Search Engine"
                TextField {
                        anchors.top: parent.top
                        width: parent.width
                        height: 40
                        placeholderText: "ID (e.g google)"
                        font.family: wt.fontFamily
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
                        font.family: wt.fontFamily
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
                        font.family: wt.fontFamily
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
                        font.family: wt.fontFamily
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
                        font.family: wt.fontFamily
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
