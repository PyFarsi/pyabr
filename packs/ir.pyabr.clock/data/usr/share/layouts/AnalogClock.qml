import QtQuick 2.0
import QtQuick.Controls 2.2
/* https://github.com/rafzby/ */
Item {
    id: clock
    //width: 600
    //height: 600
    //anchors.centerIn: parent

    property int hours
    property int minutes
    property int seconds


    function timeChanged() {
        var date = new Date();
        hours = date.getHours();
        minutes = date.getMinutes();
        seconds = date.getSeconds();
    }

    Timer {
        interval: 100
        repeat: true
        running: true
        onTriggered: timeChanged()
    }

    Image {
        id: clockFace
        source: "file:///stor/usr/share/images/clock-face.png"
        anchors.fill: parent
        width: parent.width
        height: parent.height
    }

    Rectangle {
        id: hourHand
        color: "black"
        radius: 100
        x: 294/2.36; y: 140/2.36
        width: 10/2.36
        height: 174/2.36
        transform: Rotation {
            id: hourRotation
            angle: (clock.hours * 30)
            origin.x: 5/2.36
            origin.y: 164/2.36

            Behavior on angle {
                SpringAnimation {
                    spring: 2
                    damping: 0.2
                    modulus: 360
                }
            }
        }
    }

    Rectangle {
        color: "gray"
        radius: 100
        id: minuteHand
        x: 295/2.36; y: 93/2.36
        width: 10/2.36
        height: 221/2.36
        transform: Rotation {
            id: minuteRotation
            angle: clock.minutes * 6
            origin.x: 5/2.36
            origin.y: 211/2.36
            Behavior on angle {
                SpringAnimation {
                    spring: 2
                    damping: 0.2
                    modulus: 360
                }
            }
        }
    }

    Rectangle {
        id: secondHand
        color: "red"
        radius: 100
        x: 297/2.36; y: 42/2.36
        width: 5/2.36
        height: 273/2.36
        transform: Rotation {
            id: secondRotation
            angle: clock.seconds * 6
            origin.x: 2.36/2.36
            origin.y: 263/2.36

            Behavior on angle {
                SpringAnimation {
                    spring: 2
                    damping: 0.2
                    modulus: 360
                }
            }
        }
    }

    Rectangle {
        anchors.centerIn: parent
        color: "black"
        width: parent.height/30
        height: parent.height/30
        radius: 50
    }
}
