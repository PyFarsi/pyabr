import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Window 2.15
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick 2.15
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12
import QtGraphicalEffects 1.12

ApplicationWindow {
    id: desktop
    visible: true
    font.family: "IRANSans"
    color: "blue"

    Text {
        id: enable_anim
        objectName: "enable_anim"
        visible: false
        text: "Yes"
    }

    Text {
        id: feedsel
        objectName: "feedsel"
        text: ""
        visible: false
    }

    Text {
        id: dsel
        objectName: "dsel"
    }

    Text {
        id: dselm
        objectName: "dselm"
    }

    /* Application Background */

     Rectangle {
        id: bWindowManager
        objectName: "bWindowManager"
        x: 100
        y: 100
        width: 400
        height: 400
        radius: 10
        visible: false
        focus: true

        property var floating: false
        property var pwidth: 0
        property var pheight: 0

        Drag.active: true
        MouseArea{
            anchors.fill: parent
            drag.target: parent
        }

        Rectangle {
            color: "transparent"
            width: parent.width
            height: 20
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.right: parent.right
            radius: 30
            anchors.topMargin: 10
            anchors.leftMargin: 10
            anchors.bottomMargin: 10
            anchors.rightMargin: 10

            ToolButton {
                anchors.right: parent.right
                width: 25
                height: 25

                Image {
                    source: "file:///stor/usr/share/icons/breeze-close.svg"
                    anchors.fill: parent
                    sourceSize: Qt.size( parent.width, parent.height )
                }

                onClicked: {
                    bWindowManager.visible = false
                }

                id: bwin_btnClose
            }

            ToolButton {
                id: bwin_btnFloat
                anchors.right: bwin_btnClose.left
                anchors.rightMargin: 5
                width: 25
                height: 25

                Image {
                    source: "file:///stor/usr/share/icons/breeze-float.svg"
                    anchors.fill: parent
                    sourceSize: Qt.size( parent.width, parent.height )
                }

                onClicked: {
                }
            }

            Text {
                anchors.centerIn: parent
                text: "Bomi Window Manager"
            }
        }
    }
    
    Text {
        id: background_app
        objectName: "background_app"
        text: ""
        visible: false
    }

    Text {
        id: restore_app
        objectName: "restore_app"
        text: ""
        visible: false
    }

    Text {
        id: act
        objectName: "act"
    }

    /* Keyless keyboard layer Background */

    Text {
        objectName: "keyless"
        id: keyless
        visible: false
        text: ''
    }

    Shortcut {
        sequence: "Esc"
        onActivated: {
            popup_pysys.open()
        }
    }

    Shortcut {
        sequence: "Alt+F4"
        onActivated: {
            popup_pysys.open()
        }
    }

    Shortcut {
        sequence: "Ctrl+A"
        onActivated: {
            background_app.text = 'rma';
        }
    }

    Shortcut {
        sequence: "F5"
        onActivated: {
            background_app.text = "refresh";
        }
    }

    Shortcut {
        sequence: "F1"
        onActivated: {
            background_app.text = "help";
        }
    }


    /* Background Image */

    background: Rectangle {
        anchors.fill: parent
        Image {
            anchors.fill: parent
            id: background
            objectName: "background"
        }
    }

    /* Topbar */
    Rectangle {
        color: "#A0FFFFFF"
        anchors.top: parent.top
        width: parent.width
        height: 30
        id: topbar

        Row {
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-shutdown.svg'
                icon.color: 'white'
                onClicked: {
                    popup_pysys.open()
                }
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-w100.svg'
                icon.color: 'white'
                objectName: 'shell_w100'
                visible: false
                onClicked: {
                    background_app.text = 'wifi';
                }
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-w080.svg'
                icon.color: 'white'
                objectName: 'shell_w080'
                visible: false
                onClicked: {
                    background_app.text = 'wifi';
                }
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-w040.svg'
                icon.color: 'white'
                objectName: 'shell_w040'
                visible: false
                onClicked: {
                    background_app.text = 'wifi';
                }
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-w020.svg'
                icon.color: 'red'
                objectName: 'shell_w020'
                visible: false
                onClicked: {
                    background_app.text = 'wifi';
                }
            }

            /* Battery */
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-000.svg'
                icon.color: 'red'
                objectName: 'battery_000'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-010.svg'
                icon.color: 'red'
                objectName: 'battery_010'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-020.svg'
                icon.color: 'white'
                objectName: 'battery_020'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-030.svg'
                icon.color: 'white'
                objectName: 'battery_030'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-040.svg'
                icon.color: 'white'
                objectName: 'battery_040'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-050.svg'
                icon.color: 'white'
                objectName: 'battery_050'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-060.svg'
                icon.color: 'white'
                objectName: 'battery_060'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-070.svg'
                icon.color: 'white'
                objectName: 'battery_070'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-080.svg'
                icon.color: 'white'
                objectName: 'battery_080'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-090.svg'
                icon.color: 'white'
                objectName: 'battery_090'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-100.svg'
                icon.color: 'white'
                objectName: 'battery_100'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-000-charging.svg'
                icon.color: 'green'
                objectName: 'battery_000_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-010-charging.svg'
                icon.color: 'green'
                objectName: 'battery_010_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-020-charging.svg'
                icon.color: 'green'
                objectName: 'battery_020_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-030-charging.svg'
                icon.color: 'green'
                objectName: 'battery_030_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-040-charging.svg'
                icon.color: 'green'
                objectName: 'battery_040_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-050-charging.svg'
                icon.color: 'green'
                objectName: 'battery_050_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-060-charging.svg'
                icon.color: 'green'
                objectName: 'battery_060_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-070-charging.svg'
                icon.color: 'green'
                objectName: 'battery_070_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-080-charging.svg'
                icon.color: 'green'
                objectName: 'battery_080_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-090-charging.svg'
                icon.color: 'green'
                objectName: 'battery_090_charging'
                visible: false
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-battery-100-charging.svg'
                icon.color: 'green'
                objectName: 'battery_100_charging'
                visible: false
            }
            ToolButton {
                objectName: "battery_percent"
                Text {
                    objectName: "battery_percent_text"
                    anchors.centerIn: parent
                    color: "white"
                    text: "0%"
                    font.family: "IRANSans"
                    font.pixelSize: battery_100_charging.width/2
                }
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-onboard.svg'
                icon.color: 'white'
                objectName: 'virtualkeyboard'
                visible: true
            }
        }

        Text {
            id: leClock
            anchors.centerIn: parent
            objectName: "leClock"
            font.family: "IRANSans"
            font.pixelSize: 16
            color: "white"
            ToolButton {
                anchors.fill: parent
                objectName: "btnClock"
                id: btnClock
            }
        }

        Row
        {
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-action-toolpen.svg'
                icon.color: 'white'
                objectName: 'btnNote'
                id: btnNote
                visible: true

                onClicked: {
                    notepanel_anim.start();
                    notepanel.visible = true;
                }
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-action-event.svg'
                icon.color: 'white'
                objectName: 'btnEvent'
                id: btnEvent
                visible: true

                onClicked: {
                    eventpanel_anim.start();
                    eventpanel.visible = true;
                }
            }
            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-action-feed.svg'
                icon.color: 'white'
                objectName: 'btnPanel'
                id: btnPanel
                visible: true

                onClicked: {
                    showpanel_anim.start();
                    showpanel.visible = true;
                }
            }
        }
    }


    /* Menu applications for bottom Dock */

    Rectangle {
       color: "#A0FFFFFF"
       anchors.bottom: toolbar.top
       anchors.horizontalCenter: parent.horizontalCenter
       width: 560
       height: 560
       radius: 30
       anchors.bottomMargin: 20
       visible: false
       //visible: true
       objectName: "menuApps"

       Rectangle {
        anchors.top: parent.top
       height: 20
       id: rex
       }

        ScrollView{
        anchors.top: rex.bottom
        anchors.bottom: rex2.top
        width: 560
        height: 560-40
        clip: true
        id: scroll
        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff

        Column {
            width: 560
            height: 560-40
            spacing: 2
            Repeater {
                model: EntryAppApplications
                anchors.fill: parent
                Rectangle {

                    width: parent.width
                    height: parent.width/8
                    color: "transparent"

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
                                id: menu_anim
                                from: 0
                                to: 1
                                duration: 100
                            }
                    }

                    Text {
                        text: model.label
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {

                            if (enable_anim.text == "Yes"){
                                menu_anim.start();
                            }
                            background_app.text = model.name;
                        }
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
    Rectangle {
        anchors.bottom: parent.bottom
       height: 20
       id: rex2
       }

       NumberAnimation on height {
            id: menuApps_anim
            objectName: "menuApps_anim"
            from: 0
            to: 560
            duration: 100
        }

    }

    /* Menu applications for top Dock */

    Rectangle {
       color: "#A0FFFFFF"
       anchors.top: toolbar2.bottom
       anchors.horizontalCenter: parent.horizontalCenter
       width: 560
       height: 560
       radius: 30
       anchors.topMargin: 20
       visible: false
       objectName: "menuApps2"

       Rectangle {
        anchors.top: parent.top
        height: 20
        id: rex3
       }

        ScrollView{
        anchors.top: rex3.bottom
        anchors.bottom: rex4.top
        width: 560
        height: 560-40
        clip: true
        id: scroll2
        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff

        Column {
            width: 560
            height: 560-40
            spacing: 2
            Repeater {
                model: EntryAppApplications
                anchors.fill: parent
                Rectangle {

                    width: parent.width
                    height: parent.width/8
                    color: "transparent"

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
                                id: menu2_anim
                                from: 0
                                to: 1
                                duration: 100
                            }
                    }

                    Text {
                        text: model.label
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                menu2_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
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
    Rectangle {
        anchors.bottom: parent.bottom
       height: 20
       id: rex4
       }
       NumberAnimation on height {
            id: menuApps2_anim
            objectName: "menuApps2_anim"
            from: 0
            to: 560
            duration: 100
        }
    }

    /* Menu applications for left Dock */
    Rectangle {
       color: "#A0FFFFFF"
       anchors.left: toolbar3.right
       //anchors.horizontalCenter: parent.horizontalCenter
       anchors.verticalCenter: parent.verticalCenter
       width: 560
       height: 560
       radius: 30
       anchors.leftMargin: 20
       visible: false
       objectName: "menuApps3"

       Rectangle {
        anchors.top: parent.top
       height: 20
       id: rex5
       }

        ScrollView{
        anchors.top: rex5.bottom
        anchors.bottom: rex6.top
        width: 560
        height: 560-40
        clip: true
        id: scroll3
        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff

        Column {
            width: 560
            height: 560-40
            spacing: 2
            Repeater {
                model: EntryAppApplications
                anchors.fill: parent
                Rectangle {

                    width: parent.width
                    height: parent.width/8
                    color: "transparent"

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
                                id: menu3_anim
                                from: 0
                                to: 1
                                duration: 100
                            }
                    }

                    Text {
                        text: model.label
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                menu3_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
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
    Rectangle {
        anchors.bottom: parent.bottom
       height: 20
       id: rex6
       }
       NumberAnimation on height {
            id: menuApps3_anim
            objectName: "menuApps3_anim"
            from: 0
            to: 560
            duration: 100
        }
    }

    /* Menu applications for right Dock */
    Rectangle {
       color: "#A0FFFFFF"
       anchors.right: toolbar4.left
       //anchors.horizontalCenter: parent.horizontalCenter
       anchors.verticalCenter: parent.verticalCenter
       width: 560
       height: 560
       radius: 30
       anchors.rightMargin: 20
       visible: false
       objectName: "menuApps4"

       Rectangle {
        anchors.top: parent.top
       height: 20
       id: rex7
       }

        ScrollView{
        anchors.top: rex7.bottom
        anchors.bottom: rex8.top
        width: 560
        height: 560-40
        clip: true
        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff

        Column {
            width: 560
            height: 560-40
            spacing: 2
            Repeater {
                model: EntryAppApplications
                anchors.fill: parent
                Rectangle {

                    width: parent.width
                    height: parent.width/8
                    color: "transparent"

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
                                id: menu4_anim
                                from: 0
                                to: 1
                                duration: 100
                            }
                    }

                    Text {
                        text: model.label
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                menu4_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
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
    Rectangle {
        anchors.bottom: parent.bottom
       height: 20
       id: rex8
       }
       NumberAnimation on height {
            id: menuApps4_anim
            objectName: "menuApps4_anim"
            from: 0
            to: 560
            duration: 100
        }
    }

    /* Bottom Dock (Default dock) */

    Rectangle {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottomMargin: 20
        width: 560
        height: 70

        color: "#A0FFFFFF"
        radius: 100
        objectName: "toolbar"
        id: toolbar

        RowLayout {
            anchors.centerIn: parent
            ToolButton {
                width: toolbar.height
                height: toolbar.height
                objectName: "btnMenu"
                Image {
                    fillMode: Image.PreserveAspectFit
                    objectName: "imgMenu"
                    anchors.fill: parent
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu_anim
                        objectName: "btnMenu_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar.height
                        height: toolbar.height
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }


                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app_anim.start();
                            }
                            background_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app_anim
                            from: 0
                            to: 1
                            duration: 100
                        }

                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar.height
                        height: toolbar.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Top Dock */

    Rectangle {
        anchors.top: topbar.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 20
        width: 560
        height: 70

        color: "#A0FFFFFF"
        radius: 100
        objectName: "toolbar2"
        id: toolbar2

        RowLayout {
            anchors.centerIn: parent
            ToolButton {
                width: toolbar2.height
                height: toolbar2.height
                objectName: "btnMenu2"
                Image {
                    fillMode: Image.PreserveAspectFit
                    objectName: "imgMenu2"
                    anchors.fill: parent
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu2_anim
                        objectName: "btnMenu2_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar2.height
                        height: toolbar2.height
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app2_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app2_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar2.height
                        height: toolbar2.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app2_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app2_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Left Dock */

    Rectangle {
        anchors.left: parent.left
        anchors.verticalCenter: parent.verticalCenter
        anchors.leftMargin: 20
        width: 70
        height: 560

        color: "#A0FFFFFF"
        radius: 100
        objectName: "toolbar3"
        id: toolbar3

        ColumnLayout {
            anchors.centerIn: parent
            ToolButton {
                width: toolbar3.width
                height: toolbar3.width
                objectName: "btnMenu3"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu3"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu3_anim
                        objectName: "btnMenu3_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar3.width
                        height: toolbar3.width
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app3_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app3_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar3.height
                        height: toolbar3.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app3_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app3_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Right Dock */
    Rectangle {
        anchors.right: parent.right
        anchors.verticalCenter: parent.verticalCenter
        anchors.rightMargin: 20
        width: 70
        height: 560

        color: "#A0FFFFFF"
        radius: 100
        objectName: "toolbar4"
        id: toolbar4

        ColumnLayout {
            anchors.centerIn: parent
            ToolButton {
                width: toolbar4.width
                height: toolbar4.width
                objectName: "btnMenu4"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu4"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu4_anim
                        objectName: "btnMenu4_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar4.width
                        height: toolbar4.width
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app4_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app4_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar4.height
                        height: toolbar4.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app4_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app4_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Windows 11 Dock */
    Rectangle {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottomMargin: 0
        width: parent.width
        height: 70
        color: "#A0FFFFFF"
        radius: 0
        objectName: "toolbar5"
        id: toolbar5
        
        
        RowLayout {
            anchors.centerIn: parent
            ToolButton {
                width: toolbar5.height
                height: toolbar5.height
                objectName: "btnMenu5"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu5"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu5_anim
                        objectName: "btnMenu5_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar5.height
                        height: toolbar5.height
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app5_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app5_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar5.height
                        height: toolbar5.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app5_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app5_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Windows 11 Dock - top */
    Rectangle {
        anchors.top: topbar.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 0
        width: parent.width
        height: 70
        color: "#A0FFFFFF"
        radius: 0
        objectName: "toolbar6"
        id: toolbar6
        
        
        RowLayout {
            anchors.centerIn: parent
            ToolButton {
                width: toolbar6.height
                height: toolbar6.height
                objectName: "btnMenu6"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu6"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu6_anim
                        objectName: "btnMenu6_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar6.height
                        height: toolbar6.height
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app6_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app6_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar6.height
                        height: toolbar6.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app6_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app6_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Windows 11 dock - left */

    Rectangle {
        anchors.left: parent.left
        anchors.top: topbar.bottom
        anchors.bottom: parent.bottom
        anchors.verticalCenter: parent.verticalCenter
        anchors.leftMargin: 0
        width: 70
        height: parent.height

        color: "#A0FFFFFF"
        radius: 0
        objectName: "toolbar7"
        id: toolbar7

        ColumnLayout {
            anchors.centerIn: parent
            ToolButton {
                width: toolbar7.width
                height: toolbar7.width
                objectName: "btnMenu7"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu7"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu7_anim
                        objectName: "btnMenu7_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar7.width
                        height: toolbar7.width
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app7_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app7_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar7.height
                        height: toolbar7.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app7_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app7_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Windows 11 dock - right */
    Rectangle {
        anchors.right: parent.right
        anchors.top: topbar.bottom
        anchors.bottom: parent.bottom
        anchors.verticalCenter: parent.verticalCenter
        anchors.rightMargin: 0
        width: 70
        height: parent.height

        color: "#A0FFFFFF"
        radius: 0
        objectName: "toolbar8"
        id: toolbar8

        ColumnLayout {
            anchors.centerIn: parent
            ToolButton {
                width: toolbar8.width
                height: toolbar8.width
                objectName: "btnMenu8"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu8"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu8_anim
                        objectName: "btnMenu8_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar8.width
                        height: toolbar8.width
                        
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app8_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app8_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar8.height
                        height: toolbar8.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app8_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app8_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Unity Dock */
    Rectangle {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottomMargin: 0
        width: parent.width
        height: 70
        color: "#A0FFFFFF"
        radius: 0
        objectName: "toolbar9"
        id: toolbar9

        RowLayout {
            anchors.left: parent.left
            anchors.verticalCenter: parent.verticalCenter
            anchors.leftMargin: 20
            ToolButton {
                width: toolbar9.height
                height: toolbar9.height
                objectName: "btnMenu9"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu9"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu9_anim
                        objectName: "btnMenu9_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar9.height
                        height: toolbar9.height
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app9_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app9_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar9.height
                        height: toolbar9.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app9_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app9_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Unity Dock - top */
    Rectangle {
        anchors.top: topbar.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 0
        width: parent.width
        height: 70
        color: "#A0FFFFFF"
        radius: 0
        objectName: "toolbar10"
        id: toolbar10

        RowLayout {
            anchors.left: parent.left
            anchors.verticalCenter: parent.verticalCenter
            anchors.leftMargin: 20
            ToolButton {
                width: toolbar10.height
                height: toolbar10.height
                objectName: "btnMenu10"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu10"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu10_anim
                        objectName: "btnMenu10_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar10.height
                        height: toolbar10.height
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app10_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app10_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar10.height
                        height: toolbar10.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app10_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app10_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Unity dock - left */

    Rectangle {
        anchors.left: parent.left
        anchors.top: topbar.bottom
        anchors.bottom: parent.bottom
        anchors.verticalCenter: parent.verticalCenter
        anchors.leftMargin: 0
        width: 70
        height: parent.height

        color: "#A0FFFFFF"
        radius: 0
        objectName: "toolbar11"
        id: toolbar11

        ColumnLayout {
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 20
            ToolButton {
                width: toolbar11.width
                height: toolbar11.width
                objectName: "btnMenu11"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu11"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu11_anim
                        objectName: "btnMenu11_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar11.width
                        height: toolbar11.width
                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app11_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app11_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar11.height
                        height: toolbar11.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app11_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app11_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Unity dock - right */
    Rectangle {
        anchors.right: parent.right
        anchors.top: topbar.bottom
        anchors.bottom: parent.bottom
        anchors.verticalCenter: parent.verticalCenter
        anchors.rightMargin: 0
        width: 70
        height: parent.height

        color: "#A0FFFFFF"
        radius: 0
        objectName: "toolbar12"
        id: toolbar12

        ColumnLayout {
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 20
            ToolButton {
                width: toolbar12.width
                height: toolbar12.width
                objectName: "btnMenu12"
                Image {
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    objectName: "imgMenu12"
                    sourceSize: Qt.size( parent.width, parent.height )
                    NumberAnimation on opacity {
                        id: btnMenu12_anim
                        objectName: "btnMenu12_anim"
                        from: 0
                        to: 1
                        duration: 100
                    }
                }
            }

            Repeater {
                model: EntryDockApplications

                    ToolButton {
                        width: toolbar12.width
                        height: toolbar12.width

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app12_anim.start();
                            }
                            background_app.text = model.name;
                            
                        }
                        NumberAnimation on opacity {
                            id: app12_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                    }
            }
            Repeater {
                model: LaunchedAppApplications

                    ToolButton {
                        width: toolbar12.height
                        height: toolbar12.height

                        Image {
                            source: model.logo
                            sourceSize: Qt.size( parent.width, parent.height )
                            anchors.fill: parent
                        }
                        onClicked: {
                            if (enable_anim.text == "Yes"){
                                app12_anim.start();
                            }
                            restore_app.text = model.name;
                        }
                        NumberAnimation on opacity {
                            id: app12_anim
                            from: 0
                            to: 1
                            duration: 100
                        }
                        Rectangle {
                            anchors.bottom: parent.bottom
                            anchors.horizontalCenter: parent.horizontalCenter
                            color: "blue"
                            width: 5
                            height: 5
                            radius: 5
                        }
                    }
            }
            Item { Layout.fillWidth: true }
        }
    }

    /* Show clock */
    Rectangle {
       color: "#A0FFFFFF"
       anchors.top: topbar.bottom
       anchors.horizontalCenter: parent.horizontalCenter
       width: 256
       height: 256
       radius: 256
       anchors.topMargin: 5
       visible: false
       //visible: true
       objectName: "showclock"
       id: showclock

       AnalogClock
       {
            width: parent.height
            height: parent.height
            anchors.centerIn: parent
       }

       NumberAnimation on height {
            id: showclock_anim
            objectName: "showclock_anim"
            from: 0
            to: 256
            duration: 100
        }
    }

    /* Show Panel */
    Rectangle {
       color: "transparent"
       anchors.right: parent.right
       anchors.top: topbar.bottom
       anchors.topMargin: 10
       width: parent.width/3
       height: parent.height-topbar.height
       radius: 0
       anchors.rightMargin: 10
       visible: false
       //visible: true
       objectName: "showpanel"
       id: showpanel

       ScrollView {
            width: parent.width
            height: parent.height
            anchors.topMargin: 10
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            anchors.bottomMargin: 10
            anchors.top: topbar.bottom
            clip: true
            id: scrollx
            Column {
                width: showpanel.width
                height: showpanel.height

                spacing: 2
                Repeater {
                    model: FeedModel

                    Rectangle {
                        width: parent.width
                        height: parent.width/1.3
                        color: "transparent"
                        radius: parent.width/20

                        Image {
                            width: parent.width
                            height: parent.height
                            source: model.image
                            fillMode: Image.PreserveAspectCrop
                            layer.enabled: true
                            layer.effect: OpacityMask {
                                maskSource: mask_feeds
                            }

                            Rectangle {
                                anchors.bottom: parent.bottom
                                width: parent.width
                                height: parent.height/6
                                color: "white"
                                radius: mask_feeds.radius

                                Text {
                                    text: model.title
                                    font.family: "IRANSans"
                                    font.pixelSize: parent.width/35
                                    font.bold: true
                                    id: titlefeed
                                    anchors.top: imagefeed.bottom
                                    anchors.topMargin: 5
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }

                                Text {
                                    text: model.summary
                                    font.family: "IRANSans"
                                    font.pixelSize: parent.width/40
                                    font.bold: false
                                    id: summaryfeed
                                    anchors.top: titlefeed.bottom
                                    anchors.topMargin: 5
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }

                                MouseArea {
                                    anchors.fill: parent
                                    onClicked: {
                                        feedsel.text = model.link;
                                    }
                                }
                            }
                        }

                        Rectangle {
                            width: parent.width
                            height: parent.height
                            radius: parent.radius
                            id: mask_feeds
                            visible: false
                        }
                    }
                }
            }
        }

       NumberAnimation on width {
            id: showpanel_anim
            objectName: "showpanel_anim"
            from: 0
            to: desktop.width/3
            duration: 100
        }
    }

    /* Event Panel */
    Rectangle {
       color: "transparent"
       anchors.right: parent.right
       anchors.top: topbar.bottom
       anchors.topMargin: 10
       width: parent.width/3
       height: parent.height-topbar.height
       radius: 0
       anchors.rightMargin: 10
       visible: false
       objectName: "eventpanel"
       id: eventpanel

       ScrollView {
            width: parent.width
            height: parent.height
            anchors.topMargin: 10
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            anchors.bottomMargin: 10
            anchors.top: topbar.bottom
            clip: true
            id: scrolle
            Column {
                width: eventpanel.width
                height: eventpanel.height

                spacing: 2

                    Image {
                        width: parent.width
                        height: parent.width/3
                        source: "../../../usr/share/backgrounds/BaaD_Clear.jpg"
                        fillMode: Image.PreserveAspectCrop
                        layer.enabled: true
                        objectName: "imgTemp"
                        layer.effect: OpacityMask {
                            maskSource: mask_weather
                        }

                        Text {
                            anchors.centerIn: parent
                            text: "34 °C"
                            color: "white"
                            font.family: "IRANSans"
                            objectName: "txtTemp"
                            font.pixelSize: parent.width/8
                        }
                    }

                    Rectangle {
                        width: parent.width
                        height: parent.width/3
                        color: "#A0FFFFFF"
                        radius: parent.width/20
                        id: mask_weather
                        visible: false
                    }

                    Rectangle {

                        width: parent.width
                        height: parent.width/1.3
                        color: "white"
                        radius: parent.width/20

                        PersianCalendar {
                            anchors.top: parent.top
                            anchors.topMargin: parent.height/18
                            anchors.left: parent.left
                            anchors.right: parent.right
                            width: parent.width
                            height: parent.height/1.3
                            objectName: "Jalali"
                        }

                        Rectangle {
                            color: "transparent"
                            anchors.bottom: parent.bottom
                            width: parent.width
                            height: parent.height/8

                            Text {
                                anchors.centerIn: parent
                                text: ""
                                id: txtD
                                objectName: "txtD"
                                font.family: "IRANSans"
                                font.pixelSize: 16
                                color: "gray"
                            }
                        }
                    }

            }
        }

       NumberAnimation on width {
            id: eventpanel_anim
            objectName: "eventpanel_anim"
            from: 0
            to: desktop.width/3
            duration: 100
        }
    }

    /* Note Panel */
    Rectangle {
       color: "transparent"
       anchors.right: parent.right
       anchors.top: topbar.bottom
       anchors.topMargin: 10
       width: parent.width/3
       height: parent.height-topbar.height
       radius: 0
       anchors.rightMargin: 10
       visible: false
       //visible: true
       objectName: "notepanel"
       id: notepanel

       ScrollView {
            width: parent.width
            height: parent.height
            anchors.topMargin: 10
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            anchors.bottomMargin: 10
            anchors.top: topbar.bottom
            clip: true
            id: scrolln
            Column {
                width: notepanel.width
                height: notepanel.height

                spacing: 2
                Repeater {
                    model: 4

                    Rectangle {
                        width: parent.width
                        height: parent.width/1.3
                        color: "#A0FFAFFF"
                        radius: parent.width/20


                        ScrollView {
                            anchors.top: parent.top
                            anchors.left: parent.left
                            anchors.right: parent.right
                            anchors.bottom: parent.bottom

                            anchors.topMargin: parent.width/30
                            anchors.leftMargin: parent.width/30
                            anchors.rightMargin: parent.width/30
                            anchors.bottomMargin: parent.width/30

                            width: parent.width
                            height: parent.height

                            clip: true
                            TextArea {
                                anchors.top: toolbar.bottom
                                id: txtNote
                                width: parent.width
                                font.family: "IRANSans"
                                objectName: "txtNote"
                                selectByMouse: true
                                MouseArea {
                                    anchors.fill: parent
                                    cursorShape: Qt.IBeamCursor
                                    acceptedButtons: Qt.NoButton
                                }
                            }
                        }

                    }
                }
            }
        }

       NumberAnimation on width {
            id: notepanel_anim
            objectName: "notepanel_anim"
            from: 0
            to: desktop.width/3
            duration: 100
        }
    }

    /* Popup PySys */
    Popup {
        id: popup_pysys
        objectName: "popup_pysys"
        anchors.centerIn: parent
        width: 520
        height: 200
        modal: true
        focus: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent

        ToolButton {
            anchors.top: parent.top
            anchors.right: parent.right
            anchors.rightMargin: 1
            anchors.leftMargin: 1
            width: 25
            height: 25

            Image {
                    source: "file:///stor/usr/share/icons/breeze-close.svg"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( parent.width, parent.height )

            }

            onClicked: {
                popup_pysys.close()
            }
        }

            ToolButton {
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                width: 100
                height: parent.height/2
                id: shutdown
                objectName: "shutdown"
                Image {
                    anchors.fill: parent
                    id: shutdown_img
                    objectName: "shutdown_img"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( shutdown.width, shutdown.height )
                }
            }
            Text {
                text: "Shutdown"
                objectName: "txtShutdown"
                anchors.top: shutdown.bottom
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: shutdown.horizontalCenter
                font.family: "IRANSans"
            }
            ToolButton {
                anchors.left: shutdown.right
                anchors.verticalCenter: parent.verticalCenter
                width: 100
                height: parent.height/2
                id: lock
                objectName: "lock"
                Image {
                    anchors.fill: parent
                    id: lock_img
                    objectName: "lock_img"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( lock.width, lock.height )
                }
            }
            Text {
                text: "Lock"
                objectName: "txtLock"
                anchors.top: lock.bottom
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: lock.horizontalCenter
                font.family: "IRANSans"
            }
            ToolButton {
                anchors.left: lock.right
                anchors.verticalCenter: parent.verticalCenter
                width: 100
                height: parent.height/2
                id: logout
                objectName: "logout"
                Image {
                    anchors.fill: parent
                    id: logout_img
                    objectName: "logout_img"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( logout.width, logout.height )
                }
            }
            Text {
                text: "Logout"
                objectName: "txtLogout"
                anchors.top: logout.bottom
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: logout.horizontalCenter
                font.family: "IRANSans"
            }
            ToolButton {
                anchors.left: logout.right
                anchors.verticalCenter: parent.verticalCenter
                width: 100
                height: parent.height/2
                id: reboot
                objectName: "reboot"
                Image {
                    anchors.fill: parent
                    id: reboot_img
                    objectName: "reboot_img"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( reboot.width, reboot.height )
                }
            }
            Text {
                text: "Restart"
                objectName: "txtReboot"
                anchors.top: reboot.bottom
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: reboot.horizontalCenter
                font.family: "IRANSans"
            }
            ToolButton {
                anchors.left: reboot.right
                anchors.verticalCenter: parent.verticalCenter
                width: 100
                height: parent.height/2
                id: suspend
                objectName: "suspend"
                Image {
                    anchors.fill: parent
                    id: suspend_img
                    objectName: "suspend_img"
                    fillMode: Image.PreserveAspectFit
                    sourceSize: Qt.size( suspend.width, suspend.height )
                }
            }
            Text {
                text: "Sleep"
                objectName: "txtSuspend"
                anchors.top: suspend.bottom
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: suspend.horizontalCenter
                font.family: "IRANSans"
            }
    }

    /* Text Popup */
    Popup {
        id: popup_text
        anchors.centerIn: parent
        width: 400
        height: 90
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

            Image {
                source: "file:///stor/usr/share/icons/breeze-close.svg"
                fillMode: Image.PreserveAspectFit
                sourceSize: Qt.size( parent.width, parent.height )
            }

            onClicked: {
                popup_text.close()
            }
        }

        Text {
            anchors.centerIn: parent
            font.family: "IRANSans"
            objectName: "popup_text_txtText"
            id: popup_text_txtText
            text: "a message"
        }
    }

    /* Feed Browser Popup */
    Popup {
        id: popup_feed
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

            Image {
                source: "file:///stor/usr/share/icons/breeze-close.svg"
                fillMode: Image.PreserveAspectFit
                sourceSize: Qt.size( parent.width, parent.height )
            }

            onClicked: {
                popup_feed.close()
            }


        }


    }


    Menu {
        id: contextMenu
        font.family: "IRANSans"
        objectName: "contextMenu"

        Action {
            text: "Appearanc"
            id: appc
            objectName: "appc"
            onTriggered: {
                background_app.text = 'appearanc'
            }
        }
        Action {
            text: "Display Settings"
            id: displayc
            objectName: "displayc"
            onTriggered: {
                background_app.text = 'displaymanager'
            }
        }
        Action {
            text: "Refresh"
            id: refresh
            objectName: "refreshc"
            onTriggered: {
                background_app.text = 'refresh'
            }
        }
        Action {
            text: "Restore minimized apps"
            id: rma
            objectName: "rmac"
            onTriggered: {
                background_app.text = 'rma'
            }
        }
        Action {
            text: "Run"
            id: runc
            objectName: "runc"
            onTriggered: {
                background_app.text = 'runapp'
            }
        }
    }

    MouseArea {
        anchors.centerIn: parent
        width: parent.width/2
        height: parent.height/2
        id: msaDesktop
        objectName: "msaDesktop"
        acceptedButtons: Qt.LeftButton | Qt.RightButton
        onClicked: {

            if (mouse.button === Qt.RightButton)
                contextMenu.popup()

        }

        onPressAndHold: {
            if (mouse.source === Qt.MouseEventNotSynthesized)
                contextMenu.popup()
        }
    }
    /*
    GridView {
        model: FileModel
        cellWidth: 64; cellHeight: 80
        highlight: highlight
        anchors.top: parent.top
        anchors.bottom: toolbar.top
        highlightFollowsCurrentItem: false
        focus: true

        delegate: Column {
            Image { 
                source: model.logo
                width: 64
                height: 70
                sourceSize: Qt.size( parent.width, parent.height )
                anchors.horizontalCenter: parent.horizontalCenter
                MouseArea {
                    anchors.fill: parent
                    acceptedButtons: Qt.LeftButton | Qt.RightButton
                    onDoubleClicked: {
                        fsel.text = model.path
                    }
                    onClicked: {
                        if (mouse.button === Qt.RightButton)
                            contextMenu.popup()

                    }

                    onPressAndHold: {
                        if (mouse.source === Qt.MouseEventNotSynthesized)
                            contextMenu.popup()
                    }
                }   
            }
            Text { 
                text: model.name
                anchors.horizontalCenter: parent.horizontalCenter
                font.family: "IRANSans"
                color: "white"
            }
        }
    }*/

}