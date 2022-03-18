import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12
import QtMultimedia 5.15

ApplicationWindow {
    id: ayene
    visible: true
    width: 1000
    height: 600

    Text {
        id: capx
        objectName: "capx"
    }


        Camera {
            id: camera

            imageProcessing.whiteBalanceMode: CameraImageProcessing.WhiteBalanceFlash

            exposure {
                exposureCompensation: -1.0
                exposureMode: Camera.ExposurePortrait
            }

            flash.mode: Camera.FlashRedEyeReduction

            imageCapture {
                onImageCaptured: {
                    photoPreview.source = preview  // Show the preview in an Image
                }
            }
        }

        VideoOutput {
            source: camera
            anchors.fill: parent
            focus : visible // to receive focus and capture key events when visible
        }

        Image {
            id: photoPreview
            objectName: "photoPreview"
            anchors.fill: parent
        }

        ToolButton {
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottomMargin: 10
            objectName: "cap"
            width: 100
            height: 100
            onClicked:
            {
                camera.imageCapture.capture();
                camera.stop();
                capx.text = "m";
            }
            Image {
                anchors.fill: parent
                sourceSize: Qt.size( parent.width, parent.height )
                source: 'file:///stor/usr/share/icons/breeze-mirror.svg'
            }
        }
}