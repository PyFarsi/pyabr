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

## Imports ##
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets, QtGui, uic, Qsci
from PyQt5.Qsci import *
import sys, hashlib, os, importlib, subprocess,time,threading,datetime
from libabr import Files, Control, Permissions, Colors, Process, Modules, App, System, Res, Commands, Script

modules = Modules()
files = Files()
control = Control()
colors = Colors()
process = Process()
permissions = Permissions()
app = App()
res = Res()
commands = Commands()
f = QFont()

## Get data ##
def getdata (name):
    return control.read_record (name,'/etc/gui')

height = int(files.readall('/tmp/height'))
width = int(files.readall('/tmp/width'))

files.remove('/tmp/height')
files.remove('/tmp/width')

files.write('/proc/info/de','Baran Desktop Enviroment')

if files.isfile('/proc/info/scn'):
    subprocess.call (['xrandr','-s',files.readall('/proc/info/scn')])

## variables ##

f.setFamily(getdata("font"))
f.setPointSize(int(getdata("fontsize")))

## ## ## ## ##

## Backend ##
class Backend (QMainWindow):
    ## Run splash page ##
    def runSplash (self):
        self.setCentralWidget(Splash([self]))

    def runLogin (self):
        self.setCentralWidget(Login([self]))

    def runEnter (self):
        self.setCentralWidget(Enter([self, self], getdata("username")))  ## Switch user
        control.write_record('username','guest','/etc/gui')

    def runDesktop (self):
        self.setCentralWidget(Desktop([self, self], getdata("username"), getdata("password")))
        control.write_record('username', 'guest', '/etc/gui')
        control.write_record('password', '*', '/etc/gui')

    def runUnlock (self):
        self.setCentralWidget(Unlock([self, self], getdata("username")))  ## Switch user
        control.write_record('username', 'guest', '/etc/gui')

    def __init__(self):
        super(Backend, self).__init__()

        ## Set port name ##
        self.setObjectName('Backend')
        self.setFont(f)

        ## Get informations ##
        cs = files.readall ('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs+' '+ver+' ('+cd+")")

        ## Get app logo ##
        self.setWindowIcon(QIcon(res.get(getdata("logo"))))

        ## Get backend color ##

        self.wb = QMainWindow()
        self.wb.setStyleSheet('background-color: ' + getdata("backend.color")+";color: black;")
        self.setCentralWidget(self.wb)

        ## Set size ##

        self.resize(int(getdata("width")), int(getdata("height")))

        ## Set sides ##
        ## Set sides ##

        if getdata("sides") == 'No':
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Show ##

            ## Get data ##


        if getdata("fullscreen") == 'Yes':
            self.showFullScreen()
        else:
            self.show()

        ## Run backend after showing backend ##

        params = getdata('params')

        control.write_record('params', 'gui', '/etc/gui')

        if params == 'splash':
            self.runSplash()
        elif params == 'login':
            self.runLogin()
        elif params == 'enter':
            self.runEnter()
        elif params == 'desktop':
            self.runDesktop()
        elif params == 'unlock':
            self.runUnlock()
        else:
            QTimer.singleShot(int(getdata("backend.timeout")), self.runSplash)  ## Run splash after 1s

## Splash ##
class Splash (QMainWindow):

    ## Run login page ##
    def runLogin(self):
        self.setCentralWidget(Login([self.Backend]))

    def __init__(self,ports):
        super(Splash, self).__init__()

        ## Set port name ##
        self.setObjectName('Splash')
        self.setFont(f)

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        self.setWindowIcon(QIcon(res.get(getdata("logo"))))


        # set font

        ## Ports ##

        self.Backend = ports[0]

        ## Get backend color ##

        ## Set color ##

        self.wb = QMainWindow()
        self.wb.setStyleSheet(f'background-color: {getdata("splash.color")}')
        self.setCentralWidget(self.wb)

        ## Set size ##


        self.resize(int(getdata("width")), int(getdata("height")))

        ## Set sides ##

        if getdata("sides") == 'No':
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Show ##
        ## Get data ##


        if getdata("fullscreen") == 'Yes':
            self.showFullScreen()
        else:
            self.show()

        ## Splash Logo ##


        self.logo = QToolButton()
        self.wb.layout().addWidget (self.logo)

        ## Set logo ##
        self.logo.setIcon(QIcon(res.get(getdata("splash.logo"))))

        self.logo.setMaximumSize(int(getdata("splash.logo-size")),int(getdata("splash.logo-size"))) ## Set size
        self.logo.setIconSize(QSize(int(getdata("splash.logo-size")),int(getdata("splash.logo-size"))))

        self.logo.setStyleSheet('border:none;')

        self.logo.setGeometry(int(self.width()/2)-int(int(getdata("splash.logo-size"))/2),int(self.height()/2)-int(int(getdata("splash.logo-size"))/2),int(getdata("splash.logo-size")),int(getdata("splash.logo-size")))

        ## Run splash after showing backend ##

        QTimer.singleShot(int(getdata("splash.timeout")), self.runLogin) ## Run login


class LeInput (QLineEdit):
    def __init__(self,ports):
        super(LeInput, self).__init__()

        self.Env = ports[0]

        self.setFocusPolicy(Qt.ClickFocus)
        self.setFont(QFont(getdata("font"), int(getdata("fontsize"))))

    def focusInEvent(self, e):
        if getdata("key.enable") == 'Yes':
            self.Env.keyboardWidget.currentTextBox = self
            self.Env.keyboardWidget.show()
            self.Env.fakewidgetkeyboard.show()

            self.Env.fakewidgetkeyboard.activateWindow()
            self.Env.fakewidgetkeyboard.raise_()

            self.Env.keyboardWidget.activateWindow()
            self.Env.keyboardWidget.raise_()

        # self.setStyleSheet("border: 1px solid red;")
        super(LeInput, self).focusInEvent(e)

    def mousePressEvent(self, e):
        # print(e)
        # self.setFocusPolicy(Qt.ClickFocus)
        super(LeInput, self).mousePressEvent(e)

## LoginW ##
class LoginWidget (QMainWindow):

    def __init__(self,ports):
        super(LoginWidget, self).__init__()

        ## ports ##

        self.Backend = ports[0]
        self.Env = ports[1]
        self.setFont(f)

        ######

        self.setMaximumSize(int(getdata("loginw.width")),int(getdata("loginw.height")))  ## Set size of loginw

        ## Locations ##

        if getdata("loginw.location") == 'center':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2),
                             int(self.Env.height() / 2) - int(self.height() / 2), self.width(),
                             self.height())  ## Geometric
        elif getdata("loginw.location") == 'top':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2), int(self.height() / 20), self.width(),
                             self.height())  ## Geometric
        elif getdata("loginw.location") == 'left':
            self.setGeometry(int(self.width() / 20), int(self.Env.height() / 2) - int(self.height() / 2), self.width(),
                             self.height())  ## Geometric
        elif getdata("loginw.location") == 'right':
            self.setGeometry(self.Env.width() - int(self.width() / 20) - self.width(),
                             int(self.Env.height() / 2) - int(self.height() / 2), self.width(),
                             self.height())  ## Geometric
        elif getdata("loginw.location") == 'bottom':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2),
                             self.Env.height() - int(self.height() / 20) - self.height(), self.width(),
                             self.height())  ## Geometric

        if getdata("loginw.shadow")=='Yes':
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.setGraphicsEffect(shadow)

            ## BackgroudcolorButton ##
        self.btnColorButton = QPushButton()
        self.btnColorButton.setGeometry(0,0,self.width(),self.height())
        self.layout().addWidget(self.btnColorButton)
            ##

            ## Set colors ##
        self.setStyleSheet(f'color:{getdata("loginw.fgcolor")};border-radius: {getdata("loginw.round-size")}% {getdata("loginw.round-size")};')  ## Set color white as default
        self.btnColorButton.setStyleSheet(f'background-color:{getdata("loginw.bgcolor")};')

        ## Userlogo ##

        self.userlogo = QToolButton()

            ## Set size & location ##
        self.userlogo.setMaximumSize(250,250)
        self.userlogo.setIconSize(QSize(250,250))
        if getdata('loginw.userlogo').startswith ('@icon/'):
            self.userlogo.setIcon(QIcon(res.get(getdata("loginw.userlogo"))))
        else:
            self.userlogo.setIcon(QIcon(files.input(getdata("loginw.userlogo"))))
        self.userlogo.setGeometry(int(self.width()/2)-int(self.userlogo.width()/2),int(self.height()/4)-int(self.userlogo.height()/4),self.userlogo.width(),self.userlogo.height())

        #if not loginw_userlogo == None:
        if self.Env.objectName() == 'Enter' or self.Env.objectName() == 'Unlock':
            logo = control.read_record('loginw.userlogo', '/etc/users/' + self.Env.username)
            if not logo == None:
                loginw_userlogo = logo
            else:
                loginw_userlogo = '@icon/account'

            if loginw_userlogo.startswith('@icon/'):
                self.userlogo.setIcon(QIcon(res.get(loginw_userlogo)))
            else:
                self.userlogo.setIcon(QIcon(files.input(loginw_userlogo)))

        self.userlogo.setStyleSheet(
            f'background-color: {getdata("loginw.userlogo.bgcolor")};border-radius: {getdata("loginw.userlogo.round-size")}% {getdata("loginw.userlogo.round-size")};')

            ## Shadow for userlogo ##
        ## Shadow ##
        if getdata("loginw.userlogo.shadow")=='Yes':
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.userlogo.setGraphicsEffect(shadow)

            ## Default userlogo ##
        self.layout().addWidget (self.userlogo)

            ## leInput username ##

        self.leInput = LeInput([self.Env])

            ## Size & Location of leInput ##
        self.leInput.setMaximumSize(int(getdata("loginw.input.width")),int(getdata("loginw.input.height")))
        self.leInput.setGeometry(int(self.width()/2)-int(self.leInput.width()/2),self.height()-int(self.height()/4)-self.leInput.height(),self.leInput.width(),self.leInput.height())

            ## Shadow of leInput ##
        ## Shadow ##
        if getdata("loginw.input.shadow")=='Yes':
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.leInput.setGraphicsEffect(shadow)

            ## Colors of leInput ##


            ## Setting up all colors ##
        self.leInput.setStyleSheet('padding-left: 10%;padding-right: 10%;background-color: '+getdata("loginw.input.bgcolor")+';color: '+getdata("loginw.input.fgcolor")+f";border-width: 3%;border-radius: {getdata('loginw.input.round-size')}% {getdata('loginw.input.round-size')}")

            ## Place holder in input ##

        if self.Env.objectName()=='Login':
            self.leInput.setPlaceholderText(res.get('@string/username_placeholder')) # See https://stackoverflow.com/questions/24274318/placeholder-text-not-showing-pyside-pyqt
            self.leInput.setFont(f)
        else:
            self.leInput.setEchoMode(QLineEdit.Password)
            self.leInput.setPlaceholderText(res.get('@string/unlock_hint'))
            self.leInput.setFont(f)

            ## Setting up font settings ##
        self.leInput.setFont(f)

            ## Connect to action ##

        self.leInput.returnPressed.connect (self.actions)

        ## Add leInput Widget ##
        self.layout().addWidget(self.leInput)

            ## Enter button ##
        if self.Env.objectName()=='Login':
            self.btnLogin = QPushButton()

            ## Shadow ##
            if getdata('loginw.login.shadow') == 'Yes':
                ## Shadow ##
                # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
                shadow = QGraphicsDropShadowEffect()
                shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
                shadow.setOffset(0)
                shadow.setBlurRadius(10)
                self.btnLogin.setGraphicsEffect(shadow)

            self.btnLogin.clicked.connect (self.actions)
            self.btnLogin.setStyleSheet('''
                    QPushButton {
                        background-color: ''' + getdata('loginw.login.bgcolor') +''';
                        color: ''' + getdata('loginw.login.fgcolor') + ''';
                        border-radius: ''' + getdata('loginw.login.round-size') + '''% '''+getdata('loginw.login.round-size')+'''%;
                    } 
                    QPushButton:hover {
                        background-color:''' + getdata('loginw.login-hover.bgcolor') + ''';
                        color:''' + getdata('loginw.login-hover.fgcolor') + ''';
                        border-radius: ''' + getdata('loginw.login.round-size') + '''% '''+ getdata('loginw.login.round-size')+''';
                    }
                    ''')

            self.btnLogin.setFont(f)
            if  getdata('loginw.login.hide') == 'Yes':
                self.btnLogin.hide()
            self.btnLogin.setText(res.get('@string/next_text'))
            self.btnLogin.setFont(f)
            self.btnLogin.setMaximumSize(int( getdata('loginw.login.width')), int( getdata('loginw.login.height')))
            self.btnLogin.setGeometry(int(self.width() / 2) - int(self.btnLogin.width() / 2),
                                      self.height() - int(self.height() / 4) - int(self.btnLogin.height() / 4) + int(self.btnLogin.height()/2),
                                      self.btnLogin.width(), self.btnLogin.height())
            self.layout().addWidget(self.btnLogin)

        elif self.Env.objectName() == 'Enter':
            self.btnEnter = QPushButton()
            ## Shadow ##
            if  getdata('loginw.enter.shadow') == 'Yes':
                ## Shadow ##
                # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
                shadow = QGraphicsDropShadowEffect()
                shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
                shadow.setOffset(0)
                shadow.setBlurRadius(10)
                self.btnEnter.setGraphicsEffect(shadow)

            self.btnEnter.clicked.connect (self.actions)
            self.btnEnter.setStyleSheet('''
                    QPushButton {
                        background-color: ''' +  getdata('loginw.enter.bgcolor') + """;
                        color: """ + getdata('loginw.enter.fgcolor') + """;
                        border-radius: """ + getdata('loginw.enter.round-size') + '''
                    } 
                    QPushButton:hover {
                        background-color:''' + getdata('loginw.enter-hover.bgcolor') + ''';
                        color:''' + getdata('loginw.enter-hover.fgcolor') + ''';
                        border-radius: ''' + getdata('loginw.enter.round-size') + ''';
                    }
                    ''')


            self.btnEnter.setFont(f)
            if getdata('loginw.enter.hide') == 'Yes':
                self.btnEnter.hide()
            self.btnEnter.setText(res.get('@string/enter_text'))
            self.btnEnter.setFont(f)
            self.btnEnter.setMaximumSize(int(getdata('loginw.enter.width')), int(getdata('loginw.enter.height')))
            self.btnEnter.setGeometry(int(self.width() / 2) - int(self.btnEnter.width() / 2),
                                      self.height() - int(self.height() / 4) - int(self.btnEnter.height() / 4) + int(self.btnEnter.height()/2),
                                      self.btnEnter.width(), self.btnEnter.height())
            self.layout().addWidget(self.btnEnter)

        elif self.Env.objectName()=='Unlock':
            self.btnUnlock = QPushButton()
            ## Shadow ##
            if getdata('loginw.unlock.shadow') == 'Yes':
                ## Shadow ##
                # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
                shadow = QGraphicsDropShadowEffect()
                shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
                shadow.setOffset(0)
                shadow.setBlurRadius(10)
                self.btnUnlock.setGraphicsEffect(shadow)

            self.btnUnlock.clicked.connect(self.actions)
            self.btnUnlock.setStyleSheet('''
                                QPushButton {
                                    background-color: ''' + getdata('loginw.unlock.bgcolor')+ """;
                                    color: """ +getdata('loginw.unlock.fgcolor') + """;
                                    border-radius: """ + getdata('loginw.unlock.round-size') + '''
                                } 
                                QPushButton:hover {
                                    background-color:''' + getdata('loginw.unlock-hover.bgcolor')+ ''';
                                    color:''' + getdata('loginw.unlock-hover.fgcolor') + ''';
                                    border-radius: ''' + getdata('loginw.unlock.round-size') + ''';
                                }
                                ''')

            self.btnUnlock.setFont(f)
            if getdata('loginw.unlock.hide') == 'Yes':
                self.btnUnlock.hide()
            self.btnUnlock.setText(res.get('@string/unlock_text'))
            self.btnUnlock.setFont(f)
            self.btnUnlock.setMaximumSize(int(getdata('loginw.unlock.width')), int(getdata('loginw.unlock.height')))
            self.btnUnlock.setGeometry(int(self.width() / 2) - int(self.btnUnlock.width() / 2),
                                      self.height() - int(self.height() / 4) - int(self.btnUnlock.height() / 4) + int(
                                          self.btnUnlock.height() / 2),
                                      self.btnUnlock.width(), self.btnUnlock.height())
            self.layout().addWidget(self.btnUnlock)

    def actions (self):
        if self.Env.objectName() == 'Login':
            username = self.leInput.text().lower()  ## Get username

            if self.Env.guest == 'Yes' and username == 'guest':
                self.Env.setCentralWidget(Desktop([self.Backend,self],username,'*'))

            elif not files.isfile('/etc/users/' + username):
                self.leInput.clear()
                self.leInput.setEnabled(False)
                message = res.get('@string/user_not_found')
                if not message==None: message = message
                self.leInput.setPlaceholderText(message)
                self.leInput.setFont(f)
                QTimer.singleShot(2500, self.clean)
            else:
                ## Check user ##
                hashname = hashlib.sha3_256(username.encode()).hexdigest()  ## Get hashname
                name = control.read_record ('username','/etc/users/'+username)

                if not hashname==name:
                    self.leInput.clear()
                    self.leInput.setEnabled(False)
                    message = res.get('@string/user_not_found')
                    if not message == None: message = message
                    self.leInput.setPlaceholderText(message)
                    self.leInput.setFont(f)
                    QTimer.singleShot(2500, self.clean)

                else:
                    ## Setting up switched user ##

                    self.Env.setCentralWidget(Enter ([self.Backend,self],username)) ## Switch user
        elif self.Env.objectName()=='Enter':

            username = self.Env.username
            password = self.leInput.text()

            ## Check password ##
            hashcode = hashlib.sha3_512(password.encode()).hexdigest() ## Create hashcode for password
            code = control.read_record('code','/etc/users/'+username)

            if not code==hashcode:
                self.leInput.clear()
                self.leInput.setEnabled(False)
                message = res.get('@string/wrong_password')
                self.leInput.setPlaceholderText(message)
                self.leInput.setFont(f)
                QTimer.singleShot(2500, self.clean)
            else:
                self.Env.setCentralWidget(Desktop([self.Backend,self],username,password))

        elif self.Env.objectName()=='Unlock':

            username = self.Env.username
            password = self.leInput.text()

            ## Check password ##
            hashcode = hashlib.sha3_512(password.encode()).hexdigest()  ## Create hashcode for password
            code = control.read_record('code', '/etc/users/' + username)

            if not code == hashcode:
                self.leInput.clear()
                self.leInput.setEnabled(False)
                message = res.get('@string/wrong_password')
                self.leInput.setPlaceholderText(message)
                self.leInput.setFont(f)
                QTimer.singleShot(2500, self.clean)
            else:
                self.close()
                self.Env.close()
                files.create('/tmp/unlock')
                sys.exit(0)

    def clean (self):
        self.leInput.setEnabled(True)
        if self.Env.objectName()=='Login':
            self.leInput.setPlaceholderText(res.get('@string/username_placeholder')) # See https://stackoverflow.com/questions/24274318/placeholder-text-not-showing-pyside-pyqt
            self.leInput.setFont(f)
        else:
            self.leInput.setPlaceholderText(res.get('@string/password_placeholder'))
            self.leInput.setFont(f)

