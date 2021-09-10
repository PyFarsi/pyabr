import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: calculator
    visible: true
    color: "white"
    width: 400
    height: 400
    TextField {
        anchors.top: parent.top
        width: parent.width
        height: parent.height/6
        enabled: true
        id: field
        objectName: "o1"
    }
    Button {
        width: parent.width/5
        anchors.top: field.bottom
        height: parent.height/6
        text: '%'
        id: baqi
        enabled: false
        objectName: "o2"
    }
    Button {
        width: parent.width/5
        anchors.top: field.bottom
        height: parent.height/6
        text: '/'
        anchors.left: baqi.right
        id: taqsim
        objectName: "o3"
        enabled: false
    }
    Button {
        width: parent.width/5
        anchors.top: field.bottom
        height: parent.height/6
        text: '*'
        anchors.left: taqsim.right
        enabled: false
        id: zarb
        objectName: "o4"
    }
    Button {
        width: parent.width/5
        anchors.top: field.bottom
        height: parent.height/6
        text: '-'
        anchors.left: zarb.right
        id: minus
        objectName: "o5"
        enabled: false
    }
    Button {
        width: parent.width/5
        anchors.top: baqi.bottom
        height: parent.height/6
        text: '7'
        anchors.left: parent.left
        id: seven
        objectName: "o7"
    }
    Button {
        width: parent.width/5
        anchors.top: taqsim.bottom
        height: parent.height/6
        text: '8'
        anchors.left: seven.right
        id: eight
        objectName: "o8"
    }
    Button {
        width: parent.width/5
        anchors.top: zarb.bottom
        height: parent.height/6
        text: '9'
        anchors.left: eight.right
        id: nine
        objectName: "o9"
    }
    Button {
        width: parent.width/5
        anchors.top: minus.bottom
        height: (parent.height/6)*2
        text: '+'
        anchors.left: nine.right
        id: add
        objectName: "o10"
        enabled: false
    }
    Button {
        width: parent.width/5
        anchors.top: field.bottom
        height: (parent.height/6)*2
        text: 'AC'
        anchors.left: minus.right
        id: ac
        objectName: "o11"
    }
    Button {
        width: parent.width/5
        anchors.top: seven.bottom
        height: parent.height/6
        text: '4'
        anchors.left: parent.left
        id: forz
        objectName: "o12"
    }
    Button {
        width: parent.width/5
        anchors.top: eight.bottom
        height: parent.height/6
        text: '5'
        anchors.left: forz.right
        id: five
        objectName: "o13"
    }
    Button {
        width: parent.width/5
        anchors.top: nine.bottom
        height: parent.height/6
        text: '6'
        anchors.left: five.right
        id: six
        objectName: "o14"
    }
    Button {
        width: parent.width/5
        anchors.top: ac.bottom
        height: parent.height/6
        text: '('
        anchors.left: add.right
        id: baz
        objectName: "o15"
    }
    Button {
        width: parent.width/5
        anchors.top: forz.bottom
        height: parent.height/6
        text: '1'
        anchors.left: parent.left
        id: one
        objectName: "o16"
    }
    Button {
        width: parent.width/5
        anchors.top: five.bottom
        height: parent.height/6
        text: '2'
        anchors.left: one.right
        id: two
        objectName: "o17"
    }
    Button {
        width: parent.width/5
        anchors.top: six.bottom
        height: parent.height/6
        text: '3'
        anchors.left: two.right
        id: three
        objectName: "o18"
    }
    Button {
        width: parent.width/5
        anchors.top: add.bottom
        height: (parent.height/6)*2
        text: '='
        anchors.left: three.right
        id: equal
        objectName: "o19"
        enabled: false
    }
    Button {
        width: parent.width/5
        anchors.top: baz.bottom
        height: parent.height/6
        text: ')'
        anchors.left: equal.right
        id: baste
        objectName: "o20"
    }
    Button {
        width: (parent.width/5)*2
        anchors.top: one.bottom
        height: parent.height/6
        text: '0'
        anchors.left: parent.left
        id: ziro
        enabled: false
        objectName: "o21"
    }
    Button {
        width: parent.width/5
        anchors.top: three.bottom
        height: parent.height/6
        text: '.'
        anchors.left: ziro.right
        id: dot
        objectName: "o22"
    }
    Button {
        width: parent.width/5
        anchors.top: baste.bottom
        height: parent.height/6
        text: '+/-'
        anchors.left: equal.right
        id: minplus
        objectName: "o23"
    }
}