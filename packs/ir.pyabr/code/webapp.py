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
                    or urlx.endswith('.egg') or urlx.endswith('.dwg') or urlx.endswith('.xls') or urlx.endswith('.xlsm') or urlx.endswith('.xlsx') or urlx.endswith('.com') or urlx.endswith('.pdf') or urlx.endswith('.ai') \
                    or urlx.endswith('.img') or urlx.endswith('.pa'):
                app.start('download',urlx)
            else:
                w = QWebEngineView()
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
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()

        self.browser.setPage(CustomWebEnginePage(self))

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