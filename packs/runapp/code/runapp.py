#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, importlib
from libabr import Files, Res, App, Control
files = Files()
res = Res()
app = App()
control = Control()

class MainApp(QLineEdit):
    def correct (self):
        self.setStyleSheet(f'background-color: {res.etc(self.AppName,"bgcolor")};color: {res.etc(self.AppName,"fgcolor")};')
        app.switch('runapp')
        self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.setEnabled(True)
        self.clear()

    def RunApp (self):
        command = self.text().split(' ')
        if app.exists(command[0]):
            self.Env.RunApp(command[0],command[1:])
            app.switch('runapp')
            self.setEnabled(False)
            QTimer.singleShot(1000, self.correct)
        else:
            app.switch('runapp')
            self.Env.RunApp('text', [res.get('@string/not_found'), res.get('@string/not_found_msg').replace('{0}',command[0])])
            app.switch('runapp')
            QTimer.singleShot(1000, self.correct)

    def __init__(self,args):
        super(MainApp, self).__init__()

        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

        ## Widget configs ##
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.setStyleSheet(f'background-color: {res.etc(self.AppName,"bgcolor")};color: {res.etc(self.AppName,"fgcolor")};')
        self.Widget.Resize (self,int(res.etc(self.AppName,"width")),int(res.etc(self.AppName,"height")))
        self.returnPressed.connect(self.RunApp)  # https://pythonbasics.org/pyqt/ learn it
        self.setFont(self.Env.font())