## Login ##
class Login (QMainWindow):

    def vkey_act(self):

        if getdata('key.enable')=='Yes':
            control.write_record('key.enable', 'No', '/etc/gui')
        else:
            control.write_record('key.enable', 'Yes', '/etc/gui')

    def reboot_act_(self):
            if not files.readall('/proc/info/os') == 'Pyabr':
                app.endall()
                self.Backend.hide()
                commands.reboot([])
                sys.exit(0)
            else:
                subprocess.call(['reboot'])

    def escape_act_(self):
            if not files.readall('/proc/info/os') == 'Pyabr':
                app.endall()
                self.Backend.hide()
                commands.shutdown([])
                sys.exit(0)
            else:
                subprocess.call(['poweroff'])
    def __init__(self,ports):
        super(Login, self).__init__()
        self.setFont(f)

        ## Guest user ##
        self.guest = control.read_record('enable_gui','/etc/guest')

        ## Set port name ##
        self.setObjectName('Login')

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        self.setWindowIcon(QIcon(res.get(getdata("logo"))))

        ## Ports ##

        self.Backend = ports[0]


        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0,0,int(getdata("width")),int(getdata("height")))
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##

        self.setStyleSheet(f'color: {getdata("login.fgcolor")};')
        self.backgroundButton.setStyleSheet(f'border:none;background-color: {getdata("loginw.bgcolor")};')


        self.setStyleSheet(f'color: {getdata("login.fgcolor")};')
        self.backgroundButton.setStyleSheet(f'border:none;background-color: {getdata("login.bgcolor")};')

        self.setStyleSheet(f'color: {getdata("login.fgcolor")};')
        self.backgroundButton.setStyleSheet(f'border:none;background-image: url({res.get(getdata("login.background"))});')
        self.setStyleSheet(f'background-color:{getdata("login.bgcolor")};color: {getdata("login.fgcolor")};')

        self.resize(int(getdata("width")), int(getdata("height")))

        ## Set sides ##
        ## Set sides ##

        if getdata("sides") == 'No':
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Login widget ##

        self.loginw = LoginWidget([self.Backend,self])
        self.layout().addWidget (self.loginw)

        #
        self.submenu = QMenuBar()  # Sub menu
        self.Backend.setMenuBar(self.submenu)

        # self.submenu.setStyleSheet(f'background-color:none;color:{submenu_bgcolor};')

        if getdata("submenu.direction") == 'ltr':
            self.submenu.setLayoutDirection(Qt.LeftToRight)
        elif getdata("submenu.direction") == 'rtl':
            self.submenu.setLayoutDirection(Qt.RightToLeft)

        # hide #
        if getdata("submenu.hide") == 'Yes':
            self.submenu.hide()

        self.submenu.setFont(f)

        ## Shell ##

        self.submenu.setCornerWidget(Shell([self.Backend, self]))

        self.etcmenu = QMenu()
        self.etcmenu.setFont(f)
        self.etcmenu.setTitle(res.get('@string/etcmenu'))
        self.etcmenu.setFont(f)
        self.submenu.addMenu(self.etcmenu)

        # Account menu #

        # Power menu #
        self.powermenu = QMenu()
        self.powermenu.setFont(f)
        self.etcmenu.addMenu(self.powermenu)
        self.powermenu.setTitle(res.get('@string/powermenu'))
        self.powermenu.setFont(f)

        # all actions in menus #

        self.escape = QAction(res.get('@string/escape'))
        self.escape.triggered.connect(self.escape_act_)
        self.escape.setFont(f)
        self.powermenu.addAction(self.escape)

        self.restart = QAction(res.get('@string/restart'))
        self.restart.triggered.connect(self.reboot_act_)
        self.restart.setFont(f)
        self.powermenu.addAction(self.restart)

        if getdata("fullscreen") == 'Yes':
            self.showFullScreen()
        else:
            self.show()

        self.enablekeyboard = QAction(res.get('@string/vkey'), checkable=True)
        self.etcmenu.addAction(self.enablekeyboard)
        if getdata('key.enable') == 'Yes':
            self.enablekeyboard.setChecked(True)
        else:
            self.enablekeyboard.setChecked(False)

        self.enablekeyboard.triggered.connect(self.vkey_act)

        self.keyboardWidget = KeyboardWidget([self])
        self.keyboardWidget.setFixedSize(900, 356)

        self.fakewidgetkeyboard = QMainWindow()
        self.fakewidgetkeyboard.setFixedHeight(356)
        self.fakewidgetkeyboard.setStyleSheet(
            f'background-color: {getdata("key.bgcolor")};background-image: url({getdata("key.background")})')

        self.layout().addWidget(self.fakewidgetkeyboard)
        self.layout().addWidget(self.keyboardWidget)

        self.fakewidgetkeyboard.setGeometry(0, self.height() - 356, self.width(), 356)
        self.keyboardWidget.setGeometry(int(self.width() / 2) - int(950 / 2), self.height() - 356, 950, 356)

        self.fakewidgetkeyboard.hide()
        self.keyboardWidget.hide()

## Enter ##
class Enter (QMainWindow):

    def vkey_act(self):

        if getdata('key.enable')=='Yes':
            control.write_record('key.enable', 'No', '/etc/gui')
        else:
            control.write_record('key.enable', 'Yes', '/etc/gui')

    def reboot_act_(self):
            if not files.readall('/proc/info/os') == 'Pyabr':
                app.endall()
                self.Backend.hide()
                commands.reboot([])
                sys.exit(0)
            else:
                subprocess.call(['reboot'])

    def escape_act_(self):
            if not files.readall('/proc/info/os') == 'Pyabr':
                app.endall()
                self.Backend.hide()
                commands.shutdown([])
                sys.exit(0)
            else:
                subprocess.call(['poweroff'])

    def signout_act_(self):
            app.endall()
            commands.shutdown([])
            subprocess.call([sys.executable, 'vmabr.pyc', "gui-login"])
            sys.exit(0)

    def __init__(self,ports,username):
        super(Enter, self).__init__()
        self.setFont(f)

        ## username ##
        self.username = username.lower()

        ## Ports ##
        self.Backend = ports[0]
        self.Env = ports[1]

        ## Set port name ##
        self.setObjectName('Enter')

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        self.setWindowIcon(QIcon(res.get(getdata("logo"))))

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, int(getdata("width")), int(getdata("height")))
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##

        ##
        ## Menu Back
        ## Etcetra menu ##
        self.submenu = QMenuBar()  # Sub menu
        self.Backend.setMenuBar(self.submenu)

        # self.submenu.setStyleSheet(f'background-color:none;color:{submenu_bgcolor};')

        if getdata("submenu.direction") == 'ltr':
            self.submenu.setLayoutDirection(Qt.LeftToRight)
        elif getdata("submenu.direction") == 'rtl':
            self.submenu.setLayoutDirection(Qt.RightToLeft)

        # hide #
        if getdata("submenu.hide") == 'Yes':
            self.submenu.hide()

        self.submenu.setFont(f)

        ## Shell ##

        self.submenu.setCornerWidget(Shell([self.Backend, self]))

        self.etcmenu = QMenu()
        self.etcmenu.setFont(f)
        self.etcmenu.setTitle(res.get('@string/etcmenu'))
        self.etcmenu.setFont(f)
        self.submenu.addMenu(self.etcmenu)

        # Account menu #
        self.usermenu = QMenu()
        self.usermenu.setFont(f)
        self.etcmenu.addMenu(self.usermenu)

        # get username first + lastname
        fullname = ''

        username = self.username

        if username == 'guest':
            fullname = res.get('@string/guest')
        else:
            fullname = control.read_record('fullname', '/etc/users/' + username)

        self.usermenu.setTitle(fullname)
        self.usermenu.setFont(f)

        # Power menu #
        self.powermenu = QMenu()
        self.powermenu.setFont(f)
        self.etcmenu.addMenu(self.powermenu)
        self.powermenu.setTitle(res.get('@string/powermenu'))
        self.powermenu.setFont(f)

        # all actions in menus #

        self.signout = QAction(res.get('@string/signout'))
        self.signout.triggered.connect(self.signout_act_)
        self.signout.setFont(f)
        self.usermenu.addAction(self.signout)

        self.escape = QAction(res.get('@string/escape'))
        self.escape.triggered.connect(self.escape_act_)
        self.escape.setFont(f)
        self.powermenu.addAction(self.escape)

        self.restart = QAction(res.get('@string/restart'))
        self.restart.triggered.connect(self.reboot_act_)
        self.restart.setFont(f)
        self.powermenu.addAction(self.restart)

        self.enablekeyboard = QAction(res.get('@string/vkey'), checkable=True)
        self.etcmenu.addAction(self.enablekeyboard)
        if getdata('key.enable') == 'Yes':
            self.enablekeyboard.setChecked(True)
        else:
            self.enablekeyboard.setChecked(False)

        self.enablekeyboard.triggered.connect(self.vkey_act)

        ## Set colors ##
        self.setStyleSheet(f'color: {getdata("enter.fgcolor")};')
        self.backgroundButton.setStyleSheet(f'border:none;background-color: {getdata("enter.bgcolor")};')
        self.setStyleSheet(f'color: {getdata("enter.fgcolor")};')
        self.backgroundButton.setStyleSheet(f'border:none;background-color: {getdata("enter.bgcolor")};')
        self.setStyleSheet(f'color: {getdata("enter.fgcolor")};')
        self.backgroundButton.setStyleSheet(f'border:none;background-image: url({res.get(getdata("enter.background"))});')
        self.setStyleSheet(f'background-color:{getdata("enter.bgcolor")};color: {getdata("enter.fgcolor")};')
        self.resize(int(getdata("width")), int(getdata("height")))

        if getdata("sides") == 'No':
            self.setWindowFlag(Qt.FramelessWindowHint)

        self.loginw = LoginWidget([self.Backend,self])
        self.layout().addWidget (self.loginw)

        if getdata("fullscreen") == 'Yes':
            self.showFullScreen()
        else:
            self.show()

        self.keyboardWidget = KeyboardWidget([self])
        self.keyboardWidget.setFixedSize(900, 356)

        self.fakewidgetkeyboard = QMainWindow()
        self.fakewidgetkeyboard.setFixedHeight(356)
        self.fakewidgetkeyboard.setStyleSheet(
            f'background-color: {getdata("key.bgcolor")};background-image: url({getdata("key.background")})')

        self.layout().addWidget(self.fakewidgetkeyboard)
        self.layout().addWidget(self.keyboardWidget)

        self.fakewidgetkeyboard.setGeometry(0,self.height()-356,self.width(),356)
        self.keyboardWidget.setGeometry(int(self.width()/2)-int(950/2),self.height()-356,950,356)

        self.fakewidgetkeyboard.hide()
        self.keyboardWidget.hide()

