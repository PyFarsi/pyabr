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

import sys

from libabr import Files, Control, Permissions, Colors, Process, Modules, Package, Res, App

modules = Modules()
files = Files()
control = Control()
colors = Colors()
process = Process()
permissions = Permissions()
pack = Package()
res = Res()
app = App()

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
def getdata (name):
    return control.read_record (name,'/etc/gui')
class MainApp (QWidget):
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
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        self.Widget.setStyleSheet(f'background-color:{res.etc(self.AppName,"bgcolor")};')

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.Widget.Resize (self,int(res.etc(self.AppName,"width")),int(res.etc(self.AppName,"height")))

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        styles = '''
        QToolButton {
            background-color: {0};
            border-radius: {2}% {2}%;
        }
        QToolButton:hover {
            background-color: {1};
            border-radius: {2}% {2}%;
        }
        '''.replace("{0}",getdata("appw.body.bgcolor")).replace("{1}",res.etc(self.AppName,"btnhovercolor")).replace("{2}",res.etc(self.AppName,"btnround"))

        btnsize = int(res.etc(self.AppName,"btnsize"))
        self.btnEscape = QToolButton()
        self.btnEscape.setIconSize(QSize(btnsize,btnsize))
        self.btnEscape.setIcon(QIcon(res.get(res.etc(self.AppName,"escape-icon"))))
        self.btnEscape.setStyleSheet(styles)
        self.btnEscape.setFixedSize(btnsize,btnsize)
        self.btnEscape.clicked.connect (self.Env.escape_act)
        self.layout.addWidget(self.btnEscape)

        self.btnLock = QToolButton()
        self.btnLock.setFixedSize(btnsize, btnsize)
        self.btnLock.setIconSize(QSize(btnsize,btnsize))
        self.btnLock.setIcon(QIcon(res.get(res.etc(self.AppName,"lock-icon"))))
        self.btnLock.setStyleSheet(styles)
        self.btnLock.clicked.connect(self.Env.lock_act)
        self.layout.addWidget(self.btnLock)

        self.btnLogout = QToolButton()
        self.btnLogout.setFixedSize(btnsize, btnsize)
        self.btnLogout.setIconSize(QSize(btnsize,btnsize))
        self.btnLogout.setIcon(QIcon(res.get(res.etc(self.AppName,"logout-icon"))))
        self.btnLogout.setStyleSheet(styles)
        self.btnLogout.clicked.connect(self.Env.signout_act)
        self.layout.addWidget(self.btnLogout)

        self.btnRestart = QToolButton()
        self.btnRestart.setFixedSize(btnsize, btnsize)
        self.btnRestart.setIconSize(QSize(btnsize,btnsize))
        self.btnRestart.setIcon(QIcon(res.get(res.etc(self.AppName,"restart-icon"))))
        self.btnRestart.clicked.connect(self.Env.reboot_act)
        self.btnRestart.setStyleSheet(styles)
        self.layout.addWidget(self.btnRestart)

        self.btnSuspend = QToolButton()
        self.btnSuspend.setFixedSize(btnsize, btnsize)
        self.btnSuspend.setIconSize(QSize(btnsize,btnsize))
        self.btnSuspend.setIcon(QIcon(res.get(res.etc(self.AppName,"suspend-icon"))))
        self.btnSuspend.setStyleSheet(styles)
        self.btnSuspend.clicked.connect(self.Env.sleep_act)
        self.layout.addWidget(self.btnSuspend)

        self.btnSwitchuser = QToolButton()
        self.btnSwitchuser.setFixedSize(btnsize, btnsize)
        self.btnSwitchuser.setIconSize(QSize(btnsize,btnsize))
        self.btnSwitchuser.setIcon(QIcon(res.get(res.etc(self.AppName,"switchuser-icon"))))
        self.btnSwitchuser.setStyleSheet(styles)
        self.btnSwitchuser.clicked.connect(self.Env.switchuser_act)
        self.layout.addWidget(self.btnSwitchuser)