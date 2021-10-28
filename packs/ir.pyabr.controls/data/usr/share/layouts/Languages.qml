import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material


ScrollView {
                anchors.top: parent.top
                width: parent.width
                height: parent.height-70*2
                clip: true
                Column {
                    width: display_exec.width
                    height: display_exec.height-70
                    spacing: 2
                    Repeater {
                        model: LanguageModel

                        Rectangle {
                            width: parent.width
                            height: parent.width/10
                            color: "transparent"

                            MouseArea {
                                anchors.fill: parent
                                acceptedButtons: Qt.LeftButton | Qt.RightButton
                                onClicked: {
                                    lsel.text = model.name
                                }
                            }

                            Text {
                                text: model.label
                                font.family: "IRANSans"
                                font.pixelSize: 18
                                anchors.verticalCenter: parent.verticalCenter
                                anchors.left: parent.left
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