class Unlock (QMainWindow):

    def __init__(self,ports,username):
        super(Unlock, self).__init__()
        self.setFont(f)

        ## username ##
        self.username = username.lower()

        ## Ports ##
        self.Backend = ports[0]
        self.Env = ports[1]

        ## Set port name ##
        self.setObjectName('Unlock')

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        self.setWindowIcon(QIcon(res.get(getdata("logo"))))

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, int(getdata("width")), int(getdata("height")))
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##

        ##
        ## Menu Back
        ## Etcetra menu ##
            ## Set colors ##
        self.setStyleSheet(f'color: {getdata("unlock.fgcolor")};')
        self.backgroundButton.setStyleSheet(f'border:none;background-color: {getdata("unlock.bgcolor")};')
        self.setStyleSheet(f'color: {getdata("unlock.fgcolor")};')
        self.backgroundButton.setStyleSheet(f'border:none;background-color: {getdata("unlock.bgcolor")};')
        self.setStyleSheet(f'color: {getdata("unlock.fgcolor")};')
        self.backgroundButton.setStyleSheet(f'border:none;background-image: url({res.get(getdata("unlock.background"))});')
        self.setStyleSheet(f'background-color:{getdata("unlock.bgcolor")};color: {getdata("unlock.fgcolor")};')
        self.resize(int(getdata("width")), int(getdata("height")))

        if getdata("sides") == 'No':
            self.setWindowFlag(Qt.FramelessWindowHint)

        self.loginw = LoginWidget([self.Backend,self])
        self.layout().addWidget (self.loginw)

        if getdata("fullscreen") == 'Yes':
            self.showFullScreen()
        else:
            self.show()

        self.keyboardWidget = KeyboardWidget([self])
        self.keyboardWidget.setFixedSize(900, 356)

        self.fakewidgetkeyboard = QMainWindow()
        self.fakewidgetkeyboard.setFixedHeight(356)
        self.fakewidgetkeyboard.setStyleSheet(
            f'background-color: {getdata("key.bgcolor")};background-image: url({getdata("key.background")})')

        self.layout().addWidget(self.fakewidgetkeyboard)
        self.layout().addWidget(self.keyboardWidget)

        self.fakewidgetkeyboard.setGeometry(0,self.height()-356,self.width(),356)
        self.keyboardWidget.setGeometry(int(self.width()/2)-int(950/2),self.height()-356,950,356)

        self.fakewidgetkeyboard.hide()
        self.keyboardWidget.hide()

class AppListView(QListView):
    def format(self, it):
        if files.isfile (it.whatsThis()):
            name = it.text().replace('.desk','')
            subname = res.etc(name,f'name[{getdata("locale")}]')
            icon = res.etc(name,'logo')
            it.setText(subname)
            it.setFont(f)
            it.setIcon(QIcon(res.get(icon)))

    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]
        self.setFont(f)
        self.username = self.Env.username


        self.setStyleSheet("""
QScrollBar
{
background : white;
}
QScrollBar::handle
{
background : #123456;
border-radius: 6% 6%;
}
QScrollBar::handle::pressed
{
background : #ABCDEF;
border-radius: 6% 6%;
}""".replace('white',getdata("menu.scroll.bgcolor")).replace('#123456',getdata("menu.scroll.color")).replace('6',getdata("menu.scroll.round-size")).replace('#ABCDEF',getdata("menu.scroll.color-hover")))

        # Get font #

        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        self.listdir = files.list('/usr/share/applications')
        self.listdir.sort()

        for text in self.listdir:

            if res.etc(text.replace('.desk',''),'application')=='Yes':
                it = QStandardItem(text.replace('.desk',''))
                it.setWhatsThis(f'/usr/share/applications/{text}')
                self.format(it)
                self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            self.Widget.hide()
            self.Env.RunApp(self.item.whatsThis().replace('.desk','').replace('/usr/share/applications/',''),None)
            files.write('/proc/info/id','desktop')

class GameListView(QListView):
    def format(self, it):
        if files.isfile (it.whatsThis()):
            name = it.text().replace('.desk','')
            subname = res.etc(name,f'name[{getdata("locale")}]')
            icon = res.etc(name,'logo')
            it.setText(subname)
            it.setFont(f)
            it.setIcon(QIcon(res.get(icon)))

    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]
        self.setFont(f)
        self.username = self.Env.username


        self.setStyleSheet("""
        QScrollBar
        {
        background : white;
        }
        QScrollBar::handle
        {
        background : #123456;
        border-radius: 6% 6%;
        }
        QScrollBar::handle::pressed
        {
        background : #ABCDEF;
        border-radius: 6% 6%;
        }""".replace('white', getdata("menu.scroll.bgcolor")).replace('#123456', getdata("menu.scroll.color")).replace('6',
                                                                                                 getdata("menu.scroll.round-size")).replace(
            '#ABCDEF', getdata("menu.scroll.color-hover")))

        # Get font #

        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        self.listdir = files.list('/usr/share/applications')
        self.listdir.sort()

        for text in self.listdir:

            if res.etc(text.replace('.desk',''),'game')=='Yes':
                it = QStandardItem(text.replace('.desk',''))
                it.setWhatsThis(f'/usr/share/applications/{text}')
                self.format(it)
                self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            self.Widget.hide()
            self.Env.RunApp(self.item.whatsThis().replace('.desk','').replace('/usr/share/applications/',''),None)
            files.write('/proc/info/id','desktop')


class ThemeListView(QListView):
    def format(self, it):
        if files.isfile (it.whatsThis()):
            name = it.text().replace('.desk','')
            subname = control.read_record(f'name[{getdata("locale")}]',f'/usr/share/themes/{name}.desk')
            icon = control.read_record(f'logo',f'/usr/share/themes/{name}.desk')
            it.setText(subname)
            it.setFont(f)
            it.setIcon(QIcon(res.get(icon)))

    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]
        self.setFont(f)
        self.username = self.Env.username

        self.setStyleSheet("""
        QScrollBar
        {
        background : white;
        }
        QScrollBar::handle
        {
        background : #123456;
        border-radius: 6% 6%;
        }
        QScrollBar::handle::pressed
        {
        background : #ABCDEF;
        border-radius: 6% 6%;
        }""".replace('white', getdata("menu.scroll.bgcolor")).replace('#123456', getdata("menu.scroll.color")).replace('6',
                                                                                                 getdata("menu.scroll.round-size")).replace(
            '#ABCDEF', getdata("menu.scroll.color-hover")))


        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        self.listdir = files.list('/usr/share/themes')
        self.listdir.sort()

        for text in self.listdir:
            if text.endswith ('.desk'):
                it = QStandardItem(text.replace('.desk',''))
                it.setWhatsThis(f'/usr/share/themes/{text}')
                self.format(it)
                self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            if self.Env.username=='guest':
                files.write('/proc/info/id', 'desktop')
                self.Env.RunApp('text', [res.get('@string/perm'), res.get('@string/guestperm')])
                files.write('/proc/info/id', 'desktop')
            elif not control.read_record ('theme-name','/etc/gui')==control.read_record('theme-name',self.item.whatsThis()):
                self.Widget.hide()
                Script(control.read_record('exec', self.item.whatsThis()))
                self.Env.signout_act()
                files.write('/proc/info/id','desktop')
            else:
                files.write('/proc/info/id', 'desktop')
                self.Env.RunApp('text', [self.item.text(), res.get('@string/selectedon')])
                files.write('/proc/info/id', 'desktop')

class SessionListView(QListView):
    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]

        self.username = self.Env.username
        self.setFont(f)

        self.setStyleSheet("""
        QScrollBar
        {
        background : white;
        }
        QScrollBar::handle
        {
        background : #123456;
        border-radius: 6% 6%;
        }
        QScrollBar::handle::pressed
        {
        background : #ABCDEF;
        border-radius: 6% 6%;
        }""".replace('white', getdata("menu.scroll.bgcolor")).replace('#123456', getdata("menu.scroll.color")).replace('6',
                                                                                                 getdata("menu.scroll.round-size")).replace(
            '#ABCDEF', getdata("menu.scroll.color-hover")))

        # Get font #
        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        it = QStandardItem('escape')
        it.setText(res.get('@string/escape')) # escape_
        it.setWhatsThis('escape')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys',"escape-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('restart')
        it.setText(res.get('@string/restart'))
        it.setWhatsThis('restart')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys', "restart-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('lock')
        it.setText(res.get('@string/lock'))
        it.setWhatsThis('lock')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys', "lock-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('logout')
        it.setText(res.get('@string/signout'))
        it.setWhatsThis('logout')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys', "logout-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('switchuser')
        it.setText(res.get('@string/switchuser'))
        it.setWhatsThis('switchuser')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys', "switchuser-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('suspend')
        it.setText(res.get('@string/sleep'))
        it.setFont(f)
        it.setWhatsThis('suspend')
        it.setIcon(QIcon(res.get(res.etc('pysys', "suspend-icon"))))
        self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            self.Widget.hide()

            if self.item.whatsThis()=='escape':
                self.Env.escape_act()
            elif self.item.whatsThis()=='restart':
                self.Env.reboot_act()
            elif self.item.whatsThis()=='suspend':
                self.Env.sleep_act()
            elif self.item.whatsThis()=='logout':
                self.Env.signout_act()
            elif self.item.whatsThis()=='switchuser':
                self.Env.switchuser_act()
            elif self.item.whatsThis()=='lock':
                self.Env.lock_act()

            files.write('/proc/info/id','desktop')

## Taskbar ##
class TaskBar (QToolBar):
    def __init__(self,ports):
        super(TaskBar,self).__init__()

        ## Ports ##
        self.Backend = ports[0]
        self.Env = ports[1]
        self.setFont(f)
        ## Set username ##
        self.username = self.Env.username

            ## Get DATAS ###################


        # styles #

        self.setStyleSheet('background-color: '+getdata("taskbar.bgcolor")+";color: "+getdata("taskbar.fgcolor")+";")

        # location #
        if getdata("taskbar.location")=='top':
            self.Env.addToolBar (Qt.TopToolBarArea,self)
        elif getdata("taskbar.location")=='left':
            self.Env.addToolBar(Qt.LeftToolBarArea, self)
        elif getdata("taskbar.location")=='right':
            self.Env.addToolBar(Qt.RightToolBarArea, self)
        elif getdata("taskbar.location")=='bottom':
            self.Env.addToolBar(Qt.BottomToolBarArea, self)

        # locked #
        if getdata("taskbar.locked")=='Yes':
            self.setMovable(False)
        else:
            self.setMovable(True)

        # float #
        if getdata("taskbar.float")=='Yes':
            self.setFloatable(True)
        else:
            self.setFloatable(False)

        # size #
        self.setMinimumSize(QSize(int(getdata("taskbar.size")),int(getdata("taskbar.size"))))
        self.setIconSize(QSize(int(getdata("taskbar.size")),int(getdata("taskbar.size")))) # https://stackoverflow.com/questions/21133612/how-to-change-iconsize-of-qtoolbutton

        self.btnMenu = QToolButton()
        self.btnMenu.setIcon(QIcon(res.get(getdata("menu"))))
        self.btnMenu.setMinimumSize(int(getdata("taskbar.size")), int(getdata("taskbar.size")))
        self.btnMenu.setObjectName('btnMenu')
        self.btnMenu.clicked.connect (self.menuApps)

        if getdata('taskbar.icon.style')=='Yes':
            self.btnMenu.setStyleSheet("""
                                   QToolButton {
                                       background-color: {2};
                                       border-radius: {1}% {1}%;
                                       border-style: solid;
                                       border-color: {4};
                                       border-width: 1%;
                                   }
                                   QToolButton::hover {
                                       background-color: {3};
                                       border-radius: {1}% {1}%;
                                       border-style: solid;
                                       border-color: {5};
                                       border-width: 1%;
                                   }
                                   """.replace('{1}', str(int(getdata('taskbar.size')) / 2)).replace('{2}', getdata(
                'taskbar.icon.bgcolor')).replace('{3}', getdata('taskbar.icon.bgcolor-hover')).replace('{4}', getdata(
                'taskbar.icon.border-color')).replace('{5}', getdata('taskbar.icon.border-color-hover')))
        self.addWidget(self.btnMenu)

        # pins #

        appsx = files.list('/usr/share/applications')
        appsx.sort()

        for i in appsx:
            find = '/usr/share/applications/'+i

            i = i.replace('.desk','')

            if control.read_record('pin',find)=='Yes':
                # app logo
                applogo = control.read_record('logo', find)
                # design
                self.btnApp = QToolButton()
                if not applogo==None:
                    self.btnApp.setIcon(QIcon(res.get(applogo)))
                self.btnApp.setMinimumSize(int(getdata("taskbar.size")),int(getdata("taskbar.size")))
                self.btnApp.setObjectName(i)

                if getdata('taskbar.icon.style') == 'Yes':
                    self.btnApp.setStyleSheet("""
                                    QToolButton {
                                        background-color: {2};
                                        border-radius: {1}% {1}%;
                                        border-style: solid;
                                        border-color: {4};
                                        border-width: 1%;
                                    }
                                    QToolButton::hover {
                                        background-color: {3};
                                        border-radius: {1}% {1}%;
                                        border-style: solid;
                                        border-color: {5};
                                        border-width: 1%;
                                    }
                                    """.replace('{1}', str(int(getdata('taskbar.size')) / 2)).replace('{2}', getdata(
                        'taskbar.icon.bgcolor')).replace('{3}', getdata('taskbar.icon.bgcolor-hover')).replace('{4}',
                                                                                                               getdata(
                                                                                                                   'taskbar.icon.border-color')).replace(
                        '{5}', getdata('taskbar.icon.border-color-hover')))

                self.btnApp.clicked.connect (self.RunApplication)
                self.addWidget(self.btnApp)

    menu_click = False

    def menuApps (self):
        if self.menu_click==False:
            self.w = MenuApplications([self.Backend,self.Env])
            self.w.setStyleSheet('background-color: white;')
            self.Env.layout().addWidget(self.w)
            self.menu_click = True
        else:
            self.w.hide()
            self.menu_click = False

    def RunApplication (self):
        sender = self.sender().objectName()
        self.Env.RunApp (sender,None)
        files.write('/proc/info/id','desktop')

