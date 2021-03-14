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

class LineEdit (baran.BLineEdit):
    def __init__(self,ports):
        super(LineEdit, self).__init__()
        self.Env = ports[1]

# input box #
class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check('input'):
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

        self.setStyleSheet('background-color: white;')
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('input',"logo"))))
        ## Finds ##
        self.leInput = LineEdit(ports)
        self.leInput.setFont(self.Env.font())

        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.Widget.Resize(self,int(self.Env.width()/3),100)
            self.leInput.resize(int(self.Env.width()/3),50)
        else:
            self.Widget.Resize(self, int(self.Env.width() / 1.5), 100)
            self.leInput.resize(int(self.Env.width() / 1.5), 50)

        self.layout().addWidget(self.leInput)
        self.leInput.returnPressed.connect (self.inp)
        password_hint = control.read_record ('input.password_hint','/etc/configbox')
        if password_hint=='Yes':
            self.leInput.setEchoMode(QLineEdit.Password)

        if self.External[0]=='' or self.External[0]==None:
            self.Widget.SetWindowTitle (res.get('@string/title'))
        else:
            self.Widget.SetWindowTitle (self.External[0])

        self.btnCancel = QPushButton()
        self.btnCancel.setText(res.get('@string/cancel'))
        self.btnCancel.setFont(self.Env.font())
        self.btnCancel.clicked.connect(self.Widget.Close)
        self.layout().addWidget(self.btnCancel)

        self.btnOK = QPushButton()
        self.btnOK.setFont(self.Env.font())
        self.btnOK.clicked.connect (self.inp)
        self.btnOK.setText(res.get('@string/ok'))
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnOK.setGeometry(int(self.Env.width() / 6), 50, int(self.Env.width() / 6), 50)
            self.btnCancel.setGeometry(0, 50, int(self.Env.width() / 6), 50)
        else:
            self.btnOK.setGeometry(int(self.Env.width() / 3), 50, int(self.Env.width() / 3), 50)
            self.btnCancel.setGeometry(0, 50, int(self.Env.width() / 3), 50)
        self.layout().addWidget(self.btnOK)

        self.Widget.DisableFloat()

    def inp(self):
        inputx = self.leInput.text()
        self.External[1](inputx)
        self.Widget.Close()