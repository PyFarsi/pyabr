from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from libabr import *

import random

files = Files()
colors = Colors()
control = Control()
res = Res()
app = App()
commands = Commands()
permissions = Permissions()

def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check('wallpaper'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)
    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.External = ports[3]

        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.onCloseProcess()

        commands.cd(['/usr/share/backgrounds'])

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.etc('wallpaper','logo')))

        self.btnDesktopWallpaper = QPushButton()
        self.btnDesktopWallpaper.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnDesktopWallpaper.setFont(self.Env.font())
        self.btnDesktopWallpaper.setText(res.get('@string/desktop'))
        self.btnDesktopWallpaper.clicked.connect (self.desktop_act)

        self.imgDesktop = QToolButton()
        self.imgDesktop.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.btnLockWallpaper = QPushButton()
        self.btnLockWallpaper.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnLockWallpaper.setFont(self.Env.font())
        self.btnLockWallpaper.setText(res.get('@string/lock'))
        self.btnLockWallpaper.clicked.connect(self.lock_act)

        self.imgLock = QToolButton()
        self.imgLock.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.btnUnlockWallpaper = QPushButton()
        self.btnUnlockWallpaper.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnUnlockWallpaper.setFont(self.Env.font())
        self.btnUnlockWallpaper.setText(res.get('@string/unlock'))
        self.btnUnlockWallpaper.clicked.connect(self.unlock_act)

        self.imgUnlock = QToolButton()
        self.imgUnlock.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.btnLoginWallpaper = QPushButton()
        self.btnLoginWallpaper.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnLoginWallpaper.setFont(self.Env.font())
        self.btnLoginWallpaper.setText(res.get('@string/login'))
        self.btnLoginWallpaper.clicked.connect(self.login_act)

        self.imgLogin = QToolButton()
        self.imgLogin.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.btnEnterWallpaper = QPushButton()
        self.btnEnterWallpaper.setFont(self.Env.font())
        self.btnEnterWallpaper.setText(res.get('@string/enter'))
        self.btnEnterWallpaper.clicked.connect(self.enter_act)
        self.btnEnterWallpaper.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.imgEnter = QToolButton()
        self.imgEnter.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.Resize (self,1280,300)

        self.imgw = QWidget()
        self.imgw.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnw = QWidget()
        self.btnw.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.layout().addWidget(self.imgw)
        self.imgw.setGeometry(0,0,self.width(),int(self.height()-self.height()/4))
        self.btnw.setGeometry(0,int(self.height()-self.height()/4),self.width(),int(self.height()/4))
        self.layout().addWidget(self.btnw)

        self.btnlayout = QHBoxLayout()
        self.btnlayout.addWidget(self.btnDesktopWallpaper)
        self.btnlayout.addWidget(self.btnLockWallpaper)
        self.btnlayout.addWidget(self.btnUnlockWallpaper)
        self.btnlayout.addWidget(self.btnLoginWallpaper)
        self.btnlayout.addWidget(self.btnEnterWallpaper)

        self.btnw.setLayout(self.btnlayout)

        self.imglayout = QHBoxLayout()
        self.imgw.setLayout(self.imglayout)

        self.imglayout.addWidget(self.imgDesktop)
        self.imglayout.addWidget(self.imgLock)
        self.imglayout.addWidget(self.imgUnlock)
        self.imglayout.addWidget(self.imgLogin)
        self.imglayout.addWidget(self.imgEnter)

        self.imgDesktop.setIcon(QIcon(res.get(getdata('desktop.background'))))
        self.imgDesktop.setFixedSize(int(self.imgw.width()/5),self.imgw.height())
        self.imgDesktop.setIconSize(QSize(int(self.imgw.width() / 5), self.imgw.height()))
        self.imgLock.setIcon(QIcon(res.get(getdata('lock.background'))))
        self.imgLock.setFixedSize(int(self.imgw.width() / 5), self.imgw.height())
        self.imgLock.setIconSize(QSize(int(self.imgw.width() / 5), self.imgw.height()))
        self.imgUnlock.setIcon(QIcon(res.get(getdata('unlock.background'))))
        self.imgUnlock.setFixedSize(int(self.imgw.width() / 5), self.imgw.height())
        self.imgUnlock.setIconSize(QSize(int(self.imgw.width() / 5), self.imgw.height()))
        self.imgLogin.setIcon(QIcon(res.get(getdata('login.background'))))
        self.imgLogin.setFixedSize(int(self.imgw.width() / 5), self.imgw.height())
        self.imgLogin.setIconSize(QSize(int(self.imgw.width() / 5), self.imgw.height()))
        self.imgEnter.setIcon(QIcon(res.get(getdata('enter.background'))))
        self.imgEnter.setFixedSize(int(self.imgw.width() / 5), self.imgw.height())
        self.imgEnter.setIconSize(QSize(int(self.imgw.width() / 5), self.imgw.height()))

    def desktop_act (self):
        app.switch('wallpaper')
        self.Env.RunApp('select', [res.get('@string/desktop'), 'open', self.desktop_])
        app.switch('wallpaper')

    def lock_act (self):
        app.switch('wallpaper')
        self.Env.RunApp('select', [res.get('@string/lock'), 'open', self.lock_])
        app.switch('wallpaper')

    def unlock_act (self):
        app.switch('wallpaper')
        self.Env.RunApp('select', [res.get('@string/unlock'), 'open', self.unlock_])
        app.switch('wallpaper')

    def login_act (self):
        app.switch('wallpaper')
        self.Env.RunApp('select', [res.get('@string/login'), 'open', self.login_])
        app.switch('wallpaper')

    def enter_act (self):
        app.switch('wallpaper')
        self.Env.RunApp('select', [res.get('@string/enter'), 'open', self.enter_])
        app.switch('wallpaper')

    def desktop_(self,filename):
        r = random.randint(1000,9999)

        if not filename.startswith ('/usr/share/backgrounds/'):
            if filename.endswith('.png'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.png')

            elif filename.endswith('.jpg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpg')

            elif filename.endswith('.jpeg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpeg')

            elif filename.endswith('.svg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.svg')

            elif filename.endswith('.tiff'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.tiff')

            control.write_record('desktop.background', f'@background/img_{str(r)}', '/etc/gui')
        else:
            control.write_record('desktop.background', f'@background/{files.filename(filename.replace(".svg","").replace(".png","").replace(".jpg","").replace(".jpeg","").replace(".tiff","").replace(".gif","").replace(".bmp",""))}', '/etc/gui')

        self.Env.backgroundButton.setStyleSheet(
            f'border:none;background-image: url({res.get(getdata("desktop.background"))});')

        self.Widget.Close()
        self.Env.RunApp('wallpaper', [None])

    def lock_(self, filename):
        r = random.randint(1000, 9999)

        if not filename.startswith('/usr/share/backgrounds/'):
            if filename.endswith('.png'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.png')

            elif filename.endswith('.jpg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpg')

            elif filename.endswith('.jpeg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpeg')

            elif filename.endswith('.svg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.svg')

            elif filename.endswith('.tiff'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.tiff')

            control.write_record('lock.background', f'@background/img_{str(r)}', '/etc/gui')
        else:
            control.write_record('lock.background', f'@background/{files.filename(filename.replace(".svg","").replace(".png","").replace(".jpg","").replace(".jpeg","").replace(".tiff","").replace(".gif","").replace(".bmp",""))}', '/etc/gui')

        self.Widget.Close()
        self.Env.RunApp('wallpaper', [None])

    def unlock_(self, filename):
        r = random.randint(1000, 9999)

        if not filename.startswith('/usr/share/backgrounds/'):
            if filename.endswith('.png'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.png')

            elif filename.endswith('.jpg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpg')

            elif filename.endswith('.jpeg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpeg')

            elif filename.endswith('.svg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.svg')

            elif filename.endswith('.tiff'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.tiff')

            control.write_record('unlock.background', f'@background/img_{str(r)}', '/etc/gui')
        else:
            control.write_record('unlock.background', f'@background/{files.filename(filename.replace(".svg","").replace(".png","").replace(".jpg","").replace(".jpeg","").replace(".tiff","").replace(".gif","").replace(".bmp",""))}', '/etc/gui')

        self.Widget.Close()
        self.Env.RunApp('wallpaper', [None])

    def login_(self, filename):
        r = random.randint(1000, 9999)

        if not filename.startswith('/usr/share/backgrounds/'):
            if filename.endswith('.png'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.png')

            elif filename.endswith('.jpg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpg')

            elif filename.endswith('.jpeg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpeg')

            elif filename.endswith('.svg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.svg')

            elif filename.endswith('.tiff'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.tiff')

            control.write_record('login.background', f'@background/img_{str(r)}', '/etc/gui')
        else:
            control.write_record('login.background', f'@background/{files.filename(filename.replace(".svg","").replace(".png","").replace(".jpg","").replace(".jpeg","").replace(".tiff","").replace(".gif","").replace(".bmp",""))}', '/etc/gui')

        self.Widget.Close()
        self.Env.RunApp('wallpaper', [None])

    def enter_(self, filename):
        r = random.randint(1000, 9999)

        if not filename.startswith('/usr/share/backgrounds/'):
            if filename.endswith('.png'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.png')

            elif filename.endswith('.jpg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpg')

            elif filename.endswith('.jpeg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.jpeg')

            elif filename.endswith('.svg'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.svg')

            elif filename.endswith('.tiff'):
                files.copy(filename, f'/usr/share/backgrounds/img_{str(r)}.tiff')

            control.write_record('enter.background', f'@background/img_{str(r)}', '/etc/gui')
        else:
            control.write_record('enter.background', f'@background/{files.filename(filename.replace(".svg","").replace(".png","").replace(".jpg","").replace(".jpeg","").replace(".tiff","").replace(".gif","").replace(".bmp",""))}', '/etc/gui')

        self.Widget.Close()
        self.Env.RunApp('wallpaper',[None])