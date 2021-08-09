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
from typing import Text

from libabr import Files, Control, Permissions, Colors, Process, Modules, Package, Commands, Res, System,App, Message

modules = Modules()
files = Files()
control = Control()
colors = Colors()
process = Process()
permissions = Permissions()
pack = Package()
commands = Commands()
res = Res()
sms = Message()
app = App()

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainApp (QWidget):

    def onCloseProcess (self):
        if not app.check('chat'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def lock (self):
        self.leSend.setEnabled(False)
        self.leSend.setText('Sending ...')
        QTimer.singleShot(1000,self.unlock)

    def unlock (self):
        self.leSend.clear()
        self.leSend.setEnabled(True)

    def SendMessage (self):
        sms.send (self.External[0],self.leSend.text())
        self.txtChat.append(f'<p style="text-align: left">Me: {self.leSend.text()}</p>')
        self.lock()

        self.refresh()

    def refresh (self):
        sms.recive()

        messages = files.readall (f'/app/messages/{self.External[0]}/'+max(files.list (f'/app/messages/{self.External[0]}')))
        self.txtChat.append(f'<p style="text-align: right">{self.External[0]}: {messages}</p>')

        #for i in files.list (f'/app/messages/{self.External[0]}'): files.remove (f'/app/messages/{self.External[0]}/{i}')
        #QTimer.singleShot(100,self.refresh)

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.Widget.SetWindowTitle ('Chat')

        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.onCloseProcess()
        #self.refresh()

        try:
            self.giver = self.External[0]

            self.lay = QVBoxLayout()
            self.setLayout(self.lay)

            self.txtChat = QTextBrowser()
            self.txtChat.setFont(self.Env.font())
            self.lay.addWidget(self.txtChat)

            self.leSend = QLineEdit()
            self.leSend.setFixedHeight(50)
            self.leSend.setFont(self.Env.font())
            self.leSend.setStyleSheet('padding-left: 5%;padding-right: 5%')
            self.leSend.returnPressed.connect (self.SendMessage)
            self.leSend.setPlaceholderText(f"Type a message")
            self.Widget.SetWindowTitle (f"Message to {self.External[0]}")
            self.lay.addWidget(self.leSend)
        except:
            self.Widget.Close()
            app.end ('chat')