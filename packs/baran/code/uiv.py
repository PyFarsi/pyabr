import py_compile
import sys

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
def getdata (name):
    return control.read_record (name,'/etc/gui')
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
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

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
                elif self.External[0].startswith ("abr://"):

                    ############# ABR Version 1 #########################
                    splitabr = self.External[0].split("://")
                    url = splitabr[1]

                    if not '/' in url:
                        url +='/index'

                    commands.get([f"{url}.xml"])
                    commands.get([f"{url}.css"])
                    commands.get([f"{url}.py"])

                    try:
                        uic.loadUi(files.input(f'/srv/{url}.xml'), self)

                        if files.isfile(f'/srv/{url}.css'):
                            self.setStyleSheet(files.readall(f'/srv/{url}.css'))

                        if files.isfile(f'/srv/{url}.py'):
                            py_compile.compile(files.input(f'/srv/{url}.py'),files.input('/srv/cloud.pyc'))
                            self.m = importlib.import_module('srv.cloud')
                            importlib.reload(self.m)
                            self.m.MainApp (self)

                        self.Widget.SetWindowTitle(self.windowTitle())
                        self.Widget.SetWindowIcon(self.windowIcon())
                        self.Widget.Resize(self, self.width(), self.height())
                    except:
                        if files.isfile(f'/srv/{url}.py'):
                            py_compile.compile(files.input(f'/srv/{url}.py'), files.input('/srv/cloud.pyc'))
                            self.m = importlib.import_module('srv.cloud')
                            importlib.reload(self.m)
                            self.m.MainApp(self)
                    ####################################################
                else:
                    uic.loadUi(files.input(self.External[0]),self)

                    self.Widget.SetWindowTitle (self.windowTitle())
                    self.Widget.SetWindowIcon (self.windowIcon())
                    self.Widget.Resize (self,self.width(),self.height())