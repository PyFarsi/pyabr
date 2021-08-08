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

import sys, subprocess, os, shutil, requests,hashlib

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
        self.user = f'/etc/users/{self.leUsername.text()}'
        if self.s=='add':
            files.mkdir(f'/desk/{self.leUsername.text()}')
            files.create(self.user)
            control.write_record('username', hashlib.sha3_256(self.leUsername.text().encode()).hexdigest(), self.user)

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

        if self.leConfirm.text()==self.lePassword.text():
            control.write_record('code',hashlib.sha3_512(self.lePassword.text().encode()).hexdigest(),self.user)

        if self.cbtype.currentText()==res.get('@string/admin'):
            files.append('/etc/sudoers',f'{self.leUsername.text()}\n')
        else:
            files.write('/etc/sudoers',files.readall('/etc/sudoers').replace(f"{self.leUsername.text()}\n",''))

        self.Widget.Close()

        if self.s=='add':
            self.Env.RunApp ('users',[None])

    def __init__(self, ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.user = f'/etc/users/{self.External[0]}'

        self.onCloseProcess()

        try:
            s = files.readall('/tmp/user-status.tmp')
            self.s = s
            files.remove('/tmp/user-status.tmp')
        except:
            self.s = 'edit'
            s = 'edit'

        app.switch('uedit')

        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('uedit', "logo"))))
        if s=='add':
            self.Widget.SetWindowTitle(res.get('@string/add'))
        else:
            self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.Widget.Resize(self, 720, 700)

        self.leUsername = LineEdit(ports)
        self.leUsername.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.lePassword = LineEdit(ports)
        self.lePassword.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leConfirm = LineEdit(ports)
        self.leConfirm.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leFullname = LineEdit(ports)
        self.leFullname.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leCompany = LineEdit(ports)
        self.leCompany.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leEmail = LineEdit(ports)
        self.leEmail.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.lePhone = LineEdit(ports)
        self.lePhone.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leBirthday = QDateEdit()
        self.leBirthday.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.cbGender = QComboBox()
        self.cbGender.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.cbBloodtype = QComboBox()
        self.cbBloodtype.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.cbtype = QComboBox()
        self.cbtype.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')

        self.btnSave = QPushButton()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.leUsername)
        self.layout.addWidget(self.lePassword)
        self.layout.addWidget(self.leConfirm)
        self.layout.addWidget(self.leFullname)
        self.layout.addWidget(self.leCompany)
        self.layout.addWidget(self.leEmail)
        self.layout.addWidget(self.lePhone)
        self.layout.addWidget(self.leBirthday)
        self.layout.addWidget(self.cbGender)
        self.layout.addWidget(self.cbBloodtype)
        self.layout.addWidget(self.cbtype)
        self.layout.addWidget(self.btnSave)

        self.leUsername.setPlaceholderText(res.get('@string/username'))
        self.lePassword.setPlaceholderText(res.get('@string/password'))
        self.leConfirm.setPlaceholderText(res.get('@string/confirm'))

        if not s=='add':
            self.leUsername.setText(self.External[0])
            self.leUsername.setEnabled(False)

        self.lePassword.setEchoMode(QLineEdit.Password)
        self.leConfirm.setEchoMode(QLineEdit.Password)

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

        self.cbtype.addItem(res.get('@string/admin'))
        self.cbtype.addItem(res.get('@string/low'))

        if s=='edit':
            if not control.read_record('fullname', self.user) == None:
                self.leFullname.setText(control.read_record('fullname', self.user))
            if not control.read_record('company', self.user) == None:
                self.leCompany.setText(control.read_record('company', self.user))
            if not control.read_record('email', self.user) == None:
                self.leEmail.setText(control.read_record('email', self.user))
            if not control.read_record('phone', self.user) == None:
                self.lePhone.setText(control.read_record('phone', self.user))
            if not control.read_record('gender', self.user) == None:
                self.cbGender.setCurrentText(control.read_record('gender', self.user))
            if not control.read_record('blood_type', self.user) == None:
                self.cbBloodtype.setCurrentText(control.read_record('blood_type', self.user))
            if self.leUsername.text() == 'root' or self.leUsername.text() in control.read_list('/etc/sudoers'):
                self.cbtype.setCurrentText(res.get('@string/admin'))
                if self.leUsername.text() == 'root':
                    self.cbtype.setEnabled(False)
            else:
                self.cbtype.setCurrentText(res.get('@string/low'))
            if not control.read_record('birthday', self.user) == None:
                x = control.read_record('birthday', self.user)
                x = x.split('-')
                y = int(x[0])
                m = int(x[1])
                d = int(x[2])
                s = QDate()
                s.setDate(y, m, d)

                self.leBirthday.setDate(s)

        self.btnSave.clicked.connect (self.btnSave_act)
        self.btnSave.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.Resize(self,336,383)