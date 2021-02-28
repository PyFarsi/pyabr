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
import sys, hashlib, os, importlib, subprocess
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

height = int(files.readall('/tmp/height'))
width = int(files.readall('/tmp/width'))

files.remove('/tmp/height')
files.remove('/tmp/width')

files.write('/proc/info/de','Baran Desktop Enviroment')

## variables ##

class variables:
    lock_clock_shadow = 'Yes'
    lock_clock_size = 100
    lock_clock_color = 'white'
    lock_clock_location = 'bottom/left'
    locale = 'en'
    submenu_hide = 'No'
    submenu_fgcolor = 'black'
    submenu_bgcolor = 'white'
    submenu_direction = 'ltr'
    submenu_fontsize = 12
    taskbar_location = 'bottom'
    taskbar_size = 50
    taskbar_locked = 'Yes'
    taskbar_float = 'Yes'
    backend_color = '#000000'
    backend_timeout = 1000
    splash_color = '#FFFFFF'
    splash_timeout = 3000
    fullscreen = True
    width = width
    height = height
    sides = False
    login_bgcolor = '#123456'
    login_fgcolor = '#000000'
    login_background = ''
    enter_bgcolor = ''
    enter_fgcolor = '#000000'
    enter_background = ''
    unlock_bgcolor = ''
    unlock_fgcolor = '#000000'
    unlock_background = ''
    username = ''
    password = ''
    desktop_bgcolor = '#FFFFFF'
    desktop_fgcolor = '#000000'
    desktop_background = ''
    lock_bgcolor = '#FFFFFF'
    lock_fgcolor = '#000000'
    lock_background = ''
    taskbar_bgcolor = '#FFFFFF'
    loginw_bgcolor = '#FFF'
    userlogo_color = '#FFFFFF'
    input_bgcolor = '#FFFFFF'
    input_fgcolor = '#000000'
    loginw_fgcolor = '#000000'
    loginw_round_size = 20
    loginw_userlogo_round_size = 125
    loginw_input_round_size = 20
    loginw_location = 'center'
    loginw_input_fontsize = 12
    loginw_login_bgcolor = '#ABCDEF'
    loginw_login_fgcolor = '#FFFFFF'
    loginw_login_hover_bgcolor = '#123456'
    loginw_login_hover_fgcolor = '#FFFFFF'
    loginw_login_fontsize = 12
    loginw_login_round = 'Yes'
    loginw_login_round_size = 20
    loginw_login_hide = 'No'
    loginw_login_width = 300
    loginw_enter_bgcolor = 'pink'
    loginw_enter_fgcolor = '#FFFFFF'
    loginw_enter_hover_bgcolor = 'purple'
    loginw_enter_hover_fgcolor = '#FFFFFF'
    loginw_enter_fontsize = 12
    loginw_enter_round = 'Yes'
    loginw_enter_round_size = 20
    loginw_enter_hide = 'No'
    loginw_enter_width = 300
    loginw_unlock_bgcolor = 'lime'
    loginw_unlock_fgcolor = 'green'
    loginw_unlock_hover_bgcolor = 'green'
    loginw_unlock_hover_fgcolor = 'lime'
    loginw_unlock_fontsize = 12
    loginw_unlock_round = 'Yes'
    loginw_unlock_round_size = 20
    loginw_unlock_hide = 'No'
    loginw_unlock_width = 300
    loginw_shadow = 'Yes'
    loginw_userlogo_shadow = 'Yes'
    loginw_input_shadow = 'Yes'
    loginw_login_shadow = 'No'
    loginw_enter_shadow = 'No'
    loginw_unlock_shadow = 'No'
    loginw_input_width = 300
    loginw_input_height = 40
    loginw_login_height = 40
    loginw_enter_height = 40
    loginw_unlock_height = 40
    app_title_size = 50
    app_title_fgcolor = '#FFFFFF'
    app_title_bgcolor = "#123456"
    app_title_float = "@icon/float"
    app_title_float_hover = "#ABCDEF"
    app_title_close = "@icon/close"
    app_title_close_hover = "red"
    app_shadow = "Yes"
    app_logo = "@icon/app"
    app_bgcolor = "#FFFFFF"
    app_fgcolor = "#000000"
    app_menu_bgcolor = "#FFFFFF"
    app_menu_fgcolor = "#000000"
    app_menu_bgcolor_pressed = "#ABCDEF"
    app_menu_fgcolor_pressed = "#FFFFFF"
    app_body_bgcolor = "white"
    app_body_fgcolor = "black"
    font = "Iran Sans" # This font is not free when you did not buy it you should change this name in /etc/gui or buy it

## ## ## ## ##

## Get data ##
def getdata (name):
    return control.read_record (name,'/etc/gui')

