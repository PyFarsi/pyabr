#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

import os,subprocess
import sys,requests

from libabr import Res, Control, Files,App

res = Res()
control = Control()
app = App()
files = Files()

# Your URL for your webview project
URL = "https://gerdoo.me"

class MainApp(QMainWindow):
    def onCloseProcess (self):
        if not app.check(self.AppName):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,ports, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)
        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        self.Widget.SetWindowIcon (QIcon(res.get('@icon/web-browser')))
        self.Widget.Resize(self,int(self.Env.width())/1.5,int(self.Env.height())/1.5)

        if self.External==[]:
            self.add_new_tab(QUrl(URL), res.get('@string/app_name'))
        else:
            if self.External[0]==None:
                self.add_new_tab(QUrl(URL), res.get('@string/app_name'))
            elif self.External[0].startswith ('http://') or self.External[0].startswith ('https://'):
                    self.add_new_tab(QUrl(self.External[0]), res.get('@string/app_name'))

    def add_new_tab(self, qurl=None, label="Blank"):

        self.browser = QWebEngineView()
        self.browser.setUrl(qurl)
        self.setCentralWidget(self.browser)
        self.Loop()

    def Loop(self):
        self.browser.update()

        if not self.browser.page().title().startswith('https://') or self.browser.page().title().startswith('http://'):
            self.Widget.SetWindowTitle (self.browser.page().title())
        self.Widget.SetWindowIcon (QIcon(self.browser.page().icon()))

        QTimer.singleShot(50,self.Loop)

    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)
