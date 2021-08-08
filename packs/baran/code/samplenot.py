#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		https://pyabr.ir
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

import sys, os
from libabr import Files, Colors, Control, Res, Commands, App
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

files = Files()
colors = Colors()
control = Control()
res = Res()
app = App()
commands = Commands()
def getdata (name):
    return control.read_record (name,'/etc/gui')

# select box #
class MainApp (QMainWindow):

    def onCloseProcess (self):
        if not app.check('samplenot'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def push_(self):
        self.Widget.Close()
        files.create('/tmp/pushnot')
        self.Env.RunApp ('not',['gap',None,'100 New messages'])

    def __init__(self, ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        QTimer.singleShot(100,self.push_)

