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
                anchors.fill: parent
                clip: true

                Column {
                    spacing: 2
                    width: recexec.width
                    height: recexec.height


                    Repeater {
                        model: ContactModel

                        Rectangle {
                            visible: true

                            width: parent.width
                            height: parent.width/8
                            color: "transparent"

                            MouseArea {
                                anchors.fill: parent
                                //acceptedButtons: Qt.LeftButton | Qt.RightButton
                                onClicked: {
                                    csel.text = model.username
                                    xfullname.text = model.fullname
                                    xprofile.text = model.profile
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

                            ToolButton {
                                icon.source: "file:///stor/usr/share/icons/breeze-next.svg"
                                icon.color: "gray"
                                anchors.verticalCenter: parent.verticalCenter
                                anchors.right: parent.right
                                anchors.leftMargin: 20
                                anchors.rightMargin: 20
                                objectName: "gotoContact"
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