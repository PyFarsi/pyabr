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

import sys , os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from libabr import Files, Control, System, Res, Commands, Permissions, App

res = Res()
files = Files()
control = Control()
commands = Commands()
permissions = Permissions()
app = App()
commands = Commands()
import baran

## Get data ##
def getdata (name):
    return control.read_record (name,'/etc/gui')

class LineEdit (baran.BLineEdit):
    def __init__(self,ports):
        super(LineEdit, self).__init__()
        self.Env = ports[1]
        self.setFont(self.Env.font())

class MainApp (QtWidgets.QWidget):
    def onCloseProcess(self):

        if not app.check('connectcloud'):
            self.Widget.Close()
        else:
            QtCore.QTimer.singleShot(1, self.onCloseProcess)

    def __init__(self,args):
        super().__init__()

        self.Env = args[1]
        self.Widget = args[2]
        self.onCloseProcess()

        self.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('connectcloud','logo'))))

        self.Widget.Resize (self,600,200)

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.leHost = LineEdit(args)
        self.leHost.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.lePassword = LineEdit(args)
        self.lePassword.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.leValue = LineEdit(args)
        self.leValue.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
    

        self.vbox.addWidget(self.leHost)
        self.vbox.addWidget(self.lePassword)
        self.vbox.addWidget(self.leValue)


        self.leHost.setPlaceholderText (res.get('@string/host'))
        self.lePassword.setEchoMode (QLineEdit.Password)
        self.lePassword.setPlaceholderText (res.get('@string/password'))
        self.leValue.setPlaceholderText (res.get('@string/value'))

        self.btnConnect = QPushButton()
        self.btnConnect.setFont(self.Env.font())
        self.btnConnect.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.btnConnect.setText(res.get('@string/add'))
        self.vbox.addWidget(self.btnConnect)
        self.btnConnect.clicked.connect (self.connect_)

    def connect_(self):

        listed = files.list('/dev')
        if listed==[]:
            maxed = 0
        else:
            maxed = int(max(listed).replace ('ic',''))+1

        files.create(f'/dev/ic{str(maxed)}')
        control.write_record('host',self.leHost.text(),f'/dev/ic{str(maxed)}')
        control.write_record('password',self.lePassword.text(),f'/dev/ic{str(maxed)}')
        control.write_record('value',self.leValue.text(),f'/dev/ic{str(maxed)}')

        try:
            commands.mount([f'ic{str(maxed)}'])
            self.Widget.Close()
            self.Env.RunApp('cloudroller', [None])
        except:
            files.remove(f'/dev/ic{str(maxed)}')
            self.Widget.Close()
            self.Env.RunApp('cloudroller', [None])
            app.switch('connectcloud')
            self.Env.RunApp('text',[res.get('@string/c'),res.get('@string/cm')])
            app.switch('connectcloud')