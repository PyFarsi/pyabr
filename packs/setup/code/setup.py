'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, Apt, Dpkg, PyPI
    * License:          GNU General Publice License v3.0

    * Source code:      https://github.com/PyFarsi/pyabr
    * PyPI:             https://pypi.org/project/pyabr

    - Download Pyabr OS

    * AMD64, Intel64:   https://dl.pyabr.ir/pyabr-x86_64.iso     
    * ARM64:            https://dl.pyabr.ir/pyabr-arm64.img
    * Platform:         https://dl.pyabr.ir/stor.sb
    * Wheel Package:    https://dl.pyabr.ir/pyabr.whl
    
    - Channels:

    * Official Website: https://pyabr.ir
    * Telegram Channel: https://t.me/pyfarsi
    * Gap Channel:      https://gap.im/pyabr
    * Sorosh Channel:   https://splus.ir/pyabr
    * Instagram:        https://instagram.com/pyabrir
    * Hoorsa:           https://hoorsa.com/pyabr
    * Aparat:           https://aparat.com/pyabr

'''


from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from PyQt5.QtGui import *
import platform
import hashlib, shutil, os, sys,subprocess
from PyQt5 import QtDesigner

from libabr import *

res = Res()
commands = Commands()
files = Files()
control = Control()

def getdata (value):
    return control.read_record(value,'/etc/gui')

class MainApp(QtWidgets.QWizard):
    def Finish(self):
        ## Get all configure information ##
        if not (
                self.leHostname.text() == None and
                self.leRootCode.text() == None and
                self.leConfirmRootCode.text() == None and
                self.leUsername.text() == None and
                self.lePassword.text() == None and
                self.leConfirmPassword.text() == None and
                self.leFirstName.text() == None and
                self.leEmail.text() == None and
                self.lePhone.text() == None and
                self.cmLang.currentText() == None and
                self.cmClock.currentText() == None
        ):
            self.Env.RunApp ('lang',[None])

            if self.chGuest.isChecked():
                guest = 'Yes'
            else:
                guest = 'No'

            if self.cmLang.currentText()=='English':
                locale = 'en'
            elif self.cmLang.currentText()=='فارسی':
                locale = 'fa'
            else:
                locale = 'en'

            try:
                subprocess.call('rm -rf /etc/localtime', shell=True)
                subprocess.call(f'ln -s /usr/share/zoneinfo/{self.cmClock.currentText()} /etc/localtime', shell=True)
                f = open('/etc/sysconfig/clock', 'w')
                f.write(f'''ZONE="{self.cmClock.currentText()}"
UTC=false
ARC=false''')
                f.close()
                subprocess.call('hwclock --systohc --localtime', shell=True)
            except:
                pass

            ## Setting GUI Table ##

            open('/stor/etc/suapp', 'w')

            ## Setting up hostname ##
            file = open("/stor/etc/hostname", "w")
            file.write(self.leHostname.text())
            file.close()

            file = open('/stor/etc/hosts','w')
            file.write(f'''127.0.0.1   localhost