# @Built in QLineEdit

class BLineEdit (QLineEdit):
    def __init__(self):
        super(BLineEdit, self).__init__()
        self.setFocusPolicy(Qt.ClickFocus)
        self.setFont(QFont(getdata("font"),int(getdata("fontsize"))))
        self.setObjectName('BLineEdit')

    def focusInEvent(self, e):

        if getdata("key.enable")=='Yes':
            self.Env.keyboardWidget.currentTextBox = self
            self.Env.keyboardWidget.show()
            self.Env.fakewidgetkeyboard.show()

            self.Env.fakewidgetkeyboard.activateWindow()
            self.Env.fakewidgetkeyboard.raise_()

            self.Env.keyboardWidget.activateWindow()
            self.Env.keyboardWidget.raise_()

        # self.setStyleSheet("border: 1px solid red;")
        super(BLineEdit, self).focusInEvent(e)

    def mousePressEvent(self, e):
        # print(e)
        # self.setFocusPolicy(Qt.ClickFocus)
        super(BLineEdit, self).mousePressEvent(e)

class BTextEdit (QTextEdit):
    def __init__(self):
        super(BTextEdit, self).__init__()
        self.setFocusPolicy(Qt.ClickFocus)
        self.setFont(QFont(getdata("font"), int(getdata("fontsize"))))
        self.setObjectName('BTextEdit')

    def focusInEvent(self, e):

        if getdata("key.enable")=='Yes':
            self.Env.keyboardWidget.currentTextBox = self
            self.Env.keyboardWidget.show()
            self.Env.fakewidgetkeyboard.show()

            self.Env.fakewidgetkeyboard.activateWindow()
            self.Env.fakewidgetkeyboard.raise_()

            self.Env.keyboardWidget.activateWindow()
            self.Env.keyboardWidget.raise_()

        # self.setStyleSheet("border: 1px solid red;")
        super(BTextEdit, self).focusInEvent(e)

    def mousePressEvent(self, e):
        # print(e)
        # self.setFocusPolicy(Qt.ClickFocus)
        super(BTextEdit, self).mousePressEvent(e)

class BCodeEdit (QsciScintilla):
    def __init__(self):
        super(BCodeEdit, self).__init__()
        self.setFocusPolicy(Qt.ClickFocus)
        self.setObjectName('BCodeEdit')

    def focusInEvent(self, e):

        if getdata("key.enable")=='Yes':
            self.Env.keyboardWidget.currentTextBox = self
            self.Env.keyboardWidget.show()
            self.Env.fakewidgetkeyboard.show()

            self.Env.fakewidgetkeyboard.activateWindow()
            self.Env.fakewidgetkeyboard.raise_()

            self.Env.keyboardWidget.activateWindow()
            self.Env.keyboardWidget.raise_()

        # self.setStyleSheet("border: 1px solid red;")
        super(BCodeEdit, self).focusInEvent(e)

    def mousePressEvent(self, e):
        # print(e)
        # self.setFocusPolicy(Qt.ClickFocus)
        super(BCodeEdit, self).mousePressEvent(e)

class MenuApplications (QMainWindow):
    def __init__(self,ports):
        super(MenuApplications, self).__init__()

        ## Ports ##
        self.Backend = ports[0]
        self.Env = ports[1]
        self.setFont(f)

        files.write('/proc/info/id','desktop')

        self.username = self.Env.username

        self.setGeometry(0,0,self.Env.width(),self.Env.height())
        self.setStyleSheet('background-color: white')


        size = int(getdata("taskbar.size"))

        if self.Env.width()>1000 and self.Env.height()>720:
            if getdata("taskbar.location") == 'bottom':
                self.setGeometry(0, int(self.Env.height() / 3), int(self.Env.width() / 3),
                                 int(self.Env.height() / 1.5) - size - 15)
            elif  getdata("taskbar.location")  == 'top':
                self.setGeometry(0, size + 15, int(self.Env.width() / 3), (self.Env.height() / 1.5) - size - 15)
            elif  getdata("taskbar.location")  == "left":
                self.setGeometry(size + 15, 0, int(self.Env.width() / 3) - size - 15, int(self.Env.height() / 1.5))
            elif  getdata("taskbar.location")  == "right":
                self.setGeometry(self.Env.width() - (self.Env.width() / 3), 0, (self.Env.width() / 3) - size - 15,
                                 int(self.Env.height() / 1.5))
            else:
                self.setGeometry(0, 0, self.Env.width(), self.Env.height())

        else:
            self.setGeometry(0, 0, self.Env.width(), self.Env.height()-size-15)


        self.tabs = QTabWidget()
        self.tabs.setFont(f)
        if getdata('menu.tab.position')=='W':
            self.tabs.setTabPosition(QTabWidget.West)
        elif getdata('menu.tab.position')=='N':
            self.tabs.setTabPosition(QTabWidget.North)
        elif getdata('menu.tab.position')=='E':
            self.tabs.setTabPosition(QTabWidget.East)
        elif getdata('menu.tab.position')=='S':
            self.tabs.setTabPosition(QTabWidget.South)
        else:
            self.tabs.setTabPosition(QTabWidget.North)

        self.x = AppListView([self.Env, self])
        self.x1 = GameListView([self.Env,self])
        self.x2 = ThemeListView([self.Env,self])
        self.x3 = SessionListView([self.Env,self])

        self.tabs.addTab(self.x, res.get('@string/apps'))
        self.tabs.addTab(self.x1, res.get('@string/games'))
        self.tabs.addTab(self.x2, res.get('@string/themes'))
        self.tabs.addTab(self.x3, res.get('@string/sessions'))
        self.setCentralWidget(self.tabs)

class AppWidget (QMainWindow):
    def Resize(self,mainw,w,h):
        self.w = w
        self.h = h

        if self.w<self.Env.width() and self.h<self.Env.height():
            mainw.resize(self.w,self.h)
            self.resize(self.w,self.h+int(getdata("appw.title.size")))
        else:
            self.setGeometry(0, 0, self.Env.width(), self.Env.height())
            mainw.resize(self.Env.width(), self.Env.height() - int(getdata("appw.title.size")))

    def SetWindowTitle (self,text):
        self.titletext.setText(text)
        self.titletext.setFont(f)

    def WindowTitle (self):
        return self.titletext.text()

    def SetWindowIcon (self,icon):
        self.iconwidget.setPixmap(icon.pixmap(int(getdata("appw.title.size"))-18,int(getdata("appw.title.size"))-18))


    def Close (self):
        if files.isfile ('/proc/info/key'):
            files.remove('/proc/info/key')
        self.close()

    maxbtn = True

    def DisableFloat (self):
        if self.maxbtn:
            self.btnMax.setEnabled(False)
            self.maxbtn = False
        else:
            self.btnMax.setEnabled(True)
            self.maxbtn = True

    max = False
    save_w = 0
    save_h = 0
    save_ww = 0
    save_wh = 0

    def ShowMaximize(self):

        size = int(getdata("taskbar.size"))

        if self.max == False:
            self.save_w = self.width()
            self.save_h = self.height()
            self.save_ww = self.mainWidget.width()
            self.save_wh = self.mainWidget.height()

            size = int(size)

            if  getdata("taskbar.location") =='bottom':
                self.setGeometry(0, 0, self.Env.width(), self.Env.height()-size-15)
                self.mainWidget.resize (self.Env.width(),self.Env.height()-int(getdata("appw.title.size"))-size-15)
                self.titlebar.setGeometry(0,0,self.Env.width(),int(getdata("appw.title.size")))

            elif  getdata("taskbar.location") =='top':
                self.setGeometry(0, size+15, self.Env.width(), self.Env.height() - size - 15)
                self.mainWidget.resize(self.Env.width(), self.Env.height() - getdata("appw.title.size") - size - 15)
                self.titlebar.setGeometry(0, 0, self.Env.width(), int(getdata("appw.title.size")))

            elif  getdata("taskbar.location") =="left":
                self.setGeometry(size+15, 0, self.Env.width() - size - 15, self.Env.height())
                self.mainWidget.resize(self.Env.width()-size-15, self.Env.height() - int(getdata("appw.title.size")))
                self.titlebar.setGeometry(0, 0, self.Env.width()-size-15, int(getdata("appw.title.size")))

            elif  getdata("taskbar.location") =="right":
                self.setGeometry(0, 0, self.Env.width() - size - 15, self.Env.height())
                self.mainWidget.resize(self.Env.width()-size-15, self.Env.height() - int(getdata("appw.title.size")))
                self.titlebar.setGeometry(0, 0, self.Env.width()-size-15, int(getdata("appw.title.size")))
            else:
                self.setGeometry(0, 0, self.Env.width(), self.Env.height())
                self.mainWidget.resize(self.Env.width(), self.Env.height() - int(getdata("appw.title.size")))
                self.titlebar.setGeometry(0, 0, self.Env.width(), int(getdata("appw.title.size")))

            self.mainWidget.update()

            self.max = True
        else:
            self.setGeometry(int(self.Env.width()/2)-int(self.save_w/2),int(self.Env.height()/2)-int(self.save_h/2),self.save_w,self.save_h)
            self.titlebar.setGeometry(0, 0, self.save_w, int(getdata("appw.title.size")))
            self.mainWidget.resize(self.save_ww,self.save_wh)
            self.mainWidget.update()
            self.max = False

    def __init__(self,ports):
        super(AppWidget, self).__init__()
        self.setFont(f)
        self.Backend = ports[0]
        self.Env = ports[1]
        self.appname = ports[2]
        self.external = ports[3]

        self.setFocusPolicy(Qt.StrongFocus)

        # user
        self.username = self.Env.username

        app.start(self.appname)  # start the application

        self.setObjectName(self.appname)

        exec = control.read_record('exec', '/usr/share/applications/' + self.appname + ".desk")

        if not exec == None:
            exec = importlib.import_module(exec)
        else:
            self.close()

        # title bar #
        self.titlebar = QWidget()
        self.titlebar.setStyleSheet(f'background-color: {getdata("appw.title.bgcolor")};color: {getdata("appw.title.fgcolor")};')

        self.layouts = QHBoxLayout()
        self.titlebar.setLayout(self.layouts)

        # icon widget #
        self.icon = QIcon(res.get(getdata("appw.logo")))
        self.iconwidget = QLabel()
        self.iconwidget.setPixmap(self.icon.pixmap(int(getdata("appw.title.size"))-18,int(getdata("appw.title.size"))-18))
        self.iconwidget.resize(int(getdata("appw.title.size")),int(getdata("appw.title.size")))
        self.layouts.addWidget(self.iconwidget)

        self.iconwidget.setGeometry(0,0,int(getdata("appw.title.size")),int(getdata("appw.title.size")))

        # text title #
        self.titletext = QLabel()
        self.titletext.setStyleSheet(f'background-color:  {getdata("appw.title.bgcolor")};color: {getdata("appw.title.fgcolor")};')
        self.titletext.setMaximumWidth(self.titlebar.width())
        self.titletext.setGeometry(int(getdata("appw.title.size")),0,self.titlebar.width(),int(getdata("appw.title.size")))

        self.titletext.setFont(f)

        self.layouts.addWidget(self.titletext)

        round = '0'

        if getdata("appw.title.btn-round")=='Yes':
            round = str(int((int(getdata("appw.title.size"))) - 16) / 2)

        # float button #
        self.btnMax = QToolButton()
        self.btnMax.setIcon(QIcon(res.get(getdata("appw.title.float"))))
        self.btnMax.setMinimumSize(int(getdata("appw.title.size"))-15,int(getdata("appw.title.size"))-15)
        self.btnMax.setGeometry(self.titlebar.width()-100,0,int(getdata("appw.title.size")),int(getdata("appw.title.size")))
        self.btnMax.clicked.connect(self.ShowMaximize)
        self.btnMax.setStyleSheet('QToolButton {border-radius: {0}% {0}%;} QToolButton::hover {border-radius: {0}% {0}%;background-color: {1}}'.replace("{1}",getdata("appw.title.float-hover")).replace("{0}",round))

        self.layouts.addWidget(self.btnMax)

        self.btnEscape = QToolButton()
        self.btnEscape.setIcon(QIcon(res.get(getdata("appw.title.close"))))
        self.btnEscape.setMinimumSize(int(getdata("appw.title.size"))-15, int(getdata("appw.title.size"))-15)
        self.btnEscape.setGeometry(self.titlebar.width()-int(getdata("appw.title.size")),0,int(getdata("appw.title.size")),int(getdata("appw.title.size")))
        self.btnEscape.clicked.connect (self.Close)
        self.btnEscape.setStyleSheet('QToolButton {border-radius: {0}% {0}%;} QToolButton::hover {border-radius: {0}% {0}%;background-color: {1}}'.replace("{1}",getdata("appw.title.close-hover")).replace("{0}",round))
        self.layouts.addWidget(self.btnEscape)

        self.whitewidget = QMainWindow()
        self.whitewidget.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};')
        self.setCentralWidget(self.whitewidget)

        # center widget #
        self.mainWidget = exec.MainApp([self.Backend,self.Env,self,self.appname,self.external])
        self.mainWidget.setGeometry(0,int(getdata("appw.title.size")),self.width(),self.height()-int(getdata("appw.title.size")))
        self.titlebar.setGeometry(0, 0, self.width(), int(getdata("appw.title.size")))
        self.setGeometry(int(self.Env.width()/2)-int(self.width()/2),int(self.Env.height()/2)-int(self.height()/2),self.width(),self.height())

        self.layout().addWidget(self.mainWidget)
        self.layout().addWidget(self.titlebar)

        if getdata("appw.shadow")=="Yes":
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.setGraphicsEffect(shadow)

    # https://stackoverflow.com/questions/41784521/move-qtwidgets-qtwidget-using-mouse
    # https://stackoverflow.com/questions/40622095/pyqt5-closeevent-method
    homeAction = None

    oldPos = QPoint()

    def mousePressEvent(self, evt):
        """Select the toolbar."""
        self.oldPos = evt.globalPos()

        app.switch(self.appname)
        self.activateWindow()
        self.raise_()

        if files.isfile ('/proc/info/key'): files.remove('/proc/info/key')

    def mouseMoveEvent(self, evt):
        """Move the toolbar with mouse iteration."""

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

