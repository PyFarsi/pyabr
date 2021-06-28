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
        if not app.check('sudoprocess'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def perm_(self):
        self.Widget.hide()

        if self.Env.username == 'root':
            self.Widget.Close()

            try:
                files.write('/proc/info/sudo',self.External[0])
                self.Env.RunApp(self.External[0], [None])
            except:
                pass

        elif self.Env.username == 'guest':
            app.switch('sudoprocess')
            self.Env.RunApp ('text',[res.get('@string/pnot'),res.get('@string/pnotm')])
            app.switch('sudoprocess')
            commands.kill([self.External[0]])
        else:
            if self.Env.username in control.read_list('/etc/sudoers'):
                app.switch('sudoprocess')
                self.Env.RunApp('code',[res.get('@string/pass'),self.getpass_])
                app.switch('sudoprocess')
                control.write_record('input.password_hint', 'No', '/etc/configbox')
            else:
                app.switch('sudoprocess')
                self.Env.RunApp('text', [res.get('@string/pnot'), res.get('@string/pnotm')])
                app.switch('sudoprocess')
                commands.kill([self.External[0]])

    def getpass_(self,password):
        if self.Env.password == password:
            self.Widget.Close()

            try:
                files.write('/proc/info/sudo', self.External[0])
                self.Env.RunApp (self.External[0],[None])
            except:
                pass
        else:
            app.switch('sudoprocess')
            self.Env.RunApp('text', [res.get('@string/pnot'), res.get('@string/wrongp')])
            app.switch('sudoprocess')

            commands.kill([self.External[0]])

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        control.write_record('input.password_hint', 'Yes', '/etc/configbox')

        self.onCloseProcess()

        app.switch('sudoprocess')

        self.Widget.Resize (self,int(self.Env.width()/0.8),int(self.Env.height()/0.8))
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('sudoprocess','logo'))))

        QTimer.singleShot(1,self.perm_)