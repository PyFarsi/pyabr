import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12
import QtWebEngine 1.2
import QtQuick.Layouts 1.11


ApplicationWindow {
    id: markDownViewer
    visible: true
    color: wt.background
    title: "MarkDown Viewer"

    width: 1000
    height: 600

                WebEngineView {
                    id: webView
                    objectName: "webView"
                    anchors.fill: parent
                    width: parent.width
                    height: parent.height
                }
}
