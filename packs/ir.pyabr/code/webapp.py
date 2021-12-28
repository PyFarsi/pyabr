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
            # Keep reference to external window, so it isn't cleared up.
            app.start('chromium',url.toString())
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