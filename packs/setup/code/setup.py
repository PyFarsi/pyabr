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


from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from PyQt5.QtGui import *
import platform
import hashlib, shutil, os, sys

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
                self.cmLang.currentText() == None
        ):
            self.Env.RunApp ('lang',[None])

            hostname = self.leHostname.text()
            rootcode = self.leRootCode.text()
            username = self.leUsername.text()
            password = self.lePassword.text()
            first_name = self.leFirstName.text()
            email = self.leEmail.text()
            phone = self.lePhone.text()
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

            ## Setting GUI Table ##

            open('/stor/etc/suapp', 'w')

            ## Setting up hostname ##
            file = open("/stor/etc/hostname", "w")
            file.write(hostname)
            file.close()

            ## Setting up Root user ##
            file = open("/stor/etc/users/root", "w")
            file.write("username: " + hashlib.sha3_256("root".encode()).hexdigest() + "\n")
            file.write("code: " + hashlib.sha3_512(rootcode.encode()).hexdigest() + "\n")
            file.write('fullname: Super Account')
            file.close()

            ## Setting up Standard user ##
            file = open("/stor/etc/users/" + username, "w")
            file.write("username: " + hashlib.sha3_256(username.encode()).hexdigest() + "\n")
            file.write("code: " + hashlib.sha3_512(password.encode()).hexdigest() + "\n")
            file.write("fullname: " + first_name + "\n")
            file.write("email: " + email + "\n")
            file.write("phone: " + phone + "\n")
            file.close()

            # permit #
            control.write_record(f'/desk/{username}', f'drwxr-x---/{username}',
                                 '/stor/etc/permtab')

            # sudoers #
            f = open('/stor/etc/sudoers', 'w')
            f.write(f'{username}\n')
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
            f.write(f'''taskbar.icon.bgcolor: white
taskbar.icon.border-color: silver
taskbar.icon.bgcolor-hover: #3daee9
taskbar.icon.border-color-hover: #3daee9
appw.title.btn-round: Yes
loginw.input.width: 300
loginw.input.height: 40
loginw.enter-hover.bgcolor: pink
loginw.enter-hover.fgcolor: purple
loginw.unlock-hover.bgcolor: lime
loginw.unlock-hover.fgcolor: green
loginw.login-hover.bgcolor: #3daee9
loginw.login-hover.fgcolor: #123456
loginw.userlogo.bgcolor: white
loginw.width: 500
loginw.height: 500
menu.tab.position: S
key.enable: No
key.bgcolor: silver
key.background: @background/breeze-splash
key.btn.round-size: 2
key.btn.shadow: Yes
key.btn.bgcolor: white
key.btn.fgcolor: black
key.btn.bgcolor-hover: #123456
key.btn.fgcolor-hover: white
alert.width: 500
alert.height: 40
alert.location: SE
locale: {locale}
layout: fa
autosize: Yes
fullscreen: Yes
width: 1920
height: 1080
terminal: commento
sides: No
font: Iran Sans
fontsize: 12
username: guest
password: *
desktop: baran
theme-name: breeze
logo: @icon/breeze
backend.color: black
backend.timeout: 1000
taskbar.location: bottom
taskbar.pins: browser,roller,barge,calculator,calendar,commento,pysys,runapp,about
splash.timeout: 3000
splash.logo: @icon/breeze-logo
splash.logo-size: 300
menu: @icon/breeze-menu
splash.color: black
login.bgcolor: #730c5a
taskbar.icon.style: Windows
login.background: @background/breeze-splash
login.fgcolor: #FFFFFF
enter.bgcolor: #fff
enter.background: @background/breeze-splash
enter.fgcolor: #FFFFFF
unlock.bgcolor: #123456
unlock.background: @background/breeze-splash
unlock.fgcolor: #FFFFFF
loginw.bgcolor: white
loginw.fgcolor: black
loginw.round: Yes
loginw.round-size: 20
loginw.location: center
loginw.shadow: Yes
loginw.userlogo: @icon/breeze-users
loginw.userlogo.shadow: Yes
loginw.userlogo.color: white
loginw.userlogo.round: Yes
loginw.userlogo.round-size: 125
loginw.input.shadow: Yes
loginw.input.fgcolor: gray
loginw.input.bgcolor: white
loginw.input.round: Yes
loginw.input.round-size: 20
loginw.input.font-size: 12
taskbar.bgcolor: white
taskbar.fgcolor: black
taskbar.locked: Yes
taskbar.float: Yes
taskbar.size: 40
desktop.bgcolor: white
desktop.fgcolor: black
desktop.background: @background/breeze-next
lock.fgcolor: black
lock.bgcolor: black
lock.background: @background/breeze-splash
lock.clock.shadow: No
lock.clock.size: 100
lock.clock.color: white
lock.clock.location: center
lock.clock.format: hh:mm:ss
loginw.login.round: Yes
loginw.login.round-size: 20
loginw.enter.round: Yes
loginw.enter.round-size: 20
loginw.unlock.round: Yes
loginw.unlock.round-size: 20
submenu.hide: No
submenu.fgcolor: white
submenu.bgcolor: #1d1d1d
submenu.direction: rtl
submenu.fontsize: 12
loginw.login.bgcolor: #3daee9
loginw.login.bgcolor-hover: #123456
loginw.login.fgcolor: #FFFFFF
loginw.login.fontsize: 12
loginw.login.hide: No
loginw.login.width: 300
loginw.enter.bgcolor: pink
loginw.enter.bgcolor-hover: purple
loginw.enter.fgcolor: #FFFFFF
loginw.enter.fontsize: 12
loginw.enter.hide: No
loginw.enter.width: 300
loginw.unlock.bgcolor: green
loginw.unlock.bgcolor-hover: lime
loginw.unlock.fgcolor: #FFFFFF
loginw.unlock.fontsize: 12
loginw.unlock.hide: No
loginw.unlock.width: 300
loginw.enter.shadow: No
loginw.unlock.shadow: No
loginw.login.shadow: No
loginw.login.height: 40
loginw.enter.height: 40
loginw.unlock.height: 40
appw.body.fgcolor: black
appw.body.bgcolor: white
appw.logo: @icon/breeze-app
appw.shadow: Yes
appw.title.size: 50
appw.title.fgcolor: white
appw.title.bgcolor: #475057
appw.title.float: @icon/breeze-float
appw.title.float-hover: white
appw.title.close: @icon/breeze-close
appw.title.close-hover: #da4453
menu.scroll.color: #4f5357
menu.scroll.color-hover: #3eb4f1
menu.scroll.round-size: 0
menu.scroll.bgcolor: white
params: gui
taskbar.direction: ltr
menu.tab.direction: ltr
''')
            f.close()

            os.system('mkdir -p /stor/proc/info')
            if os.path.isfile ('/stor/proc/0'):
                os.system('rm /stor/proc/0')

            os.system('reboot')

    def __init__(self,ports):
        super(MainApp, self).__init__()


        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External  = ports[4]

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
        self.cmLang.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
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

        ## Browse button click ##
        ## Show setup ##
    def Discard (self):
        self.Env.escape_act()
