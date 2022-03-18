from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from pyabr.core import *
import os
import sys

class CustomWebEnginePage(QWebEnginePage):
    """ Custom WebEnginePage to customize how we handle link navigation """
    # Store external windows.
    external_windows = []


    def acceptNavigationRequest(self, url,  _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            urlx = url.toString()
            if urlx.endswith('.exe') or urlx.endswith('.msi') or urlx.endswith('.doc') or urlx.endswith('.docx') or urlx.endswith('.ppt') or urlx.endswith('.pptx') or \
               urlx.endswith('.dot') or urlx.endswith('.dotx') or urlx.endswith('.iso') or urlx.endswith('.bin') or urlx.endswith('.zip') or urlx.endswith('.tar') or urlx.endswith('.xz') or urlx.endswith('.bz2') \
                    or urlx.endswith('.bz') or urlx.endswith('.sb') or urlx.endswith('.squashfs') or urlx.endswith('.rar') or urlx.endswith('.cab') or urlx.endswith('.run') or urlx.endswith('.apk') or urlx.endswith('.rtf') \
                    or urlx.endswith('.egg') or urlx.endswith('.dwg') or urlx.endswith('.xls') or urlx.endswith('.xlsm') or urlx.endswith('.xlsx') or urlx.endswith('.com') or urlx.endswith('.ai') \
                    or urlx.endswith('.img') or urlx.endswith('.pa'):
                app.start('download',urlx)
            else:
                w = QWebEngineView()
                w.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
                w.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
                w.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
                w.setUrl(url)
                w.show()

                try:
                    w.setWindowIcon(QIcon(res.get(sys.argv[2])))
                except:
                    w.setWindowIcon(QIcon(res.get('@icon/breeze-app')))

                try:
                    w.setWindowTitle(sys.argv[3])
                except:
                    pass

                # Keep reference to external window, so it isn't cleared up.
                self.external_windows.append(w)
            return False
        return super().acceptNavigationRequest(url,  _type, isMainFrame)

class MainWindow(QMainWindow):
    style='''<!DOCTYPE HTML>
<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<style>
@font-face {
	font-family: 'IRANSansX';
	src: url('/usr/share/fonts/truetype/IRANSansX-Regular.ttf') format('truetype');
} 
body {
    font-family: "IRANSansX" !important;
}
</style>
</head>
<body>
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>'''

    def processHTML(self,html):
        
        files.write('m.html',f"{self.style}{html}</body></html>")

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()

        self.browser.setPage(CustomWebEnginePage(self))
        self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        self.browser.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled,True)
        self.browser.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls,True)
        self.browser.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls,True)
        self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled,True)

        icon = False
        title = False

        try:
            self.browser.setUrl(QUrl(sys.argv[1]))
        except:
            pass

        try:
            icon = True
            self.setWindowIcon(QIcon(res.get(sys.argv[2])))
        except:
            icon = False
            self.setWindowIcon(QIcon(res.get('@icon/breeze-app')))

        try:
            title = True
            self.setWindowTitle(sys.argv[3])
        except:
            title = False

        if title==True and icon==True:
            app.launchedlogo(sys.argv[3],sys.argv[2])
        elif icon:
            app.launchedlogo("WebApp",sys.argv[2])
        elif title:
            app.launchedlogo(sys.argv[3], '@icon/breeze-app')
        else:
            app.launchedlogo('WebApp','@icon/breeze-app')

        self.setCentralWidget(self.browser)

appx = QApplication(sys.argv)
window = MainWindow()
window.show()
appx.exec_()