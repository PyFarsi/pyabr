'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, Apt, Dpkg, PyPI
    * License:          GNU General Publice License v3.0

    * Source code:      https://github.com/PyFarsi/pyabr
    * PyPI:             https://pypi.org/project/pyabr

    - Download Pyabr OS

    * AMD64, Intel64:   https://dl.pyabr.ir/pyabr-x86_64.iso     
    * ARM64:            https://dl.pyabr.ir/pyabr-arm64.img
    * Platform:         https://dl.pyabr.ir/stor.sb
    * Wheel Package:    https://dl.pyabr.ir/pyabr.whl
    
    - Channels:

    * Official Website: https://pyabr.ir
    * Telegram Channel: https://t.me/pyfarsi
    * Gap Channel:      https://gap.im/pyabr
    * Sorosh Channel:   https://splus.ir/pyabr
    * Instagram:        https://instagram.com/pyabrir
    * Hoorsa:           https://hoorsa.com/pyabr
    * Aparat:           https://aparat.com/pyabr

'''

import sys, subprocess,os,shutil,requests

from libabr import Files, Control, Permissions, Colors, Process, Modules, Package, Commands, Res, System,App

modules = Modules()
files = Files()
control = Control()
colors = Colors()
process = Process()
permissions = Permissions()
pack = Package()
commands = Commands()
res = Res()
app = App()

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainApp (QMainWindow):

    def onCloseProcess (self):
        if not app.check('not'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def opener (self):
        self.Widget.Close()
        self.Env.RunApp (self.External[0],[self.External[1]])

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.onCloseProcess()
        self.Widget.Resize (self,int(getdata('alert.width')),int(getdata('alert.height')))
        self.Widget.DisableFloat()

        self.btnView = QToolButton()
        self.btnView.setText (self.External[2]) # External[0]
        self.Widget.SetWindowTitle(res.etc(self.External[0],f"name[{getdata('locale')}]"))
        #  External[1]
        self.btnView.clicked.connect (self.opener)
        self.btnView.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.setCentralWidget(self.btnView)

        self.Widget.SetWindowIcon (QIcon(res.get(res.etc(self.External[0],'logo'))))
        # self.Env.RunApp ('not',['gap',None,'100 new messages']) // Run Notifications

        QTimer.singleShot(3000,self.Widget.Close)
        app.end('not')