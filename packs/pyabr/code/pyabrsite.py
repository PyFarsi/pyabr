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
        System('/usr/app/wapp')  # Run CatBall Browser

    def onCloseProcess (self):
        if not app.check('gap'):
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

        files.write('/tmp/url.tmp','https://pyabr.ir')
        files.write('/tmp/wapp-logo.tmp','@icon/breeze-cloud')
        files.write('/tmp/wapp-title.tmp',res.get('@string/app_name'))
        files.write('/tmp/width.tmp', str(self.Env.width()))
        files.write('/tmp/height.tmp', str(self.Env.height()))
        self.onCloseProcess()

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.Widget.Resize(self,self.Env.width(),self.Env.height())

        self.Widget.hide()
        self.Widget.Close()

        QTimer.singleShot(1,self.Browser)