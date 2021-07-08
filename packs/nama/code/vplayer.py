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

import sys, subprocess,os,shutil,requests

from libabr import *

modules = Modules()
files = Files()
control = Control()
colors = Colors()
process = Process()
permissions = Permissions()
pack = Package()
commands = Commands()
res = Res()
app = App()

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainApp (QMainWindow):

    def onCloseProcess (self):
        if not app.check('vplayer'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.width = self.Env.width()
        self.height = self.Env.height()

        self.onCloseProcess()

        app.switch('vplayer')

        self.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.Resize (self,int(self.Env.width()/0.8),int(self.Env.height()/0.8))
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('vplayer','logo'))))

        self.btnImage = QToolButton()
        self.btnImage.setStyleSheet('background-color: black;border:none;color: black;')
        self.setCentralWidget(self.btnImage)

        try:
            if self.External[0].endswith('.pv'):
                shutil.unpack_archive(files.input(self.External[0]), files.input('/tmp'), 'zip')

                try:
                    self.timeout = int(control.read_record('timeout', '/tmp/data'))
                    self.frames = int(control.read_record('frames', '/tmp/data'))
                    self.width = int(control.read_record('width', '/tmp/data'))
                    self.height = int(control.read_record('height', '/tmp/data'))
                    self.slider.setMaximum(self.frames)
                    self.stop = False
                    self.stopa.setIcon(QIcon(res.get('@icon/breeze-pause')))
                except:
                    pass

                self.Widget.Resize(self, self.width, self.height)
                self.Player_()
            else:
                app.switch('vplayer')
                self.Env.RunApp('text', [res.get('@string/npv'), res.get('@string/npvm')])
                app.switch('vplayer')
        except:
            pass

        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)
        self.menubar.setFont(self.Env.font())
        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)

        self.opena = self.menubar.addAction(res.get('@string/open'))
        self.opena.setFont(self.Env.font())
        self.opena.triggered.connect(self.open_act)
        self.opena.setShortcut ('Ctrl+O')

        self.fullscreena = self.menubar.addAction(res.get('@string/hide'))
        self.fullscreena.setFont(self.Env.font())
        self.fullscreena.triggered.connect(self.full_act)
        self.fullscreena.setShortcut('Ctrl+H')

        self.tools = QToolBar()
        self.stopa = QToolButton()
        self.stopa.setIcon(QIcon(res.get('@icon/breeze-start')))
        self.stopa.setIconSize(QSize(15,15))
        self.tools.addWidget(self.stopa)

        self.slider = QSlider(Qt.Horizontal)
        self.tools.addWidget(self.slider)
        self.slider.setValue(self.entry)
        self.slider.setMaximum(self.frames)
        self.slider.setMinimum(self.entry)

        self.stopa.clicked.connect (self.stop_act)
        self.addToolBar(self.tools)

    def open_act(self):
        app.switch('vplayer')
        self.Env.RunApp('select', [res.get('@string/open'), 'open', self.open_act_])
        app.switch('vplayer')

    def Player_(self):
        self.btnImage.setIcon(QIcon(files.input('/tmp/' + str(self.entry))))
        self.btnImage.setIconSize(QSize(self.Env.width(),self.Env.height()))

        if self.stop:
            pass
        else:
            if self.entry < self.frames:
                self.entry += 1
                self.slider.setValue(self.entry)
                QTimer.singleShot(self.timeout, self.Player_)
            else:
                files.removedirs('/tmp')
                files.mkdir('/tmp')

    entry = 0
    timeout = 100
    frames = 1

    def open_act_(self, filename):
        if filename.endswith ('.pv'):
            shutil.unpack_archive(files.input(filename), files.input('/tmp'), 'zip')

            try:
                self.timeout = int(control.read_record('timeout', '/tmp/data'))
                self.frames = int(control.read_record('frames', '/tmp/data'))
                self.width = int(control.read_record('width', '/tmp/data'))
                self.height = int(control.read_record('height', '/tmp/data'))
                self.slider.setMaximum(self.frames)
                self.stop = False
                self.stopa.setIcon(QIcon(res.get('@icon/breeze-pause')))
            except:
                pass

            self.Widget.Resize(self,self.width,self.height)
            self.Player_()
        else:
            app.switch('vplayer')
            self.Env.RunApp('text',[res.get('@string/npv'),res.get('@string/npvm')])
            app.switch('vplayer')

    def full_act (self):
        self.menubar.hide()
        self.tools.hide()

    stop = False

    def stop_act (self):
        if self.stop:
            self.stop = False
            self.stopa.setIcon(QIcon(res.get('@icon/breeze-pause')))
            self.Player_()
        else:
            self.stop = True
            self.stopa.setIcon(QIcon(res.get('@icon/breeze-start')))