## Backend ##
class Backend (QMainWindow):
    ## Run splash page ##
    def runSplash (self):
        self.setCentralWidget(Splash([self]))

    def runLogin (self):
        self.setCentralWidget(Login([self,self]))

    def runEnter (self):
        self.setCentralWidget(Enter([self,self],self.gui_params[1]))

    def runDesktop (self):
        self.setCentralWidget(Desktop([self],self.gui_params[1],self.gui_params[2]))

    def __init__(self):
        super(Backend, self).__init__()

        ## Set port name ##
        self.setObjectName('Backend')

        ## Get informations ##
        cs = files.readall ('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs+' '+ver+' ('+cd+")")

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        ## Get backend color ##
        color = getdata('backend.color')

        ## Set color ##
        if not color==None:
            variables.backend_color = color

        self.wb = QMainWindow()
        self.wb.setStyleSheet('background-color: ' + variables.backend_color+";color: black;")
        self.setCentralWidget(self.wb)

        ## Set size ##
        autosize = getdata('autosize')
        width = getdata('width')
        height = getdata('height')

        if not width==None and not autosize=='Yes':
            variables.width = int(width)

        if not height==None and not autosize=='Yes':
            variables.height = int(height)

        self.resize(variables.width, variables.height)

        ## Set sides ##
        ## Set sides ##
        sides = getdata('sides')

        if sides == 'Yes':
            variables.sides = True
        else:
            variables.sides = False

        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Show ##

            ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

        ## Run backend after showing backend ##
        timeout = getdata('backend.timeout')
        if timeout == None:
            variables.backend_timeout = 1000
        else:
            variables.backend_timeout = int(timeout)

        self.gui_params = getdata('params')

        if self.gui_params==None: self.gui_params=[]
        else:
            self.gui_params = self.gui_params.split(',')

        if self.gui_params==[]:
            control.write_record('params','splash','/etc/gui')
            QTimer.singleShot(variables.backend_timeout, self.runSplash)  ## Run splash after 1s
        elif self.gui_params[0]=='splash':
            control.write_record('params','splash','/etc/gui')
            QTimer.singleShot(variables.backend_timeout, self.runSplash)
        elif self.gui_params[0]=='login':
            control.write_record('params','login','/etc/gui')
            QTimer.singleShot(variables.backend_timeout, self.runLogin)
        elif self.gui_params[0]=='enter':
            control.write_record('params','enter','/etc/gui')
            QTimer.singleShot(variables.backend_timeout, self.runEnter)
        elif self.gui_params[0]=='desktop':
            control.write_record('params','desktop','/etc/gui')
            QTimer.singleShot(variables.backend_timeout, self.runDesktop)
        else:
            sys.exit(0)

## Splash ##
class Splash (QMainWindow):

    ## Run login page ##
    def runLogin(self):
        self.setCentralWidget(Login([self.Backend]))

    def __init__(self,ports):
        super(Splash, self).__init__()

        ## Set port name ##
        self.setObjectName('Splash')

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo==None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        # set font
        f.setFamily(variables.font)

        ## Ports ##

        self.Backend = ports[0]

        ## Get backend color ##
        color = getdata('splash.color')

        ## Set color ##
        if not color==None:
            variables.splash_color = color

        self.wb = QMainWindow()
        self.wb.setStyleSheet(f'background-color: {variables.splash_color}')
        self.setCentralWidget(self.wb)

        ## Set size ##
        width = getdata('width')
        height = getdata('height')
        autosize =getdata('autosize')

        if not width == None  and not autosize=='Yes':
            variables.width = int(width)

        if not height == None and not autosize=='Yes':
            variables.height = int(height)

        self.resize(variables.width, variables.height)

        ## Set sides ##
        sides = getdata('sides')

        if sides=='Yes':
            variables.sides = True
        else:
            variables.sides = False

        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Show ##
        ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

        ## Splash Logo ##

        logo = getdata('splash.logo')

        self.logo = QToolButton()
        self.wb.layout().addWidget (self.logo)

        ## Set logo ##
        if not logo==None:
            self.logo.setIcon(QIcon(res.get(logo)))

        logo_size = getdata('splash.logo-size')

        if not logo_size==None:
            self.w = int(logo_size)
        else:
            self.w = 300

        self.logo.setMaximumSize(self.w,self.w) ## Set size
        self.logo.setIconSize(QSize(self.w,self.w))

        self.logo.setStyleSheet('border:none;')

        self.logo.setGeometry(int(self.width()/2)-int(self.w/2),int(self.height()/2)-int(self.w/2),self.w,self.w)

        ## Run splash after showing backend ##
        timeout = getdata('splash.timeout')
        if timeout==None:
            variables.splash_timeout = 3000
        else:
            variables.splash_timeout = int(timeout)

        QTimer.singleShot(variables.splash_timeout, self.runLogin) ## Run login

## LoginW ##
class LoginWidget (QMainWindow):
    def __init__(self,ports):
        super(LoginWidget, self).__init__()

        ## ports ##

        self.Backend = ports[0]
        self.Env = ports[1]

        ######

        loginw_bgcolor = getdata('loginw.bgcolor')
        loginw_fgcolor = getdata('loginw.fgcolor')
        loginw_width = getdata('loginw.width')
        loginw_height = getdata('loginw.height')
        loginw_round = getdata('loginw.round')
        loginw_round_size = getdata('loginw.round-size')
        loginw_location = getdata('loginw.location')
        loginw_shadow = getdata('loginw.shadow')
        loginw_userlogo = getdata('loginw.userlogo')
        loginw_userlogo_shadow = getdata('loginw.userlogo.shadow')
        loginw_userlogo_color = getdata('loginw.userlogo.color')
        loginw_input_bgcolor = getdata('loginw.input.bgcolor')
        loginw_input_fgcolor = getdata('loginw.input.fgcolor')
        loginw_input_shadow = getdata('loginw.input.shadow')
        loginw_input_round = getdata('loginw.input.round')
        loginw_input_width = getdata('loginw.input.width')
        loginw_input_round_size = getdata('loginw.input.round-size')
        loginw_userlogo_round = getdata('loginw.userlogo.round')
        loginw_userlogo_round_size = getdata('loginw.userlogo.round-size')
        loginw_input_fontsize = getdata('loginw.input.fontsize')
        loginw_login_bgcolor = getdata('loginw.login.bgcolor')
        loginw_login_fgcolor = getdata('loginw.login.fgcolor')
        loginw_login_fontsize = getdata('loginw.login.fontsize')
        loginw_login_round = getdata('loginw.login.round')
        loginw_login_round_size = getdata('loginw.login.round-size')
        loginw_login_hide = getdata ('loginw.login.hide')
        loginw_login_hover_fgcolor = getdata('loginw.login.hover-fgcolor')
        loginw_login_hover_bgcolor = getdata('loginw.login.hover-bgcolor')
        loginw_login_width = getdata('loginw.login.width')
        loginw_login_shadow = getdata('loginw.login.shadow')
        loginw_enter_bgcolor = getdata('loginw.enter.bgcolor')
        loginw_enter_fgcolor = getdata('loginw.enter.fgcolor')
        loginw_enter_fontsize = getdata('loginw.enter.fontsize')
        loginw_enter_round = getdata('loginw.enter.round')
        loginw_enter_round_size = getdata('loginw.enter.round-size')
        loginw_enter_hide = getdata('loginw.enter.hide')
        loginw_enter_hover_fgcolor = getdata('loginw.enter.hover-fgcolor')
        loginw_enter_hover_bgcolor = getdata('loginw.enter.hover-bgcolor')
        loginw_enter_width = getdata('loginw.enter.width')
        loginw_enter_shadow = getdata('loginw.enter.shadow')
        loginw_unlock_bgcolor = getdata('loginw.unlock.bgcolor')
        loginw_unlock_fgcolor = getdata('loginw.unlock.fgcolor')
        loginw_unlock_fontsize = getdata('loginw.unlock.fontsize')
        loginw_unlock_round = getdata('loginw.unlock.round')
        loginw_unlock_round_size = getdata('loginw.unlock.round-size')
        loginw_unlock_hide = getdata('loginw.unlock.hide')
        loginw_unlock_hover_fgcolor = getdata('loginw.unlock.hover-fgcolor')
        loginw_unlock_hover_bgcolor = getdata('loginw.unlock.hover-bgcolor')
        loginw_unlock_width = getdata('loginw.unlock.width')
        loginw_unlock_shadow = getdata('loginw.unlock.shadow')
        loginw_input_height = getdata('loginw.input.height')
        loginw_login_height = getdata('loginw.login.height')
        loginw_enter_height = getdata('loginw.enter.height')
        loginw_unlock_height = getdata('loginw.unlock.height')
        font = getdata('font')

        ## Check data ##
        if font == None:
            font = variables.font

        f.setFamily(font)

        if loginw_bgcolor == None:
            loginw_bgcolor = variables.loginw_bgcolor

        if loginw_input_height == None:
            loginw_input_height = variables.loginw_input_height
        else:
            loginw_input_height = int(loginw_input_height)

        if loginw_login_height == None:
            loginw_login_height = variables.loginw_login_height
        else:
            loginw_login_height = int(loginw_login_height)

        if loginw_enter_height == None:
            loginw_enter_height = variables.loginw_enter_height
        else:
            loginw_enter_height = int(loginw_enter_height)

        if loginw_unlock_height == None:
            loginw_unlock_height = variables.loginw_unlock_height
        else:
            loginw_unlock_height = int(loginw_unlock_height)

        if loginw_login_width == None:
            loginw_login_width = variables.loginw_login_width
        else:
            loginw_login_width = int(loginw_login_width)

        if loginw_input_width == None:
            loginw_input_width = variables.loginw_input_width
        else:
            loginw_input_width = int(loginw_input_width)

        if loginw_enter_width == None:
            loginw_enter_width = variables.loginw_enter_width
        else:
            loginw_enter_width = int(loginw_enter_width)

        if loginw_unlock_width == None:
            loginw_unlock_width = variables.loginw_unlock_width
        else:
            loginw_unlock_width = int(loginw_unlock_width)

        if loginw_fgcolor == None:
            loginw_fgcolor = variables.loginw_fgcolor

        if loginw_login_bgcolor == None:
            loginw_login_bgcolor = variables.loginw_login_bgcolor

        if loginw_login_fgcolor == None:
            loginw_login_fgcolor = variables.loginw_login_fgcolor

        if loginw_login_hover_bgcolor == None:
            loginw_login_hover_bgcolor = variables.loginw_login_hover_bgcolor

        if loginw_login_hover_fgcolor == None:
            loginw_login_hover_fgcolor = variables.loginw_login_hover_fgcolor

        if loginw_enter_bgcolor == None:
            loginw_enter_bgcolor = variables.loginw_enter_bgcolor

        if loginw_enter_fgcolor == None:
            loginw_enter_fgcolor = variables.loginw_enter_fgcolor

        if loginw_enter_hover_bgcolor == None:
            loginw_enter_hover_bgcolor = variables.loginw_enter_hover_bgcolor

        if loginw_enter_hover_fgcolor == None:
            loginw_enter_hover_fgcolor = variables.loginw_enter_hover_fgcolor

        if loginw_unlock_bgcolor == None:
            loginw_unlock_bgcolor = variables.loginw_unlock_bgcolor

        if loginw_unlock_fgcolor == None:
            loginw_unlock_fgcolor = variables.loginw_unlock_fgcolor

        if loginw_unlock_hover_bgcolor == None:
            loginw_unlock_hover_bgcolor = variables.loginw_unlock_hover_bgcolor

        if loginw_unlock_hover_fgcolor == None:
            loginw_unlock_hover_fgcolor = variables.loginw_unlock_hover_fgcolor

        if loginw_width == None:
            loginw_width = self.width()

        if loginw_height == None:
            loginw_height = self.height()

        if loginw_round_size == None:
            loginw_round_size = str(variables.loginw_round_size)+'% '+str(variables.loginw_round_size)+'%'
        else:
            loginw_round_size = loginw_round_size.replace(' ','% ')+'%'

        if loginw_userlogo_round_size == None:
            loginw_userlogo_round_size = str(variables.loginw_userlogo_round_size)+'% '+str(variables.loginw_userlogo_round_size)+'%'
        else:
            loginw_userlogo_round_size = loginw_userlogo_round_size.replace(' ','% ')+'%'

        if loginw_input_round_size == None:
            loginw_input_round_size = str(variables.loginw_input_round_size)+'% '+str(variables.loginw_input_round_size)+'%'
        else:
            loginw_input_round_size = loginw_input_round_size.replace(' ','% ')+'%'

        if loginw_login_round_size == None:
            loginw_login_round_size = str(variables.loginw_login_round_size)+'% '+str(variables.loginw_login_round_size)+'%'
        else:
            loginw_login_round_size = loginw_login_round_size.replace(' ','% ')+'%'

        if loginw_enter_round_size == None:
            loginw_enter_round_size = str(variables.loginw_enter_round_size)+'% '+str(variables.loginw_enter_round_size)+'%'
        else:
            loginw_enter_round_size = loginw_enter_round_size.replace(' ','% ')+'%'

        if loginw_unlock_round_size == None:
            loginw_unlock_round_size = str(variables.loginw_unlock_round_size)+'% '+str(variables.loginw_unlock_round_size)+'%'
        else:
            loginw_unlock_round_size = loginw_unlock_round_size.replace(' ','% ')+'%'

        if loginw_round == 'Yes':
            loginw_round = loginw_round_size
        else:
            loginw_round ='0% 0%'

        if loginw_userlogo_round == 'Yes':
            loginw_userlogo_round = loginw_userlogo_round_size
        else:
            loginw_userlogo_round = '0% 0%'

        if loginw_input_round == 'Yes':
            loginw_input_round = loginw_input_round_size
        else:
            loginw_input_round = '0% 0%'

        if loginw_login_round == 'Yes':
            loginw_login_round = loginw_login_round_size
        else:
            loginw_login_round = '0% 0%'

        if loginw_enter_round == 'Yes':
            loginw_enter_round = loginw_enter_round_size
        else:
            loginw_enter_round = '0% 0%'

        if loginw_unlock_round == 'Yes':
            loginw_unlock_round = loginw_unlock_round_size
        else:
            loginw_unlock_round = '0% 0%'

        if loginw_location == None:
            loginw_location = variables.loginw_location

        if loginw_input_fontsize==None:
            loginw_input_fontsize = variables.loginw_input_fontsize
        else:
            loginw_input_fontsize = int(loginw_input_fontsize)

        if loginw_login_fontsize==None:
            loginw_login_fontsize = variables.loginw_login_fontsize
        else:
            loginw_login_fontsize = int(loginw_login_fontsize)

        if loginw_login_hide == None: loginw_login_hide = variables.loginw_login_hide

        if loginw_enter_fontsize==None:
            loginw_enter_fontsize = variables.loginw_enter_fontsize
        else:
            loginw_enter_fontsize = int(loginw_enter_fontsize)

        if loginw_enter_hide == None: loginw_enter_hide = variables.loginw_enter_hide

        if loginw_unlock_fontsize==None:
            loginw_unlock_fontsize = variables.loginw_unlock_fontsize
        else:
            loginw_unlock_fontsize = int(loginw_unlock_fontsize)

        if loginw_unlock_hide == None:
            loginw_unlock_hide = variables.loginw_unlock_hide

        self.setMaximumSize(loginw_width,loginw_height)  ## Set size of loginw

        ## Locations ##

        if loginw_location == 'center':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2),
                             int(self.Env.height() / 2) - int(self.height() / 2), self.width(),
                             self.height())  ## Geometric
        elif loginw_location == 'top':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2), int(self.height() / 20), self.width(),
                             self.height())  ## Geometric
        elif loginw_location == 'left':
            self.setGeometry(int(self.width() / 20), int(self.Env.height() / 2) - int(self.height() / 2), self.width(),
                             self.height())  ## Geometric
        elif loginw_location == 'right':
            self.setGeometry(self.Env.width() - int(self.width() / 20) - self.width(),
                             int(self.Env.height() / 2) - int(self.height() / 2), self.width(),
                             self.height())  ## Geometric
        elif loginw_location == 'bottom':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2),
                             self.Env.height() - int(self.height() / 20) - self.height(), self.width(),
                             self.height())  ## Geometric

        if loginw_shadow==None: loginw_shadow = variables.loginw_shadow
        if loginw_userlogo_shadow == None: loginw_userlogo_shadow = variables.loginw_userlogo_shadow
        if loginw_input_shadow == None: loginw_input_shadow = variables.loginw_input_shadow
        if loginw_login_shadow == None: loginw_login_shadow = variables.loginw_login_shadow
        if loginw_enter_shadow == None: loginw_enter_shadow = variables.loginw_enter_shadow
        if loginw_unlock_shadow == None: loginw_unlock_shadow = variables.loginw_unlock_shadow

        if loginw_shadow=='Yes':
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
        self.setStyleSheet(f'color:{loginw_fgcolor};border-radius:{loginw_round};')  ## Set color white as default
        self.btnColorButton.setStyleSheet(f'background-color:{loginw_bgcolor};')

        ## Userlogo ##

        self.userlogo = QToolButton()

            ## Set size & location ##
        self.userlogo.setMaximumSize(250,250)
        self.userlogo.setIconSize(QSize(250,250))
        self.userlogo.setIcon(QIcon(res.get(loginw_userlogo)))
        self.userlogo.setGeometry(int(self.width()/2)-int(self.userlogo.width()/2),int(self.height()/4)-int(self.userlogo.height()/4),self.userlogo.width(),self.userlogo.height())

        if loginw_userlogo_color == None: loginw_userlogo_color = variables.userlogo_color

        #if not loginw_userlogo == None:
        if self.Env.objectName() == 'Enter' or self.Env.objectName() == 'Unlock':
            logo = control.read_record('loginw.userlogo', '/etc/users/' + self.Env.username)
            if not logo == None: loginw_userlogo = logo

        self.userlogo.setStyleSheet(
            f'background-color: {loginw_userlogo_color};border-radius: {loginw_userlogo_round};')

            ## Shadow for userlogo ##
        ## Shadow ##
        if loginw_userlogo_shadow=='Yes':
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.userlogo.setGraphicsEffect(shadow)

            ## Default userlogo ##
        self.layout().addWidget (self.userlogo)

            ## leInput username ##

        self.leInput = QLineEdit()

            ## Size & Location of leInput ##
        self.leInput.setMaximumSize(loginw_input_width,loginw_input_height)
        self.leInput.setGeometry(int(self.width()/2)-int(self.leInput.width()/2),self.height()-int(self.height()/4)-self.leInput.height(),self.leInput.width(),self.leInput.height())

            ## Shadow of leInput ##
        ## Shadow ##
        if loginw_input_shadow=='Yes':
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.leInput.setGraphicsEffect(shadow)

            ## Colors of leInput ##
        if loginw_input_bgcolor==None: loginw_input_bgcolor=variables.input_bgcolor
        if loginw_input_fgcolor==None: loginw_input_fgcolor=variables.input_fgcolor

            ## Setting up all colors ##
        self.leInput.setStyleSheet('padding-left: 10%;padding-right: 10%;background-color: '+loginw_input_bgcolor+';color: '+loginw_input_fgcolor+";border-width: 3%;border-radius: "+loginw_input_round)

            ## Place holder in input ##

        if self.Env.objectName()=='Login':
            self.leInput.setPlaceholderText(res.get('@string/username_placeholder')) # See https://stackoverflow.com/questions/24274318/placeholder-text-not-showing-pyside-pyqt
            self.leInput.setFont(f)
        else:
            self.leInput.setEchoMode(QLineEdit.Password)
            self.leInput.setPlaceholderText(res.get('@string/unlock_hint'))
            self.leInput.setFont(f)

            ## Setting up font settings ##
        f.setPointSize(loginw_input_fontsize)
        self.leInput.setFont(f)

            ## Connect to action ##

        self.leInput.returnPressed.connect (self.actions)

        ## Add leInput Widget ##
        self.layout().addWidget(self.leInput)

            ## Enter button ##
        if self.Env.objectName()=='Login':
            self.btnLogin = QPushButton()

            ## Shadow ##
            if loginw_login_shadow == 'Yes':
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
                        background-color: ''' + loginw_login_bgcolor + """;
                        color: """ + loginw_login_fgcolor + """;
                        border-radius: """ + loginw_login_round + '''
                    } 
                    QPushButton:hover {
                        background-color:''' + loginw_login_hover_bgcolor + ''';
                        color:''' + loginw_login_hover_fgcolor + ''';
                        border-radius: ''' + loginw_login_round + ''';
                    }
                    ''')

            f.setPointSize(loginw_login_fontsize)
            self.btnLogin.setFont(f)
            if loginw_login_hide == 'Yes':
                self.btnLogin.hide()
            self.btnLogin.setText(res.get('@string/next_text'))
            self.btnLogin.setFont(f)
            self.btnLogin.setMaximumSize(loginw_login_width, loginw_login_height)
            self.btnLogin.setGeometry(int(self.width() / 2) - int(self.btnLogin.width() / 2),
                                      self.height() - int(self.height() / 4) - int(self.btnLogin.height() / 4) + int(self.btnLogin.height()/2),
                                      self.btnLogin.width(), self.btnLogin.height())
            self.layout().addWidget(self.btnLogin)

        elif self.Env.objectName() == 'Enter':
            self.btnEnter = QPushButton()
            ## Shadow ##
            if loginw_enter_shadow == 'Yes':
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
                        background-color: ''' + loginw_enter_bgcolor + """;
                        color: """ + loginw_enter_fgcolor + """;
                        border-radius: """ + loginw_enter_round + '''
                    } 
                    QPushButton:hover {
                        background-color:''' + loginw_enter_hover_bgcolor + ''';
                        color:''' + loginw_enter_hover_fgcolor + ''';
                        border-radius: ''' + loginw_enter_round + ''';
                    }
                    ''')

            f.setPointSize(loginw_enter_fontsize)
            self.btnEnter.setFont(f)
            if loginw_enter_hide == 'Yes':
                self.btnEnter.hide()
            self.btnEnter.setText(res.get('@string/enter_text'))
            self.btnEnter.setFont(f)
            self.btnEnter.setMaximumSize(loginw_enter_width, loginw_enter_height)
            self.btnEnter.setGeometry(int(self.width() / 2) - int(self.btnEnter.width() / 2),
                                      self.height() - int(self.height() / 4) - int(self.btnEnter.height() / 4) + int(self.btnEnter.height()/2),
                                      self.btnEnter.width(), self.btnEnter.height())
            self.layout().addWidget(self.btnEnter)

        elif self.Env.objectName()=='Unlock':
            self.btnUnlock = QPushButton()
            ## Shadow ##
            if loginw_unlock_shadow == 'Yes':
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
                                    background-color: ''' + loginw_unlock_bgcolor + """;
                                    color: """ + loginw_unlock_fgcolor + """;
                                    border-radius: """ + loginw_unlock_round + '''
                                } 
                                QPushButton:hover {
                                    background-color:''' + loginw_unlock_hover_bgcolor + ''';
                                    color:''' + loginw_unlock_hover_fgcolor + ''';
                                    border-radius: ''' + loginw_unlock_round + ''';
                                }
                                ''')

            f.setPointSize(loginw_unlock_fontsize)
            self.btnUnlock.setFont(f)
            if loginw_enter_hide == 'Yes':
                self.btnUnlock.hide()
            self.btnUnlock.setText(res.get('@string/unlock_text'))
            self.btnUnlock.setFont(f)
            self.btnUnlock.setMaximumSize(loginw_unlock_width, loginw_unlock_height)
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
            print(self.Backend)
            print(self.Env)

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
                self.Backend.submenu.show()
                self.Backend.taskbar.show()
                self.Backend.backgroundButton.show()
                self.Env.BtnUnlock.hide()
                self.Env.lock.hide()

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
    def __init__(self,ports):
        super(Login, self).__init__()

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
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        ## Ports ##

        self.Backend = ports[0]

        bgcolor = getdata('login.bgcolor')
        background = getdata('login.background')
        fgcolor = getdata('login.fgcolor')

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0,0,variables.width,variables.height)
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##

        if background==None and bgcolor==None and not fgcolor==None:
            variables.login_fgcolor = fgcolor
            ## Set colors ##
            self.setStyleSheet(f'color: {variables.login_fgcolor};')
            self.backgroundButton.setStyleSheet(f'border:none;background-color: {variables.login_bgcolor};')

        elif background==None and not fgcolor==None:

            ## Set colors ##
            variables.login_bgcolor = bgcolor
            variables.login_fgcolor = fgcolor

            self.setStyleSheet(f'color: {variables.login_fgcolor};')
            self.backgroundButton.setStyleSheet(f'border:none;background-color: {variables.login_bgcolor};')
        elif not background==None and not fgcolor==None:
            ## Set bgcolor ##

            variables.login_background = res.get(background)
            self.setStyleSheet(f'color: {variables.login_fgcolor};')
            self.backgroundButton.setStyleSheet(f'border:none;background-image: url({variables.login_background});')
        else:
            self.setStyleSheet(f'background-color:{variables.login_bgcolor};color: {variables.login_fgcolor};')

        ## Set size ##
        width = getdata('width')
        height = getdata('height')
        autosize =getdata('autosize')

        if not width == None  and not autosize=='Yes':
            variables.width = int(width)

        if not height == None and not autosize=='Yes':
            variables.height = int(height)

        self.resize(variables.width, variables.height)

        ## Set sides ##
        ## Set sides ##
        sides = getdata('sides')

        if sides == 'Yes':
            variables.sides = True
        else:
            variables.sides = False
        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Login widget ##

        self.loginw = LoginWidget([self.Backend,self])
        self.layout().addWidget (self.loginw)

        ## Show ##
        ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

## Enter ##
class Enter (QMainWindow):
    def __init__(self,ports,username):
        super(Enter, self).__init__()

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
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        bgcolor = getdata('enter.bgcolor')
        background = getdata('enter.background')
        fgcolor = getdata('enter.fgcolor')

        if not self.username=='guest':
            value = control.read_record('enter.bgcolor','/etc/users/'+self.username)
            if not value==None: bgcolor = value

        if not self.username=='guest':
            value = control.read_record('enter.background','/etc/users/'+self.username)
            if not value==None: background = value

        if not self.username=='guest':
            value = control.read_record('enter.fgcolor','/etc/users/'+self.username)
            if not value==None: fgcolor = value

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, variables.width, variables.height)
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##

        if background == None and bgcolor == None and not fgcolor == None:
            variables.enter_fgcolor = fgcolor
            ## Set colors ##
            self.setStyleSheet(f'color: {variables.enter_fgcolor};')
            self.backgroundButton.setStyleSheet(
                f'border:none;background-color: {variables.enter_bgcolor};')

        elif background == None and not fgcolor == None:

            ## Set colors ##
            variables.enter_bgcolor = bgcolor
            variables.enter_fgcolor = fgcolor

            self.setStyleSheet(f'color: {variables.enter_fgcolor};')

            self.backgroundButton.setStyleSheet(
                f'border:none;background-color: {variables.enter_bgcolor};')
        elif not background == None and not fgcolor == None:
            ## Set bgcolor ##

            variables.enter_background = res.get(background)
            self.setStyleSheet(f'color: {variables.enter_fgcolor};')
            self.backgroundButton.setStyleSheet(
                f'border:none;background-image: url({variables.enter_background});')
        else:
            self.setStyleSheet(f'background-color:{variables.enter_bgcolor};color: {variables.enter_fgcolor};')

        ## Set size ##
        width = getdata('width')
        height = getdata('height')
        autosize =getdata('autosize')

        if not width == None  and not autosize=='Yes':
            variables.width = int(width)

        if not height == None and not autosize=='Yes':
            variables.height = int(height)

        self.resize(variables.width, variables.height)

        ## Set sides ##
        ## Set sides ##
        sides = getdata('sides')

        if sides == 'Yes':
            variables.sides = True
        else:
            variables.sides = False
        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Login widget ##

        self.loginw = LoginWidget([self.Backend,self])
        self.layout().addWidget (self.loginw)

        ## Show ##
        ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

class AppListView(QListView):
    def format(self, it):
        if files.isfile (it.whatsThis()):
            name = it.text().replace('.desk','')
            locale = control.read_record('locale','/etc/gui')
            subname = res.etc(name,f'name[{locale}]')
            icon = res.etc(name,'logo')
            it.setText(subname)
            it.setFont(f)
            it.setIcon(QIcon(res.get(icon)))

    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]

        # Get font #
        font = getdata('font')
        if not self.Env.username == 'guest':
            value = control.read_record('font', '/etc/users/' + self.Env.username)
            if not value == None: font = value
        if font == None: font = variables.font

        f.setFamily(font)

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
            locale = control.read_record('locale','/etc/gui')
            subname = res.etc(name,f'name[{locale}]')
            icon = res.etc(name,'logo')
            it.setText(subname)
            it.setFont(f)
            it.setIcon(QIcon(res.get(icon)))

    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]

        # Get font #
        font = getdata('font')
        if not self.Env.username == 'guest':
            value = control.read_record('font', '/etc/users/' + self.Env.username)
            if not value == None: font = value
        if font == None: font = variables.font

        f.setFamily(font)

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
            locale = control.read_record('locale','/etc/gui')
            subname = control.read_record(f'name[{locale}]',f'/usr/share/themes/{name}.desk')
            icon = control.read_record(f'logo',f'/usr/share/themes/{name}.desk')
            it.setText(subname)
            it.setFont(f)
            it.setIcon(QIcon(res.get(icon)))

    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]

        # Get font #
        font = getdata('font')
        if not self.Env.username == 'guest':
            value = control.read_record('font', '/etc/users/' + self.Env.username)
            if not value == None: font = value
        if font == None: font = variables.font

        f.setFamily(font)

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
                self.Env.RunApp('text', ['عدم دسترسی', 'حساب مهمان دسترسی به تغییر پوسته ندارد'])
                files.write('/proc/info/id', 'desktop')
            elif not control.read_record ('theme-name','/etc/gui')==control.read_record('theme-name',self.item.whatsThis()):
                self.Widget.hide()
                self.Env.RunApp('bool', [self.item.text(), 'برای اعمال این تم باید پای ابر را راه اندازی مجدد کنید', self.reboot_act_])
                files.write('/proc/info/id','desktop')
            else:
                files.write('/proc/info/id', 'desktop')
                self.Env.RunApp('text', [self.item.text(), 'این تم از پیش تنظیم شده است'])
                files.write('/proc/info/id', 'desktop')

    def reboot_act_(self,yes):
        if yes:
            Script(control.read_record('exec', self.item.whatsThis()))
            app.endall()
            self.Env.hide()
            commands.reboot([])
            sys.exit(0)

class SessionListView(QListView):
    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]

        # Get font #
        font = getdata('font')
        if not self.Env.username == 'guest':
            value = control.read_record('font', '/etc/users/' + self.Env.username)
            if not value == None: font = value
        if font == None: font = variables.font

        f.setFamily(font)

        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        it = QStandardItem('escape')
        it.setText('فرار کردن')
        it.setWhatsThis('escape')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys',"escape-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('restart')
        it.setText('راه اندازی مجدد')
        it.setWhatsThis('restart')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys', "restart-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('lock')
        it.setText('قفل کردن')
        it.setWhatsThis('lock')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys', "lock-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('logout')
        it.setText('خروج از نشست')
        it.setWhatsThis('logout')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys', "logout-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('switchuser')
        it.setText('رفتن به نشستی دیگر')
        it.setWhatsThis('switchuser')
        it.setFont(f)
        it.setIcon(QIcon(res.get(res.etc('pysys', "switchuser-icon"))))
        self.entry.appendRow(it)

        it = QStandardItem('suspend')
        it.setText('حالت خواب')
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
            self.Env.RunApp(self.item.whatsThis().replace('.desk','').replace('/usr/share/applications/',''),None)

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

        ## Set username ##
        self.username = self.Env.username

            ## Get DATAS ###################

        ## Set bgcolor ##
        bgcolor = getdata('taskbar.bgcolor')
        if not self.Env.username=='guest':
            value = control.read_record('taskbar.bgcolor','/etc/users/'+self.username)
            if not value==None: bgcolor = value
        if bgcolor == None: bgcolor = variables.taskbar_bgcolor

        ## Set fgcolor ##
        fgcolor = getdata('taskbar.fgcolor')
        if not self.Env.username=='guest':
            value = control.read_record('taskbar.fgcolor','/etc/users/'+self.username)
            if not value==None: fgcolor = value
        if fgcolor == None: fgcolor = 'black'

        ## Set location ##
        location = getdata('taskbar.location')
        if not self.Env.username == 'guest':
            value = control.read_record('taskbar.location', '/etc/users/' + self.username)
            if not value == None: location = value
        if location == None: location = variables.taskbar_location

        ## locked ##
        locked = getdata('taskbar.locked')
        if not self.Env.username == 'guest':
            value = control.read_record('taskbar.locked', '/etc/users/' + self.username)
            if not value == None: locked = value
        if locked == None: locked = variables.taskbar_locked

        ## locked ##
        size = getdata('taskbar.size')
        if not self.Env.username == 'guest':
            value = control.read_record('taskbar.size', '/etc/users/' + self.username)
            if not value == None: size = int(value)
        if size == None: size = int(variables.taskbar_size)

        # float #
        float = getdata('taskbar.float')
        if not self.Env.username == 'guest':
            value = control.read_record('taskbar.float', '/etc/users/' + self.username)
            if not value == None: float = value
        if float == None: float = variables.taskbar_float

        # styles #

        self.setStyleSheet('background-color: '+bgcolor+";color: "+fgcolor+";")

        # location #
        if location=='top':
            self.Env.addToolBar (Qt.TopToolBarArea,self)
        elif location=='left':
            self.Env.addToolBar(Qt.LeftToolBarArea, self)
        elif location=='right':
            self.Env.addToolBar(Qt.RightToolBarArea, self)
        elif location=='bottom':
            self.Env.addToolBar(Qt.BottomToolBarArea, self)

        # locked #
        if locked=='Yes':
            self.setMovable(False)
        else:
            self.setMovable(True)

        # float #
        if float=='Yes':
            self.setFloatable(True)
        else:
            self.setFloatable(False)

        # size #
        self.setMinimumSize(QSize(int(size),int(size)))
        self.setIconSize(QSize(int(size),int(size))) # https://stackoverflow.com/questions/21133612/how-to-change-iconsize-of-qtoolbutton

        self.btnMenu = QToolButton()
        self.btnMenu.setIcon(QIcon(res.get(control.read_record('menu','/etc/gui'))))
        self.btnMenu.setMinimumSize(int(size), int(size))
        self.btnMenu.setObjectName('btnMenu')
        self.btnMenu.clicked.connect (self.menuApps)
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
                self.btnApp.setMinimumSize(int(size),int(size))
                self.btnApp.setObjectName(i)
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

class MenuApplications (QMainWindow):
    def __init__(self,ports):
        super(MenuApplications, self).__init__()

        ## Ports ##
        self.Backend = ports[0]
        self.Env = ports[1]

        self.username = self.Env.username

        self.setGeometry(0,0,self.Env.width(),self.Env.height())
        self.setStyleSheet('background-color: white')

        location = getdata('taskbar.location')
        if not self.Env.username == 'guest':
            value = control.read_record('taskbar.location', '/etc/users/' + self.username)
            if not value == None: location = value
        if location == None: location = variables.taskbar_location

        size = int(getdata('taskbar.size'))
        if not self.Env.username == 'guest':
            value = control.read_record('taskbar.size', '/etc/users/' + self.username)
            if not value == None: size = int(value)
        if size == None: size = int(variables.taskbar_size)

        if self.Env.width()>1000 and self.Env.height()>720:
            if location == 'bottom':
                self.setGeometry(0, int(self.Env.height() / 3), int(self.Env.width() / 3),
                                 int(self.Env.height() / 1.5) - size - 15)
            elif location == 'top':
                self.setGeometry(0, size + 15, int(self.Env.width() / 3), (self.Env.height() / 1.5) - size - 15)
            elif location == "left":
                self.setGeometry(size + 15, 0, int(self.Env.width() / 3) - size - 15, int(self.Env.height() / 1.5))
            elif location == "right":
                self.setGeometry(self.Env.width() - (self.Env.width() / 3), 0, (self.Env.width() / 3) - size - 15,
                                 int(self.Env.height() / 1.5))
            else:
                self.setGeometry(0, 0, self.Env.width(), self.Env.height())

        else:
            self.setGeometry(0, 0, self.Env.width(), self.Env.height()-size-15)

        self.tabs = QTabWidget()
        self.tabs.setFont(f)
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
            self.resize(self.w,self.h+variables.app_title_size)
        else:
            self.setGeometry(0, 0, self.Env.width(), self.Env.height())
            mainw.resize(self.Env.width(), self.Env.height() - variables.app_title_size)

    def SetWindowTitle (self,text):
        self.titletext.setText(text)
        self.titletext.setFont(f)

    def WindowTitle (self):
        return self.titletext.text()

    def SetWindowIcon (self,icon):
        self.iconwidget.setPixmap(icon.pixmap(int(variables.app_title_size)-18,int(variables.app_title_size)-18))

    def Close (self):
        app.end(self.appname)
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
        location = getdata('taskbar.location')
        if not self.Env.username == 'guest':
            value = control.read_record('taskbar.location', '/etc/users/' + self.username)
            if not value == None: location = value
        if location == None: location = variables.taskbar_location

        size = int(getdata('taskbar.size'))
        if not self.Env.username == 'guest':
            value = control.read_record('taskbar.size', '/etc/users/' + self.username)
            if not value == None: size = int(value)
        if size == None: size = int(variables.taskbar_size)

        if self.max == False:
            self.save_w = self.width()
            self.save_h = self.height()
            self.save_ww = self.mainWidget.width()
            self.save_wh = self.mainWidget.height()

            size = int(size)
            self.app_title_size = int(self.app_title_size)

            if location=='bottom':
                self.setGeometry(0, 0, self.Env.width(), self.Env.height()-size-15)
                self.mainWidget.resize (self.Env.width(),self.Env.height()-variables.app_title_size-size-15)
                self.titlebar.setGeometry(0,0,self.Env.width(),self.app_title_size)
                #self.titletext.setGeometry(self.app_title_size, 0, self.Env.width(), self.app_title_size)

            elif location=='top':
                self.setGeometry(0, size+15, self.Env.width(), self.Env.height() - size - 15)
                self.mainWidget.resize(self.Env.width(), self.Env.height() - variables.app_title_size - size - 15)
                self.titlebar.setGeometry(0, 0, self.Env.width(), self.app_title_size)
                #self.titletext.setGeometry(self.app_title_size, 0, self.Env.width(), self.app_title_size)

            elif location=="left":
                self.setGeometry(size+15, 0, self.Env.width() - size - 15, self.Env.height())
                self.mainWidget.resize(self.Env.width()-size-15, self.Env.height() - variables.app_title_size)
                self.titlebar.setGeometry(0, 0, self.Env.width()-size-15, self.app_title_size)
                #self.titletext.setGeometry(self.app_title_size, 0, self.Env.width()-size-15, self.app_title_size)

            elif location=="right":
                self.setGeometry(0, 0, self.Env.width() - size - 15, self.Env.height())
                self.mainWidget.resize(self.Env.width()-size-15, self.Env.height() - variables.app_title_size)
                self.titlebar.setGeometry(0, 0, self.Env.width()-size-15, self.app_title_size)
                #self.titletext.setGeometry(self.app_title_size, 0, self.Env.width()-size-15, self.app_title_size)
            else:
                self.setGeometry(0, 0, self.Env.width(), self.Env.height())
                self.mainWidget.resize(self.Env.width(), self.Env.height() - variables.app_title_size)
                self.titlebar.setGeometry(0, 0, self.Env.width(), self.app_title_size)
                #self.titletext.setGeometry(self.app_title_size, 0, self.Env.width(), self.app_title_size)

            self.mainWidget.update()

            self.max = True
        else:
            self.setGeometry(int(self.Env.width()/2)-int(self.save_w/2),int(self.Env.height()/2)-int(self.save_h/2),self.save_w,self.save_h)
            self.titlebar.setGeometry(0, 0, self.save_w, variables.app_title_size)
            self.mainWidget.resize(self.save_ww,self.save_wh)
            self.mainWidget.update()
            self.max = False

    def __init__(self,ports):
        super(AppWidget, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.appname = ports[2]
        self.external = ports[3]

        self.setFocusPolicy(Qt.StrongFocus)

        font = getdata('font')
        if not self.Env.username == 'guest':
            value = control.read_record('font', '/etc/users/' + self.Env.username)
            if not value == None: font = value
        if font == None: font = variables.font

        f.setFamily(font)
        self.setFont(f)

        # user
        self.username = self.Env.username

        app.start(self.appname)  # start the application

        app_title_size = getdata('appw.title.size')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.title.size', '/etc/users/' + self.username)
            if not value == None: app_title_size = value
        if app_title_size == None: app_title_size = variables.app_title_size


        app_bgcolor = getdata('appw.bgcolor')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.bgcolor', '/etc/users/' + self.username)
            if not value == None: app_bgcolor = value
        if app_bgcolor == None: app_bgcolor = variables.app_bgcolor

        app_shadow = getdata('appw.shadow')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.shadow', '/etc/users/' + self.username)
            if not value == None: app_shadow = value
        if app_shadow == None: app_shadow = variables.app_shadow

        app_fgcolor = getdata('appw.fgcolor')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.fgcolor', '/etc/users/' + self.username)
            if not value == None: app_fgcolor = value
        if app_fgcolor == None: app_fgcolor = variables.app_fgcolor

        app_menu_bgcolor = getdata('appw.menu.bgcolor')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.menu.bgcolor', '/etc/users/' + self.username)
            if not value == None: app_menu_bgcolor = value
        if app_menu_bgcolor == None: app_menu_bgcolor = variables.app_menu_bgcolor

        app_logo = getdata('appw.logo')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.logo', '/etc/users/' + self.username)
            if not value == None: app_logo = value
        if app_logo == None: app_logo = variables.app_logo

        app_menu_fgcolor = getdata('appw.menu.fgcolor')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.menu.fgcolor', '/etc/users/' + self.username)
            if not value == None: app_menu_fgcolor = value
        if app_menu_fgcolor == None: app_menu_fgcolor = variables.app_menu_fgcolor

        app_title_bgcolor = getdata('appw.title.bgcolor')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.title.bgcolor', '/etc/users/' + self.username)
            if not value == None: app_title_bgcolor = value
        if app_title_bgcolor == None: app_title_bgcolor = variables.app_title_bgcolor

        app_title_fgcolor = getdata('appw.title.fgcolor')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.title.fgcolor', '/etc/users/' + self.username)
            if not value == None: app_title_fgcolor = value
        if app_title_fgcolor == None: app_title_fgcolor = variables.app_title_fgcolor

        app_title_close = getdata('appw.title.close')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.title.close', '/etc/users/' + self.username)
            if not value == None: app_title_close = value
        if app_title_close == None: app_title_close = variables.app_title_close

        app_title_float = getdata('appw.title.float')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.title.float', '/etc/users/' + self.username)
            if not value == None: app_title_float = value
        if app_title_float == None: app_title_float = variables.app_title_float

        app_title_float_hover = getdata('appw.title.float-hover')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.title.float-hover', '/etc/users/' + self.username)
            if not value == None: app_title_float_hover = value
        if app_title_float_hover == None: app_title_float_hover = variables.app_title_float_hover

        app_title_close = getdata('appw.title.close')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.title.close', '/etc/users/' + self.username)
            if not value == None: app_title_close = value
        if app_title_close == None: app_title_close = variables.app_title_close

        app_title_close_hover = getdata('appw.title.close-hover')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.title.close-hover', '/etc/users/' + self.username)
            if not value == None: app_title_close_hover = value
        if app_title_close_hover == None: app_title_close_hover = variables.app_title_close_hover

        # will create IGW
        app_menu_bgcolor_pressed = getdata('appw.menu.bgcolor-pressed')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.menu.bgcolor-pressed', '/etc/users/' + self.username)
            if not value == None: app_menu_bgcolor_pressed = value
        if app_menu_bgcolor_pressed == None: app_menu_bgcolor_pressed = variables.app_menu_bgcolor_pressed

        # will create IGW
        app_menu_fgcolor_pressed = getdata('appw.menu.fgcolor-pressed')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.menu.fgcolor-pressed', '/etc/users/' + self.username)
            if not value == None: app_menu_fgcolor_pressed = value
        if app_menu_fgcolor_pressed == None: app_menu_fgcolor_pressed = variables.app_menu_fgcolor_pressed

        app_body_bgcolor = getdata('appw.body.bgcolor')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.body.bgcolor', '/etc/users/' + self.username)
            if not value == None: app_body_bgcolor = value
        if app_body_bgcolor == None: app_body_bgcolor = variables.app_body_bgcolor

        app_body_fgcolor = getdata('appw.body.fgcolor')
        if not self.Env.username == 'guest':
            value = control.read_record('appw.body.fgcolor', '/etc/users/' + self.username)
            if not value == None: app_body_fgcolor = value
        if app_body_fgcolor == None: app_body_fgcolor = variables.app_body_fgcolor

        self.app_title_bgcolor = app_title_bgcolor
        self.app_title_fgcolor = app_title_fgcolor
        self.app_title_size = app_title_size

        self.setObjectName(self.appname)

        exec = control.read_record('exec', '/usr/share/applications/' + self.appname + ".desk")

        if not exec == None:
            exec = importlib.import_module(exec)
        else:
            self.close()

        # title bar #
        self.titlebar = QWidget()
        self.titlebar.setStyleSheet(f'background-color: {app_title_bgcolor};color: {app_title_fgcolor};')

        self.layouts = QHBoxLayout()
        self.titlebar.setLayout(self.layouts)

        # icon widget #
        self.icon = QIcon(res.get(app_logo))
        self.iconwidget = QLabel()
        self.iconwidget.setPixmap(self.icon.pixmap(int(variables.app_title_size)-18,int(variables.app_title_size)-18))
        self.iconwidget.resize(int(variables.app_title_size),int(variables.app_title_size))
        self.layouts.addWidget(self.iconwidget)

        self.iconwidget.setGeometry(0,0,int(variables.app_title_size),int(variables.app_title_size))

        # text title #
        self.titletext = QLabel()
        self.titletext.setStyleSheet(f'background-color:  {app_title_bgcolor};color: {app_title_fgcolor};')
        self.titletext.setMaximumWidth(self.titlebar.width())
        self.titletext.setGeometry(int(self.app_title_size),0,self.titlebar.width(),int(app_title_size))

        f.setPointSize(12)
        self.titletext.setFont(f)

        self.layouts.addWidget(self.titletext)

        # float button #
        self.btnMax = QToolButton()
        self.btnMax.setIcon(QIcon(res.get(app_title_float)))
        self.btnMax.setMinimumSize(int(app_title_size)-15,int(app_title_size)-15)
        self.btnMax.setGeometry(self.titlebar.width()-100,0,int(app_title_size),int(app_title_size))
        self.btnMax.clicked.connect(self.ShowMaximize)
        self.btnMax.setStyleSheet('QToolButton {border-radius: {0}% {0}%;} QToolButton::hover {border-radius: {0}% {0}%;background-color: {1}}'.replace("{1}",app_title_float_hover).replace("{0}",str(int((int(app_title_size))-16)/2)))

        self.layouts.addWidget(self.btnMax)

        self.btnEscape = QToolButton()
        self.btnEscape.setIcon(QIcon(res.get(app_title_close)))
        self.btnEscape.setMinimumSize(int(app_title_size)-15, int(app_title_size)-15)
        self.btnEscape.setGeometry(self.titlebar.width()-int(app_title_size),0,int(app_title_size),int(app_title_size))
        self.btnEscape.clicked.connect (self.Close)
        self.btnEscape.setStyleSheet('QToolButton {border-radius: {0}% {0}%;} QToolButton::hover {border-radius: {0}% {0}%;background-color: {1}}'.replace("{1}",app_title_close_hover).replace("{0}",str(int((int(app_title_size))-16)/2)))
        self.layouts.addWidget(self.btnEscape)

        self.whitewidget = QMainWindow()
        self.whitewidget.setStyleSheet(f'background-color: {app_body_bgcolor};color: {app_body_fgcolor};')
        self.setCentralWidget(self.whitewidget)

        # center widget #
        self.mainWidget = exec.MainApp([self.Backend,self.Env,self,self.appname,self.external])
        self.mainWidget.setGeometry(0,int(app_title_size),self.width(),self.height()-int(app_title_size))
        self.titlebar.setGeometry(0, 0, self.width(), int(app_title_size))
        self.setGeometry(int(self.Env.width()/2)-int(self.width()/2),int(self.Env.height()/2)-int(self.height()/2),self.width(),self.height())

        self.layout().addWidget(self.mainWidget)
        self.layout().addWidget(self.titlebar)

        if app_shadow=="Yes":
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

    def mouseMoveEvent(self, evt):
        """Move the toolbar with mouse iteration."""

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

## Shell ##
class Shell (QWidget):
    def __init__(self,ports):
        super(Shell, self).__init__()

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

## Desktop ##
class Desktop (QMainWindow):
    locale = control.read_record("locale", "/etc/gui")

    def RunApp (self,appname,external):
        app.switch(appname)
        files.write('/proc/info/su', self.username)

        if appname==getdata('terminal'):
            files.write('/proc/info/pass', self.password)
            self.layout().addWidget(AppWidget([self.Backend, self, getdata('terminal'), external]))
        elif files.isfile(f'/usr/share/applications/{appname}.desk'):
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
            subprocess.call([sys.executable, files.readall('/proc/info/boot'), "gui-login"])
            sys.exit(0)

    def switchuser_act (self):
        files.write('/proc/info/id','desktop')
        self.RunApp('bool', [res.get('@string/sau'), res.get('@string/saum'), self.switchuser_act_])
        files.write('/proc/info/id','desktop')

    def switchuser_act_(self,yes):
        if yes:
            files.create('/tmp/switched-user')
            subprocess.call([sys.executable, files.readall('/proc/info/boot'), "gui-login"])  # just run the login

    def unlock_act (self):
        self.submenu.show()
        self.taskbar.show()
        self.backgroundButton.show()
        self.BtnUnlock.hide()
        self.lock.hide()

    def enterlock_act (self):
        ## Set port name ##
        self.unlock = QMainWindow()
        self.unlock.setObjectName('Unlock')

        bgcolor = getdata('unlock.bgcolor')
        background = getdata('unlock.background')
        fgcolor = getdata('unlock.fgcolor')

        if not self.username == 'guest':
            value = control.read_record('unlock.bgcolor', '/etc/users/' + self.username)
            if not value == None: bgcolor = value

        if not self.username == 'guest':
            value = control.read_record('unlock.background', '/etc/users/' + self.username)
            if not value == None: background = value

        if not self.username == 'guest':
            value = control.read_record('unlock.fgcolor', '/etc/users/' + self.username)
            if not value == None: fgcolor = value

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, variables.width, variables.height)
        self.unlock.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##

        if background == None and bgcolor == None and not fgcolor == None:
            variables.unlock_fgcolor = fgcolor
            ## Set colors ##
            self.unlock.setStyleSheet(f'color: {variables.unlock_fgcolor};')
            self.unlock.backgroundButton.setStyleSheet(
                f'border:none;background-color: {variables.unlock_bgcolor};')

        elif background == None and not fgcolor == None:

            ## Set colors ##
            variables.unlock_bgcolor = bgcolor
            variables.unlock_fgcolor = fgcolor

            self.unlock.setStyleSheet(f'color: {variables.unlock_fgcolor};')

            self.unlock.backgroundButton.setStyleSheet(
                f'border:none;background-color: {variables.unlock_bgcolor};')
        elif not background == None and not fgcolor == None:
            ## Set bgcolor ##

            variables.unlock_background = res.get(background)
            self.unlock.setStyleSheet(f'color: {variables.unlock_fgcolor};')
            self.backgroundButton.setStyleSheet(
                f'border:none;background-image: url({variables.unlock_background});')
        else:
            self.unlock.setStyleSheet(f'background-color:{variables.unlock_bgcolor};color: {variables.unlock_fgcolor};')

        self.loginw = LoginWidget([self.Backend, self])
        self.unlock.layout().addWidget(self.loginw)

        self.setCentralWidget(self.unlock)

    def showTime_lock (self):
        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        label_time = current_time.toString(control.read_record('lock.clock.format','/etc/gui'))

        # showing it to the label
        self.lblClock.setText(res.num(label_time))
        self.lblClock.setFont(f)

    def lock_act (self):
        self.lock = QMainWindow()

        self.submenu.hide()
        self.taskbar.hide()
        self.backgroundButton.hide()
        self.BtnUnlock = QPushButton()
        self.BtnUnlock.setText('')
        self.lock.setCentralWidget(self.BtnUnlock)

        bgcolor = getdata('lock.bgcolor')
        background = getdata('lock.background')
        fgcolor = getdata('lock.fgcolor')
        clock_shadow = getdata('lock.clock.shadow')
        clock_size = getdata('lock.clock.size')
        clock_location = getdata('lock.clock.location')
        clock_color = getdata('lock.clock.color')

        ## Check background or bgcolor in users ##
        if not self.username == 'guest':
            value = control.read_record('lock.bgcolor', '/etc/users/' + self.username)
            if not value == None: bgcolor = value

        if bgcolor==None: bgcolor = variables.lock_bgcolor

        if not self.username == 'guest':
            value = control.read_record('lock.background', '/etc/users/' + self.username)
            if not value == None: background = value

        if background == None:
            background = variables.lock_background

        if not self.username == 'guest':
            value = control.read_record('lock.fgcolor', '/etc/users/' + self.username)
            if not value == None: fgcolor = value

        if fgcolor == None:
            fgcolor = variables.lock_fgcolor

        if not self.username == 'guest':
            value = control.read_record('lock.clock.shadow', '/etc/users/' + self.username)
            if not value == None: clock_shadow = variables.lock_clock_shadow

        if clock_shadow == None:
            clock_shadow = variables.lock_clock_shadow

        if not self.username == 'guest':
            value = control.read_record('lock.clock.color', '/etc/users/' + self.username)
            if not value == None: clock_color =  variables.lock_clock_color

        if clock_color == None:
            clock_color = variables.lock_clock_color

        if not self.username == 'guest':
            value = control.read_record('lock.clock.size', '/etc/users/' + self.username)
            if not value == None: clock_size =  variables.lock_clock_size

        if clock_size == None:
            clock_size =   variables.lock_clock_size

        if not self.username == 'guest':
            value = control.read_record('lock.clock.location', '/etc/users/' + self.username)
            if not value == None: clock_location =   variables.lock_clock_location

        if clock_location==None: clock_location = variables.lock_clock_location

            ## Set bgcolor and background ##

        if background == None and bgcolor == None and not fgcolor == None:
            variables.lock_fgcolor = fgcolor
            ## Set colors ##
            self.BtnUnlock.setStyleSheet(
                f'border:none;background-color: {variables.lock_bgcolor};color:{variables.lock_fgcolor};')

        elif background == None and not fgcolor == None:

            ## Set colors ##
            variables.lock_bgcolor = bgcolor
            variables.lock_fgcolor = fgcolor

            self.BtnUnlock.setStyleSheet(
                f'border:none;background-color: {variables.lock_bgcolor};color:{variables.lock_fgcolor};')
        elif not background == None and not fgcolor == None:
            ## Set bgcolor ##

            variables.lock_background = res.get(background)
            self.BtnUnlock.setStyleSheet(
                f'border:none;background-image: url({variables.lock_background});color: {variables.lock_fgcolor};')
        else:
            self.BtnUnlock.setStyleSheet(
                f'background-color:{variables.lock_bgcolor};color: {variables.lock_fgcolor};')

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

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo == None:
            self.lock.setWindowIcon(QIcon(res.get(applogo)))

        ## Set size ##
        width = getdata('width')
        height = getdata('height')
        autosize = getdata('autosize')

        if not width == None and not autosize == 'Yes':
            variables.width = int(width)

        if not height == None and not autosize == 'Yes':
            variables.height = int(height)

        self.lock.resize(int(variables.width), int(variables.height))
        self.BtnUnlock.resize(int(variables.width), int(variables.height))

        # lbl Clock #
        self.lblClock = QLabel()
        self.lock.layout().addWidget(self.lblClock)

        # shadow #
        if clock_shadow=='Yes':
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow  = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.lblClock.setGraphicsEffect(shadow)

        # font size clock #

        f.setPointSize(int(clock_size))

        self.lblClock.setFont(f)

        # color clock #
        self.lblClock.setStyleSheet('color:'+clock_color)

        # set lbl Clock location #
        if clock_location == 'top':
            self.lblClock.setGeometry(int(self.BtnUnlock.width() / 2) - int(self.lblClock.width() / 2), 0,
                                          self.lblClock.width(), self.lblClock.height())
        elif clock_location == 'center':
            self.lblClock.setGeometry(int(self.BtnUnlock.width() / 2) - int(self.lblClock.width() / 2),
                                          int(self.lock.height() / 2) - int(self.lblClock.height() / 2),
                                          self.lblClock.width(),
                                          self.lblClock.height())

        elif clock_location == 'left':
            self.lblClock.setGeometry(0,
                                          int(self.lock.height() / 2) - int(self.lblClock.height() / 2),
                                          self.lblClock.width(),
                                          self.lblClock.height())

        elif clock_location == 'right':
            self.lblClock.setGeometry(self.BtnUnlock.width()-self.lblClock.width(),
                                          int(self.lock.height() / 2) - int(self.lblClock.height() / 2),
                                          self.lblClock.width(),
                                          self.lblClock.height())
        elif clock_location == 'bottom':
            self.lblClock.setGeometry(int(self.BtnUnlock.width() / 2) - int(self.lblClock.width() / 2),
                                          self.lock.height() -self.lblClock.height(),
                                          self.lblClock.width(),
                                          self.lblClock.height())

        elif clock_location == 'top/left':
            self.lblClock.setGeometry(0,
                                          0,
                                          self.lblClock.width(),
                                          self.lblClock.height())

        elif clock_location == 'top/right':
            self.lblClock.setGeometry(self.BtnUnlock.width()-self.lblClock.width(),
                                          0,
                                          self.lblClock.width(),
                                          self.lblClock.height())

        elif clock_location == 'bottom/left':
            self.lblClock.setGeometry(0,
                                      self.BtnUnlock.height()-self.lblClock.height(),
                                      self.lblClock.width(),
                                      self.lblClock.height())

        elif clock_location == 'bottom/right':
            self.lblClock.setGeometry(self.BtnUnlock.width() - self.lblClock.width(),
                                      self.BtnUnlock.height()-self.lblClock.height(),
                                      self.lblClock.width(),
                                      self.lblClock.height())

        self.BtnUnlock.clicked.connect(self.unlock_act)
        self.setCentralWidget(self.lock)

    def accoutsetting (self):
        self.RunApp('usermanager',None)
        files.write('/proc/info/id','desktop')

    def Loop(self):
        self.update()
        QTimer.singleShot(300,self.update)

    def __init__(self,ports,username,password):
        super(Desktop, self).__init__()

        ## Set port name ##
        self.setObjectName('Desktop')

        ## ports ##
        self.Backend = ports[0]

        ## username ##
        self.username = username.lower()
        self.password = password

        font = getdata('font')
        if not self.username == 'guest':
            value = control.read_record('font', '/etc/users/' + self.username)
            if not value == None: font = value
        if font == None: font = variables.font

        f.setFamily(font)
        self.setFont(f)

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
                if not files.isdir("/root/" + i):
                    files.mkdir("/root/" + i)
        else:
            if not files.isdir("/desk/" + self.username): files.mkdir("/desk/" + self.username)
            for i in deskdirs:
                if not files.isdir("/desk/" + self.username + "/" + i):
                    files.mkdir("/desk/" + self.username + "/" + i)

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
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        ## Menu ##

            # hide the menu #
        submenu_hide = getdata('submenu.hide')
        if not self.username == 'guest':
            value = control.read_record('submenu.hide', '/etc/users/' + self.username)
            if not value == None: submenu_hide = value
        if submenu_hide == None: submenu_hide = variables.submenu_hide

        submenu_bgcolor = getdata('submenu.bgcolor')
        if not self.username == 'guest':
            value = control.read_record('submenu.bgcolor', '/etc/users/' + self.username)
            if not value == None: submenu_bgcolor = value
        if submenu_bgcolor == None: submenu_bgcolor = variables.submenu_bgcolor

        submenu_fgcolor = getdata('submenu.fgcolor')
        if not self.username == 'guest':
            value = control.read_record('submenu.fgcolor', '/etc/users/' + self.username)
            if not value == None: submenu_fgcolor = value
        if submenu_fgcolor == None: submenu_fgcolor = variables.submenu_fgcolor

        submenu_direction = getdata('submenu.direction')
        if not self.username == 'guest':
            value = control.read_record('submenu.direction', '/etc/users/' + self.username)
            if not value == None: submenu_direction = value
        if submenu_direction == None: submenu_direction = variables.submenu_direction

        submenu_fontsize = getdata('submenu.fontsize')
        if not self.username == 'guest':
            value = control.read_record('submenu.fontsize', '/etc/users/' + self.username)
            if not value == None: submenu_fontsize = value
        if submenu_fontsize == None: submenu_fontsize = variables.submenu_fontsize
        ## menu section

        self.submenu =QMenuBar() # Sub menu
        self.Backend.setMenuBar(self.submenu)

        #self.submenu.setStyleSheet(f'background-color:none;color:{submenu_bgcolor};')

        if submenu_direction=='ltr': self.submenu.setLayoutDirection(Qt.LeftToRight)
        elif submenu_direction=='rtl': self.submenu.setLayoutDirection(Qt.RightToLeft)

        # hide #
        if submenu_hide=='Yes':
            self.submenu.hide()

        f.setPointSize(int(submenu_fontsize))

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
        if self.locale==None: self.locale = variables.locale

        # menu action
        for i in cate:
            if i.endswith('.cat'):
                find = '/usr/share/categories/' + i

                catname = control.read_record('name[' + self.locale + "]", find)
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
                        appname = control.read_record('name[' + self.locale + "]", find)
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
            first_name = control.read_record('first_name','/etc/users/'+username)
            last_name = control.read_record('last_name','/etc/users/'+username)

            if first_name==None and last_name==None:
                fullname = username
            elif not first_name==None and last_name==None:
                fullname = first_name
            elif not first_name==None and not last_name==None:
                fullname = first_name +" "+last_name
            else:
                fullname = last_name

        self.usermenu.setTitle(fullname)
        self.usermenu.setFont(f)

        # Power menu #
        self.powermenu = QMenu()
        self.powermenu.setFont(f)
        self.etcmenu.addMenu(self.powermenu)
        self.powermenu.setTitle(res.get('@string/powermenu'))
        self.powermenu.setFont(f)

        # all actions in menus #

        self.accoutsettings = QAction(res.get('@string/accountsettings'))
        self.accoutsettings.triggered.connect (self.accoutsetting)
        self.accoutsettings.setFont(f)
        self.accoutsettings.setVisible(False)
        self.usermenu.addAction(self.accoutsettings)

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

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, variables.width, variables.height)
        self.layout().addWidget(self.backgroundButton)

        bgcolor = getdata('desktop.bgcolor')
        background = getdata('desktop.background')
        fgcolor = getdata('desktop.fgcolor')


        ## Check background or bgcolor in users ##
        if not self.username=='guest':
            value = control.read_record('desktop.bgcolor','/etc/users/'+self.username)
            if not value==None: bgcolor = value

        if not self.username=='guest':
            value = control.read_record('desktop.background','/etc/users/'+self.username)
            if not value==None: background = value

        if not self.username=='guest':
            value = control.read_record('desktop.fgcolor','/etc/users/'+self.username)
            if not value==None: fgcolor = value

            ## Set bgcolor and background ##

        if background == None and bgcolor == None and not fgcolor == None:
            variables.desktop_fgcolor = fgcolor
            ## Set colors ##
            self.setStyleSheet(f'color: {variables.desktop_fgcolor};')
            self.backgroundButton.setStyleSheet(
                f'border:none;background-color: {variables.desktop_bgcolor};')

        elif background == None and not fgcolor == None:

            ## Set colors ##
            variables.desktop_bgcolor = bgcolor
            variables.desktop_fgcolor = fgcolor

            self.setStyleSheet(f'color: {variables.desktop_fgcolor};')

            self.backgroundButton.setStyleSheet(
                f'border:none;background-color: {variables.desktop_bgcolor};')

        elif not background == None and not fgcolor == None:
            ## Set bgcolor ##

            variables.desktop_background = res.get(background)
            self.setStyleSheet(f'color: {variables.desktop_fgcolor};')
            self.backgroundButton.setStyleSheet(
                f'border:none;background-image: url({variables.desktop_background});')
        else:
            self.setStyleSheet(
                f'background-color:{variables.desktop_bgcolor};color: {variables.desktop_fgcolor};')

        ## Set size ##
        width = getdata('width')
        height = getdata('height')
        autosize =getdata('autosize')

        if not width == None  and not autosize=='Yes':
            variables.width = int(width)

        if not height == None and not autosize=='Yes':
            variables.height = int(height)

        self.resize(int(variables.width), int(variables.height))

        ## Startup Applications ##
        self.StartupApplication()
        ## Set sides ##
        ## Set sides ##
        sides = getdata('sides')

        if sides == 'Yes':
            variables.sides = True
        else:
            variables.sides = False
        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Taskbar ##
        self.taskbar = TaskBar ([Backend,self])

        ## Show ##
        ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

        self.Loop()
