import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ScrollView {
                anchors.fill: parent
                clip: true

                Column {
                    spacing: 2
                    width: rechat.width
                    height: rechat.height


                    Repeater {
                        model: ChatModel

                        Rectangle {
                            color: "#123456"
                            radius: 20
                            id: recthan
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.topMargin: 20
                            anchors.bottomMargin: 20

                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    cid.text = model.id
                                    csender.text = model.sender
                                    cgiver.text = model.giver
                                    cdata.text = model.data
                                }
                            }

                            Rectangle {
                                width: parent.width
                                height: 1
                                id: linex1
                                color: "white"
                                anchors.top: parent.top
                            }

                            Text {
                                text: model.data
                                font.family: "IRANSans"
                                font.pixelSize: 18
                                anchors.top: linex1.bottom
                                anchors.topMargin: 20
                                anchors.leftMargin: 20
                                color: "white"
                                id: text
                            }

                            Rectangle {
                                width: parent.width
                                height: 1
                                color: "white"
                                anchors.top: parent.bottom
                            }

                            width: text.implicitWidth+24;
                            height: text.implicitHeight+24;
                        }
                    }
                }
            }