## Shell ##
class Shell (QWidget):
    def __init__(self,ports):
        super(Shell, self).__init__()
        self.setFont(f)
        self.boxl = QVBoxLayout() # layout
        self.setLayout(self.boxl)

        # ports #
        self.Backend = ports[0]
        self.Env = ports[1]

        # shells #
        shells = files.list('/usr/share/shells')

        for i in shells:
            exec = control.read_record ('exec','/usr/share/shells/'+i)
            self.shell = importlib.import_module(exec)
            self.shell = self.shell.MainApp ([self.Backend,self.Env,self])
            self.boxl.addWidget(self.shell)

        # self.threadIsStarted = False
## Desktop ##
class Desktop (QMainWindow):

    def RunApp (self,appname,external):
        app.switch(appname)
        files.write('/proc/info/su', self.username)

        if appname==getdata("terminal"):
            files.write('/proc/info/pass', self.password)
            self.layout().addWidget(AppWidget([self.Backend, self,getdata("terminal") , external]))

        elif files.isfile(f'/usr/share/applications/{appname}.desk'):
            sudoprocess = res.etc(appname,'sudoprocess')
            if sudoprocess=='Yes':
                if not files.readall('/proc/info/sudo')==appname:
                    self.layout().addWidget(AppWidget([self.Backend, self, 'sudoprocess',[appname]]))
                else:
                    self.layout().addWidget(AppWidget([self.Backend, self, appname, external]))
            else:
                self.layout().addWidget(AppWidget([self.Backend, self, appname,external]))

        else:
            files.write('/proc/info/id','desktop')
            self.layout().addWidget(AppWidget([self.Backend, self, 'text', [res.get('@string/notf'), res.get('@string/notfm')]]))
            files.write('/proc/info/id','desktop')

    def StartupApplication (self):

        self.suapp = control.read_list('/etc/suapp')

        if not files.readall('/etc/suapp')=='':
            for i in self.suapp:
                x = i.split(' ')
                strv = ''
                for j in x[1:]:
                    if strv=='':
                        strv+=j
                    else:
                        strv+=' '+j
                print(strv)
                self.RunApp(x[0],[strv])
                files.write('/proc/info/id','desktop')

    def RunApplication (self):
        sender = self.sender().objectName()
        self.RunApp (sender.replace('.desk',''),None)
        files.write('/proc/info/id','desktop')

    def escape_act (self):
        files.write('/proc/info/id','desktop')
        self.RunApp('bool',[res.get('@string/esc'),res.get('@string/escm'),self.escape_act_])
        files.write('/proc/info/id', 'desktop')
        

    def escape_act_(self,yes):
        if yes:
            if not files.readall('/proc/info/os')=='Pyabr':
                app.endall()
                self.Backend.hide()
                commands.shutdown([])
                sys.exit(0)
            else:
                subprocess.call(['poweroff'])

    def reboot_act (self):
        files.write('/proc/info/id','desktop')
        self.RunApp('bool', [res.get('@string/rb'), res.get('@string/rbm'), self.reboot_act_])
        files.write('/proc/info/id','desktop')

    def reboot_act_(self,yes):
        if yes:
            if not files.readall('/proc/info/os') == 'Pyabr':
                app.endall()
                self.Backend.hide()
                commands.reboot([])
                sys.exit(0)
            else:
                subprocess.call(['reboot'])

    def print_screen_act (self):
        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        files.write('/proc/info/id','desktop')
        # https://stackoverflow.com/questions/51361674/is-there-a-way-to-take-screenshot-of-a-window-in-pyqt5-or-qt5
        #

        os.environ['TZ'] = files.readall( "/proc/info/tz")  # https://stackoverflow.com/questions/1301493/setting-timezone-in-python
        time.tzset()

        screenshot.save(files.input(res.get('@string/pictures'))+f'/Screenshot {datetime.datetime.now().ctime()}.png', 'png')
        files.write('/proc/info/id', 'desktop')

    def wakeup_act (self):
        self.submenu.show()
        self.taskbar.show()
        self.BtnWakeUp.hide()

    def sleep_act (self):
        self.submenu.hide()
        self.taskbar.hide()
        self.BtnWakeUp = QPushButton()
        self.BtnWakeUp.setStyleSheet('background: black;color: black;border: black;')
        self.BtnWakeUp.setText('')
        self.BtnWakeUp.setCursor(Qt.BlankCursor)
        self.BtnWakeUp.clicked.connect (self.wakeup_act)
        self.setCentralWidget(self.BtnWakeUp)

    def signout_act (self):
        files.write('/proc/info/id','desktop')
        self.RunApp('bool', [res.get('@string/sg'), res.get('@string/sgm'), self.signout_act_])
        files.write('/proc/info/id','desktop')

    def signout_act_ (self,yes):
        if yes:
            app.endall()
            commands.shutdown([])
            subprocess.call([sys.executable, 'vmabr.pyc', "gui-login"])
            sys.exit(0)

    def switchuser_act (self):
        files.write('/proc/info/id','desktop')
        self.RunApp('bool', [res.get('@string/sau'), res.get('@string/saum'), self.switchuser_act_])
        files.write('/proc/info/id','desktop')

    def switchuser_act_(self,yes):
        if yes:
            files.create('/tmp/switched-user')
            subprocess.call([sys.executable, 'vmabr.pyc', "gui-login"])  # just run the login

    def unlock_act (self):
        if self.username=='guest':
            self.submenu.show()
            self.taskbar.show()
            self.backgroundButton.show()
            self.BtnUnlock.hide()
            self.lock.hide()
        else:
            subprocess.call([sys.executable,'vmabr.pyc','gui-unlock',self.username])

    def showTime_lock (self):

        try:
        # getting current time
            current_time = QTime.currentTime()

        # converting QTime object to string
            label_time = current_time.toString(getdata("lock.clock.format"))

        # showing it to the label
            self.lblClock.setText(res.num(label_time))
            self.lblClock.setFont(QFont(f.family(),int(getdata('lock.clock.size'))))
        except:
            pass

    def lock_act (self):
        self.lock = QMainWindow()

        if files.isfile ('/tmp/unlock'):
            files.remove('/tmp/unlock')
        else:
            self.submenu.hide()
            self.taskbar.hide()
            self.backgroundButton.hide()
            self.BtnUnlock = QPushButton()
            self.BtnUnlock.setText('')
            self.lock.setCentralWidget(self.BtnUnlock)
            ## Check background or bgcolor in users ##

            ## Set bgcolor and background ##

            ## Set colors ##

            self.BtnUnlock.setStyleSheet(
                f'border:none;background-color: {getdata("lock.bgcolor")};color:{getdata("lock.fgcolor")};')
            self.BtnUnlock.setStyleSheet(
                f'border:none;background-image: url({res.get(getdata("lock.background"))});color: {getdata("lock.fgcolor")};')

            ## Get informations ##
            cs = files.readall('/proc/info/cs')
            ver = files.readall('/proc/info/ver')
            cd = files.readall('/proc/info/cd')

            self.lock.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

            ## Clock ##
            # creating a timer object
            timer = QTimer(self)

            # adding action to timer
            timer.timeout.connect(self.showTime_lock)

            # update the timer every second
            timer.start(1000)

            self.lock.setWindowIcon(QIcon(res.get(getdata("logo"))))

            self.lock.resize(int(getdata('width')), int(getdata("height")))
            self.BtnUnlock.resize(int(getdata("width")), int(getdata("height")))

            # lbl Clock #
            self.lblClock = QLabel()
            self.lock.layout().addWidget(self.lblClock)

            # shadow #
            if getdata("lock.clock.shadow") == 'Yes':
                ## Shadow ##
                # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
                shadow = QGraphicsDropShadowEffect()
                shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
                shadow.setOffset(0)
                shadow.setBlurRadius(10)
                self.lblClock.setGraphicsEffect(shadow)

            # font size clock #

            self.lblClock.setFont(f)
            self.lblClock.setAlignment(Qt.AlignCenter)

            # color clock #
            self.lblClock.setStyleSheet('background:none;color:' + getdata("lock.clock.color"))

            # set lbl Clock location #
            if getdata('lock.clock.location') == 'top':
                self.lblClock.setGeometry(int(self.BtnUnlock.width() / 2) - int(self.lblClock.width() / 2), 0,
                                          self.lblClock.width(), self.lblClock.height())
            elif getdata('lock.clock.location') == 'center':
                self.lblClock.setGeometry(int(self.BtnUnlock.width() / 2) - int(self.lblClock.width() / 2),
                                          int(self.lock.height() / 2) - int(self.lblClock.height() / 2),
                                          self.lblClock.width(),
                                          self.lblClock.height())

            elif getdata('lock.clock.location') == 'left':
                self.lblClock.setGeometry(0,
                                          int(self.lock.height() / 2) - int(self.lblClock.height() / 2),
                                          self.lblClock.width(),
                                          self.lblClock.height())

            elif getdata('lock.clock.location') == 'right':
                self.lblClock.setGeometry(self.BtnUnlock.width() - self.lblClock.width(),
                                          int(self.lock.height() / 2) - int(self.lblClock.height() / 2),
                                          self.lblClock.width(),
                                          self.lblClock.height())
            elif getdata('lock.clock.location') == 'bottom':
                self.lblClock.setGeometry(int(self.BtnUnlock.width() / 2) - int(self.lblClock.width() / 2),
                                          self.lock.height() - self.lblClock.height(),
                                          self.lblClock.width(),
                                          self.lblClock.height())

            elif getdata('lock.clock.location') == 'top/left':
                self.lblClock.setGeometry(0,
                                          0,
                                          self.lblClock.width(),
                                          self.lblClock.height())

            elif getdata('lock.clock.location') == 'top/right':
                self.lblClock.setGeometry(self.BtnUnlock.width() - self.lblClock.width(),
                                          0,
                                          self.lblClock.width(),
                                          self.lblClock.height())

            elif getdata('lock.clock.location') == 'bottom/left':
                self.lblClock.setGeometry(0,
                                          self.BtnUnlock.height() - self.lblClock.height(),
                                          self.lblClock.width(),
                                          self.lblClock.height())

            elif getdata('lock.clock.location') == 'bottom/right':
                self.lblClock.setGeometry(self.BtnUnlock.width() - self.lblClock.width(),
                                          self.BtnUnlock.height() - self.lblClock.height(),
                                          self.lblClock.width(),
                                          self.lblClock.height())

            self.BtnUnlock.clicked.connect(self.unlock_act)

            self.layout().addWidget(self.lock)
            self.refreshlock()

    def refreshlock (self):
        if files.isfile('/tmp/unlock'):
            files.remove('/tmp/unlock')
            self.lock.hide()
            self.submenu.show()
            self.taskbar.show()
            self.backgroundButton.show()
        else:
            QTimer.singleShot(1,self.refreshlock)

    def Loop(self):
        self.update()

        ## Start start applications

        if files.isfile ('/tmp/start.tmp'):
            appx = files.readall ('/tmp/start.tmp')
            files.remove('/tmp/start.tmp')

            self.RunApp(appx,[None])

        QTimer.singleShot(1,self.Loop)


    def vkey_act (self):

        if getdata('key.enable')=='Yes':
            control.write_record('key.enable','No','/etc/gui')
        else:
            control.write_record('key.enable', 'Yes','/etc/gui')

    def __init__(self,ports,username,password):
        super(Desktop, self).__init__()
        self.setFont(f)
        ## Set port name ##
        self.setObjectName('Desktop')

        ## ports ##
        self.Backend = ports[0]

        ## username ##
        self.username = username.lower()
        self.password = password
        ## Setting ups ##
        files.write("/proc/info/su", self.username)
        permissions.user = self.username

        ## Check user ##
        if not self.username == "guest":
            if not files.isfile("/etc/users/" + self.username):
                exit(0)

            user = control.read_record("username", "/etc/users/" + self.username)
            hashname = hashlib.sha3_256(
                str(self.username).encode()).hexdigest()

            if not user == hashname:
                exit(0)

            password = control.read_record("code", "/etc/users/" + self.username)
            hashcode = hashlib.sha3_512(
                str(self.password).encode()).hexdigest()

            if not password == hashcode:
                exit(0)
        else:
            enable_gui = control.read_record("enable_gui", "/etc/guest")
            if enable_gui == "No":
                exit(0)

        ## Desktop /desk files extract ##

        deskdirs = control.read_list("/etc/deskdirs")

        if self.username == "root":
            for i in deskdirs:
                if not files.isdir("/root/" + res.get(i)):
                    files.mkdir("/root/" + res.get(i))
        else:
            if not files.isdir("/desk/" + self.username): files.mkdir("/desk/" + self.username)
            for i in deskdirs:
                if not files.isdir("/desk/" + self.username + "/" + res.get(i)):
                    files.mkdir("/desk/" + self.username + "/" + res.get(i))

        ## Create pwd for this user
        if self.username == "root":
            files.write("/proc/info/pwd", "/root")
        else:
            files.write("/proc/info/pwd", "/desk/" + self.username)

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        self.setWindowIcon(QIcon(res.get(getdata("logo"))))
        #############################

        ## Menu ##

        ## menu section

        self.submenu =QMenuBar() # Sub menu
        self.Backend.setMenuBar(self.submenu)

        #self.submenu.setStyleSheet(f'background-color:none;color:{submenu_bgcolor};')

        if getdata("submenu.direction")=='ltr': self.submenu.setLayoutDirection(Qt.LeftToRight)
        elif getdata("submenu.direction")=='rtl': self.submenu.setLayoutDirection(Qt.RightToLeft)

        # hide #
        if getdata("submenu.hide")=='Yes':
            self.submenu.hide()


        self.submenu.setFont(f)

        ## Shell ##

        self.submenu.setCornerWidget(Shell([self.Backend,self]))

        ## Menu Applications #

        self.appmenu = QMenu (res.get('@string/appmenu'))
        self.submenu.addMenu(self.appmenu)
        self.appmenu.setFont(f)

        cate = files.list('/usr/share/categories')
        cate.remove('others.cat')
        cate.sort()
        cate.append('others.cat')

        # default language

        # menu action
        for i in cate:
            if i.endswith('.cat'):
                find = '/usr/share/categories/' + i

                catname = control.read_record('name[' + getdata("locale") + "]", find)
                if catname == None:
                    catname = i.replace('.cate', '')

                self.catMenu = self.appmenu.addMenu(i)
                self.catMenu.setFont(f)  # set font actions
                self.catMenu.setObjectName(i)
                self.catMenu.setTitle(catname)

                apps = files.list('/usr/share/applications')

                for j in apps:
                    find = '/usr/share/applications/' + j

                    iscate = control.read_record('category',find)

                    if iscate==None:
                        iscate='others'

                    if i.replace('.cat','')==iscate:
                        j = j.replace('.desk', '')

                        self.actApp = self.catMenu.addAction(j)
                        self.actApp.setObjectName(j)

                        # data
                        # app name
                        appname = control.read_record('name[' + getdata("locale") + "]", find)
                        shortcut = control.read_record('shortcut', find)
                        hidden = control.read_record('hidden', find)

                        if appname == None:
                            appname = j.replace('.desk', '')

                        # app logo
                        applogo = control.read_record('logo', find)

                        # design
                        self.actApp.setText(appname)
                        self.actApp.setFont(f)

                        if not applogo == None:
                            self.actApp.setIcon(QIcon(res.get(applogo)))

                        if not shortcut == None:
                            self.actApp.setShortcut(shortcut)

                        self.actApp.setFont(f)  # set font actions

                        self.actApp.triggered.connect(self.RunApplication)

                        if hidden == 'Yes':
                            self.actApp.setVisible(False)

        ## Etcetra menu ##
        self.etcmenu = QMenu()
        self.etcmenu.setFont(f)
        self.etcmenu.setTitle (res.get('@string/etcmenu'))
        self.etcmenu.setFont(f)
        self.submenu.addMenu(self.etcmenu)

        # Account menu #
        self.usermenu = QMenu()
        self.usermenu.setFont(f)
        self.etcmenu.addMenu(self.usermenu)

        # get username first + lastname
        fullname = ''

        if username=='guest':
            fullname = res.get('@string/guest')
        else:
            fullname = control.read_record('fullname','/etc/users/'+username)

        self.usermenu.setTitle(fullname)
        self.usermenu.setFont(f)

        # Power menu #
        self.powermenu = QMenu()
        self.powermenu.setFont(f)
        self.etcmenu.addMenu(self.powermenu)
        self.powermenu.setTitle(res.get('@string/powermenu'))
        self.powermenu.setFont(f)

        # all actions in menus #

        self.signout = QAction(res.get('@string/signout'))
        self.signout.triggered.connect (self.signout_act)
        self.signout.setFont(f)
        self.usermenu.addAction(self.signout)

        self.switchuser = QAction(res.get('@string/switchuser'))
        self.switchuser.triggered.connect (self.switchuser_act)
        self.switchuser.setFont(f)
        self.usermenu.addAction(self.switchuser)

        self.locks = QAction(res.get('@string/lock'))
        self.locks.setFont(f)
        self.locks.triggered.connect (self.lock_act)
        self.usermenu.addAction(self.locks)

        self.escape = QAction(res.get('@string/escape'))
        self.escape.triggered.connect (self.escape_act)
        self.escape.setFont(f)
        self.powermenu.addAction(self.escape)

        self.restart = QAction(res.get('@string/restart'))
        self.restart.triggered.connect (self.reboot_act)
        self.restart.setFont(f)
        self.powermenu.addAction(self.restart)

        self.sleep = QAction(res.get('@string/sleep'))
        self.sleep.setFont(f)
        self.sleep.triggered.connect (self.sleep_act)
        self.powermenu.addAction(self.sleep)

        self.screenshot = QAction(res.get('@string/screenshot'))
        self.screenshot.setFont(f)
        self.screenshot.triggered.connect (self.print_screen_act)
        self.screenshot.setShortcut('Ctrl+P')
        self.etcmenu.addAction(self.screenshot)

        self.enablekeyboard = QAction(res.get('@string/vkey'),checkable=True)
        self.etcmenu.addAction(self.enablekeyboard)


        if getdata('key.enable')=='Yes':
            self.enablekeyboard.setChecked(True)
        else:
            self.enablekeyboard.setChecked(False)

        self.enablekeyboard.triggered.connect (self.vkey_act)

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, int(getdata("width")), int(getdata("height")))
        self.layout().addWidget(self.backgroundButton)

            ## Set bgcolor and background ##

            ## Set colors ##
        self.setStyleSheet(f'color: {getdata("desktop.fgcolor")};')
        self.backgroundButton.setStyleSheet(
                f'border:none;background-color: {getdata("desktop.bgcolor")};')


        self.setStyleSheet(f'color: {getdata("desktop.fgcolor")};')

        self.backgroundButton.setStyleSheet(
                f'border:none;background-color: {getdata("desktop.bgcolor")};')

        self.setStyleSheet(f'color: {getdata("desktop.fgcolor")};')
        self.backgroundButton.setStyleSheet(
                f'border:none;background-image: url({res.get(getdata("desktop.background"))});')
        self.setStyleSheet(
                f'background-color:{getdata("desktop.bgcolor")};color: {getdata("desktop.fgcolor")};')


        self.resize(int(getdata("width")), int(getdata("height")))

        ## Startup Applications ##
        self.StartupApplication()
        ## Set sides ##
        ## Set sides ##

        if getdata("sides") == 'No':
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Taskbar ##
        self.taskbar = TaskBar ([Backend,self])

        ## Show ##
        ## Get data ##

        if getdata("fullscreen") == 'Yes':
            self.showFullScreen()
        else:
            self.show()

        self.keyboardWidget = KeyboardWidget([self])
        self.keyboardWidget.setFixedSize(900,356)

        self.fakewidgetkeyboard = QMainWindow()
        self.fakewidgetkeyboard.setFixedHeight(356)
        self.fakewidgetkeyboard.setStyleSheet(f'background-color: {getdata("key.bgcolor")};background-image: url({res.get(getdata("key.background"))})')

        if getdata("taskbar.location") == 'top':
            self.keyboardWidget.setGeometry(int(self.width()/2)-int(self.keyboardWidget.width()/2),self.height()-self.keyboardWidget.height(),self.width(),self.keyboardWidget.height())
            self.fakewidgetkeyboard.setGeometry(0,self.height() - self.fakewidgetkeyboard.height(), self.width(),self.fakewidgetkeyboard.height())
        elif getdata("taskbar.location") == 'left':
            self.fakewidgetkeyboard.setGeometry(int(getdata("taskbar.size"))+15, self.height() - self.fakewidgetkeyboard.height(), self.width()-15-int(getdata("taskbar.size")),self.fakewidgetkeyboard.height())
            self.keyboardWidget.setGeometry(int(self.width()/2)-int(self.keyboardWidget.width()/2), self.height() - self.keyboardWidget.height(), self.width(), self.keyboardWidget.height())
        elif getdata("taskbar.location") == 'right':
            self.fakewidgetkeyboard.setGeometry(0, self.height() - self.fakewidgetkeyboard.height(), self.width()-15-int(getdata("taskbar.size")),self.fakewidgetkeyboard.height())
            self.keyboardWidget.setGeometry(int(self.width()/2)-int(self.keyboardWidget.width()/2), self.height() - self.keyboardWidget.height(), self.width(), self.keyboardWidget.height())
        elif getdata("taskbar.location") == 'bottom':
            self.fakewidgetkeyboard.setGeometry(0, self.height()-int(getdata("taskbar.size"))-self.fakewidgetkeyboard.height()-50, self.width(),self.fakewidgetkeyboard.height())
            self.keyboardWidget.setGeometry(int(self.width()/2)-int(self.keyboardWidget.width()/2),self.height()-int(getdata("taskbar.size"))-self.keyboardWidget.height()-15,self.width(),self.keyboardWidget.height())

        self.layout().addWidget(self.fakewidgetkeyboard)
        self.layout().addWidget(self.keyboardWidget)

        self.fakewidgetkeyboard.hide()
        self.keyboardWidget.hide()

        self.Loop()

