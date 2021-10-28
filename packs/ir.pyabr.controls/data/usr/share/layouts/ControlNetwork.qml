import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ScrollView {
                anchors.top: parent.top
                width: parent.width
                height: parent.height-70
                clip: true
                Column {
                    width: network_exec.width
                    height: network_exec.height-70
                    spacing: 2
                    Repeater {
                        model: NetworkModel

                        Rectangle {
                            width: parent.width
                            height: parent.width/10
                            color: "transparent"

                            MouseArea {
                                anchors.fill: parent
                                acceptedButtons: Qt.LeftButton | Qt.RightButton
                                onClicked: {
                                    wsel.text = model.ssid
                                }
                            }

                            Image {
                                    source: model.netlogo
                                    anchors.left: parent.left
                                    anchors.leftMargin: 20
                                    anchors.rightMargin: 20
                                    width: parent.height
                                    sourceSize: Qt.size( parent.width, parent.height )
                                    height: parent.height
                                    id: imagenet
                            }

                            Text {
                                text: model.ssid
                                font.family: "IRANSans"
                                font.pixelSize: 18
                                anchors.verticalCenter: parent.verticalCenter
                                anchors.left: imagenet.right
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