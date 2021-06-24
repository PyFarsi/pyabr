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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import os
import sys, subprocess

from libabr import Res, Control, Files, App

res = Res()
control = Control()
files = Files()
app = App()
def getdata (name):
    return control.read_record (name,'/etc/gui')
class MainApp(QWidget):
    def onCloseProcess (self):
        if not app.check('screen'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,ports, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)
        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.Widget.Resize(self,560,200)

        self.cmBox = QComboBox()
        self.cmBox.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.cmBox.addItem('800x600')
        self.cmBox.addItem('2560x1600')
        self.cmBox.addItem('1920x1440')
        self.cmBox.addItem('1856x1392')
        self.cmBox.addItem('1792x1344')
        self.cmBox.addItem('1920x1200')
        self.cmBox.addItem('1600x1200')
        self.cmBox.addItem('1680x1050')
        self.cmBox.addItem('1400x1050')
        self.cmBox.addItem('1280x1024')
        self.cmBox.addItem('1440x900')
        self.cmBox.addItem('1280x960')
        self.cmBox.addItem('1360x768')
        self.cmBox.addItem('1152x864')
        self.cmBox.addItem('1280x768')
        self.cmBox.addItem('1024x768')
        self.cmBox.addItem('640x460')

        self.btnSet = QPushButton (res.get('@string/savec'))
        self.btnSet.clicked.connect (self.act_Set)
        self.btnSet.setFont(self.Env.font())
        self.btnSet.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.cmBox)
        self.vbox.addWidget(self.btnSet)
        self.setLayout(self.vbox)

    def act_Set (self):
        files.write('/proc/info/scn',self.cmBox.currentText())
        split = self.cmBox.currentText().split("x")
        width = split[0]
        height = split[1]
        control.write_record('autosize','No','/etc/gui')
        control.write_record('width',width,'/etc/gui')
        control.write_record('height',height,'/etc/gui')
        app.switch('screen')
        self.Env.RunApp('bool', [res.get('@string/savec'), res.get('@string/reboot'), self.reboot_act_])
        app.switch('screen')

    def reboot_act_(self,yes):
        if yes:
            self.Env.reboot_act()