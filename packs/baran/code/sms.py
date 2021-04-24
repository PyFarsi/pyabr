#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

import sys, os, baran
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

class LineEdit(baran.BLineEdit):
    def __init__(self,ports):
        super(LineEdit, self).__init__()

        self.Env = ports[1]

class MainApp (QMainWindow):

    def onCloseProcess (self):
        if not app.check('sms'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def sendMessage (self):

        if not self.leSend.text()=='':
            self.txtChat.append(f'<p><strong>Me: </strong>{self.leSend.text()}</p>')
            self.leSend.clear()

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.Appname = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        # sender, giver #
        self.txtChat = QTextBrowser()
        self.leSend = LineEdit(ports)

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('sms','logo'))))
        self.Widget.Resize (self,1000,600)

        self.layout().addWidget (self.txtChat)
        self.layout().addWidget (self.leSend)

        self.txtChat.setGeometry(0,0,1000,550)
        self.leSend.setGeometry(0,550,1000,50)

        self.leSend.returnPressed.connect (self.sendMessage)

        self.leSend.setPlaceholderText(res.get('@string/enter'))
        self.leSend.setStyleSheet('padding-left: 10%;padding-right: 10%;')