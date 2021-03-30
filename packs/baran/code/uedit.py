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

import sys, subprocess, os, shutil, requests

from libabr import Files, Control, Permissions, Colors, Process, Modules, Package, Commands, Res, System, App

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
from PyQt5 import uic

import baran

from PyQt5 import QtCore, QtGui, QtWidgets

def getdata(name):
    return control.read_record(name, '/etc/gui')

class LineEdit (baran.BLineEdit):
    def __init__(self,ports):
        super(LineEdit, self).__init__()
        self.Env = ports[1]

class MainApp(QWidget):

    def onCloseProcess(self):
        if not app.check('uedit'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1, self.onCloseProcess)

    def btnSave_act (self):
        # Get text #
        self.fullname = self.leFullname.text()
        self.company = self.leCompany.text()
        self.email = self.leEmail.text()
        self.gender = self.cbGender.currentText()
        self.bloodtype = self.cbBloodtype.currentText()
        self.birthday = self.leBirthday.text()

        # save it #
        control.write_record('fullname',self.fullname,self.user)
        control.write_record('company', self.company, self.user)
        control.write_record('email', self.email, self.user)
        control.write_record('gender', self.gender, self.user)
        control.write_record('blood_type', self.bloodtype, self.user)
        control.write_record('birthday', self.birthday, self.user)

        self.Widget.Close()

    def __init__(self, ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.user = f'/etc/users/{self.External[0]}'

        self.onCloseProcess()


        app.switch('users')

        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('uedit', "logo"))))
        self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.Widget.Resize(self, 720, 640)

        self.leFullname = LineEdit(ports)
        self.leCompany = LineEdit(ports)
        self.leEmail = LineEdit(ports)
        self.lePhone = LineEdit(ports)
        self.leBirthday = QDateEdit()
        self.cbGender = QComboBox()
        self.cbBloodtype = QComboBox()

        self.btnSave = QPushButton()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.leFullname)
        self.layout.addWidget(self.leCompany)
        self.layout.addWidget(self.leEmail)
        self.layout.addWidget(self.lePhone)
        self.layout.addWidget(self.leBirthday)
        self.layout.addWidget(self.cbGender)
        self.layout.addWidget(self.cbBloodtype)
        self.layout.addWidget(self.btnSave)

        self.leFullname.setPlaceholderText(res.get('@string/fullname'))
        self.leCompany.setPlaceholderText(res.get('@string/company'))
        self.leEmail.setPlaceholderText(res.get('@string/email'))
        self.lePhone.setPlaceholderText(res.get('@string/phone'))
        self.btnSave.setText(res.get('@string/save'))
        self.btnSave.setFont(self.Env.font())
        self.setLayout(self.layout)

        self.cbGender.addItem(res.get('@string/male'))
        self.cbGender.addItem(res.get('@string/female'))
        self.cbGender.setFont(self.Env.font())
        self.leBirthday.setFont(self.Env.font())

        self.cbBloodtype.addItem('O+')
        self.cbBloodtype.addItem('O-')
        self.cbBloodtype.addItem('A+')
        self.cbBloodtype.addItem('A-')
        self.cbBloodtype.addItem('B+')
        self.cbBloodtype.addItem('B-')
        self.cbBloodtype.addItem('AB+')
        self.cbBloodtype.addItem('AB-')

        self.btnSave.clicked.connect (self.btnSave_act)

        if not control.read_record('fullname',self.user)==None:
            self.leFullname.setText (control.read_record('fullname',self.user))
        if not control.read_record('company', self.user) == None:
            self.leCompany.setText(control.read_record('company', self.user))
        if not control.read_record('email', self.user) == None:
            self.leEmail.setText(control.read_record('email', self.user))
        if not control.read_record('phone', self.user) == None:
            self.lePhone.setText(control.read_record('phone', self.user))
        if not control.read_record('gender', self.user) == None:
            self.cbGender.setItemText(control.read_record('gender', self.user))
        if not control.read_record('blood_type', self.user) == None:
            self.cbBloodtype.setItemText(control.read_record('blood_type', self.user))
        if not control.read_record('birthday', self.user) == None:
            self.leBirthday.setText(control.read_record('birthday', self.user))

        self.Widget.Resize(self,336,383)
