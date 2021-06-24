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

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, importlib, baran
from libabr import Files, Res, App, Control, Commands
files = Files()
res = Res()
app = App()
commands = Commands()
control = Control()
def getdata (value):
    return control.read_record(value,'/etc/gui')
class MainApp(baran.BLineEdit):

    def onCloseProcess (self):
        if not app.check(self.AppName):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def correct (self):
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        app.switch('runapp')
        self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.setEnabled(True)
        self.clear()

    def RunApp (self):
        command = self.text().split(' ')

        ## Desktop based applications ##
        if app.exists(command[0]):
            try:
                self.Env.RunApp(command[0],command[1:])
            except:
                commands.start([command[0]])

            app.switch('runapp')
            self.setEnabled(False)

        elif command[0].startswith ('http://') or command[0].startswith ('https://'):
            self.Env.RunApp('wapp',[command[0]])

        elif command[0].startswith ('abr://'):
            commands.cl([command[0]])

        ## Command based application ##
        elif hasattr(commands,command[0]):
            app.switch('runapp')
            getattr(commands,command[0])(command[1:])
            app.switch('runapp')

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

        self.onCloseProcess()


        if not self.External==None:
            if not self.External==[]:
                if not self.External[0]==None:
                    self.Widget.Close()
                    desk = files.filename(self.External[0]).replace('.desk', '')
                    if files.parentdir(self.External[0]).__contains__('/usr/share/applications'):
                        self.Env.RunApp(desk,None)
                    else:
                        files.copy(self.External[0],f'/usr/share/applications/{desk}.desk')
                        self.Env.RunApp(desk,None)

        ## Widget configs ##
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.Widget.Resize (self,int(res.etc(self.AppName,"width")),int(res.etc(self.AppName,"height")))
        self.returnPressed.connect(self.RunApp)  # https://pythonbasics.org/pyqt/ learn it
        self.setFont(self.Env.font())