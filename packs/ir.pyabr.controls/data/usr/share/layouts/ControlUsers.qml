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
                    width: users_exec.width
                    height: users_exec.height


                    Repeater {
                        model: UserModel

                        Rectangle {
                            visible: true

                            width: parent.width
                            height: parent.width/10
                            color: "transparent"

                            MouseArea {
                                anchors.fill: parent
                                acceptedButtons: Qt.LeftButton | Qt.RightButton
                                onClicked: {
                                    usel.text = model.username
                                    fsel.text = "showuser"
                                }
                            }

                            Image {
                                    source: model.profile
                                    anchors.left: parent.left
                                    anchors.leftMargin: 20
                                    anchors.rightMargin: 20
                                    width: parent.height
                                    sourceSize: Qt.size( parent.width, parent.height )
                                    height: parent.height
                                    id: imagexx
                            }

                            Text {
                                text: model.fullname
                                font.family: "IRANSans"
                                font.pixelSize: 18
                                anchors.verticalCenter: parent.verticalCenter
                                anchors.left: imagexx.right
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