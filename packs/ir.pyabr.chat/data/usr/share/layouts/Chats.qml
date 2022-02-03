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

                 Menu {
                    id: contextMenu
                    font.family: "IRANSans"
                    objectName: "contextMenu"

                    Action {
                        text: "Delete"
                        id: delete_m
                        objectName: "delete_m"
                        onTriggered: {
                            act.text = 'delete'
                        }
                    }
                    Action {
                        text: "Clear history"
                        id: history_m
                        objectName: "history_m"
                        onTriggered: {
                            act.text = 'clear'
                        }
                    }
                    Action {
                        text: "Delete Chat"
                        id: delete_c
                        objectName: "delchat"
                        onTriggered: {
                            act.text = 'delchat'
                        }
                    }
                }



                Column {
                    spacing: 2
                    width: rechat.width
                    height: rechat.height


                    Repeater {
                        model: ChatModel

                        Rectangle {
                            color: "#ABCDEF"
                            radius: 20
                            id: recall
                            width: parent.width
                            height: parent.height/6
                            anchors.leftMargin: 20
                            anchors.topMargin: 20
                            anchors.bottomMargin: 20

                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    cid.text = model.id;
                                    csender.text = model.sender;
                                    cgiver.text = model.giver;
                                    cdata.text = model.data;
                                }
                                onDoubleClicked: {
                                    cid.text = model.id;
                                    csender.text = model.sender;
                                    cgiver.text = model.giver;
                                    cdata.text = model.data;
                                    contextMenu.popup();
                                }
                            }

                            Rectangle {
                                id: recme
                                color: "#123456"

                                radius: 200

                                Text {
                                    text: model.data
                                    font.family: "IRANSans"
                                    font.pixelSize: 18
                                    anchors.centerIn: recme
                                    anchors.topMargin: 20
                                    anchors.leftMargin: 20
                                    color: "white"
                                    id: textme
                                    visible: true
                                }
                                anchors.left: parent.left
                                width: textme.implicitWidth+24;
                                height: textme.implicitHeight+24;
                            }

                            Rectangle {
                                id: recthan
                                color: "white"

                                radius: 200

                                Text {
                                    text: model.data
                                    font.family: "IRANSans"
                                    font.pixelSize: 18
                                    anchors.centerIn: recthan
                                    anchors.topMargin: 20
                                    anchors.leftMargin: 20
                                    visible: true
                                    color: "gray"
                                    id: textthan
                                }
                                anchors.right: parent.right
                                width: textthan.implicitWidth+24;
                                height: textthan.implicitHeight+24;
                            }

                            function startupFunction() {
                                if (model.me)
                                {
                                    recthan.visible = false;
                                    recme.visible = true;
                                }
                                else
                                {
                                    recthan.visible = true;
                                    recme.visible = false;
                                }
                            }

                            Component.onCompleted: startupFunction();
                        }
                    }
                }
            }