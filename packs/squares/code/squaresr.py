from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

import os
import sys

from libabr import Res, Control, Files, System

res = Res()
control = Control()
files = Files()

class MainApp(QMainWindow):
    def Game (self):
        System('/usr/games/squares')  # Run CatBall Game

    def __init__(self,ports, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)
        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.Widget.Resize(self,self.Env.width(),self.Env.height())

        self.Widget.hide()
        self.Widget.Close()

        files.write('/tmp/w',str(self.Env.width()))
        files.write('/tmp/h', str(self.Env.height()))

        QTimer.singleShot(1,self.Game)

