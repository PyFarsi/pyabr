from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from libabr import *

import random, baran

files = Files()
colors = Colors()
control = Control()
res = Res()
app = App()
commands = Commands()
permissions = Permissions()

def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check('themes'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.External = ports[3]

        self.onCloseProcess()
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.SetWindowIcon (QIcon(res.etc('theme','logo')))

        self.Widget.SetWindowTitle (res.get('@string/app_name'))

        self.x = baran.ThemeListView([self.Env,self])
        self.setCentralWidget(self.x)