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