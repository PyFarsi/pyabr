from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import os
import sys

from libabr import Res, Control, Files, System, App

res = Res()
control = Control()
app = App()
files = Files()

class MainApp(QMainWindow):
    def Browser (self):
        System('/usr/app/browser')  # Run CatBall Browser

    def onCloseProcess (self):
        if not app.check('browser'):
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

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.Widget.Resize(self,self.Env.width(),self.Env.height())

        self.Widget.hide()
        self.Widget.Close()

        QTimer.singleShot(1,self.Browser)