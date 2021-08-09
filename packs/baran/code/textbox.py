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

import sys, os
from libabr import Files, Colors, Control, Res, App
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

files = Files()
colors = Colors()
control = Control()
res = Res()
app = App()
def getdata (name):
    return control.read_record (name,'/etc/gui')
class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check('text'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)
    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.Appname = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('text',"logo"))))
        ## Finds ##

        if self.Env.width()>1000 and self.Env.height()>720:
            self.Widget.Resize(self, int(self.Env.width() / 3), 100)
        else:
            self.Widget.Resize(self, int(self.Env.width()/1.5 ), 100)

        self.lblText = QLabel()
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.lblText.resize(int(self.Env.width() / 3), 50)
        else:
            self.lblText.resize(int(self.Env.width()/1.5),50)

        self.lblText.setFont(self.Env.font())
        self.lblText.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.layout().addWidget(self.lblText)

        if self.External[0]=='' or self.External[0]==None:
            self.Widget.SetWindowTitle (res.get('@string/title'))
        elif self.External[1]=='' or self.External[1]==None:
            self.lblText.setText(res.get('@string/text'))
        elif (self.External[1]=='' or self.External[1]==None) and (self.External[0]=='' or self.External[0]==None):
            self.Widget.SetWindowTitle(res.get('@string/title'))
            self.lblText.setText(res.get('@string/text'))
        else:
            self.lblText.setText(self.External[1])
            self.Widget.SetWindowTitle (self.External[0])

        self.btnOK = QPushButton()
        self.btnOK.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnOK.clicked.connect (self.ok_)
        self.btnOK.setFont(self.Env.font())
        self.btnOK.setText(res.get('@string/ok'))
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnOK.setGeometry(0, 50, int(self.Env.width())/3, 50)
        else:
            self.btnOK.setGeometry(0,50,int(self.Env.width()/1.5),50)
        self.layout().addWidget(self.btnOK)

    def ok_ (self):
        self.Widget.Close()