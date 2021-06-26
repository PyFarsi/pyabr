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
        if not app.check('nama'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        app.switch('nama')

        self.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.Resize (self,int(self.Env.width()/0.8),int(self.Env.height()/0.8))
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('nama','logo'))))

        self.btnImage = QToolButton()
        self.btnImage.setStyleSheet('background-color: black;border:none;color: black;')
        self.setCentralWidget(self.btnImage)

        try:
            self.btnImage.setIcon(QIcon(files.input(self.External[0])))
            self.btnImage.setIconSize(QSize(self.Env.width(),self.Env.height()))
        except:
            pass

        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)
        self.menubar.setFont(self.Env.font())
        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)

        self.opena = self.menubar.addAction(res.get('@string/open'))
        self.opena.setFont(self.Env.font())
        self.opena.triggered.connect(self.open_act)
        self.opena.setShortcut ('Ctrl+O')

    def open_act(self):
        app.switch('nama')
        self.Env.RunApp('select', [res.get('@string/open'), 'open', self.open_act_])
        app.switch('nama')

    def open_act_(self, filename):
        self.btnImage.setIcon(QIcon(files.input(filename)))