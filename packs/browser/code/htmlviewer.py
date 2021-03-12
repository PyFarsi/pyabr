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
            self.Widget.Close()
        else:
            if self.External[0]==None:
                self.Widget.Close()
            else:
                self.abr(self.External[0])

    def abr (self, data):
        ## Connect to ABR Finder location AFL
        self.browser = QWebEngineView()
        self.browser.setHtml(files.readall(data))
        self.setCentralWidget(self.browser)
        self.Loop()


    def Loop(self):
        self.browser.update()
        self.Widget.SetWindowTitle (self.browser.page().title())
        self.Widget.SetWindowIcon (QIcon(self.browser.page().icon()))

        QTimer.singleShot(50,self.Loop)