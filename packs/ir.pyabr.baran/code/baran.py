'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, PyPI
    * License:          GNU General Publice License v3.0

    - Official Website

    * Persian Page:     https://pyabr.ir
    * English Page:     https://en.pyabr.ir
'''
import os,multiprocessing
import subprocess
import sys, hashlib,shutil
from typing import Text

from pyabr.core import *
from pyabr.quick import *

res = Res()
control = Control()
files = Files()
app = App()
process = Process()

def ql (name):
    return control.read_record (name,'/etc/default/quicklogo')

application = QGuiApplication(sys.argv)
application.setWindowIcon(QIcon(res.get(ql('pyabr'))))


shutil.copyfile('/stor/etc/default/openbox.xml','/root/.config/openbox/rc.xml')
subprocess.call(['sudo','openbox','--reconfigure'])

keylessx = ''
for i in files.list ('/usr/share/locales'):
    if i.endswith('.locale'):
        ic = control.read_record ('keyless',f'/usr/share/locales/{i}')
        if keylessx=='':
            keylessx+=ic
        else:
            keylessx+=f',{ic}'

subprocess.call(f'setxkbmap -layout "{keylessx}" -option "grp:alt_shift_toggle"',shell=True)

if files.isfile ('/proc/info/randr'): subprocess.call(['xrandr','-s',files.readall('/proc/info/randr')])

files.write('/proc/info/id','baran')

## Get data ##
def getdata (name):
    return control.read_record (name,'/etc/gui')

class Backend (MainApp):
    def runSplash (self):
        self.splash = Splash([self])

    def runLogin (self):
        self.login = Login([self])

    def runEnter (self):
        self.enter = Enter([self,control.read_record("username","/etc/gui")])
        control.write_record('username','guest','/etc/gui')

    def runDesktop (self):
        self.desktop = Desktop([self,control.read_record("username","/etc/gui"),control.read_record("password","/etc/gui")])
        control.write_record('username', 'guest', '/etc/gui')
        control.write_record('password', '*', '/etc/gui')

    def runUnlock (self):
        control.write_record('username', 'guest', '/etc/gui')

    def __init__(self):
        super(Backend,self).__init__()

        
        self.load (res.get('@layout/backend'))
        self.setProperty ('height',int(getdata("height")))
        self.setProperty ('width',int(getdata("width")))
        self.setProperty ('title','Pyabr OS')
        self.setProperty ('visibility',getdata("visibility"))

        # Actions

        params = getdata('params')

        control.write_record('params', 'gui', '/etc/gui')

        self.close()

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
            QTimer.singleShot(1000, self.runSplash)  ## Run splash after 1s

class Splash (MainApp):
    def runLogin (self):
        self.close()
        self.login = Login([self.Backend])

    def __init__(self,ports):
        super(Splash, self).__init__()

        
        self.Backend = ports[0]
        self.load(res.get('@layout/splash'))
        self.logo = self.findChild ('logo')
        self.logo.setProperty('source',res.qmlget(ql('pyabr')))
        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('title', 'Pyabr OS')
        self.setProperty('visibility', getdata("visibility"))

        QTimer.singleShot(3000, self.runLogin)  ## Run login

class Login (MainApp):
    def shutdown_ (self):
        subprocess.call(['poweroff'])

    def restart_ (self):
        subprocess.call(['reboot'])

    def sleep_ (self):
        self.sleep = Sleep()

    def lang_(self):
        pass

    def clean(self):
        self._username.setProperty('enabled',True)
        self._username.setProperty('placeholderText',res.get('@string/username_placeholder'))

    def next_(self):
        if self._username.property("text")=='':
            pass
        elif self._username.property("text")=='guest' and files.readall('/etc/guest')=='enable':
            self.close()
            self.desktop = Desktop([self.Backend, self._username.property("text"),'*'])
        elif files.isfile(f'/etc/users/{self._username.property("text")}'):
            self.close()
            self.enter = Enter([self.Backend,self._username.property("text")])
        else:
            self.usernamet = self._username.property('text')
            self._username.setProperty('text','')
            self._username.setProperty("placeholderText",res.get('@string/user_not_found').replace('{0}',self.usernamet))
            self._username.setProperty('enabled',False)
            QTimer.singleShot(3000,self.clean)

    NameRole = QtCore.Qt.ItemDataRole.UserRole + 1000
    LabelRole = QtCore.Qt.ItemDataRole.UserRole + 1001
    LogoRole = QtCore.Qt.ItemDataRole.UserRole + 1002
    ShortcutRole = QtCore.Qt.ItemDataRole.UserRole + 1003

    def create_model(self):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo',self.ShortcutRole:b'shortcut'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/locales'):
            if control.read_record('keyless.enable',f'/usr/share/locales/{name}')=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record('name', f'/usr/share/locales/{name}')
                it.setData(namex, self.LabelRole)
                it.setData(control.read_record ('keyless.shortcut',f'/usr/share/locales/{name}'),self.ShortcutRole)
                it.setData('../../../'+res.get(control.read_record('logo', f'/usr/share/locales/{name}')), self.LogoRole)
                model.appendRow(it)
        return model

    def loop (self):
        if not self._keyless.property('text')=='':
            subprocess.call(control.read_record('keyless',f'/usr/share/locales/{self._keyless.property("text")}'),shell=True)

        self._keyless.setProperty('text','')
        QTimer.singleShot(10,self.loop)

    def __init__(self,ports):
        super(Login, self).__init__()

        

        self.Backend = ports[0]

        self.langModel = self.create_model()
        self.rootContext().setContextProperty("Lang", self.langModel)

        self.load(res.get('@layout/login'))

        if not self.rootObjects():
            sys.exit(-1)

        self.profile = self.findChild('profile')
        self.profile.setProperty('source',res.qmlget(ql('users')))

        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title', 'Pyabr OS')

        # Connects

        self._submenu = self.findChild( 'submenu')
        self._submenu.setProperty('title',res.get('@string/etcetra'))
        self._shutdown = self.findChild('shutdown')
        self._shutdown.setProperty('text',res.get('@string/escape'))
        self._shutdown.triggered.connect (self.shutdown_)
        self._restart = self.findChild( 'restart')
        self._restart.setProperty('text', res.get('@string/restart'))
        self._restart.triggered.connect(self.restart_)
        self._sleep = self.findChild( 'sleep')
        self._sleep.setProperty('text', res.get('@string/sleep'))
        self._sleep.triggered.connect(self.sleep_)
        self._next = self.findChild( 'next')
        self._username = self.findChild( 'username')
        self._username.setProperty("placeholderText",res.get('@string/username_placeholder'))
        self._next.clicked.connect(self.next_)
        self._next.setProperty('text',res.get('@string/next'))
        self._lang = self.findChild( 'lang')
        self._lang.setProperty('title', res.get('@string/keyboard_languages'))
        self._exit = self.findChild( 'exit')
        self._exit.setProperty('title', res.get('@string/power_options'))
        self._background = self.findChild( 'background')

        if getdata("login.background").startswith('@background/'):
            self._background.setProperty('source', res.qmlget(getdata("login.background")))
        else:
            self._background.setProperty('source', files.input_qml(getdata("login.background")))

        self._virtualkeyboard = self.findChild('virtualkeyboard')
        self._virtualkeyboard.setProperty('text',res.get('@string/virtualkeyboard'))
        self._keyless = self.findChild('keyless')

        self.loop()


class Sleep (MainApp):
    def __init__(self):
        super(Sleep, self).__init__()

        

        self.load(res.get('@layout/sleep'))
        if not self.rootObjects():
            sys.exit(-1)

        # Get data

        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title', 'Pyabr OS')


        # Connects
        self._wakeup = self.findChild( 'wakeup')
        self._wakeup.clicked.connect (self.close)

class Enter (MainApp):
    def shutdown_ (self):
        subprocess.call(['poweroff'])

    def restart_ (self):
        subprocess.call(['reboot'])

    def sleep_ (self):
        self.sleep = Sleep()

    def lang_(self):
        pass

    def clean(self):
        self._password.setProperty('enabled',True)
        self._password.setProperty('placeholderText', res.get('@string/password_placeholder').replace('{0}',self.username))

    def login_(self):

        if control.read_record('code',f'/etc/users/{self.username}')==hashlib.sha3_512(self._password.property("text").encode()).hexdigest():
            self.close()
            self.desktop = Desktop([self.Backend,self.username,self._password.property("text")])
        else:
            self._password.setProperty('text','')
            self._password.setProperty('placeholderText', res.get('@string/wrong_password'))
            self._password.setProperty('enabled',False)
            QTimer.singleShot(3000,self.clean)

    def loop (self):
        if not self._keyless.property('text')=='':
            subprocess.call(control.read_record('keyless',f'/usr/share/locales/{self._keyless.property("text")}'),shell=True)

        self._keyless.setProperty('text','')
        QTimer.singleShot(10,self.loop)

    NameRole = QtCore.Qt.ItemDataRole.UserRole + 1000
    LabelRole = QtCore.Qt.ItemDataRole.UserRole + 1001
    LogoRole = QtCore.Qt.ItemDataRole.UserRole + 1002

    def create_model(self):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/locales'):
            if control.read_record('keyless.enable',f'/usr/share/locales/{name}')=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record('name', f'/usr/share/locales/{name}')
                it.setData(namex, self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo', f'/usr/share/locales/{name}')), self.LogoRole)
                model.appendRow(it)
        return model

    def logout_(self):

        self.close()

        System ("kma")

        # Logout
        files.create ('/proc/info/pause')
        subprocess.call([sys.executable,'vmabr.pyc','gui-login'])

    def getdata(self, name):
        try:
            x = control.read_record(name, f'/etc/users/{self.username}')
            if x == '' or x == None:
                x = getdata(name)
        except:
            x = getdata(name)

        return x

    def __init__(self, ports):
        super(Enter, self).__init__()

        

        self.Backend = ports[0]
        self.username = ports[1]

        self.langModel = self.create_model()
        self.rootContext().setContextProperty("Lang", self.langModel)

        self.load(res.get('@layout/enter'))
        if not self.rootObjects():
            sys.exit(-1)

        # Get data

        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title', 'Pyabr OS')

        # Connects

        self._submenu = self.findChild( 'submenu')
        self._submenu.setProperty('title',res.get('@string/etcetra'))
        self._shutdown = self.findChild( 'shutdown')
        self._shutdown.setProperty('text',res.get('@string/escape'))
        self._shutdown.triggered.connect(self.shutdown_)
        self._restart = self.findChild( 'restart')
        self._restart.setProperty('text', res.get('@string/restart'))
        self._restart.triggered.connect(self.restart_)
        self._sleep = self.findChild( 'sleep')
        self._sleep.setProperty('text', res.get('@string/sleep'))
        self._sleep.triggered.connect(self.sleep_)
        self._login = self.findChild( 'login')
        self._password = self.findChild( 'password')
        self._password.setProperty('placeholderText',res.get('@string/password_placeholder').replace('{0}',self.username))
        self._login.clicked.connect(self.login_)
        self._login.setProperty('text',res.get('@string/login'))
        self._lang = self.findChild( 'lang')
        self._lang.setProperty('title', res.get('@string/keyboard_languages'))
        self._logout = self.findChild( 'logout')
        self._logout.setProperty('text',res.get('@string/logout'))
        self._logout.triggered.connect(self.logout_)
        self._exit = self.findChild( 'exit')
        self._exit.setProperty('title', res.get('@string/power_options'))
        self._account = self.findChild('account')
        if self.getdata("fullname")=='':
            self._account.setProperty('title',self.username)
        else:   
            self._account.setProperty('title',self.getdata("fullname"))
        self._background = self.findChild( 'background')

        if self.getdata("enter.background").startswith('@background/'):        
            self._background.setProperty('source', res.qmlget(self.getdata("enter.background")))
        else:
            self._background.setProperty('source', files.input_qml(self.getdata("enter.background")))
        self._profile = self.findChild('profile')

        if self.getdata("profile").startswith('@icon/'):
            self._profile.setProperty('source',res.qmlget(self.getdata("profile")))
        else:
            self._profile.setProperty('source',files.input_qml(self.getdata("profile")))

        self._virtualkeyboard = self.findChild('virtualkeyboard')
        self._virtualkeyboard.setProperty('text',res.get('@string/virtualkeyboard'))
        self._keyless = self.findChild('keyless')

        self.loop()


class Unlock (MainApp):
    def clean(self):
        self._password.setProperty('enabled',True)
        self._password.setProperty('placeholderText',res.get('@string/password_placeholder').replace('{0}',self.Env.username))

    def unlock_(self):

        if control.read_record('code',f'/etc/users/{self.Env.username}')==hashlib.sha3_512(self._password.property("text").encode()).hexdigest():
            self.close()
        else:
            self._password.setProperty('text','')
            self._password.setProperty("placeholderText",res.get('@string/wrong_password'))
            self._password.setProperty('enabled',False)
            QTimer.singleShot(3000,self.clean)

    def getdata(self, name):
        x = control.read_record(name, f'/etc/users/{self.Env.username}')
        if x == '' or x == None:
            x = getdata(name)

        return x

    def loop (self):
        if not self._keyless.property('text')=='':
            subprocess.call(control.read_record('keyless',f'/usr/share/locales/{self._keyless.property("text")}'),shell=True)

        self._keyless.setProperty('text','')
        QTimer.singleShot(10,self.loop)

    NameRole = QtCore.Qt.ItemDataRole.UserRole + 1000
    LabelRole = QtCore.Qt.ItemDataRole.UserRole + 1001
    LogoRole = QtCore.Qt.ItemDataRole.UserRole + 1002

    def create_model(self):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/locales'):
            if control.read_record('keyless.enable',f'/usr/share/locales/{name}')=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record('name', f'/usr/share/locales/{name}')
                it.setData(namex, self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo', f'/usr/share/locales/{name}')), self.LogoRole)
                model.appendRow(it)
        return model

    def __init__(self, ports):
        super(Unlock, self).__init__()

        

        self.Backend = ports[0]
        self.Env = ports[1]

        self.langModel = self.create_model()
        self.rootContext().setContextProperty("Lang", self.langModel)

        self.load(res.get('@layout/unlock'))
        if not self.rootObjects():
            sys.exit(-1)

        # Get data

        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title', 'Pyabr OS')

        # Connects
        self._password = self.findChild( 'password')
        self._password.setProperty('placeholderText',res.get('@string/password_placeholder').replace('{0}',self.Env.username))
        self._unlock = self.findChild('login')
        self._unlock.setProperty('text',res.get('@string/unlock'))
        self._unlock.clicked.connect(self.unlock_)


        self._background = self.findChild( 'background')

        if  self.getdata("unlock.background").startswith('@background/'):     
            self._background.setProperty('source', res.qmlget(self.getdata("unlock.background")))
        else:
            self._background.setProperty('source', files.input_qml(self.getdata("unlock.background")))
        self._profile = self.findChild( 'profile')

        if self.getdata("profile").startswith('@icon/'):
            self._profile.setProperty('source', res.qmlget(self.getdata("profile")))
        else:
            self._profile.setProperty('source', files.input_qml(self.getdata("profile")))
        self._submenu = self.findChild('submenu')
        self._submenu.setProperty('title',res.get('@string/etcetra'))
        self._virtualkeyboard = self.findChild( 'virtualkeyboard')
        self._virtualkeyboard.setProperty('text', res.get('@string/virtualkeyboard'))
        self._lang = self.findChild( 'lang')
        self._lang.setProperty('title', res.get('@string/keyboard_languages'))
        self._keyless = self.findChild ('keyless')

        self.loop()

class Lock (MainApp):
    def unlock_(self):
        self.close()
        if not self.Env.username=='guest':
            self.unlock = Unlock([self.Backend,self.Env])

    def getdata (self,name):
        x = control.read_record(name,f'/etc/users/{self.Env.username}')
        if x=='' or x==None:
            x = getdata(name)

        return x

    def showTime (self):
        current_time = QTime.currentTime()
  
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        self.txtClock.setProperty('text',res.num(label_time))

    def __init__(self, ports):
        super(Lock, self).__init__()

        

        self.Backend = ports[0]
        self.Env = ports[1]

        self.load(res.get('@layout/lock'))
        if not self.rootObjects():
            sys.exit(-1)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        # Get data

        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title', 'Pyabr OS')

        # Connects
        self._unlock = self.findChild('unlock')
        self._unlock.clicked.connect (self.unlock_)


        self._background = self.findChild( 'background')
        self.txtClock = self.findChild('txtClock')

        if self.getdata("lock.background").startswith('@background/'):
            self._background.setProperty('source', res.qmlget(self.getdata("lock.background")))
        else:
            self._background.setProperty('source', files.input_qml(self.getdata("lock.background")))        

class Desktop (MainApp):
    AUDIOS = ''
    DESKTOP = ''
    DOCUMENTS = ''
    DOWNLOADS = ''
    PICTURES = ''
    PROJECTS = ''
    SAMPLES = ''
    VIDEOS = ''
    
    def shutdown_ (self):
        subprocess.call(['poweroff'])

    def restart_ (self):
        subprocess.call(['reboot'])

    def sleep_ (self):
        self.sleep = Sleep()

    def logout_(self):
        self.close()
        
        System ("kma")

        # Logout
        files.create ('/proc/info/pause')
        subprocess.call([sys.executable,'vmabr.pyc','gui-login'])

    def lock_(self):
        self.lock = Lock([self.Backend,self])

    NameRole = QtCore.Qt.ItemDataRole.UserRole + 1000
    LabelRole = QtCore.Qt.ItemDataRole.UserRole + 1001
    LogoRole = QtCore.Qt.ItemDataRole.UserRole + 1002
    pins = 0

    def create_model(self,dir_path,category):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name",self.LabelRole: b'label',self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list(dir_path):
            categoryx = control.read_record('category',f'{dir_path}/{name}')
            hidden = control.read_record('hidden',f'{dir_path}/{name}')
            if categoryx==category and not hidden=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record(f'name[{getdata("locale")}]',f'{dir_path}/{name}')
                if namex=='' or namex==None:
                    namex = control.read_record(f'name[en]', f'{dir_path}/{name}')
                it.setData(namex,self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo',f'{dir_path}/{name}')),self.LogoRole)
                model.appendRow(it)
        return model

    def check_cat (self,dir_path,category):
        i = 0
        for name in files.list(dir_path):
            categoryx = control.read_record('category',f'{dir_path}/{name}')
            hidden = control.read_record('hidden',f'{dir_path}/{name}')
            if categoryx==category and not hidden=='Yes':
                i+=1
        return i

    def create_model2(self):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/locales'):
            if control.read_record('keyless.enable',f'/usr/share/locales/{name}')=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record('name', f'/usr/share/locales/{name}')
                it.setData(namex, self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo', f'/usr/share/locales/{name}')), self.LogoRole)
                model.appendRow(it)
        return model


    def create_model3(self):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/applications'):
            if res.etc(name.replace('.desk',''),'pin')=='Yes':
                self.pins+=1
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record(f'name[{getdata("locale")}]', f'/usr/share/applications/{name}')
                if namex == '' or namex == None:
                    namex = control.read_record(f'name[en]', f'/usr/share/applications/{name}')
                it.setData(namex, self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo', f'/usr/share/applications/{name}')), self.LogoRole)
                model.appendRow(it)
        return model

    def create_model4(self,dir_path):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name",self.LabelRole: b'label',self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list(dir_path):
            hidden = control.read_record('hidden',f'{dir_path}/{name}')
            if not hidden=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record(f'name[{getdata("locale")}]',f'{dir_path}/{name}')
                if namex=='' or namex==None:
                    namex = control.read_record(f'name[en]', f'{dir_path}/{name}')
                it.setData(namex,self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo',f'{dir_path}/{name}')),self.LogoRole)
                model.appendRow(it)
        return model

    def create_model5(self):
        #model = QtGui.QStandardItemModel()
        #roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo'}
        #model.setItemRoleNames(roles)

        lista = subprocess.check_output ("wmctrl -l | awk '{print $4}'",shell=True).decode ('utf-8').split('\n')
        lista.pop(0)

        if '' in lista:
            lista.remove('')

        
        listb = files.list ('/proc/id')
        #return model

    def getdata (self,name):
        try:
            x = control.read_record(name,f'/etc/users/{self.username}')
            if x=='' or x==None:
                x = getdata(name)
        except:
            x = res.get('@string/guest')

        return x

    def getnamex (self,database):
        try:
            x = control.read_record(f'name[{self.getdata("locale")}]', database)
            if x=='' or x==None:
                x = control.read_record(f'name[en]', database)
        except:
            x = control.read_record(f'name[en]', database)
        return x

    def signal (self):
        if not files.isfile('/proc/info/sig'):
            files.create('/proc/info/sig')

        if files.readall('/proc/info/sig')=='apps':
            files.create('/proc/info/sig')
            self.modelAllApplications = self.create_model4('/usr/share/applications')
            self.rootContext().setContextProperty('EntryAppApplications', self.modelAllApplications)

        if files.readall('/proc/info/sig')=='sleep':
            files.create('/proc/info/sig')
            self.sleep_()

        elif files.readall('/proc/info/sig')=='shutdown':
            files.create('/proc/info/sig')
            self.shutdown_()

        elif files.readall('/proc/info/sig') == 'restart':
            files.create('/proc/info/sig')
            self.restart_()

        elif files.readall('/proc/info/sig')=='lock':
            files.create('/proc/info/sig')
            self.lock_()

        elif files.readall('/proc/info/sig')=='logout':
            files.create('/proc/info/sig')
            self.logout_()

        elif files.readall('/proc/info/sig')=='username':
            if self.getdata("fullname")=='':
                self._account.setProperty('title',self.username)
            else:   
                self._account.setProperty('title',self.getdata("fullname"))

        elif files.readall('/proc/info/sig')=='background':
            try:
                if self.getdata('desktop.background').startswith('@background/'):
                    self._background.setProperty('source', res.qmlget(self.getdata("desktop.background")))
                else:
                    self._background.setProperty('source', files.input_qml(self.getdata("desktop.background")))
            except:
                pass

        elif files.readall('/proc/info/sig')=='dock':
            if self.getdata  ('dock')=='bottom':
                self._toolbar.setProperty ('visible',True)
                self._toolbar2.setProperty('visible',False)
                self._toolbar3.setProperty('visible',False)
                self._toolbar4.setProperty('visible',False)
                self._toolbar5.setProperty('visible',False)
                self._toolbar6.setProperty('visible',False)
                self._toolbar7.setProperty('visible',False)
                self._toolbar8.setProperty('visible',False)
                self._btnMenu = self.findChild ('btnMenu')
                self._btnMenu.clicked.connect (self.menuApps_)
                self._menuApps = self.findChild ('menuApps')
                self.menuApps_anim = self.findChild('menuApps_anim')

            elif self.getdata ('dock')=='top':
                self._toolbar.setProperty ('visible',False)
                self._toolbar2.setProperty('visible',True)
                self._toolbar3.setProperty('visible',False)
                self._toolbar4.setProperty('visible',False)
                self._toolbar5.setProperty('visible',False)
                self._toolbar6.setProperty('visible',False)
                self._toolbar7.setProperty('visible',False)
                self._toolbar8.setProperty('visible',False)
                self._btnMenu = self.findChild ('btnMenu2')
                self._btnMenu.clicked.connect (self.menuApps_)
                self._menuApps = self.findChild ('menuApps2')
                self.menuApps_anim = self.findChild('menuApps2_anim')

            elif self.getdata  ('dock')=='left':
                self._toolbar.setProperty ('visible',False)
                self._toolbar2.setProperty('visible',False)
                self._toolbar3.setProperty('visible',True)
                self._toolbar4.setProperty('visible',False)
                self._toolbar5.setProperty('visible',False)
                self._toolbar6.setProperty('visible',False)
                self._toolbar7.setProperty('visible',False)
                self._toolbar8.setProperty('visible',False)
                self._btnMenu = self.findChild ('btnMenu3')
                self._btnMenu.clicked.connect (self.menuApps_)
                self._menuApps = self.findChild ('menuApps3')
                self.menuApps_anim = self.findChild('menuApps3_anim')

            elif self.getdata  ('dock')=='right':
                self._toolbar.setProperty ('visible',False)
                self._toolbar2.setProperty('visible',False)
                self._toolbar3.setProperty('visible',False)
                self._toolbar4.setProperty('visible',True)
                self._toolbar5.setProperty('visible',False)
                self._toolbar6.setProperty('visible',False)
                self._toolbar7.setProperty('visible',False)
                self._toolbar8.setProperty('visible',False)
                self._btnMenu = self.findChild ('btnMenu4')
                self._btnMenu.clicked.connect (self.menuApps_)
                self._menuApps = self.findChild ('menuApps4')
                self.menuApps_anim = self.findChild('menuApps4_anim')

            elif self.getdata  ('dock')=='windows' or self.getdata  ('dock')=='windows-bottom':
                self._toolbar.setProperty ('visible',False)
                self._toolbar2.setProperty('visible',False)
                self._toolbar3.setProperty('visible',False)
                self._toolbar4.setProperty('visible',False)
                self._toolbar5.setProperty('visible',True)
                self._toolbar6.setProperty('visible',False)
                self._toolbar7.setProperty('visible',False)
                self._toolbar8.setProperty('visible',False)
                self._btnMenu = self.findChild ('btnMenu5')
                self._btnMenu.clicked.connect (self.menuApps_)
                self._menuApps = self.findChild ('menuApps')
                self.menuApps_anim = self.findChild('menuApps_anim')

            elif self.getdata ('dock')=='windows-top':
                self._toolbar.setProperty ('visible',False)
                self._toolbar2.setProperty('visible',False)
                self._toolbar3.setProperty('visible',False)
                self._toolbar4.setProperty('visible',False)
                self._toolbar5.setProperty('visible',False)
                self._toolbar6.setProperty('visible',True)
                self._toolbar7.setProperty('visible',False)
                self._toolbar8.setProperty('visible',False)
                self._btnMenu = self.findChild ('btnMenu6')
                self._btnMenu.clicked.connect (self.menuApps_)
                self._menuApps = self.findChild ('menuApps2')
                self.menuApps_anim = self.findChild('menuApps2_anim')

            elif self.getdata ('dock')=='windows-left':
                self._toolbar.setProperty ('visible',False)
                self._toolbar2.setProperty('visible',False)
                self._toolbar3.setProperty('visible',False)
                self._toolbar4.setProperty('visible',False)
                self._toolbar5.setProperty('visible',False)
                self._toolbar6.setProperty('visible',False)
                self._toolbar7.setProperty('visible',True)
                self._toolbar8.setProperty('visible',False)
                self._btnMenu = self.findChild ('btnMenu7')
                self._btnMenu.clicked.connect (self.menuApps_)
                self._menuApps = self.findChild ('menuApps3')
                self.menuApps_anim = self.findChild('menuApps3_anim')

            elif self.getdata ('dock')=='windows-right':
                self._toolbar.setProperty ('visible',False)
                self._toolbar2.setProperty('visible',False)
                self._toolbar3.setProperty('visible',False)
                self._toolbar4.setProperty('visible',False)
                self._toolbar5.setProperty('visible',False)
                self._toolbar6.setProperty('visible',False)
                self._toolbar7.setProperty('visible',False)
                self._toolbar8.setProperty('visible',True)
                self._btnMenu = self.findChild ('btnMenu8')
                self._btnMenu.clicked.connect (self.menuApps_)
                self._menuApps = self.findChild ('menuApps4')
                self.menuApps_anim = self.findChild('menuApps4_anim')

    def loop (self):
        # Applications starts in background
        if not self._background_app.property('text')=='':
            self._menuApps.setProperty('visible', False)
            self.menuClicked = False
            
            if files.isfile ('/proc/info/ext'): files.remove ('/proc/info/ext')

            System ('rma')

            app.start(self._background_app.property('text').replace('.desk',''),'')

        # Check signals #
        if not files.isfile('/proc/info/pause'):
            files.write('/proc/info/su',self.username)

        self.signal()

        if not self._keyless.property('text')=='':
            subprocess.call(control.read_record('keyless',f'/usr/share/locales/{self._keyless.property("text")}'),shell=True)

        self._keyless.setProperty('text','')

        self._background_app.setProperty('text','')

        # scrot

        try:
            subprocess.call(f'mv /root/*scrot* /stor/{self.PICTURES}',shell=True)
        except:
            pass

        self.addFileModel('/root/Desktop')

        QTimer.singleShot(200,self.loop)

    def startup (self):
        # Startup applications
        try:
            lists = control.read_list('/etc/suapp')
            for i in lists:
                app.start(i, '')
        except:
            pass

    def bashrc (self):
        try:
            if self.username=='guest':
                f = open('/etc/bash.bashrc','w')
                f.write(f'cd /stor\npython3 vmabr.pyc user guest\nexit')
                f.close()
            else:
                f = open('/etc/bash.bashrc','w')
                f.write(f'cd /stor\npython3 vmabr.pyc user {self.username} {self.password}\nexit')
                f.close()
        except:
            pass

    def pwduser (self):
        if self.username=='root':
            commands.cd (['/root'])
        else:
            commands.cd ([f'/desk/{self.username}'])

    def deskdirs (self):
        deskdirspath = files.readall('/etc/deskdirs')

        for i in files.list (deskdirspath):
            if files.isdir (f'{deskdirspath}/{i}'):
                try:
                    files.copydir (f'{deskdirspath}/{i}',f'{i}')
                except:
                    pass

        if self.username == 'root':
            self.AUDIOS = '/root/Audios'
            self.DESKTOP = '/root/Desktop'
            self.DOCUMENTS = '/root/Documents'
            self.DOWNLOADS = '/root/Downloads'
            self.PICTURES = '/root/Pictures'
            self.PROJECTS = '/root/Projects'
            self.SAMPLES = '/root/Samples'
            self.VIDEOS = '/root/Videos'
        else:
            self.AUDIOS = f'/desk/{self.username}/Audios'
            self.DESKTOP = f'/desk/{self.username}/Desktop'
            self.DOCUMENTS = f'/desk/{self.username}/Documents'
            self.DOWNLOADS = f'/desk/{self.username}/Downloads'
            self.PICTURES = f'/desk/{self.username}/Pictures'
            self.PROJECTS = f'/desk/{self.username}/Projects'
            self.SAMPLES = f'/desk/{self.username}/Samples'
            self.VIDEOS = f'/desk/{self.username}/Videos'

    def homelogo (self):
        files.write ('.logo',ql('homes'))

    menuClicked = False

    def menuApps_(self):
        self.btnMenu_anim.start()
        if self.menuClicked:
            self._menuApps.setProperty('visible',False)
            self.msaDesktop.setProperty('visible',True)
            self.menuClicked = False
        else:
            self.menuApps_anim.start()
            self._menuApps.setProperty('visible', True)
            self.msaDesktop.setProperty('visible',False)
            self.menuClicked = True

    def account_setting_(self):
        app.start ('controls','users')

    def __init__(self,ports):
        super(Desktop, self).__init__()

        self.addFileModel('/usr/share/samples/deskdirs')
        
        self.Backend = ports[0]
        self.username = ports[1]
        self.password = ports[2]
        self.modelDevelop = self.create_model('/usr/share/applications','develop')
        self.rootContext().setContextProperty("EntryDevelop", self.modelDevelop)
        self.modelGames = self.create_model('/usr/share/applications', 'games')
        self.rootContext().setContextProperty("EntryGames", self.modelGames)
        self.modelInternet = self.create_model('/usr/share/applications', 'internet')
        self.rootContext().setContextProperty("EntryInternet", self.modelInternet)
        self.modelMultimedia = self.create_model('/usr/share/applications', 'multimedia')
        self.rootContext().setContextProperty("EntryMultimedia", self.modelMultimedia)
        self.modelOthers = self.create_model('/usr/share/applications', 'others')
        self.rootContext().setContextProperty("EntryOthers", self.modelOthers)
        self.modelSystem = self.create_model('/usr/share/applications', 'system')
        self.rootContext().setContextProperty("EntrySystem", self.modelSystem)
        self.modelTools = self.create_model('/usr/share/applications', 'tools')
        self.rootContext().setContextProperty("EntryTools", self.modelTools)
        self.modelDockApplications = self.create_model3()
        self.rootContext().setContextProperty('EntryDockApplications',self.modelDockApplications)
        self.modelLang = self.create_model2()
        self.rootContext().setContextProperty("Lang", self.modelLang)

        self.create_model5()

        self.modelAllApplications = self.create_model4('/usr/share/applications')
        self.rootContext().setContextProperty('EntryAppApplications', self.modelAllApplications)

        self.load(res.get('@layout/desktop'))
        if not self.rootObjects():
            sys.exit(-1)
        self.setProperty('height',int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title','Pyabr OS')
        self._submenu = self.findChild('submenu')
        self.imgMenu = self.findChild('imgMenu')
        self.imgMenu.setProperty('source',res.qmlget(ql('pyabr')))
        self.imgMenu2 = self.findChild('imgMenu2')
        self.imgMenu2.setProperty('source',res.qmlget(ql('pyabr')))
        self.imgMenu3 = self.findChild('imgMenu3')
        self.imgMenu3.setProperty('source',res.qmlget(ql('pyabr')))
        self.imgMenu4 = self.findChild('imgMenu4')
        self.imgMenu4.setProperty('source',res.qmlget(ql('pyabr')))
        self.imgMenu5 = self.findChild('imgMenu5')
        self.imgMenu5.setProperty('source',res.qmlget(ql('pyabr')))
        self.imgMenu6 = self.findChild('imgMenu6')
        self.imgMenu6.setProperty('source',res.qmlget(ql('pyabr')))
        self.imgMenu7 = self.findChild('imgMenu7')
        self.imgMenu7.setProperty('source',res.qmlget(ql('pyabr')))
        self.imgMenu8 = self.findChild('imgMenu8')
        self.imgMenu8.setProperty('source',res.qmlget(ql('pyabr')))
        self._submenu.setProperty('title',res.get('@string/etcetra'))
        self._shutdown = self.findChild( 'shutdown')
        self._shutdown.triggered.connect(self.shutdown_)
        self._shutdown.setProperty('text',res.get('@string/escape'))
        self._restart = self.findChild( 'restart')
        self._restart.triggered.connect(self.restart_)
        self._restart.setProperty('text', res.get('@string/restart'))
        self._sleep = self.findChild( 'sleep')
        self._sleep.setProperty('text', res.get('@string/sleep'))
        self._sleep.triggered.connect(self.sleep_)
        self._logout = self.findChild( 'logout')
        self._logout.triggered.connect(self.logout_)
        self._logout.setProperty('text',res.get('@string/logout'))
        self.appc = self.findChild( 'appc')
        self.appc.setProperty('text',res.get('@string/appearance'))
        self.displayc = self.findChild( 'displayc')
        self.displayc.setProperty('text',res.get('@string/display'))
        self.rmac = self.findChild( 'rmac')
        self.rmac.setProperty('text',res.get('@string/rma'))
        self.runc = self.findChild( 'runc')
        self.runc.setProperty('text',res.get('@string/runner'))
        self._applications = self.findChild( 'applications')
        self._applications.setProperty('title',res.get('@string/applications'))
        self._lock = self.findChild('lock')
        self._lock.triggered.connect (self.lock_)
        self._lock.setProperty('text',res.get('@string/lock'))
        self._developcat = self.findChild('developcat')
        self._developcat.setProperty('title',self.getnamex("/usr/share/categories/develop.cat"))
        if self.check_cat('/usr/share/applications','develop')==0:
            self._developcat.setProperty('enabled',False)
        self._gamescat = self.findChild( 'gamescat')
        self._gamescat.setProperty('title',self.getnamex('/usr/share/categories/games.cat'))
        if self.check_cat('/usr/share/applications','games')==0:
            self._gamescat.setProperty('enabled',False)
        self._internetcat = self.findChild( 'internetcat')
        self._internetcat.setProperty('title', self.getnamex('/usr/share/categories/internet.cat'))
        if self.check_cat('/usr/share/applications','internet')==0:
            self._internetcat.setProperty('enabled',False)
        self._multimediacat = self.findChild( 'multimediacat')
        self._multimediacat.setProperty('title', self.getnamex('/usr/share/categories/multimedia.cat'))
        if self.check_cat('/usr/share/applications','multimedia')==0:
            self._multimediacat.setProperty('enabled',False)
        self._otherscat = self.findChild( 'otherscat')
        self._otherscat.setProperty('title', self.getnamex('/usr/share/categories/others.cat'))
        if self.check_cat('/usr/share/applications','others')==0:
            self._otherscat.setProperty('enabled',False)
        self._systemcat = self.findChild( 'systemcat')
        self._virtualkeyboard = self.findChild('virtualkeyboard')
        self._virtualkeyboard.setProperty('text',res.get('@string/virtualkeyboard'))
        self._systemcat.setProperty('title', self.getnamex('/usr/share/categories/system.cat'))
        if self.check_cat('/usr/share/applications','system')==0:
            self._systemcat.setProperty('enabled',False)
        self._toolscat = self.findChild( 'toolscat')
        self._toolscat.setProperty('title', self.getnamex('/usr/share/categories/tools.cat'))
        if self.check_cat('/usr/share/applications','tools')==0:
            self._toolscat.setProperty('enabled',False)
        self._background = self.findChild( 'background')
        try:
            if self.getdata('desktop.background').startswith('@background/'):
                self._background.setProperty('source', res.qmlget(self.getdata("desktop.background")))
            else:
                self._background.setProperty('source', files.input_qml(self.getdata("desktop.background")))
        except:
            pass

        self._exit = self.findChild('exit')
        self._exit.setProperty('title', res.get('@string/power_options'))
        self._lang = self.findChild('lang')
        self._lang.setProperty('title', res.get('@string/keyboard_languages'))
        self._account = self.findChild('account')
        if self.getdata("fullname")=='':
            self._account.setProperty('title',self.username)
        else:   
            self._account.setProperty('title',self.getdata("fullname"))
        self._account_setting = self.findChild('account_setting')
        self._account_setting.triggered.connect (self.account_setting_)
        self._account_setting.setProperty('text',res.get('@string/accounts'))
        self._background_app = self.findChild('background_app')
        self._toolbar = self.findChild('toolbar')
        self._toolbar2 = self.findChild('toolbar2')
        self._toolbar3 = self.findChild('toolbar3')
        self._toolbar4 = self.findChild('toolbar4')
        self._toolbar5 = self.findChild('toolbar5')
        self._toolbar6 = self.findChild('toolbar6')
        self._toolbar7 = self.findChild('toolbar7')
        self._toolbar8 = self.findChild('toolbar8')
        self.toolbar_height = self._toolbar.property('height')
        self.toolbar_height2 = self._toolbar2.property('height')
        self.toolbar_width3 = self._toolbar3.property('width')
        self.toolbar_width4 = self._toolbar4.property('width')
        self._toolbar.setProperty('width',self.pins*self.toolbar_height)
        self._toolbar2.setProperty('width',self.pins*self.toolbar_height2)
        self._toolbar3.setProperty('height',self.pins*self.toolbar_width3)
        self._toolbar4.setProperty('height',self.pins*self.toolbar_width4)
        self.msaDesktop = self.findChild('msaDesktop')
        self._keyless = self.findChild('keyless')
        

        if self.getdata  ('dock')=='bottom':
            self._toolbar.setProperty ('visible',True)
            self._toolbar2.setProperty('visible',False)
            self._toolbar3.setProperty('visible',False)
            self._toolbar4.setProperty('visible',False)
            self._toolbar5.setProperty('visible',False)
            self._toolbar6.setProperty('visible',False)
            self._toolbar7.setProperty('visible',False)
            self._toolbar8.setProperty('visible',False)
            self._btnMenu = self.findChild ('btnMenu')
            self.btnMenu_anim = self.findChild ('btnMenu_anim')
            self._btnMenu.clicked.connect (self.menuApps_)
            self._menuApps = self.findChild ('menuApps')
            self.menuApps_anim = self.findChild('menuApps_anim')

        elif self.getdata ('dock')=='top':
            self._toolbar.setProperty ('visible',False)
            self._toolbar2.setProperty('visible',True)
            self._toolbar3.setProperty('visible',False)
            self._toolbar4.setProperty('visible',False)
            self._toolbar5.setProperty('visible',False)
            self._toolbar6.setProperty('visible',False)
            self._toolbar7.setProperty('visible',False)
            self._toolbar8.setProperty('visible',False)
            self._btnMenu = self.findChild ('btnMenu2')
            self.btnMenu_anim = self.findChild ('btnMenu2_anim')
            self._btnMenu.clicked.connect (self.menuApps_)
            self._menuApps = self.findChild ('menuApps2')
            self.menuApps_anim = self.findChild('menuApps2_anim')

        elif self.getdata  ('dock')=='left':
            self._toolbar.setProperty ('visible',False)
            self._toolbar2.setProperty('visible',False)
            self._toolbar3.setProperty('visible',True)
            self._toolbar4.setProperty('visible',False)
            self._toolbar5.setProperty('visible',False)
            self._toolbar6.setProperty('visible',False)
            self._toolbar7.setProperty('visible',False)
            self._toolbar8.setProperty('visible',False)
            self._btnMenu = self.findChild ('btnMenu3')
            self.btnMenu_anim = self.findChild ('btnMenu3_anim')
            self._btnMenu.clicked.connect (self.menuApps_)
            self._menuApps = self.findChild ('menuApps3')
            self.menuApps_anim = self.findChild('menuApps3_anim')

        elif self.getdata  ('dock')=='right':
            self._toolbar.setProperty ('visible',False)
            self._toolbar2.setProperty('visible',False)
            self._toolbar3.setProperty('visible',False)
            self._toolbar4.setProperty('visible',True)
            self._toolbar5.setProperty('visible',False)
            self._toolbar6.setProperty('visible',False)
            self._toolbar7.setProperty('visible',False)
            self._toolbar8.setProperty('visible',False)
            self._btnMenu = self.findChild ('btnMenu4')
            self.btnMenu_anim = self.findChild ('btnMenu4_anim')
            self._btnMenu.clicked.connect (self.menuApps_)
            self._menuApps = self.findChild ('menuApps4')
            self.menuApps_anim = self.findChild('menuApps4_anim')

        elif self.getdata  ('dock')=='windows' or self.getdata  ('dock')=='windows-bottom':
            self._toolbar.setProperty ('visible',False)
            self._toolbar2.setProperty('visible',False)
            self._toolbar3.setProperty('visible',False)
            self._toolbar4.setProperty('visible',False)
            self._toolbar5.setProperty('visible',True)
            self._toolbar6.setProperty('visible',False)
            self._toolbar7.setProperty('visible',False)
            self._toolbar8.setProperty('visible',False)
            self._btnMenu = self.findChild ('btnMenu5')
            self.btnMenu_anim = self.findChild ('btnMenu5_anim')
            self._btnMenu.clicked.connect (self.menuApps_)
            self._menuApps = self.findChild ('menuApps')
            self.menuApps_anim = self.findChild('menuApps_anim')

        elif self.getdata ('dock')=='windows-top':
            self._toolbar.setProperty ('visible',False)
            self._toolbar2.setProperty('visible',False)
            self._toolbar3.setProperty('visible',False)
            self._toolbar4.setProperty('visible',False)
            self._toolbar5.setProperty('visible',False)
            self._toolbar6.setProperty('visible',True)
            self._toolbar7.setProperty('visible',False)
            self._toolbar8.setProperty('visible',False)
            self._btnMenu = self.findChild ('btnMenu6')
            self.btnMenu_anim = self.findChild ('btnMenu6_anim')
            self._btnMenu.clicked.connect (self.menuApps_)
            self._menuApps = self.findChild ('menuApps2')
            self.menuApps_anim = self.findChild('menuApps2_anim')

        elif self.getdata ('dock')=='windows-left':
            self._toolbar.setProperty ('visible',False)
            self._toolbar2.setProperty('visible',False)
            self._toolbar3.setProperty('visible',False)
            self._toolbar4.setProperty('visible',False)
            self._toolbar5.setProperty('visible',False)
            self._toolbar6.setProperty('visible',False)
            self._toolbar7.setProperty('visible',True)
            self._toolbar8.setProperty('visible',False)
            self._btnMenu = self.findChild ('btnMenu7')
            self.btnMenu_anim = self.findChild ('btnMenu7_anim')
            self._btnMenu.clicked.connect (self.menuApps_)
            self._menuApps = self.findChild ('menuApps3')
            self.menuApps_anim = self.findChild('menuApps3_anim')

        elif self.getdata ('dock')=='windows-right':
            self._toolbar.setProperty ('visible',False)
            self._toolbar2.setProperty('visible',False)
            self._toolbar3.setProperty('visible',False)
            self._toolbar4.setProperty('visible',False)
            self._toolbar5.setProperty('visible',False)
            self._toolbar6.setProperty('visible',False)
            self._toolbar7.setProperty('visible',False)
            self._toolbar8.setProperty('visible',True)
            self._btnMenu = self.findChild ('btnMenu8')
            self.btnMenu_anim = self.findChild ('btnMenu8_anim')
            self._btnMenu.clicked.connect (self.menuApps_)
            self._menuApps = self.findChild ('menuApps4')
            self.menuApps_anim = self.findChild('menuApps4_anim')

        # check cats
        self.bashrc()
        self.pwduser()
        self.deskdirs()
        self.homelogo()

        # remove pause
        if files.isfile ('/proc/info/pause'): files.remove ('/proc/info/pause')

        # Start up applications
        self.startup()
        # Main Loop
        self.loop()

class Application:
    def __init__(self, ports):
        super(Application, self).__init__()

        

desktop = Backend()
sys.exit(application.exec())