class KeyboardWidget (QWidget):
    def __init__(self,ports, parent=None):
        super(KeyboardWidget, self).__init__(parent)
        self.currentTextBox = None

        self.signalMapper = QSignalMapper(self)
        self.signalMapper.mapped[int].connect(self.buttonClicked)

        self.initUI(ports)

    def shiftx (self):

        if self.shift:
            self.shift = False
            self.settingUp()
        else:
            self.shift = True
            self.settingUp()

    def settingUp (self):

        self.tab_button.setText(control.read_record('tab', f'/usr/share/locales/{getdata("layout")}.locale'))
        self.shift_button.setText(control.read_record('shift', f'/usr/share/locales/{getdata("layout")}.locale'))
        self.back_button.setText(control.read_record('back', f'/usr/share/locales/{getdata("layout")}.locale'))
        self.enter_button.setText(control.read_record('enter', f'/usr/share/locales/{getdata("layout")}.locale'))


        if self.shift:
            keyx = res.key('!')
        else:
            keyx = res.key('1')

        self.button1.KEY_CHAR = ord(keyx)
        self.button1.setText(keyx)

        if self.shift:
            keyx = res.key('@')
        else:
            keyx = res.key('2')
        self.button2.KEY_CHAR = ord(keyx)
        self.button2.setText(keyx)

        if self.shift:
            keyx = res.key('#')
        else:
            keyx = res.key('3')
        self.button3.KEY_CHAR = ord(keyx)
        self.button3.setText(keyx)

        if self.shift:
            keyx = res.key('$')
        else:
            keyx = res.key('4')
        self.button4.KEY_CHAR = ord(keyx)
        self.button4.setText(keyx)

        if self.shift:
            keyx = res.key('%')
        else:
            keyx = res.key('5')

        self.button5.KEY_CHAR = ord(keyx)
        self.button5.setText(keyx)

        if self.shift:
            keyx = res.key('^')
        else:
            keyx = res.key('6')
        self.button6.KEY_CHAR = ord(keyx)
        self.button6.setText(keyx)

        if self.shift:
            keyx = res.key('&')
        else:
            keyx = res.key('7')
        self.button7.KEY_CHAR = ord(keyx)
        self.button7.setText(keyx)

        if self.shift:
            keyx = res.key('*')
        else:
            keyx = res.key('8')

        self.button8.KEY_CHAR = ord(keyx)
        self.button8.setText(keyx)

        if self.shift:
            keyx = res.key('(')
        else:
            keyx = res.key('9')

        self.button9.KEY_CHAR = ord(keyx)
        self.button9.setText(keyx)

        if self.shift:
            keyx = res.key(')')
        else:
            keyx = res.key('0')
        self.button0.KEY_CHAR = ord(keyx)
        self.button0.setText(keyx)

        if self.shift:
            keyx = res.key('A')
        else:
            keyx = res.key('a')

        self.buttona.KEY_CHAR = ord(keyx)
        self.buttona.setText(keyx)

        if self.shift:
            keyx = res.key('B')
        else:
            keyx = res.key('b')
        self.buttonb.KEY_CHAR = ord(keyx)
        self.buttonb.setText(keyx)

        if self.shift:
            keyx = res.key('C')
        else:
            keyx = res.key('c')

        self.buttonc.KEY_CHAR = ord(keyx)
        self.buttonc.setText(keyx)

        if self.shift:
            keyx = res.key('D')
        else:
            keyx = res.key('d')

        self.buttond.KEY_CHAR = ord(keyx)
        self.buttond.setText(keyx)

        if self.shift:
            keyx = res.key('E')
        else:
            keyx = res.key('e')
        self.buttone.KEY_CHAR = ord(keyx)
        self.buttone.setText(keyx)


        if self.shift:
            keyx = res.key('F')
        else:
            keyx = res.key('f')
        self.buttonf.KEY_CHAR = ord(keyx)
        self.buttonf.setText(keyx)


        if self.shift:
            keyx = res.key('G')
        else:
            keyx = res.key('g')
        self.buttong.KEY_CHAR = ord(keyx)
        self.buttong.setText(keyx)


        if self.shift:
            keyx = res.key('H')
        else:
            keyx = res.key('h')
        self.buttonh.KEY_CHAR = ord(keyx)
        self.buttonh.setText(keyx)

        if self.shift:
            keyx = res.key('I')
        else:
            keyx = res.key('i')
        self.buttoni.KEY_CHAR = ord(keyx)
        self.buttoni.setText(keyx)

        if self.shift:
            keyx = res.key('J')
        else:
            keyx = res.key('j')
        self.buttonj.KEY_CHAR = ord(keyx)
        self.buttonj.setText(keyx)

        if self.shift:
            keyx = res.key('K')
        else:
            keyx = res.key('k')
        self.buttonk.KEY_CHAR = ord(keyx)

        self.buttonk.setText(keyx)

        if self.shift:
            keyx = res.key('L')
        else:
            keyx = res.key('l')

        self.buttonl.KEY_CHAR = ord(keyx)
        self.buttonl.setText(keyx)

        if self.shift:
            keyx = res.key('M')
        else:
            keyx = res.key('m')
        self.buttonm.KEY_CHAR = ord(keyx)

        self.buttonm.setText(keyx)

        if self.shift:
            keyx = res.key('N')
        else:
            keyx = res.key('n')
        self.buttonn.KEY_CHAR = ord(keyx)

        self.buttonn.setText(keyx)

        if self.shift:
            keyx = res.key('O')
        else:
            keyx = res.key('o')
        self.buttono.KEY_CHAR = ord(keyx)

        self.buttono.setText(keyx)

        if self.shift:
            keyx = res.key('P')
        else:
            keyx = res.key('p')
        self.buttonp.KEY_CHAR = ord(keyx)
        self.buttonp.setText(keyx)


        if self.shift:
            keyx = res.key('Q')
        else:
            keyx = res.key('q')
        self.buttonq.KEY_CHAR = ord(keyx)
        self.buttonq.setText(keyx)


        if self.shift:
            keyx = res.key('R')
        else:
            keyx = res.key('r')
        self.buttonr.KEY_CHAR = ord(keyx)
        self.buttonr.setText(keyx)


        if self.shift:
            keyx = res.key('S')
        else:
            keyx = res.key('s')
        self.buttons.KEY_CHAR = ord(keyx)
        self.buttons.setText(keyx)


        if self.shift:
            keyx = res.key('T')
        else:
            keyx = res.key('t')
        self.buttont.KEY_CHAR = ord(keyx)
        self.buttont.setText(keyx)


        if self.shift:
            keyx = res.key('U')
        else:
            keyx = res.key('u')
        self.buttonu.KEY_CHAR = ord(keyx)
        self.buttonu.setText(keyx)


        if self.shift:
            keyx = res.key('V')
        else:
            keyx = res.key('v')
        self.buttonv.KEY_CHAR = ord(keyx)
        self.buttonv.setText(keyx)


        if self.shift:
            keyx = res.key('W')
        else:
            keyx = res.key('w')
        self.buttonw.KEY_CHAR = ord(keyx)
        self.buttonw.setText(keyx)

        if self.shift:
            keyx = res.key('X')
        else:
            keyx = res.key('x')
        self.buttonx.KEY_CHAR = ord(keyx)

        self.buttonx.setText(keyx)

        if self.shift:
            keyx = res.key('Y')
        else:
            keyx = res.key('y')

        self.buttony.KEY_CHAR = ord(keyx)
        self.buttony.setText(keyx)


        if self.shift:
            keyx = res.key('Z')
        else:
            keyx = res.key('z')
        self.buttonz.KEY_CHAR = ord(keyx)
        self.buttonz.setText(keyx)


        if self.shift:
            keyx = res.key('~')
        else:
            keyx = res.key('`')
        self.buttonups.KEY_CHAR = ord(keyx)
        self.buttonups.setText(keyx)


        if self.shift:
            keyx = res.key('_')

        else:
            keyx = res.key('-')
        self.button_.KEY_CHAR = ord(keyx)
        self.button_.setText(keyx)
        if self.shift:
            keyx = res.key('+')
        else:
            keyx = res.key('=')
        self.buttonequal.KEY_CHAR = ord(keyx)
        self.buttonequal.setText(keyx)
        if self.shift:
            keyx = res.key('{')
        else:
            keyx = res.key('[')

        self.btnaquladbaz.KEY_CHAR = ord(keyx)
        self.btnaquladbaz.setText(keyx)
        if self.shift:
            keyx = res.key('}')
        else:
            keyx = res.key(']')

        self.btnaquladbaste.KEY_CHAR = ord(keyx)
        self.btnaquladbaste.setText(keyx)
        if self.shift:
            keyx = res.key('|')
        else:
            keyx = res.key('\\')
        self.btnbackslash.KEY_CHAR = ord(keyx)
        self.btnbackslash.setText(keyx)

        if self.shift:
            keyx = ':'
        else:
            keyx = res.key(';')
        self.btnsimi.KEY_CHAR = ord(keyx)
        self.btnsimi.setText(keyx)

        if self.shift:
            keyx = res.key('"')
        else:
            keyx = res.key("'")
        self.btncotayshen.KEY_CHAR = ord(keyx)
        self.btncotayshen.setText(keyx)
        if self.shift:
            keyx = res.key('?')

        else:
            keyx = res.key('/')
        self.btnslash.KEY_CHAR = ord(keyx)
        self.btnslash.setText(keyx)
        if self.shift:
            keyx = res.key('>')

        else:
            keyx = res.key('.')
        self.btndot.KEY_CHAR = ord(keyx)
        self.btndot.setText(keyx)

        if self.shift:
            keyx = res.key('<')
        else:
            keyx = res.key(',')

        self.btndot1.KEY_CHAR = ord(keyx)
        self.btndot1.setText(keyx)


        self.lang_button.setText(control.read_record('name',f'/usr/share/locales/{getdata("layout")}.locale'))


        self.signalMapper.setMapping(self.button1, self.button1.KEY_CHAR)
        self.signalMapper.setMapping(self.button2, self.button2.KEY_CHAR)
        self.signalMapper.setMapping(self.button3, self.button3.KEY_CHAR)
        self.signalMapper.setMapping(self.button4, self.button4.KEY_CHAR)
        self.signalMapper.setMapping(self.button5, self.button5.KEY_CHAR)
        self.signalMapper.setMapping(self.button6, self.button6.KEY_CHAR)
        self.signalMapper.setMapping(self.button7, self.button7.KEY_CHAR)
        self.signalMapper.setMapping(self.button8, self.button8.KEY_CHAR)
        self.signalMapper.setMapping(self.button9, self.button9.KEY_CHAR)
        self.signalMapper.setMapping(self.button0, self.button0.KEY_CHAR)
        self.signalMapper.setMapping(self.buttona, self.buttona.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonb, self.buttonb.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonc, self.buttonc.KEY_CHAR)
        self.signalMapper.setMapping(self.buttond, self.buttond.KEY_CHAR)
        self.signalMapper.setMapping(self.buttone, self.buttone.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonf, self.buttonf.KEY_CHAR)
        self.signalMapper.setMapping(self.buttong, self.buttong.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonh, self.buttonh.KEY_CHAR)
        self.signalMapper.setMapping(self.buttoni, self.buttoni.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonj, self.buttonj.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonk, self.buttonk.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonl, self.buttonl.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonm, self.buttonm.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonn, self.buttonn.KEY_CHAR)
        self.signalMapper.setMapping(self.buttono, self.buttono.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonp, self.buttonp.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonq, self.buttonq.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonr, self.buttonr.KEY_CHAR)
        self.signalMapper.setMapping(self.buttons, self.buttons.KEY_CHAR)
        self.signalMapper.setMapping(self.buttont, self.buttont.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonu, self.buttonu.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonv, self.buttonv.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonw, self.buttonw.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonx, self.buttonx.KEY_CHAR)
        self.signalMapper.setMapping(self.buttony, self.buttony.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonz, self.buttonz.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonups, self.buttonups.KEY_CHAR)
        self.signalMapper.setMapping(self.button_, self.button_.KEY_CHAR)
        self.signalMapper.setMapping(self.buttonequal, self.buttonequal.KEY_CHAR)
        self.signalMapper.setMapping(self.btnaquladbaz, self.btnaquladbaz.KEY_CHAR)
        self.signalMapper.setMapping(self.btnaquladbaste, self.btnaquladbaste.KEY_CHAR)
        self.signalMapper.setMapping(self.btnbackslash, self.btnbackslash.KEY_CHAR)
        self.signalMapper.setMapping(self.btnsimi, self.btnsimi.KEY_CHAR)
        self.signalMapper.setMapping(self.btncotayshen, self.btncotayshen.KEY_CHAR)
        self.signalMapper.setMapping(self.btnslash, self.btnslash.KEY_CHAR)
        self.signalMapper.setMapping(self.btndot, self.btndot.KEY_CHAR)
        self.signalMapper.setMapping(self.btndot1, self.btndot1.KEY_CHAR)

    def onCloseKeyboard (self):
        if not files.isfile ('/proc/info/key'):
            self.Env.fakewidgetkeyboard.close()
            self.close()
        else:
            QTimer.singleShot(100,self.onCloseKeyboard)

    def initUI(self,ports):
        layout = QGridLayout()

        uic.loadUi('usr/share/layouts/laptopkeyboard.ui',self)

        self.shift = False
        self.Env = ports[0]


        # p = self.palette()
        # p.setColor(self.backgroundRole(),Qt.white)
        # self.setPalette(p)

        self.setAutoFillBackground(True)
        self.text_box = QTextEdit()
        self.text_box.setFont(QFont('Arial', 12))
        self.text_box.hide()
        # text_box.setFixedHeight(50)
        # self.text_box.setFixedWidth(300)
        layout.addWidget(self.text_box, 0, 0, 1, 13)

        f = QFont('Iran Sans', 16)
        size = 50

        files.create('/proc/info/key')

        self.enable_style ='''
        QPushButton {
            background-color: {1};
            color: {2};
            border-radius: {3}% {3}%;
        }
        QPushButton::hover {
            background-color: {4};
            color: {5};
            border-radius: {3}% {3}%;
        }
        '''.replace('{1}',getdata("key.btn.bgcolor")).replace('{2}',getdata("key.btn.fgcolor")).replace('{3}',getdata("key.btn.round-size")).replace('{4}',getdata("key.btn.bgcolor-hover")).replace('{5}',getdata("key.btn.fgcolor-hover"))
        self.setStyleSheet(self.enable_style)

        if getdata("key.btn.shadow") == 'Yes': shadowx = True
        else: shadowx = False

        self.button1 = self.findChild(QPushButton,f'btn1')
        self.button1.setFont(f)
        self.button1.setFixedHeight(size)
        self.button1.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button1.setGraphicsEffect(shadow)
        self.button1.clicked.connect(self.signalMapper.map)

        self.button2 = self.findChild(QPushButton, f'btn2')
        self.button2.setFont(f)
        self.button2.setFixedHeight(size)
        self.button2.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button2.setGraphicsEffect(shadow)
        self.button2.clicked.connect(self.signalMapper.map)

        self.button3 = self.findChild(QPushButton, f'btn3')
        self.button3.setFont(f)
        self.button3.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button3.setGraphicsEffect(shadow)
        self.button3.setFixedWidth(size)
        self.button3.clicked.connect(self.signalMapper.map)

        self.button4 = self.findChild(QPushButton, f'btn4')
        self.button4.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button4.setGraphicsEffect(shadow)
        self.button4.setFixedHeight(size)
        self.button4.setFixedWidth(size)
        self.button4.clicked.connect(self.signalMapper.map)

        self.button5 = self.findChild(QPushButton, f'btn5')
        self.button5.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button5.setGraphicsEffect(shadow)
        self.button5.setFixedHeight(size)
        self.button5.setFixedWidth(size)
        self.button5.clicked.connect(self.signalMapper.map)

        self.button6 = self.findChild(QPushButton, f'btn6')
        self.button6.setFont(f)
        self.button6.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button6.setGraphicsEffect(shadow)
        self.button6.setFixedWidth(size)
        self.button6.clicked.connect(self.signalMapper.map)

        self.button7 = self.findChild(QPushButton, f'btn7')
        self.button7.setFont(f)
        self.button7.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button7.setGraphicsEffect(shadow)
        self.button7.setFixedWidth(size)
        self.button7.clicked.connect(self.signalMapper.map)

        self.button8 = self.findChild(QPushButton, f'btn8')
        self.button8.setFont(f)
        self.button8.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button8.setGraphicsEffect(shadow)
        self.button8.setFixedWidth(size)
        self.button8.clicked.connect(self.signalMapper.map)

        self.button9 = self.findChild(QPushButton, f'btn9')
        self.button9.setFont(f)
        self.button9.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button9.setGraphicsEffect(shadow)
        self.button9.setFixedWidth(size)
        self.button9.clicked.connect(self.signalMapper.map)

        self.button0 = self.findChild(QPushButton, f'btn0')
        self.button0.setFont(f)
        self.button0.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button0.setGraphicsEffect(shadow)
        self.button0.setFixedWidth(size)
        self.button0.clicked.connect(self.signalMapper.map)

        self.buttona = self.findChild(QPushButton, f'btna')
        self.buttona.setFont(f)
        self.buttona.setFixedHeight(size)
        self.buttona.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttona.setGraphicsEffect(shadow)
        self.buttona.clicked.connect(self.signalMapper.map)

        self.buttonb = self.findChild(QPushButton, f'btnb')
        self.buttonb.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonb.setGraphicsEffect(shadow)
        self.buttonb.setFixedHeight(size)
        self.buttonb.setFixedWidth(size)
        self.buttonb.clicked.connect(self.signalMapper.map)

        self.buttonc = self.findChild(QPushButton, f'btnc')
        self.buttonc.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonc.setGraphicsEffect(shadow)
        self.buttonc.setFixedHeight(size)
        self.buttonc.setFixedWidth(size)
        self.buttonc.clicked.connect(self.signalMapper.map)

        self.buttond = self.findChild(QPushButton, f'btnd')
        self.buttond.setFont(f)
        self.buttond.setFixedHeight(size)
        self.buttond.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttond.setGraphicsEffect(shadow)
        self.buttond.clicked.connect(self.signalMapper.map)

        self.buttone = self.findChild(QPushButton, f'btne')
        self.buttone.setFont(f)
        self.buttone.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttone.setGraphicsEffect(shadow)
        self.buttone.setFixedWidth(size)
        self.buttone.clicked.connect(self.signalMapper.map)

        self.buttonf = self.findChild(QPushButton, f'btnf')
        self.buttonf.setFont(f)
        self.buttonf.setFixedHeight(size)
        self.buttonf.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonf.setGraphicsEffect(shadow)
        self.buttonf.clicked.connect(self.signalMapper.map)

        self.buttong = self.findChild(QPushButton, f'btng')
        self.buttong.setFont(f)
        self.buttong.setFixedHeight(size)
        self.buttong.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttong.setGraphicsEffect(shadow)
        self.buttong.clicked.connect(self.signalMapper.map)

        self.buttonh = self.findChild(QPushButton, f'btnh')
        self.buttonh.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonh.setGraphicsEffect(shadow)
        self.buttonh.setFixedHeight(size)
        self.buttonh.setFixedWidth(size)
        self.buttonh.clicked.connect(self.signalMapper.map)

        self.buttoni = self.findChild(QPushButton, f'btni')
        self.buttoni.setFont(f)
        self.buttoni.setFixedHeight(size)
        self.buttoni.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttoni.setGraphicsEffect(shadow)
        self.buttoni.clicked.connect(self.signalMapper.map)

        self.buttonj = self.findChild(QPushButton, f'btnj')
        self.buttonj.setFont(f)
        self.buttonj.setFixedHeight(size)
        self.buttonj.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonj.setGraphicsEffect(shadow)
        self.buttonj.clicked.connect(self.signalMapper.map)

        self.buttonk = self.findChild(QPushButton, f'btnk')
        self.buttonk.setFont(f)
        self.buttonk.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonk.setGraphicsEffect(shadow)
        self.buttonk.setFixedWidth(size)
        self.buttonk.clicked.connect(self.signalMapper.map)

        self.buttonl = self.findChild(QPushButton, f'btnl')
        self.buttonl.setFont(f)
        self.buttonl.setFixedHeight(size)
        self.buttonl.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonl.setGraphicsEffect(shadow)
        self.buttonl.clicked.connect(self.signalMapper.map)

        self.buttonm = self.findChild(QPushButton, f'btnm')
        self.buttonm.setFont(f)
        self.buttonm.setFixedHeight(size)
        self.buttonm.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonm.setGraphicsEffect(shadow)
        self.buttonm.clicked.connect(self.signalMapper.map)

        self.buttonn = self.findChild(QPushButton, f'btnn')
        self.buttonn.setFont(f)
        self.buttonn.setFixedHeight(size)
        self.buttonn.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonn.setGraphicsEffect(shadow)
        self.buttonn.clicked.connect(self.signalMapper.map)

        self.buttono = self.findChild(QPushButton, f'btno')
        self.buttono.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttono.setGraphicsEffect(shadow)
        self.buttono.setFixedHeight(size)
        self.buttono.setFixedWidth(size)
        self.buttono.clicked.connect(self.signalMapper.map)

        self.buttonp = self.findChild(QPushButton, f'btnp')
        self.buttonp.setFont(f)
        self.buttonp.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonp.setGraphicsEffect(shadow)
        self.buttonp.setFixedWidth(size)
        self.buttonp.clicked.connect(self.signalMapper.map)

        self.buttonq = self.findChild(QPushButton, f'btnq')
        self.buttonq.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonq.setGraphicsEffect(shadow)
        self.buttonq.setFixedHeight(size)
        self.buttonq.setFixedWidth(size)
        self.buttonq.clicked.connect(self.signalMapper.map)

        self.buttonr = self.findChild(QPushButton, f'btnr')
        self.buttonr.setFont(f)
        self.buttonr.setFixedHeight(size)
        self.buttonr.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonr.setGraphicsEffect(shadow)
        self.buttonr.clicked.connect(self.signalMapper.map)

        self.buttons = self.findChild(QPushButton, f'btns')
        self.buttons.setFont(f)
        self.buttons.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttons.setGraphicsEffect(shadow)
        self.buttons.setFixedWidth(size)
        self.buttons.clicked.connect(self.signalMapper.map)

        self.buttont = self.findChild(QPushButton, f'btnt')
        self.buttont.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttont.setGraphicsEffect(shadow)
        self.buttont.setFixedHeight(size)
        self.buttont.setFixedWidth(size)
        self.buttont.clicked.connect(self.signalMapper.map)

        self.buttonu = self.findChild(QPushButton, f'btnu')
        self.buttonu.setFont(f)
        self.buttonu.setFixedHeight(size)
        self.buttonu.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonu.setGraphicsEffect(shadow)
        self.buttonu.clicked.connect(self.signalMapper.map)

        self.buttonv = self.findChild(QPushButton, f'btnv')
        self.buttonv.setFont(f)
        self.buttonv.setFixedHeight(size)
        self.buttonv.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonv.setGraphicsEffect(shadow)
        self.buttonv.clicked.connect(self.signalMapper.map)
        self.buttonw = self.findChild(QPushButton, f'btnw')
        self.buttonw.setFont(f)
        self.buttonw.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonw.setGraphicsEffect(shadow)
        self.buttonw.setFixedWidth(size)
        self.buttonw.clicked.connect(self.signalMapper.map)

        self.buttonx = self.findChild(QPushButton, f'btnx')
        self.buttonx.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonx.setGraphicsEffect(shadow)
        self.buttonx.setFixedHeight(size)
        self.buttonx.setFixedWidth(size)
        self.buttonx.clicked.connect(self.signalMapper.map)

        self.buttony = self.findChild(QPushButton, f'btny')
        self.buttony.setFont(f)
        self.buttony.setFixedHeight(size)
        self.buttony.setFixedWidth(size)
        self.buttony.clicked.connect(self.signalMapper.map)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttony.setGraphicsEffect(shadow)

        self.buttonz = self.findChild(QPushButton, f'btnz')
        self.buttonz.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonz.setGraphicsEffect(shadow)
        self.buttonz.setFixedHeight(size)
        self.buttonz.setFixedWidth(size)
        self.buttonz.clicked.connect(self.signalMapper.map)

        self.buttonups = self.findChild(QPushButton, f'btnups')
        self.buttonups.setFont(f)
        self.buttonups.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonups.setGraphicsEffect(shadow)
        self.buttonups.setFixedWidth(size)
        self.buttonups.clicked.connect(self.signalMapper.map)

        self.button_ = self.findChild(QPushButton, f'btn_')
        self.button_.setFont(f)
        self.button_.setFixedHeight(size)
        self.button_.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.button_.setGraphicsEffect(shadow)
        self.button_.clicked.connect(self.signalMapper.map)

        self.buttonequal = self.findChild(QPushButton, f'btnequal')
        self.buttonequal.setFont(f)
        self.buttonequal.setFixedHeight(size)
        self.buttonequal.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.buttonequal.setGraphicsEffect(shadow)
        self.buttonequal.clicked.connect(self.signalMapper.map)

        self.btnaquladbaz = self.findChild(QPushButton, f'btnaquladbaz')
        self.btnaquladbaz.setFont(f)
        self.btnaquladbaz.setFixedHeight(size)
        self.btnaquladbaz.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.btnaquladbaz.setGraphicsEffect(shadow)
        self.btnaquladbaz.clicked.connect(self.signalMapper.map)

        self.btnaquladbaste = self.findChild(QPushButton, f'btnaquladbaste')
        self.btnaquladbaste.setFont(f)
        self.btnaquladbaste.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.btnaquladbaste.setGraphicsEffect(shadow)
        self.btnaquladbaste.setFixedWidth(size)
        self.btnaquladbaste.clicked.connect(self.signalMapper.map)

        self.btnbackslash = self.findChild(QPushButton, f'btnbackslash')
        self.btnbackslash.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.btnbackslash.setGraphicsEffect(shadow)
        self.btnbackslash.setFixedHeight(size)
        self.btnbackslash.setFixedWidth(size)
        self.btnbackslash.clicked.connect(self.signalMapper.map)

        self.btnsimi = self.findChild(QPushButton, f'btnsimi')
        self.btnsimi.setFont(f)
        self.btnsimi.setFixedHeight(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.btnsimi.setGraphicsEffect(shadow)
        self.btnsimi.setFixedWidth(size)
        self.btnsimi.clicked.connect(self.signalMapper.map)

        self.btncotayshen = self.findChild(QPushButton, f'btncotayshen')
        self.btncotayshen.setFont(f)
        self.btncotayshen.setFixedHeight(size)
        self.btncotayshen.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.btncotayshen.setGraphicsEffect(shadow)
        self.btncotayshen.clicked.connect(self.signalMapper.map)

        self.btnslash = self.findChild(QPushButton, f'btnslash')
        self.btnslash.setFont(f)
        self.btnslash.setFixedHeight(size)
        self.btnslash.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.btnslash.setGraphicsEffect(shadow)
        self.btnslash.clicked.connect(self.signalMapper.map)

        self.btndot = self.findChild(QPushButton, f'btndot')
        self.btndot.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.btndot.setGraphicsEffect(shadow)
        self.btndot.setFixedHeight(size)
        self.btndot.setFixedWidth(size)
        self.btndot.clicked.connect(self.signalMapper.map)

        self.btndot1 = self.findChild(QPushButton, f'btndot1')
        self.btndot1.setFont(f)
        self.btndot1.setFixedHeight(size)
        self.btndot1.setFixedWidth(size)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.btndot1.setGraphicsEffect(shadow)
        self.btndot1.clicked.connect(self.signalMapper.map)

        # Cancel button

        self.space_button = self.findChild(QPushButton, f'btnspace')
        self.space_button.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.space_button.setGraphicsEffect(shadow)
        self.space_button.KEY_CHAR = Qt.Key_Space
        self.space_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(self.space_button, self.space_button.KEY_CHAR)

        self.tab_button = self.findChild(QPushButton, f'btntab')
        self.tab_button.setFont(f)

        self.tab_button.KEY_CHAR = Qt.Key_Tab
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.tab_button.setGraphicsEffect(shadow)
        self.tab_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(self.tab_button, self.tab_button.KEY_CHAR)

        self.shift_button = self.findChild(QPushButton, f'btnshift')
        self.shift_button.setFont(f)
        self.shift_button.KEY_CHAR = Qt.Key_Shift
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.shift_button.setGraphicsEffect(shadow)
        #shift_button.clicked.connect(self.signalMapper.map)
        self.shift_button.clicked.connect (self.shiftx)
        self.signalMapper.setMapping(self.shift_button, self.shift_button.KEY_CHAR)

        self.back_button = self.findChild(QPushButton, f'btnback')
        self.back_button.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.back_button.setGraphicsEffect(shadow)
        self.back_button.KEY_CHAR = Qt.Key_Backspace
        self.back_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(self.back_button, self.back_button.KEY_CHAR)

        self.enter_button = self.findChild(QPushButton, f'btnenter')
        self.enter_button.setFont(f)
        self.enter_button.KEY_CHAR = Qt.Key_Enter
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.enter_button.setGraphicsEffect(shadow)
        self.enter_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(self.enter_button, self.enter_button.KEY_CHAR)

        self.done_button = self.findChild(QPushButton, f'btndone')
        self.done_button.setFont(f)
        self.done_button.setText (control.read_record('done',f'/usr/share/locales/{getdata("layout")}.locale'))
        self.done_button.KEY_CHAR = Qt.Key_Home
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.done_button.setGraphicsEffect(shadow)
        self.done_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(self.done_button, self.done_button.KEY_CHAR)

        self.lang_button = self.findChild(QPushButton, f'btnlang')
        self.lang_button.setFont(f)
        if shadowx:
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.lang_button.setGraphicsEffect(shadow)
        self.lang_button.clicked.connect(self.chooseKeyLayout)

        self.setGeometry(0, 0, 950, 356)
        self.setLayout(layout)

        self.settingUp()


        self.activateWindow()
        self.raise_()

        self.onCloseKeyboard()

    def chooseKeyLayout (self):
        files.write('/proc/info/id','desktop')

        try:
            self.Env.RunApp('key',[self.settingUp])
        except:
            layout = control.read_record('layout','/etc/gui')

            if layout=='en':
                control.write_record('layout','fa','/etc/gui')
            elif layout=='fa':
                control.write_record('layout','en','/etc/gui')

            self.settingUp()

        files.write('/proc/info/id', 'desktop')

    def buttonClicked(self, char_ord):
        try:
            self.Env.fakewidgetkeyboard.activateWindow()
            self.Env.fakewidgetkeyboard.raise_()
            self.activateWindow()
            self.raise_()

            if not self.currentTextBox.objectName()=='BTextEdit':
                self.text_box.setPlainText(self.currentTextBox.text())
                txt = self.text_box.toPlainText()
            else:
                self.text_box.setPlainText(self.currentTextBox.toPlainText())
                txt = self.text_box.toPlainText()

            if char_ord == Qt.Key_Backspace:
                txt = txt[:-1]
            elif char_ord == Qt.Key_Enter:
                txt += chr(10)
            elif char_ord == Qt.Key_Home:
                self.hide()
                self.Env.fakewidgetkeyboard.hide()
                return
            elif char_ord == Qt.Key_Clear:
                txt = ""
            elif char_ord == Qt.Key_Space:
                txt += ' '
            elif char_ord == Qt.Key_Tab:
                txt += '\t'
            else:
                txt += chr(char_ord)

            if not self.currentTextBox.objectName() == 'BTextEdit':
                self.currentTextBox.setText(txt)
            else:
                self.currentTextBox.setPlainText(txt)

        except:
            pass