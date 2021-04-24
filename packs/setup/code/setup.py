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
            f.write('''# lock : Lock Screen Style
lock.clock.shadow: Yes
lock.clock.color: white
lock.clock.location: center
lock.clock.format: hh:mm
lock.clock.size: 100
lock.bgcolor: white
lock.fgcolor: white
lock.background: @background/glass

# submenu : Submenu Style
submenu.hide: No
submenu.bgcolor: white
submenu.direction: rtl

# taskbar : Taskbar Style
taskbar.location: bottom
taskbar.size: 70
taskbar.locked: Yes
taskbar.float: No
taskbar.bgcolor: white
taskbar.fgcolor: black

# backend : Backend Style
backend.color: black
backend.timeout: 1000

# splash : Splash Style
splash.logo: @icon/pyabr-logo
splash.logo-size: 300
splash.color: #ABCDEF
splash.timeout: 3000

# login : Login Style
login.bgcolor: white
login.fgcolor: black
login.background: @background/glass

# enter : Enter password page Style
enter.bgcolor: white
enter.fgcolor: black
enter.background: @background/glass

# unlock : Unlock page
unlock.bgcolor: white
unlock.fgcolor: black
unlock.background: @background/glass

# appw : Application Window page Style
appw.title.size: 50
appw.title.fgcolor: white
appw.title.bgcolor: #123456
appw.title.float: @icon/float
appw.title.float-hover: #ABCDEF
appw.title.close: @icon/close
appw.title.close-hover: red
appw.title.btn-round: Yes
appw.shadow: Yes
appw.logo: @icon/runner
appw.body.bgcolor: white
appw.body.fgcolor: gray

# desktop : Desktop style
desktop.bgcolor: white
desktop.fgcolor: black
desktop.background: @background/glass

# loginw : Login Dialog Style
loginw.input.bgcolor: white
loginw.input.fgcolor: black
loginw.input.round-size: 20
loginw.input.shadow: Yes
loginw.input.width: 300
loginw.input.height: 40
loginw.enter.bgcolor: purple
loginw.enter.fgcolor: pink
loginw.enter-hover.bgcolor: pink
loginw.enter-hover.fgcolor: purple
loginw.enter.round-size: 20
loginw.enter.hide: No
loginw.enter.width: 300
loginw.enter.shadow: Yes
loginw.enter.height: 40
loginw.unlock.bgcolor: green
loginw.unlock.fgcolor: lime
loginw.unlock-hover.bgcolor: lime
loginw.unlock-hover.fgcolor: green
loginw.unlock.round-size: 20
loginw.unlock.hide: No
loginw.unlock.width: 300
loginw.unlock.height: 40
loginw.unlock.shadow: Yes
loginw.login.hide: No
loginw.login.shadow: Yes
loginw.login.height: 40
loginw.login-hover.bgcolor: #ABCDEF
loginw.login-hover.fgcolor: #123456
loginw.login.width: 300
loginw.login.bgcolor: #123456
loginw.login.fgcolor: #ABCDEF
loginw.login.round-size: 20
loginw.userlogo: @icon/account
loginw.userlogo.shadow: Yes
loginw.userlogo.bgcolor: white
loginw.userlogo.round-size: 125
loginw.bgcolor: white
loginw.fgcolor: black
loginw.round-size: 40
loginw.location: center
loginw.shadow: Yes
loginw.width: 500
loginw.height: 500

# menu : Menu Applications Style
menu: @icon/menu
menu.scroll.color: #123456
menu.scroll.color-hover: #ABCDEF
menu.scroll.round-size: 0
menu.scroll.bgcolor: white
# S, N, E, W
menu.tab.position: S

# virtual keyboard
key.enable: No
key.bgcolor: silver
key.background: @background/none
key.btn.round-size: 15
key.btn.shadow: Yes
key.btn.bgcolor: white
key.btn.fgcolor: black
key.btn.bgcolor-hover: #123456
key.btn.fgcolor-hover: white

# root : Root Settings in GUI
locale: fa
layout: fa
logo: @icon/pyabr-logo
autosize: Yes
fullscreen: Yes
width: 1920
height: 1080
terminal: commento
params: gui
sides: No
font: Iran Sans
fontsize: 12
theme-name: glass-light
username: guest
password: *
desktop: baran''')
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
        self.setStyleSheet('background-color:white;')

        self.lblLang = self.findChild(QtWidgets.QLabel,'lblLang')
        self.lblLang.setFont(self.Env.font())

        self.widget = self.findChild(QtWidgets.QWidget,'widget')
        self.widget.setStyleSheet(f'background-image: url({res.get("@image/setup")})')

        self.leHostname = self.findChild(QtWidgets.QLineEdit, 'leHostname')
        self.leHostname.setFont(self.Env.font())
        self.leHostname.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')

        self.leRootCode = self.findChild(QtWidgets.QLineEdit, 'leRootCode')
        self.leRootCode.setFont(self.Env.font())
        self.leRootCode.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leUsername = self.findChild(QtWidgets.QLineEdit, 'leUsername')
        self.leUsername.setFont(self.Env.font())
        self.leUsername.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.lePassword = self.findChild(QtWidgets.QLineEdit, 'lePassword')
        self.lePassword.setFont(self.Env.font())
        self.lePassword.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')

        self.chGuest = self.findChild(QtWidgets.QCheckBox, 'chGuest')

        self.chGuest.setFont(self.Env.font())
        self.chGuest.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.cmLang = self.findChild(QtWidgets.QComboBox, 'cmLang')
        self.cmLang.setFont(self.Env.font())
        self.cmLang.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leFirstName = self.findChild(QtWidgets.QLineEdit, 'leFirstName')
        self.leFirstName.setFont(self.Env.font())
        self.leFirstName.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leEmail = self.findChild(QtWidgets.QLineEdit, 'leEmail')
        self.leEmail.setFont(self.Env.font())
        self.leEmail.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.lePhone = self.findChild(QtWidgets.QLineEdit, 'lePhone')
        self.lePhone.setFont(self.Env.font())
        self.lePhone.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')

        self.button(QtWidgets.QWizard.FinishButton).clicked.connect(self.Finish)
        self.button(QtWidgets.QWizard.FinishButton).setFont(self.Env.font())
        self.button(QtWidgets.QWizard.FinishButton).setStyleSheet ('''
        QPushButton {
            background-color: #ABCDEF;
            color: white;
            border-radius: 20% 20%;
        }
        QPushButton::hover {
            background-color: #123456;
            color: white;
            border-radius: 20% 20%;
        }
        ''')
        self.button(QtWidgets.QWizard.FinishButton).setMinimumSize(100,40)
        self.button(QtWidgets.QWizard.FinishButton).setText(res.get('@string/install'))

        self.button(QtWidgets.QWizard.NextButton).setStyleSheet ('''
        QPushButton {
            background-color: #ABCDEF;
            color: white;
            border-radius: 20% 20%;
        }
        QPushButton::hover {
            background-color: #123456;
            color: white;
            border-radius: 20% 20%;
        }
        ''')
        self.button(QtWidgets.QWizard.NextButton).setMinimumSize(100,40)
        self.button(QtWidgets.QWizard.NextButton).setFont(self.Env.font())
        self.button(QtWidgets.QWizard.NextButton).setText(res.get('@string/next'))

        self.button(QtWidgets.QWizard.CancelButton).setStyleSheet ('''
        QPushButton {
            background-color: #ABCDEF;
            color: white;
            border-radius: 20% 20%;
        }
        QPushButton::hover {
            background-color: #123456;
            color: white;
            border-radius: 20% 20%;
        }
        ''')
        self.button(QtWidgets.QWizard.CancelButton).setMinimumSize(100,40)
        self.button(QtWidgets.QWizard.CancelButton).clicked.connect (self.Discard)
        self.button(QtWidgets.QWizard.CancelButton).setFont(self.Env.font())
        self.button(QtWidgets.QWizard.CancelButton).setText(res.get('@string/cancel'))

        self.button(QtWidgets.QWizard.BackButton).setStyleSheet ('''
        QPushButton {
            background-color: #ABCDEF;
            color: white;
            border-radius: 20% 20%;
        }
        QPushButton::hover {
            background-color: #123456;
            color: white;
            border-radius: 20% 20%;
        }
        ''')
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
