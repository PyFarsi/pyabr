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
import platform
import hashlib, shutil, os, sys
from buildlibs import pack_archives as pack, control

app = QtWidgets.QApplication([])

f = QtGui.QFont()
f.setFamily('Iran Sans') # Pyabr bought it see /usr/share/docs/IRANSans/FontLicense.txt in Pyabr
f.setPointSize(12)

class FakeDesktop (QtWidgets.QMainWindow):
    def __init__(self):
        super(FakeDesktop, self).__init__()

        ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()

        self.resize(width,height)
        self.x = QtWidgets.QWidget()
        self.x.setStyleSheet('background-image: url("packs/baran/data/usr/share/backgrounds/glass.jpg")')
        self.showFullScreen()

        # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setColor(QtGui.QColor(10, 2, 34, 255 ))
        shadow.setOffset(0)
        shadow.setBlurRadius(10)

        self.w = MainApp()
        self.w.setGraphicsEffect(shadow)

        self.setCentralWidget(self.x)
        self.layout().addWidget(self.w)

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
                self.leLastName.text() == None and
                self.leEmail.text() == None and
                self.lePhone.text() == None and
                self.cmLang.currentText() == None
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

            if self.cmLang.currentText()=='English':
                locale = 'en'
            elif self.cmLang.currentText()=='فارسی':
                locale = 'fa'
            else:
                locale = 'en'

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


            ## Setting GUI Table ##
            file = open("stor/etc/gui", "w")
            file.write(f'''
# lock : Lock Screen Style
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
backend.color: white
backend.timeout: 1000

# splash : Splash Style
splash.logo: @icon/pyabr-blue-logo
splash.logo-size: 300
splash.color: white
splash.timeout: 3000

# login : Login Style
login.bgcolor: white
login.fgcolor: black
login.background: @background/glass

# enter : Enter password page Style
enter.bgcolor: white
enter.fgcolor: black
enter.background: @background/glass

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
loginw.unlock.round-size: 40
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
loginw.userlogo.round-size: 70
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


# root : Root Settings in GUI
locale: {locale}
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
desktop: baran
            ''')
            file.close()

            ## Copying to location ##
            shutil.make_archive("stor", "zip", "stor")
            os.system('chmod 777 -R /stor')
            shutil.unpack_archive("stor.zip", '/stor', "zip")
            ## run pyabr ##
            os.system('mkdir -p /stor/proc/info')
            if os.path.isfile ('/stor/proc/0'):
                os.system('rm /stor/proc/0')
            os.system('systemctl reboot')

    def __init__(self):
        super(MainApp, self).__init__()
        uic.loadUi('installer.ui', self)


        ## Finds ##
        self.setStyleSheet('background-color:white;')

        self.lblLang = self.findChild(QtWidgets.QLabel,'lblLang')
        self.lblLang.setFont(f)

        self.leHostname = self.findChild(QtWidgets.QLineEdit, 'leHostname')
        self.leHostname.setFont(f)
        self.leHostname.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')

        self.leRootCode = self.findChild(QtWidgets.QLineEdit, 'leRootCode')
        self.leRootCode.setFont(f)
        self.leRootCode.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leUsername = self.findChild(QtWidgets.QLineEdit, 'leUsername')
        self.leUsername.setFont(f)
        self.leUsername.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.lePassword = self.findChild(QtWidgets.QLineEdit, 'lePassword')
        self.lePassword.setFont(f)
        self.lePassword.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')

        self.chGuest = self.findChild(QtWidgets.QCheckBox, 'chGuest')
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.label.setFont(f)

        self.toolButton = self.findChild(QtWidgets.QToolButton, 'toolButton')
        self.toolButton.clicked.connect (self.LiveRun)
        self.toolButton.setIconSize (QtCore.QSize(200,200))
        self.toolButton.setFixedSize(300,300)
        self.toolButton.setIcon (QtGui.QIcon('packs/numix/data/usr/share/icons/cdrom.svg'))

        self.chGuest.setFont(f)
        self.chGuest.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.cmLang = self.findChild(QtWidgets.QComboBox, 'cmLang')
        self.cmLang.setFont(f)
        self.cmLang.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leFirstName = self.findChild(QtWidgets.QLineEdit, 'leFirstName')
        self.leFirstName.setFont(f)
        self.leFirstName.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leLastName = self.findChild(QtWidgets.QLineEdit, 'leLastName')
        self.leLastName.setFont(f)
        self.leLastName.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.leEmail = self.findChild(QtWidgets.QLineEdit, 'leEmail')
        self.leEmail.setFont(f)
        self.leEmail.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')
        self.lePhone = self.findChild(QtWidgets.QLineEdit, 'lePhone')
        self.lePhone.setFont(f)
        self.lePhone.setStyleSheet ('background-color: white;border-radius: 20% 20%;border-color: #ABCDEF;border-style: solid;padding-left: 10%;padding-right: 10%;border-width: 2%')

        self.button(QtWidgets.QWizard.FinishButton).clicked.connect(self.Finish)
        self.button(QtWidgets.QWizard.FinishButton).setFont(f)
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
        self.button(QtWidgets.QWizard.FinishButton).setText('قبلی')

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
        self.button(QtWidgets.QWizard.NextButton).setFont(f)
        self.button(QtWidgets.QWizard.NextButton).setText('بعدی')

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
        self.button(QtWidgets.QWizard.CancelButton).setFont(f)
        self.button(QtWidgets.QWizard.CancelButton).setText('لغو')

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
        self.button(QtWidgets.QWizard.BackButton).setFont(f)
        self.button(QtWidgets.QWizard.BackButton).setText('قبلی')

        self.toolButton.setIconSize (QtCore.QSize(200,200))

        ## Browse button click ##
        ## Show setup ##
        self.show()

    def Discard (self):
        os.system('systemctl poweroff')

    def LiveRun (self):
        os.system(f"env QTWEBENGINE_DISABLE_SANDBOX=1 '{sys.executable}' debug.py")
        os.system('systemctl poweroff')

w = FakeDesktop()
app.exec_()