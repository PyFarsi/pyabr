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

import hashlib
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

from PyQt5 import QtWidgets, uic

from buildlibs import pack_archives as pack, control


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
            fullname = self.leFirstName.text()+" "+self.leLastName.text()
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
            else:
                locale = 'fa'

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
            file.write('fullname: Super Account')
            file.close()

            ## Setting up Standard user ##
            file = open("stor/etc/users/" + username, "w")
            file.write("username: " + hashlib.sha3_256(username.encode()).hexdigest() + "\n")
            file.write("code: " + hashlib.sha3_512(password.encode()).hexdigest() + "\n")
            file.write("fullname: " + fullname + "\n")
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
            f = open('stor/etc/gui','r')
            s = f.read()
            f.close()

            f = open('stor/etc/gui','w')
            f.write(s.replace('locale: fa',f'locale: {locale}'))
            f.close()

            ## Copying to location ##
            shutil.make_archive("stor", "zip", "stor")
            shutil.unpack_archive("stor.zip", location, "zip")

            ## Clean the cache ##
            os.remove("stor.zip")
            subprocess.call([sys.executable,'clean.py'])

            ## run pyabr ##
            try:
                os.system(f'cd "{location}" && {sys.executable} vmabr.pyc')
            except:
                print(f"Pyabr successfully installed in {location}")

    def __init__(self):
        super(MainApp, self).__init__()
        uic.loadUi('setup.ui', self)

        ## Finds ##
        self.setStyleSheet('background-color:white;')
        self.leLocation = self.findChild(QtWidgets.QLineEdit, 'leLocation')
        self.leLocation.setEnabled(False)
        #self.leLocation.setStyleSheet ('background-color: white;border-radius: 15% 15%')
        self.btnLocation = self.findChild(QtWidgets.QPushButton, 'btnLocation')
        self.leHostname = self.findChild(QtWidgets.QLineEdit, 'leHostname')
        self.leRootCode = self.findChild(QtWidgets.QLineEdit, 'leRootCode')
        self.leUsername = self.findChild(QtWidgets.QLineEdit, 'leUsername')
        self.lePassword = self.findChild(QtWidgets.QLineEdit, 'lePassword')
        self.chGuest = self.findChild(QtWidgets.QCheckBox, 'chGuest')
        self.cmUI = self.findChild(QtWidgets.QComboBox, 'cmUI')
        self.cmLang = self.findChild(QtWidgets.QComboBox, 'cmLang')
        self.leFirstName = self.findChild(QtWidgets.QLineEdit, 'leFirstName')
        self.leLastName = self.findChild(QtWidgets.QLineEdit, 'leLastName')
        self.leEmail = self.findChild(QtWidgets.QLineEdit, 'leEmail')
        self.lePhone = self.findChild(QtWidgets.QLineEdit, 'lePhone')

        self.button(QtWidgets.QWizard.FinishButton).clicked.connect(self.Finish)

        self.button(QtWidgets.QWizard.FinishButton).setMinimumSize(100,30)

        self.button(QtWidgets.QWizard.NextButton).setMinimumSize(100,30)

        self.button(QtWidgets.QWizard.CancelButton).setMinimumSize(100,30)

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