127.0.1.1   {self.leHostname.text()}

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters''')
            file.close()

            ## Setting up Root user ##
            file = open("/stor/etc/users/root", "w")
            file.write(f"code: {hashlib.sha3_512(self.leRootCode.text().encode()).hexdigest()}\n")
            file.write('fullname: Super Account')
            file.close()

            ## Setting up Standard user ##
            file = open(f"/stor/etc/users/{self.leUsername.text()}", "w")
            file.write(f"code: {hashlib.sha3_512((self.lePassword.text()).encode()).hexdigest()}\n")
            file.write(f"fullname: {self.leFirstName.text()}\n")
            file.write(f"email: {self.leEmail.text()}\n")
            file.write(f"phone: {self.lePhone.text()}\n")
            file.close()

            # permit #
            control.write_record(f'/desk/{ self.leUsername.text()}', f'drwxr-x---/{ self.leUsername.text()}',
                                 '/stor/etc/permtab')

            # sudoers #
            f = open('/stor/etc/sudoers', 'w')
            f.write(f'{self.leUsername.text()}\n')
            f.close()

            ## Setting up Guest user ##
            file = open("/stor/etc/guest", "w")
            if guest == "No":
                file.write("enable_cli: No\nenable_gui: No\n")
            elif guest == "Yes":
                file.write("enable_cli: Yes\nenable_gui: Yes\n")
            else:
                file.write("enable_cli: No\nenable_gui: No\n")
            file.close()

            f = open('/stor/etc/gui','w')
            f.write(files.readall('/etc/gui').replace('locale: fa',f'locale: {locale}'))
            f.close()

            os.system('mkdir -p /stor/proc/info')
            if os.path.isfile ('/stor/proc/0'):
                os.system('rm /stor/proc/0')

            if os.path.isdir('/build-packs'):
                os.system('reboot')

    def __init__(self,ports):
        super(MainApp, self).__init__()


        self.Env = ports[1]
        self.Widget = ports[2]

        uic.loadUi(res.get('@layout/setup'), self)

        ## Finds ##
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};')
        self.lblLang = self.findChild(QtWidgets.QLabel,'lblLang')
        self.lblLang.setFont(self.Env.font())

        self.widget = self.findChild(QtWidgets.QWidget,'widget')
        self.widget.setStyleSheet(f'background-image: url({res.get("@image/setup")})')

        self.leHostname = self.findChild(QtWidgets.QLineEdit, 'leHostname')
        self.leHostname.setFont(self.Env.font())
        self.leHostname.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leRootCode = self.findChild(QtWidgets.QLineEdit, 'leRootCode')
        self.leRootCode.setFont(self.Env.font())
        self.leRootCode.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leUsername = self.findChild(QtWidgets.QLineEdit, 'leUsername')
        self.leUsername.setFont(self.Env.font())
        self.leUsername.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.lePassword = self.findChild(QtWidgets.QLineEdit, 'lePassword')
        self.lePassword.setFont(self.Env.font())
        self.lePassword.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')

        self.chGuest = self.findChild(QtWidgets.QCheckBox, 'chGuest')
        self.chGuest.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')

        self.chGuest.setFont(self.Env.font())
        self.cmLang = self.findChild(QtWidgets.QComboBox, 'cmLang')
        self.cmLang.setFont(self.Env.font())
        self.cmClock = self.findChild(QtWidgets.QComboBox,'comboBox')
        self.cmClock.setFont(self.Env.font())
        self.leFirstName = self.findChild(QtWidgets.QLineEdit, 'leFirstName')
        self.leFirstName.setFont(self.Env.font())
        self.leFirstName.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leEmail = self.findChild(QtWidgets.QLineEdit, 'leEmail')
        self.leEmail.setFont(self.Env.font())
        self.leEmail.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.lePhone = self.findChild(QtWidgets.QLineEdit, 'lePhone')
        self.lePhone.setFont(self.Env.font())
        self.lePhone.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')

        self.button(QtWidgets.QWizard.FinishButton).clicked.connect(self.Finish)
        self.button(QtWidgets.QWizard.FinishButton).setFont(self.Env.font())
        self.button(QtWidgets.QWizard.FinishButton).setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.button(QtWidgets.QWizard.FinishButton).setMinimumSize(100,40)
        self.button(QtWidgets.QWizard.FinishButton).setText(res.get('@string/install'))

        self.button(QtWidgets.QWizard.NextButton).setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.button(QtWidgets.QWizard.NextButton).setMinimumSize(100,40)
        self.button(QtWidgets.QWizard.NextButton).setFont(self.Env.font())
        self.button(QtWidgets.QWizard.NextButton).setText(res.get('@string/next'))

        self.button(QtWidgets.QWizard.CancelButton).setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.button(QtWidgets.QWizard.CancelButton).setMinimumSize(100,40)
        self.button(QtWidgets.QWizard.CancelButton).clicked.connect (self.Discard)
        self.button(QtWidgets.QWizard.CancelButton).setFont(self.Env.font())
        self.button(QtWidgets.QWizard.CancelButton).setText(res.get('@string/cancel'))

        self.button(QtWidgets.QWizard.BackButton).setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.button(QtWidgets.QWizard.BackButton).setMinimumSize(100,40)
        self.button(QtWidgets.QWizard.BackButton).setFont(self.Env.font())
        self.button(QtWidgets.QWizard.BackButton).setText(res.get('@string/back'))

        self.Widget.Resize (self,616,465)
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QtGui.QIcon(res.get("@icon/setup")))

        self.leHostname.setPlaceholderText (res.get('@string/hostname'))
        self.leRootCode.setPlaceholderText (res.get('@string/rootcode'))
        self.leUsername.setPlaceholderText(res.get('@string/username'))
        self.lePassword.setPlaceholderText(res.get('@string/password'))
        self.leFirstName.setPlaceholderText(res.get('@string/fullname'))
        self.lePhone.setPlaceholderText(res.get('@string/phone'))
        self.leEmail.setPlaceholderText(res.get('@string/email'))
        self.chGuest.setText(res.get('@string/guest'))
        self.lblLang.setText(res.get('@string/lang'))
        self.lblLang_2 = self.findChild(QtWidgets.QLabel,'lblLang_2')
        self.lblLang_2.setText (res.get('@string/cap'))
        self.lblLang_2.setFont(self.Env.font())
        self.cmClock.setCurrentText('Asia/Tehran')

        ## Browse button click ##
        ## Show setup ##
    def Discard (self):
        self.Env.escape_act()