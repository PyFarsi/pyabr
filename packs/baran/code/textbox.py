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

class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check(self.AppName):
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
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('text',"logo"))))
        ## Finds ##

        if self.Env.width()>1000 and self.Env.height()>720:
            self.Widget.Resize(self, int(self.Env.width() / 3), 100)
        else:
            self.Widget.Resize(self, int(self.Env.width()/1.5 ), 100)

        self.lblText = QLabel()
        self.lblText.setStyleSheet('padding-left: 10%;padding-right: 10%;')
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.lblText.resize(int(self.Env.width() / 3), 50)
        else:
            self.lblText.resize(int(self.Env.width()/1.5),50)

        self.lblText.setFont(self.Env.font())
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