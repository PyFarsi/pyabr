from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from libabr import *
from PyQt5 import uic
import requests,shutil,os,importlib
app = App()
res = Res()
files = Files()
control = Control()
commands = Commands()

class MainApp(QMainWindow):

    def onCloseProcess (self):
        if not app.check('uiv'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,args):
        super(MainApp, self).__init__()

        # ports
        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

        self.onCloseProcess()

        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('uiv','logo'))))

        # External ui #
        if self.External==None:
            self.Widget.Close()
        else:
            if self.External==[]:
                self.Widget.Close()
            else:
                if self.External[0]==None:
                    self.Widget.Close()
                else:
                    uic.loadUi(files.input(self.External[0]),self)

                    self.Widget.SetWindowTitle (self.windowTitle())
                    self.Widget.SetWindowIcon (self.windowIcon())
                    self.Widget.Resize (self,self.width(),self.height())