import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12
ScrollView {
                anchors.top: parent.top
                width: parent.width
                height: parent.height-70
                clip: true
                Column {
                    width: display_exec.width
                    height: display_exec.height-70
                    spacing: 2
                    Repeater {
                        model: DisplayModel

                        ToolButton {
                            width: parent.width
                            height: parent.width/10
                            //color: "transparent"

                            MouseArea {
                                anchors.fill: parent
                                acceptedButtons: Qt.LeftButton | Qt.RightButton
                                onClicked: {
                                    rsel.text = model.display
                                }
                            }

                            Text {
                                text: model.display
                                font.family: wt.fontFamily
                                color: wt.color
                                font.pixelSize: 18
                                anchors.verticalCenter: parent.verticalCenter
                                anchors.left: parent.left
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