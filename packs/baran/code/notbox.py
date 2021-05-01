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

        self.onCloseProcess()
        self.Widget.Resize (self,int(getdata('alert.width')),int(getdata('alert.height')))
        self.Widget.DisableFloat()

        self.btnView = QToolButton()
        self.btnView.setText (self.External[2]) # External[0]
        self.Widget.SetWindowTitle(res.etc(self.External[0],'name['+getdata('locale')+"]"))
        #  External[1]
        self.btnView.clicked.connect (self.opener)
        self.setCentralWidget(self.btnView)

        self.Widget.SetWindowIcon (QIcon(res.get(res.etc(self.External[0],'logo'))))
        # self.Env.RunApp ('not',['gap',None,'100 new messages']) // Run Notifications