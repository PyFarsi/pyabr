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

from PyQt5 import QtGui, QtCore, QtWidgets, uic
import platform
import hashlib, shutil, os, sys
from buildlibs import pack_archives as pack, control
from pathlib import Path

from pathlib import  Path

class MainApp(QtWidgets.QWizard):
    def BrowseClick(self):
        self.leLocation.setText((QtWidgets.QFileDialog().getExistingDirectory()))

    def Finish(self):
        ## Get all configure information ##
        if not (
                self.leLocation.text() == None and
                self.leHostname.text() == None and
                self.leRootCode.text() == None and
                self.leConfirmRootCode.text() == None and
                self.leUsername.text() == None and
                self.lePassword.text() == None and
                self.leConfirmPassword.text() == None and
                self.leFirstName.text() == None and
                self.leLastName.text() == None and
                self.leEmail.text() == None and
                self.lePhone.text() == None and
                self.cmUI.currentText() == None and
                self.cmLang.currentText() == None and
                self.cmScreen.currentText() == None
        ):
            hostname = self.leHostname.text()
            rootcode = self.leRootCode.text()
            username = self.leUsername.text()
            password = self.lePassword.text()
            first_name = self.leFirstName.text()
            last_name = self.leLastName.text()
            email = self.leEmail.text()
            phone = self.lePhone.text()
            if self.chGuest.isChecked():
                guest = 'Yes'
            else:
                guest = 'No'

            interface = self.cmUI.currentText()
            if self.cmLang.currentText()=='English':
                locale = 'en'
            elif self.cmLang.currentText()=='فارسی':
                locale = 'fa'
            elif self.cmLang.currentText()=='عربی':
                locale = 'ar'
            else:
                locale = 'en'

            location = self.leLocation.text()

            ## Compile Pyabr ##
            if os.path.isdir("stor"): shutil.rmtree("stor")

            if not os.path.isdir("app"):
                os.mkdir("app")
                os.mkdir("app/cache")
                os.mkdir("app/cache/archives")
                os.mkdir("app/cache/archives/data")
                os.mkdir("app/cache/archives/control")
                os.mkdir("app/cache/archives/code")
                os.mkdir("app/cache/archives/build")
                os.mkdir("app/cache/gets")

            if not os.path.isdir("stor"):
                os.mkdir("stor")
                os.mkdir("stor/app")
                os.mkdir("stor/app/packages")

            if not os.path.isdir("build-packs"): os.mkdir("build-packs")

            pack.install()
            pack.inst('baran')

            if platform.system()=='Linux' and platform.node()=='localhost':
                os.remove('stor/vmabr.pyc')
                shutil.copyfile('packs/pyabr/code/vmabr.py', 'stor/vmabr.py')

            # clean #
            if os.path.isdir('app'): shutil.rmtree('app')
            if os.path.isdir('build-packs'): shutil.rmtree('build-packs')

            ## Setting up hostname ##
            file = open("stor/etc/hostname", "w")
            file.write(hostname)
            file.close()

            ## Setting up Root user ##
            file = open("stor/etc/users/root", "w")
            file.write("username: " + hashlib.sha3_256("root".encode()).hexdigest() + "\n")
            file.write("code: " + hashlib.sha3_512(rootcode.encode()).hexdigest() + "\n")
            file.write('first_name: Super Account')
            file.close()

            ## Setting up Standard user ##
            file = open("stor/etc/users/" + username, "w")
            file.write("username: " + hashlib.sha3_256(username.encode()).hexdigest() + "\n")
            file.write("code: " + hashlib.sha3_512(password.encode()).hexdigest() + "\n")
            file.write("first_name: " + first_name + "\n")
            file.write("last_name: " + last_name + "\n")
            file.write("email: " + email + "\n")
            file.write("phone: " + phone + "\n")
            file.close()

            # permit #
            control.write_record(f'/desk/{username}',f'drwxr-x---/{username}','stor/etc/permtab')

            # sudoers #
            f = open('stor/etc/sudoers','w')
            f.write(f'{username}\n')
            f.close()

            ## Setting up Guest user ##
            file = open("stor/etc/guest", "w")
            if guest == "No":
                file.write("enable_cli: No\nenable_gui: No\n")
            elif guest == "Yes":
                file.write("enable_cli: Yes\nenable_gui: Yes\n")
            else:
                file.write("enable_cli: No\nenable_gui: No\n")
            file.close()
            
            ## Setting up interface ##
            file = open("stor/etc/interface", "w")
            if interface.startswith("C"):
                file.write("CLI")
            elif interface.startswith("G"):
                file.write("GUI")
            file.close()

            ## Setting GUI Table ##
            file = open("stor/etc/gui", "w")
            file.write(f'''
desktop: baran
fullscreen: Yes
sides: Yes
width: 1000
height: 720
autosize: Yes
logo: @icon/pyabr-logo
locale: {locale}
font: Iran Sans
theme-name: Glass theme
backend.color: black
backend.timeout: 1000
taskbar.location: bottom
taskbar.pins: browser,roller,barge,calculator,calendar,commento,pysys,runapp,about
splash.timeout: 3000
splash.logo: @icon/pyabr-logo
splash.logo-size: 300
splash.color: #ABCDEF
login.bgcolor: #123456
login.background: @background/glass
login.fgcolor: #FFFFFF
enter.bgcolor: #fff
enter.background: @background/glass
enter.fgcolor: #FFFFFF
unlock.bgcolor: #123456
unlock.background: @background/glass
unlock.fgcolor: #FFFFFF
loginw.bgcolor: white
loginw.fgcolor: black
loginw.round: Yes
loginw.round-size: 20 20
loginw.location: center
loginw.shadow: Yes
loginw.userlogo: @icon/account
loginw.userlogo.shadow: Yes
loginw.userlogo.color: white
loginw.userlogo.round: Yes
loginw.userlogo.round-size: 125 125
loginw.input.shadow: Yes
loginw.input.fgcolor: gray
loginw.input.bgcolor: white
loginw.input.round: Yes
loginw.input.round-size: 20 20
loginw.input.font-size: 12
taskbar.bgcolor: white
taskbar.fgcolor: black
taskbar.locked: Yes
taskbar.float: Yes
taskbar.size: 70
desktop.bgcolor: white
desktop.fgcolor: black
desktop.background: @background/glass
lock.fgcolor: black
lock.bgcolor: black
lock.background: @background/glass
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
submenu.fgcolor: black
submenu.bgcolor: white
submenu.direction: ltr
submenu.fontsize: 12
loginw.login.bgcolor: #ABCDEF
loginw.login.fgcolor: #FFFFFF
loginw.login.bgcolor-hover: #123456
loginw.login.fgcolor: #FFFFFF
loginw.login.fontsize: 12
loginw.login.hide: No
loginw.login.width: 300
loginw.enter.bgcolor: pink
loginw.enter.fgcolor: #FFFFFF
loginw.enter.bgcolor-hover: purple
loginw.enter.fgcolor: #FFFFFF
loginw.enter.fontsize: 12
menu: @icon/menu
loginw.enter.hide: No
loginw.enter.width: 300
loginw.unlock.bgcolor: green
loginw.unlock.fgcolor: #FFFFFF
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
appw.logo: @icon/app
appw.shadow: Yes
appw.title.size: 50
appw.title.fgcolor: white
appw.title.bgcolor: #123456
appw.title.float: @icon/float
appw.title.float-hover: #ABCDEF
appw.title.close: @icon/close
appw.title.close-hover: red
            ''')
            file.close()

            ## Copying to location ##
            shutil.make_archive("stor", "zip", "stor")
            shutil.unpack_archive("stor.zip", location, "zip")

            ## Clean the cache ##
            os.remove("stor.zip")
            os.system("\"" + sys.executable + "\" clean.py")

            ## run pyabr ##
            if not platform.node()=='localhost':
                os.system(f'cd {location} && {sys.executable} vmabr.pyc')

    def __init__(self):
        super(MainApp, self).__init__()
        uic.loadUi('setup.ui', self)

        ## Finds ##
        self.setStyleSheet('background-color:white;')
        self.leLocation = self.findChild(QtWidgets.QLineEdit, 'leLocation')
        self.leLocation.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leLocation.setEnabled(False)
        #self.leLocation.setStyleSheet ('background-color: white;border-radius: 15% 15%')
        self.btnLocation = self.findChild(QtWidgets.QPushButton, 'btnLocation')
        self.btnLocation.setStyleSheet ('''
        QPushButton {
            background-color: #ABCDEF;
            color: white;
            border-radius: 15% 15%;
        }
        QPushButton::hover {
            background-color: #123456;
            color: white;
            border-radius: 15% 15%;
        }
        ''')
        self.leHostname = self.findChild(QtWidgets.QLineEdit, 'leHostname')
        self.leHostname.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leRootCode = self.findChild(QtWidgets.QLineEdit, 'leRootCode')
        self.leRootCode.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leUsername = self.findChild(QtWidgets.QLineEdit, 'leUsername')
        self.leUsername.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.lePassword = self.findChild(QtWidgets.QLineEdit, 'lePassword')
        self.lePassword.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.chGuest = self.findChild(QtWidgets.QCheckBox, 'chGuest')
        self.chGuest.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.cmUI = self.findChild(QtWidgets.QComboBox, 'cmUI')
        self.cmUI.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.cmLang = self.findChild(QtWidgets.QComboBox, 'cmLang')
        self.cmLang.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leFirstName = self.findChild(QtWidgets.QLineEdit, 'leFirstName')
        self.leFirstName.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leLastName = self.findChild(QtWidgets.QLineEdit, 'leLastName')
        self.leLastName.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leEmail = self.findChild(QtWidgets.QLineEdit, 'leEmail')
        self.leEmail.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.lePhone = self.findChild(QtWidgets.QLineEdit, 'lePhone')
        self.lePhone.setStyleSheet ('background-color: white;border-radius: 15% 15%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')

        self.button(QtWidgets.QWizard.FinishButton).clicked.connect(self.Finish)
        self.button(QtWidgets.QWizard.FinishButton).setStyleSheet ('''
        QPushButton {
            background-color: #ABCDEF;
            color: white;
            border-radius: 15% 15%;
        }
        QPushButton::hover {
            background-color: #123456;
            color: white;
            border-radius: 15% 15%;
        }
        ''')
        self.button(QtWidgets.QWizard.FinishButton).setMinimumSize(100,30)
        self.button(QtWidgets.QWizard.NextButton).setStyleSheet ('''
        QPushButton {
            background-color: #ABCDEF;
            color: white;
            border-radius: 15% 15%;
        }
        QPushButton::hover {
            background-color: #123456;
            color: white;
            border-radius: 15% 15%;
        }
        ''')
        self.button(QtWidgets.QWizard.NextButton).setMinimumSize(100,30)


        self.button(QtWidgets.QWizard.CancelButton).setStyleSheet ('''
        QPushButton {
            background-color: #ABCDEF;
            color: white;
            border-radius: 15% 15%;
        }
        QPushButton::hover {
            background-color: #123456;
            color: white;
            border-radius: 15% 15%;
        }
        ''')
        self.button(QtWidgets.QWizard.CancelButton).setMinimumSize(100,30)


        self.button(QtWidgets.QWizard.BackButton).setStyleSheet ('''
        QPushButton {
            background-color: #ABCDEF;
            color: white;
            border-radius: 15% 15%;
        }
        QPushButton::hover {
            background-color: #123456;
            color: white;
            border-radius: 15% 15%;
        }
        ''')
        self.button(QtWidgets.QWizard.BackButton).setMinimumSize(100,30)

        ## Browse button click ##
        self.btnLocation.clicked.connect(self.BrowseClick)

        # https://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python
        pyabr_inst = str(Path.home())

        ## Default location to install ##
        if platform.system()=="Windows":
            self.leLocation.setText(pyabr_inst+"\\Pyabr")
        else:
            self.leLocation.setText(pyabr_inst+"/Pyabr")

        ## Show setup ##
        self.show()

app = QtWidgets.QApplication([])
w = MainApp()
app.exec_()
