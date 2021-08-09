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
        if not app.check('nama'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        app.switch('nama')

        self.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.Resize (self,int(self.Env.width()/0.8),int(self.Env.height()/0.8))
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('nama','logo'))))

        self.btnImage = QToolButton()
        self.btnImage.setStyleSheet('background-color: black;border:none;color: black;')
        self.setCentralWidget(self.btnImage)

        try:
            self.btnImage.setIcon(QIcon(files.input(self.External[0])))
            self.btnImage.setIconSize(QSize(self.Env.width(),self.Env.height()))
        except:
            pass

        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)
        self.menubar.setFont(self.Env.font())
        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)

        self.opena = self.menubar.addAction(res.get('@string/open'))
        self.opena.setFont(self.Env.font())
        self.opena.triggered.connect(self.open_act)
        self.opena.setShortcut ('Ctrl+O')

    def open_act(self):
        app.switch('nama')
        self.Env.RunApp('select', [res.get('@string/open'), 'open', self.open_act_])
        app.switch('nama')

    def open_act_(self, filename):
        self.btnImage.setIcon(QIcon(files.input(filename)))