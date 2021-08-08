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

import sys , os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from libabr import Files, Control, System, Res, Commands, Permissions, App

res = Res()
files = Files()
control = Control()
commands = Commands()
permissions = Permissions()
app = App()
commands = Commands()
import baran

## Get data ##
def getdata (name):
    return control.read_record (name,'/etc/gui')

class LineEdit (baran.BLineEdit):
    def __init__(self,ports):
        super(LineEdit, self).__init__()
        self.Env = ports[1]
        self.setFont(self.Env.font())

class MainApp (QtWidgets.QWidget):
    def onCloseProcess(self):

        if not app.check('connectcloud'):
            self.Widget.Close()
        else:
            QtCore.QTimer.singleShot(1, self.onCloseProcess)

    def __init__(self,args):
        super().__init__()

        self.Env = args[1]
        self.Widget = args[2]
        self.onCloseProcess()

        self.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('connectcloud','logo'))))

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.leHost = LineEdit(args)
        self.leHost.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.lePassword = LineEdit(args)
        self.lePassword.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.leCheck = LineEdit(args)
        self.leCheck.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.leList = LineEdit(args)
        self.leList.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.leDownload = LineEdit(args)
        self.leDownload.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.leUpload = LineEdit(args)
        self.leUpload.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.leRemove = LineEdit(args)
        self.leRemove.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.leDirectory = LineEdit(args)
        self.leDirectory.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.leValue = LineEdit(args)
        self.leValue.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
    

        self.vbox.addWidget(self.leHost)
        self.vbox.addWidget(self.lePassword)
        self.vbox.addWidget(self.leCheck)
        self.vbox.addWidget(self.leList)
        self.vbox.addWidget(self.leDownload)
        self.vbox.addWidget(self.leUpload)
        self.vbox.addWidget(self.leRemove)
        self.vbox.addWidget(self.leDirectory)
        self.vbox.addWidget(self.leValue)


        self.leHost.setPlaceholderText (res.get('@string/host'))
        self.lePassword.setEchoMode (QLineEdit.Password)
        self.lePassword.setPlaceholderText (res.get('@string/password'))
        self.leCheck.setText ("index.php")
        self.leCheck.setPlaceholderText (res.get('@string/check'))
        self.leList.setText ("list.php")
        self.leList.setPlaceholderText (res.get('@string/list'))
        self.leDownload.setText ("download.php")
        self.leDownload.setPlaceholderText (res.get('@string/download'))
        self.leUpload.setText ("upload.php")
        self.leUpload.setPlaceholderText (res.get('@string/upload'))
        self.leRemove.setText ("remove.php")
        self.leRemove.setPlaceholderText (res.get('@string/remove'))
        self.leDirectory.setText ("directory.php")
        self.leDirectory.setPlaceholderText (res.get('@string/dir'))
        self.leValue.setPlaceholderText (res.get('@string/value'))

        self.btnConnect = QPushButton()
        self.btnConnect.setFont(self.Env.font())
        self.btnConnect.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-right: 5%;padding-left: 5%')
        self.btnConnect.setText(res.get('@string/add'))
        self.vbox.addWidget(self.btnConnect)
        self.btnConnect.clicked.connect (self.connect_)

    def connect_(self):

        listed = files.list('/dev')
        if listed==[]:
            maxed = 0
        else:
            maxed = int(max(listed).replace ('ic',''))+1

        files.create(f'/dev/ic{str(maxed)}')
        control.write_record('host',self.leHost.text(),f'/dev/ic{str(maxed)}')
        control.write_record('password',self.lePassword.text(),f'/dev/ic{str(maxed)}')
        control.write_record('index',self.leCheck.text(),f'/dev/ic{str(maxed)}')
        control.write_record('list',self.leList.text(),f'/dev/ic{str(maxed)}')
        control.write_record('download',self.leDownload.text(),f'/dev/ic{str(maxed)}')
        control.write_record('upload',self.leUpload.text(),f'/dev/ic{str(maxed)}')
        control.write_record('remove',self.leRemove.text(),f'/dev/ic{str(maxed)}')
        control.write_record('directory',self.leDirectory.text(),f'/dev/ic{str(maxed)}')
        control.write_record('value',self.leValue.text(),f'/dev/ic{str(maxed)}')

        try:
            commands.mount([f'ic{str(maxed)}'])
            self.Widget.Close()
            self.Env.RunApp('cloudroller', [None])
        except:
            files.remove(f'/dev/ic{str(maxed)}')
            self.Widget.Close()
            self.Env.RunApp('cloudroller', [None])
            app.switch('connectcloud')
            self.Env.RunApp('text',[res.get('@string/c'),res.get('@string/cm')])
            app.switch('connectcloud')